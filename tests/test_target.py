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
        
        # Start with a target comfortably in the middle
        start_target = MAX_TARGET // 2
        chain.current_target = start_target
        chain.chain[0].target = start_target
        chain.chain[0].hash = chain.chain[0].compute_hash()
        
        # Fast mining: timestamps only 1ms apart
        # avg = 0.5 * 1 + 0.5 * 1000 = 500.5 (which truncates to 500 in integer ops if needed, but in Python it's a float)
        # new_target = (start_target * int(500.5)) // 1000 = (start_target * 500) // 1000 = start_target // 2
        ts = chain.last_block.timestamp + 1
        block1 = Block(index=1, previous_hash=chain.last_block.hash, transactions=[], timestamp=ts, target=chain.current_target, state_root=chain.state.state_root())
        mined_block1 = mine_block(block1)
        self.assertEqual(chain.add_block(mined_block1), ValidationStatus.VALID)
        expected_target_fast = (start_target * 500) // 1000
        self.assertEqual(chain.current_target, expected_target_fast)
        
        # Slow mining: timestamp 5000ms apart
        # avg = 0.5 * 5000 + 0.5 * 500.5 = 2750.25
        # new_target = (expected_target_fast * int(2750.25)) // 1000 = (expected_target_fast * 2750) // 1000
        ts = chain.last_block.timestamp + 5000
        block2 = Block(index=2, previous_hash=chain.last_block.hash, transactions=[], timestamp=ts, target=chain.current_target, state_root=chain.state.state_root())
        mined_block2 = mine_block(block2)
        self.assertEqual(chain.add_block(mined_block2), ValidationStatus.VALID)
        expected_target_slow = (expected_target_fast * 2750) // 1000
        self.assertEqual(chain.current_target, expected_target_slow)

    def test_reorg_target_validation(self):
        chain1 = Blockchain()
        chain1.target_block_time = 1000
        chain1.alpha = 0.5
        chain1.avg_block_time = 1000
        start_target = MAX_TARGET // 2
        chain1.current_target = start_target
        chain1.chain[0].target = start_target
        chain1.chain[0].hash = chain1.chain[0].compute_hash()
        
        chain2 = Blockchain()
        chain2.target_block_time = 1000
        chain2.alpha = 0.5
        chain2.avg_block_time = 1000
        chain2.current_target = start_target
        chain2.chain[0].target = start_target
        chain2.chain[0].hash = chain2.chain[0].compute_hash()

        # Chain 2 mines a fast block
        block1 = Block(1, chain2.last_block.hash, [], timestamp=chain2.last_block.timestamp + 1, target=chain2.current_target, state_root=chain2.state.state_root())
        mine_block(block1)
        chain2.add_block(block1)
        
        expected_target_fast = (start_target * 500) // 1000
        self.assertEqual(chain2.current_target, expected_target_fast)
        
        # Reorg chain1 to chain2
        success, _ = chain1.resolve_conflicts(chain2.chain)
        self.assertTrue(success)
        self.assertEqual(chain1.current_target, expected_target_fast)

        # Forging a chain with wrong target should be rejected
        forged_chain = list(chain2.chain)
        # Should be expected_target_fast but we provide start_target instead!
        forged_block = Block(2, chain2.last_block.hash, [], timestamp=chain2.last_block.timestamp + 1000, target=start_target, state_root=chain2.state.state_root())
        mine_block(forged_block)
        forged_chain.append(forged_block)
        
        success, _ = chain1.resolve_conflicts(forged_chain)
        self.assertFalse(success) # Rejected because target is wrong!
