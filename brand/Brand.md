# MiniChain Brand Guide

MiniChain is a minimal, fully functional blockchain implemented in Python, built by [Stability Nexus](https://stability.nexus/) with three goals: **education**, **research**, and **innovation**. The brand should read the same way the codebase does — clean, minimal, and unpretentious. No visual noise, no unnecessary ornamentation.

## Logo

MiniChain's mark is an octahedron-style wireframe: eight triangular edges radiating from a central point, each vertex marked with a glowing node. It's meant to evoke a network graph — nodes connected by edges — rather than a literal chain, which fits a project about distributed state rather than links in a chain.

- [`logo.svg`](logo.svg) — the MiniChain mark, 330×330, transparent background. Use this as the primary logo wherever MiniChain is referenced on its own.
- [`org-logo.svg`](org-logo.svg) — the Stability Nexus organization mark, 500×500. Use alongside the MiniChain logo when representing the org/project pairing (as in the [README](../README.md) header), never as a substitute for it.

**Usage rules**

- Keep clear space around the logo equal to at least the radius of one vertex node.
- Do not recolor the gradient — it is the identifying feature of the mark.
- Do not stretch or skew; the mark is designed as a regular octahedron and should scale uniformly.
- Minimum display size: 32px, below which the vertex nodes become illegible.

## Favicons and Icons

- [`favicon.svg`](favicon.svg) — the MiniChain mark, suitable for use as a browser tab icon / site favicon. Reuses the same source as `logo.svg` since the mark is simple enough to stay legible at small sizes without a separate simplified variant.
- For platforms that require raster favicons (`.ico`, PNG sizes like 16×16/32×32/180×180 for Apple touch icons), export from `favicon.svg` at build time rather than hand-maintaining bitmap copies.

## Color Palette

Pulled directly from the logo's gradient and glow layers:

| Swatch | Hex | Role |
| ------ | --- | ---- |
| 🟩 | `#228B22` | Primary — forest green, gradient start |
| 🟢 | `#5A981A` | Primary support — edge glow |
| 🟡 | `#C8B209` | Accent — gradient midpoint |
| 🟠 | `#FFBF00` | Accent — gradient end |
| 🟡 | `#FFC517` | Highlight — gold glow, used as the badge label color in the README |
| 🫒 | `#91A511` | Node fill — vertex points |

**Usage rules**

- `#228B22` is the primary brand color — use it for the dominant accent in any MiniChain-branded surface (badges, links, headings).
- `#FFC517` / `#FFBF00` are gold accents — use sparingly, for highlights and call-to-action elements, not body text or large fills.
- Maintain WCAG AA contrast (4.5:1 for body text) when pairing these colors with text; the greens and golds above are tuned for use on dark or neutral backgrounds, not as text-on-white body copy.

## Typography

MiniChain doesn't currently ship custom web fonts — GitHub-rendered Markdown (README, docs) uses GitHub's default system font stack. For any future site, dashboard, or block explorer built for the project, the recommended pairing is:

- **Headings / UI:** [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) — a geometric sans with a slightly technical feel that matches the wireframe logo, without being a generic startup sans.
- **Body text:** [Inter](https://fonts.google.com/specimen/Inter) — high legibility at small sizes, wide language support.
- **Code / addresses / hashes:** [JetBrains Mono](https://www.jetbrains.com/lp/mono/) — monospace, disambiguates `0`/`O` and `1`/`l`/`I`, which matters for public keys, transaction hashes, and CLI output.

Fall back to the system font stack (`-apple-system, Segoe UI, Roboto, sans-serif`) if none of the above are loaded, rather than a generic web-safe serif.

## File Location

All brand assets and this guide live in the [`brand/`](.) folder at the repository root:

```
brand/
├── Brand.md       # this file
├── logo.svg        # primary MiniChain mark
├── org-logo.svg     # Stability Nexus organization mark
└── favicon.svg      # favicon-ready MiniChain mark
```
