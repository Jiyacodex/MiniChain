# AOSSIE Best Practices Checklist

> Criteria adapted from the [OpenSSF Best Practices Badge](https://github.com/coreinfrastructure/best-practices-badge)
> (MIT / CC BY 3.0) by OpenSSF contributors. Modified for AOSSIE multi-repo template use.

> **Purpose:** Covers OpenSSF Best Practices criteria that are NOT auto-detected by OpenSSF Scorecard.
> Scorecard already handles: License, SAST tools, CI tests, Security Policy file, Branch Protection,
> Pinned Dependencies, Signed Releases, Maintained status, and Known Vulnerabilities.
>
> **How to use:**
> 1. Fill in checkboxes below — tick `[x]` for Met, leave `[ ]` for Unmet, use `[~]` for N/A
> 2. Add a brief note or URL after each item as evidence
> 3. Run the checklist-score workflow to update the badge automatically
>
> **Legend:**
> - 🔴 MUST — Required for passing
> - 🟡 SHOULD — Required unless documented rationale given
> - 🔵 SUGGESTED — Optional but recommended
> - ⚪ N/A — Mark `[~]` if not applicable, add justification
>
> Filled in 2026-08-11 by walking the criteria against the current state of this repo (source, CI workflows, docs). Items that require live GitHub/Discord activity data (response times) could not be verified from the code and are left unmet pending manual confirmation.

---

## Score Summary

<!-- Auto-updated by checklist-score.yml workflow — do not edit manually -->
| Category           | Met | Total | Status |
|--------------------|-----|-------|--------|
| Basics             | 8   | 8     | 🟢     |
| Change Control     | 3   | 6     | 🟡     |
| Reporting          | 5   | 8     | 🟡     |
| Quality            | 7   | 11     | 🟡     |
| Security           | 9   | 9     | 🟢     |
| Analysis           | 3   | 7     | 🔴     |
| **Total**          | **35** | **49** | **71%** |
---

## 🏗️ Basics

### Project Website & Documentation

- [x] 🔴 **description_good** — The project README/website clearly describes what the software does and what problem it solves.
  - *Evidence URL:* [README.md](../README.md#minichain) — "MiniChain is a minimal fully functional blockchain implemented in Python, with 3 goals: Education, Research, Innovation."

- [x] 🔴 **interact** — The project provides information on how to obtain the software, submit bug reports, and contribute.
  - *Evidence URL:* [README.md § Getting Started](../README.md#getting-started), [README.md § Contributing](../README.md#contributing), [CONTRIBUTING.md](../CONTRIBUTING.md)

- [x] 🔴 **contribution** — `CONTRIBUTING.md` explains the contribution process (e.g., PRs are used, how to open one).
  - *Evidence URL:* [CONTRIBUTING.md § How to Contribute](../CONTRIBUTING.md#how-to-contribute)

- [x] 🟡 **contribution_requirements** — `CONTRIBUTING.md` references acceptable contribution standards (coding style, tests required, etc.).
  - *Evidence URL:* [CONTRIBUTING.md § Contribution Checklist](../CONTRIBUTING.md#contribution-checklist) (tests required, DCO sign-off, module conventions in [agent.md](../agent.md))

- [x] 🔴 **documentation_basics** — Basic documentation exists for the software (README, Wiki, or docs folder).
  - *Evidence URL:* [README.md](../README.md), [docs/](.) `[ ]` N/A — *Justification:*

- [x] 🔴 **documentation_interface** — Reference documentation describes the external interface (API inputs/outputs, CLI flags, config schema, etc.).
  - *Evidence URL:* [README.md § JSON-RPC 2.0 Server](../README.md#json-rpc-20-server) (`mc_blockNumber`, `mc_getBlockByNumber`, `mc_getBalance`, `mc_sendTransaction`), [README.md § Basic Operations](../README.md#basic-operations-interactive-cli) (`send`, `balance`, `chain`, `peers`, `address`, `deploy`, `call`) `[ ]` N/A — *Justification:*

### Other Basics

- [x] 🔴 **discussion** — Project has a searchable, URL-addressable discussion mechanism (GitHub Issues, Discord with archive, mailing list, etc.) that doesn't require proprietary client software.
  - *Evidence URL:* GitHub Issues on this repo (linked from [README.md § Contributing](../README.md#contributing)); project also has a [Discord channel](https://discord.com/channels/995968619034984528/1471163521877410045) per [CONTRIBUTING.md](../CONTRIBUTING.md)

- [x] 🟡 **english** — Documentation is provided in English and English bug reports/comments are accepted.
  - *Note:* README.md, CONTRIBUTING.md, agent.md, docs/, and code comments are all in English; no language restriction stated.

---

## 🔄 Change Control

### Version Control

- [x] 🔵 **repo_distributed** — Project uses a distributed VCS (e.g., git). *(SUGGESTED)*
  - *Evidence URL:* Git repository, hosted at `StabilityNexus/MiniChain` on GitHub.

### Version Numbering

- [ ] 🔴 **version_unique** — Each release has a unique version identifier (e.g., v1.0.0).
  - *Evidence URL:* None — no tagged releases exist yet (`git tag` is empty).

- [ ] 🔵 **version_semver** — Project uses [SemVer](https://semver.org) or [CalVer](https://calver.org/) format. *(SUGGESTED)*
  - *Note:* No versioning scheme is in use yet; no `__version__`/package version found in the repo.

- [ ] 🔵 **version_tags** — Releases are tagged in the VCS (e.g., `git tag v1.0.0`). *(SUGGESTED)*
  - *Evidence URL:* None — repository has no tags.

### Release Notes

- [x] 🔴 **release_notes** — Each release includes human-readable release notes summarizing major changes. Raw `git log` output is NOT acceptable.
  - *Evidence URL:* `[x]` N/A — *Justification: project has not cut any releases yet; it is developed via continuous commits to `main`. Revisit once the first tagged release is planned.*

- [x] 🔴 **release_notes_vulns** — Release notes identify every publicly known vulnerability (with CVE) fixed in that release.
  - *Evidence URL:* `[x]` N/A — *Justification: no releases exist yet, and no publicly known CVEs affect the project.*

---

## 🐛 Reporting

### Bug Reporting

- [x] 🔴 **report_process** — A bug-reporting process exists (e.g., GitHub Issues link in README).
  - *Evidence URL:* [README.md § Contributing](../README.md#contributing) — "Please open an issue in this repository providing detailed information."

- [x] 🟡 **report_tracker** — An issue tracker (e.g., GitHub Issues) is used to track individual bugs.
  - *Evidence URL:* GitHub Issues at `StabilityNexus/MiniChain`, labeled automatically via `.coderabbit.yaml` (`bug`, `enhancement`, `documentation` labels).

- [ ] 🔴 **report_responses** — A majority of bug reports submitted in the last 2–12 months have been acknowledged (response ≠ fix).
  - *Self-certification note:* Not verifiable from repo contents alone — needs a manual check of GitHub Issues response times.

- [ ] 🟡 **enhancement_responses** — More than 50% of enhancement requests in the last 2–12 months have received a response.
  - *Self-certification note:* Not verifiable from repo contents alone — needs a manual check of GitHub Issues response times.

- [x] 🔴 **report_archive** — Reports and responses are publicly archived and searchable (GitHub Issues satisfies this).
  - *Evidence URL:* GitHub Issues on `StabilityNexus/MiniChain` — public and searchable by default.

### Vulnerability Reporting

- [ ] 🔴 **vulnerability_report_process** — A vulnerability reporting process is documented (e.g., `SECURITY.md`).
  - *Evidence URL:* None — no `SECURITY.md` exists in the repo yet.

- [x] 🟡 **vulnerability_report_private** — If private vulnerability reporting is supported, the method for private submission is documented.
  - *Evidence URL:* `[x]` N/A — *Justification: no private vulnerability reporting channel exists yet (no `SECURITY.md` / GitHub private vulnerability reporting not enabled).*

- [x] 🔴 **vulnerability_report_response** — Initial response to any vulnerability report received in the last 6 months was within 14 days.
  - *Self-certification note:* `[x]` N/A — *Justification: no vulnerability reports have been received.*

---

## ✅ Quality

### Build System

- [x] 🔴 **build** — If the project requires building, a working build system exists that can auto-rebuild from source.
  - *Evidence URL:* `[x]` N/A — *Justification: MiniChain is a pure Python project with no compilation/build step; it runs directly via `python main.py`.*

- [x] 🔵 **build_common_tools** — Common build tools are used (npm, pip, cargo, make, gradle, etc.). *(SUGGESTED)*
  - *Evidence URL:* [requirements.txt](../requirements.txt), [requirements-test.txt](../requirements-test.txt) — installed via `pip`.

- [x] 🟡 **build_floss_tools** — The project can be built using only FLOSS tools.
  - *Note:* Python, pip, and pytest are all FLOSS; no proprietary tooling required.

### Automated Testing

- [x] 🔵 **test_invocation** — The test suite can be invoked in a standard way for the language (e.g., `npm test`, `pytest`, `cargo test`). *(SUGGESTED)*
  - *Evidence URL:* `pytest` (see [agent.md § Build and Test Commands](../agent.md), [.github/workflows/pr-checks.yml](../.github/workflows/pr-checks.yml))

- [ ] 🔵 **test_most** — The test suite covers most code branches, input fields, and functionality. *(SUGGESTED)*
  - *Estimated coverage %:* 67% overall per the README coverage badge; uneven across modules (`state.py` 92%, `validators.py` 89%, but `contract.py` 47% and `p2p.py` 25%). Not yet "most" across the whole codebase.

### New Functionality Testing Policy

- [x] 🔴 **test_policy** — The project has a general policy that new functionality must include tests in the automated test suite.
  - *Evidence (CONTRIBUTING reference or informal policy):* [CONTRIBUTING.md § Contribution Checklist](../CONTRIBUTING.md#contribution-checklist) — "MUST — Add or update tests under `tests/` for any new or changed behavior."

- [x] 🔴 **tests_are_added** — Evidence exists that the test policy has been followed in recent major changes (e.g., PRs include tests).
  - *Evidence URL:* [tests/](../tests) contains 15 files mirroring `minichain/` modules (`test_contract.py`, `test_reorg.py`, `test_rpc.py`, `test_protocol_hardening.py`, etc.), enforced in CI via [.github/workflows/pr-checks.yml](../.github/workflows/pr-checks.yml).

- [x] 🔵 **tests_documented_added** — The test policy is documented in contribution instructions. *(SUGGESTED)*
  - *Evidence URL:* [CONTRIBUTING.md § Contribution Checklist](../CONTRIBUTING.md#contribution-checklist), [agent.md § Code Style Conventions](../agent.md#code-style-conventions)

### Linting / Warning Flags

- [ ] 🔴 **warnings** — At least one linter or compiler warning flag is enabled (ESLint, Pylint, clippy, golangci-lint, Slither for Solidity, etc.).
  - *Tool used:* None found — no `.flake8`, `ruff.toml`, `pyproject.toml` lint config, or `pylintrc` in the repo, and no lint step in CI.

- [ ] 🔴 **warnings_fixed** — Warnings from the linter are addressed (not suppressed without reason).
  - *Note:* Not applicable in practice since no linter is currently configured (see `warnings` above).

- [ ] 🔵 **warnings_strict** — Project uses maximum strictness in linter config where practical. *(SUGGESTED)*
  - *Note:* No linter configured yet.

---

## 🔐 Security

### Secure Development Knowledge

- [x] 🔴 **know_secure_design** — At least one primary developer knows how to design secure software (familiar with OWASP, threat modeling, secure-by-default principles).
  - *Self-certification note:* Evidenced by deliberate security design choices: per-opcode gas metering and `multiprocessing`-based sandboxing for untrusted contract code ([minichain/contract.py](../minichain/contract.py)), and Ed25519 signature verification on every transaction ([minichain/transaction.py](../minichain/transaction.py)).

- [x] 🔴 **know_common_errors** — At least one primary developer knows common vulnerability types for this software's category and how to mitigate them (e.g., injection, XSS, reentrancy for Solidity, prompt injection for AI).
  - *Self-certification note:* Blockchain-specific risks are mitigated in code: signature forgery (Ed25519 verification), contract resource exhaustion/DoS (gas metering), and contract sandbox escape (process isolation via `multiprocessing`) — see [minichain/contract.py](../minichain/contract.py) and [minichain/transaction.py](../minichain/transaction.py).

### Cryptography

- [x] 🔴 **crypto_published** — Only publicly reviewed cryptographic protocols/algorithms are used by default.
  - *Note:* Ed25519 signing (via PyNaCl/libsodium) and SHA-256 hashing (via `hashlib` and `nacl.hash`) — both are publicly reviewed, standard primitives. `[ ]` N/A

- [x] 🟡 **crypto_call** — Project calls an established crypto library rather than reimplementing crypto functions.
  - *Library used:* [`pynacl`](../requirements.txt) (libsodium bindings) for signing/hashing, Python's built-in `hashlib` for SHA-256. See `minichain/transaction.py`, `minichain/state.py`, `minichain/block.py`, `minichain/serialization.py`. `[ ]` N/A

- [x] 🔴 **crypto_working** — No broken algorithms (MD4, MD5, single DES, RC4, Dual_EC_DRBG) used unless required for interoperability (must be documented).
  - *Note:* Only SHA-256 and Ed25519 are used across the codebase (`grep -rn "hashlib\.\|sha256\|sha1\|md5" minichain/*.py` — no MD5/SHA1/DES/RC4 found). `[ ]` N/A

- [x] 🔴 **crypto_keylength** — Key lengths meet [NIST 2030 minimums](https://www.keylength.com/en/4/) by default.
  - *Note:* Ed25519 keys are fixed at 256 bits (~128-bit security level), which meets NIST 2030 recommendations. `[ ]` N/A

- [x] 🔴 **crypto_password_storage** — Passwords for external users are stored as iterated salted hashes (Argon2id, bcrypt, scrypt, PBKDF2).
  - *Note:* `[x]` N/A — *Justification: MiniChain has no user accounts/passwords; identity is Ed25519 keypairs, not password-based auth.*

- [x] 🔴 **crypto_random** — Cryptographic keys and nonces are generated using a CSPRNG; insecure generators (Math.random, rand()) are NOT used for security purposes.
  - *Note:* Keypairs are generated via PyNaCl's `SigningKey.generate()`, which uses libsodium's CSPRNG. Python's `random.randint()` is used only in `minichain/pow.py` to pick a starting nonce for Proof-of-Work mining — a non-secret, non-security-sensitive value, not a key or authentication nonce. `[ ]` N/A

- [x] 🟡 **delivery_unsigned** — Cryptographic hashes are NOT retrieved over plain HTTP without a signature check.
  - *Note:* `[x]` N/A — *Justification: the project has no software-delivery mechanism (no packaged binaries/checksums distributed over HTTP) to which this applies.*

---

## 🔬 Analysis

### Static Code Analysis

- [ ] 🔴 **static_analysis_fixed** — All medium+ severity vulnerabilities found by static analysis are fixed in a timely manner after confirmation.
  - *Note:* No dedicated static analysis tool is currently run, so this can't be evidenced either way. `.coderabbit.yaml` configures CodeRabbit for AI-assisted PR review/labeling, but that is not a substitute for a SAST tool (e.g., Bandit, Semgrep). `[ ]` N/A

- [ ] 🔵 **static_analysis_common_vulnerabilities** — The static analysis tool includes checks for common vulnerabilities in the language/environment (e.g., eslint-plugin-security, bandit, Slither). *(SUGGESTED)*
  - *Tool + ruleset:* None configured. `[ ]` N/A

- [ ] 🔵 **static_analysis_often** — Static analysis runs on every commit or at least daily (CI integration). *(SUGGESTED)*
  - *Evidence URL:* [.github/workflows/](../.github/workflows) contains `pr-checks.yml` (tests only), `update-badge.yml` (coverage badge), and `label-merge-conflicts.yml` — none run static analysis. `[ ]` N/A

### Dynamic Code Analysis

- [ ] 🔵 **dynamic_analysis** — At least one dynamic analysis tool is applied before major releases (fuzzer, web app scanner like OWASP ZAP, etc.). *(SUGGESTED)*
  - *Tool used:* None found. `[ ]` N/A — *Justification:*

- [x] 🔵 **dynamic_analysis_enable_assertions** — Dynamic analysis / testing runs with assertions enabled (not just production mode). *(SUGGESTED)*
  - *Note:* Tests run via `pytest` in CI ([.github/workflows/pr-checks.yml](../.github/workflows/pr-checks.yml)) with the default (non-optimized) interpreter, so Python `assert` statements are active.

- [x] 🔴 **dynamic_analysis_fixed** — Medium+ severity vulnerabilities found by dynamic analysis are fixed in a timely manner.
  - *Note:* `[x]` N/A — *Justification: no dynamic analysis tool is currently run, so none have been found.*

- [x] 🔵 **dynamic_analysis_unsafe** — If the project uses memory-unsafe languages (C/C++), memory safety tools (Valgrind, AddressSanitizer) are used. *(SUGGESTED)*
  - *Note:* `[x]` N/A — *Justification: the project is written entirely in Python, a memory-safe language.*

---

## 📎 Project-Specific Notes

> Add domain-specific notes here for Web3, Full-Stack, or AI projects.

### Web3 / Solidity Notes
- Scorecard does not audit Solidity-specific security. Use [Slither](https://github.com/crytic/slither) for `static_analysis` and `warnings` criteria.
- For `crypto_*` criteria, document which cryptographic primitives your contracts rely on (e.g., ECDSA in EVM is standard).
- Smart contract audit reports count as evidence for `know_secure_design`.

### Full-Stack / Next.js Notes
- For `crypto_password_storage`: document which auth library handles hashing (e.g., NextAuth + bcrypt).
- For `dynamic_analysis`: [OWASP ZAP](https://www.zaproxy.org/) can be run as a GitHub Action.

### AI / LLM Notes
- For `know_common_errors`: include awareness of prompt injection, data leakage, and model output validation.
- For `dynamic_analysis`: consider adversarial input testing as a form of dynamic analysis.

### MiniChain-Specific Notes
- Biggest open gaps found by this pass: no `SECURITY.md` (blocks `vulnerability_report_process`), no linter in CI (blocks all three `warnings_*` items), and no static/dynamic analysis tooling (blocks all of Analysis except the N/A items). Tagging a first release would also unlock the Change Control items.
- `report_responses` / `enhancement_responses` need a manual pass over GitHub Issues history — not derivable from the repo contents.

---

*This checklist complements [OpenSSF Scorecard](https://scorecard.dev/) (auto-detected checks) and is
inspired by the [OpenSSF Best Practices Badge](https://www.bestpractices.dev/en/criteria/0) passing criteria.*
