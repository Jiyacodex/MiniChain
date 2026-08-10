# Security Policy

## Supported Versions

MiniChain does not yet have tagged releases or a formal versioning scheme. Security fixes are applied to the latest commit on `main`, which is the only version supported.

## Reporting a Vulnerability

**Please do not open a public GitHub Issue for security vulnerabilities.** Publicly disclosing a vulnerability before it's fixed can put users at risk.

Instead, report it privately using one of these channels:

1. **GitHub Private Vulnerability Reporting** (preferred): open a report using the "Security" tab on the [MiniChain repository](https://github.com/StabilityNexus/MiniChain/security/advisories/new).
2. **Discord DM:** send a direct message to one of the maintainers listed in [docs/maintainer.md](docs/maintainer.md)— do not post details in a public channel.

Please include as much of the following as you can:

- A description of the vulnerability and its potential impact.
- Steps to reproduce it (proof-of-concept code, a malicious contract, a crafted P2P message, etc.).
- The affected file(s)/module(s), if known.
- Any suggested fix or mitigation.

## What to Expect

- We aim to acknowledge new reports within **14 days**.
- We'll work with you to understand and validate the issue, and will keep you updated as a fix is developed.
- Once a fix is released, we'll credit you in the release notes/changelog unless you'd prefer to remain anonymous.

## Scope

Given MiniChain's goals — education, research, and innovation on a minimal blockchain — vulnerabilities of particular interest include:

- Transaction signature forgery or verification bypass (see `minichain/transaction.py`).
- Smart contract sandbox escape or gas-metering bypass (see `minichain/contract.py`).
- Consensus/fork-choice manipulation or state root corruption (see `minichain/chain.py`, `minichain/state.py`, `minichain/pow.py`).
- P2P protocol issues that allow a peer to crash, partition, or deny service to a node (see `minichain/p2p.py`).
- JSON-RPC issues that allow unauthorized access to node data or funds (see `minichain/rpc.py`).

Out of scope: issues in vendored third-party binaries (`bore_bin/`, `bore.zip`) should be reported upstream to their respective projects.

## Questions

For non-security questions, use the [Stability Nexus Discord](https://discord.gg/YzDKeEfWtS) or open a regular GitHub Issue, per [CONTRIBUTING.md](CONTRIBUTING.md).
