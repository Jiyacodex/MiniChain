# Contributing to MiniChain

Thanks for your interest in contributing to MiniChain! This document explains how to get involved, from discussing an idea to getting a pull request merged.

## Before You Start: Discuss It First

**Every contribution — bug fix, feature, or refactor — should be discussed before you start writing code.** This avoids duplicate work and makes sure the change fits the project's minimality-first philosophy.

1. Join the [Stability Nexus Discord server](https://discord.gg/YzDKeEfWtS).
2. Discuss your issue, bug, or feature idea in the project's channel/thread: [MiniChain discussion](https://discord.com/channels/995968619034984528/1471163521877410045).
3. If it's a confirmed bug or an agreed-upon feature, open a matching GitHub Issue in this repository describing the problem and the proposed approach.

Only after that discussion should you start implementation — this is the first and most important rule below.

## Contribution Checklist

- 🔴 **MUST** — Discuss non-trivial changes in Discord (see above) or in a GitHub Issue before opening a PR.
- 🔴 **MUST** — Follow the module layout and architecture constraints described in [agent.md](agent.md) (one concern per module under `minichain/`, state changes go through `state.py`, etc.).
- 🔴 **MUST** — Add or update tests under `tests/` for any new or changed behavior.
- 🔴 **MUST** — Run `pytest` locally and confirm it passes before opening a PR.
- 🔴 **MUST** — Sign off every commit per the [Developer Certificate of Origin](DCO.md).
- 🟡 **SHOULD** — Keep PRs focused on a single logical change; split unrelated changes into separate PRs.
- 🟡 **SHOULD** — Update relevant docs ([README.md](README.md), [agent.md](agent.md), [brand/Brand.md](brand/Brand.md)) when behavior, commands, or conventions change.
- 🟡 **SHOULD** — Check `pytest --cov=minichain` to make sure coverage on touched modules doesn't regress.
- 🔵 **SUGGESTED** — Link the Discord discussion or GitHub Issue in your PR description for context.
- 🔵 **SUGGESTED** — Prefer small, incremental PRs over large ones when the change can reasonably be split.

## How to Contribute

1. **Discuss** the change in Discord or a GitHub Issue (see above).
2. **Fork** the repository and create a branch off `main`.
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt -r requirements-test.txt
   ```
4. **Make your changes**, following the conventions in [agent.md](agent.md).
5. **Test:**
   ```bash
   pytest
   ```
6. **Sign off your commits** per the [DCO](DCO.md) (`git commit -s`).
7. **Open a pull request** against `main`, describing the problem and the fix, and linking back to the Discord discussion or issue.

## Getting Help

- Ask questions in the [Stability Nexus Discord](https://discord.gg/YzDKeEfWtS).
- Please do not contact contributors directly — keep discussion in Discord or GitHub Issues so it stays public and searchable.

---

## Contributors

By having yourself in the table below, all your contributions to this project
are made under the terms of the [Developer Certificate of Origin](DCO.md).

| Name                             | Github Username    | Discord Username   | Email Address                |
| --------------------------------- | ------------------- | ------------------- | ------------------------------ |
| Bruno Woltzenlogel Paleo          | @Zahnentferner       | @b.wp                | zahnentferner@gmail.com        |
| TODO                              | TODO                 | TODO                 | TODO                           |
