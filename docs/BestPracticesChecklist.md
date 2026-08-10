# Best Practices Checklist

Use this checklist before opening or merging a PR against MiniChain.

## Code

- [ ] New logic lives in the correct module under `minichain/` (`block.py`, `chain.py`, `state.py`, `mempool.py`, `p2p.py`, `pow.py`, `rpc.py`, `persistence.py`, `contract.py`) rather than a new ad-hoc file.
- [ ] State changes (balances, contract storage) go through `state.py`'s Merkle Patricia Trie APIs, not direct mutation.
- [ ] Contract execution changes preserve gas-per-opcode metering (`sys.settrace`) and process-level sandboxing (`multiprocessing`).
- [ ] Consensus-affecting logic (fork choice, block validity, difficulty) lives in `chain.py`/`pow.py`, not duplicated in `p2p.py`.
- [ ] New JSON-RPC methods follow the `mc_*` naming convention and are documented.
- [ ] No hardcoded secrets, private keys, or node addresses.
- [ ] No edits to `genesis.json`, a node's `--datadir`, or vendored binaries (`bore_bin/`, `bore.zip`) as part of a feature/fix.

## Tests

- [ ] New/changed behavior has a corresponding test in `tests/`, named to mirror the module it covers (e.g. `state.py` -> `tests/test_core.py` or a dedicated `tests/test_<feature>.py`).
- [ ] `pytest` passes locally.
- [ ] `pytest --cov=minichain` shows coverage did not regress for touched modules.
- [ ] Edge cases covered: invalid transactions/signatures, chain reorgs, malformed P2P messages, contract gas exhaustion, as relevant to the change.

## Documentation

- [ ] `README.md` updated if user-facing CLI/RPC behavior changed (do not hand-edit the coverage badge/table — it's CI-generated).
- [ ] `agent.md` updated if a new project-wide convention or boundary was introduced.
- [ ] Docstrings/comments added only where the *why* isn't obvious from the code.

## Git / PR Hygiene

- [ ] Branch created off `main`.
- [ ] Commits are signed off per [DCO.md](../DCO.md).
- [ ] PR description explains the problem and the fix, per [Contributors.md](../Contributors.md).
- [ ] No unrelated changes bundled into the PR (formatting-only diffs, unrelated files).

## Security

- [ ] Signature verification (Ed25519 via `pynacl`) is not weakened or bypassed.
- [ ] Contract sandboxing boundaries are not loosened without explicit discussion.
- [ ] Any new external input (RPC params, P2P payloads, contract bytecode) is validated before use.
