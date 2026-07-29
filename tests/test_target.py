import unittest
from minichain import Blockchain, Block
from minichain.pow import mine_block
from minichain.validators import ValidationStatus
from minichain.network_config import MAX_TARGET

class TestEMATarget(unittest.TestCase):
    def test_target_adjustment(self):
        chain = Blockchain()
        chain.target_block_time = 1000
        chain.alpha = 0.5
        chain.avg_block_time = 1000
        chain.current_target = MAX_TARGET - 10
        chain.chain[0].target = MAX_TARGET - 10
        
        # Fast mining: timestamps only 1ms apart
        # avg = 0.5 * 1 + 0.5 * 1000 = 500.5 (which is < 1000) => target decrements by 1
        ts = chain.last_block.timestamp + 1
        block1 = Block(index=1, previous_hash=chain.last_block.hash, transactions=[], timestamp=ts, target=chain.current_target, state_root=chain.state.state_root())
        mined_block1 = mine_block(block1)
        self.assertEqual(chain.add_block(mined_block1), ValidationStatus.VALID)
        self.assertEqual(chain.current_target, MAX_TARGET - 11)
        
        # Slow mining: timestamp 5000ms apart
        # avg = 0.5 * 5000 + 0.5 * 500.5 = 2750.25 (which is > 1000) => target increments by 1
        ts = chain.last_block.timestamp + 5000
        block2 = Block(index=2, previous_hash=chain.last_block.hash, transactions=[], timestamp=ts, target=chain.current_target, state_root=chain.state.state_root())
        mined_block2 = mine_block(block2)
        self.assertEqual(chain.add_block(mined_block2), ValidationStatus.VALID)
        self.assertEqual(chain.current_target, MAX_TARGET - 10)

    def test_reorg_target_validation(self):
        chain1 = Blockchain()
        chain1.target_block_time = 1000
        chain1.alpha = 0.5
        chain1.avg_block_time = 1000
        chain1.current_target = MAX_TARGET - 10
        chain1.chain[0].target = MAX_TARGET - 10
        
        chain2 = Blockchain()
        chain2.target_block_time = 1000
        chain2.alpha = 0.5
        chain2.avg_block_time = 1000
        chain2.current_target = MAX_TARGET - 10
        chain2.chain[0].target = MAX_TARGET - 10

        # Chain 2 mines a fast block, target goes to MAX_TARGET - 11
        block1 = Block(1, chain2.last_block.hash, [], timestamp=chain2.last_block.timestamp + 1, target=chain2.current_target, state_root=chain2.state.state_root())
        mine_block(block1)
        chain2.add_block(block1)
        self.assertEqual(chain2.current_target, MAX_TARGET - 11)
        
        # Reorg chain1 to chain2
        success, orphans = chain1.resolve_conflicts(chain2.chain)
        self.assertTrue(success)
        self.assertEqual(chain1.current_target, MAX_TARGET - 11)

        # Forging a chain with wrong target should be rejected
        forged_chain = list(chain2.chain)
        forged_block = Block(2, chain2.last_block.hash, [], timestamp=chain2.last_block.timestamp + 1000, target=MAX_TARGET - 10, state_root=chain2.state.state_root())
        mine_block(forged_block)
        forged_chain.append(forged_block)
        
        success, _ = chain1.resolve_conflicts(forged_chain)
        self.assertFalse(success) # Rejected because target should have been MAX_TARGET - 11!
