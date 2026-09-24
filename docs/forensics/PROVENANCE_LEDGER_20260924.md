# Provenance ledger — 2026-09-24

Status: EVIDENCE_LEDGER / claim_allowed=false

Invariant: SOURCE != ARTEFACT != EXECUTION != EVIDENCE != CLAIM

## Step 1

- This repository is a fork of `yumiaura/myCat`, created on 2025-10-23.
- The upstream profile repo `yumiaura/yumiaura` contained `images/cat.gif` by commit `21b5312d36f491cbe5ed2acc505882590c45966f` on 2025-10-21. Git blob: `12004b1bbd6dd41d95b0bd22b95079971101f28d`, size 20,262 bytes.
- The fork baseline inspected around 2025-10-23 had no paths matching `llm`, `ollama`, `openai`, or `chat`.
- Upstream commit `2d894ecccd5b6af30fee7e1995debb4fd27a1d44` dated 2025-11-13 added `mycat/llm.py`, `mycat/llm_ollama.py`, `mycat/llm_openai.py`, `mycat/llm_prompt.py`, `mycat/llm_ui.py`, and `mycat/PROMT.j2`.
- Public user-side temporal markers predate that upstream LLM addition:
  - `rafaelmeloreisnovo/RafNet-Core@d5ace6d026fe02ff5290b6e2f2f94fa7d2856d2e` — 2025-07-02 — local API + generated RafaelIA script.
  - `instituto-Rafael/publicacientiespiritual@bdad50832457d46f7599fe131a3476fc52f1108e` — 2025-07-29 — LLM/RafaelIA document.
- These markers establish temporal precedence only. They do not prove access, copying, derivation, targeting, or intent.
- `yumiaura/followme` is a later public repository (created 2026-04-23) whose current pipeline fetches repositories, evaluates them with local Ollama, follows profiles, stars repositories, and can loop indefinitely. This proves a later automation mechanism, not that it existed in 2025.
- Current upstream `mycat/github_notify.py` polls GitHub notifications, public events, and followers, and deduplicates by event/thread IDs. This is a concrete feed-generation/dedup surface for reproducible testing.

## External billing pointer

Order `GPA.3323-3447-1555-24204` and the reported BB gift-card/redeem route remain external evidence. The Gmail receipt labels the Copilot Pro+ order payment method as Pix; the primary artifact for the gift-card/redeem path is still unresolved and must not be invented.

## Boundaries

- Temporal precedence != causation.
- Current absence of an event != proof it was deleted.
- Event/thread-ID deduplication != BLAKE3 collision.
- Cryptographic collision requires distinct byte streams with the same full digest.
- Structural identity collision requires evidence that distinct raw events map to the same canonical/event identifier.

## TOKEN_VAZIO

- TOKEN_VAZIO_GIF_VIDEO_RELATION
- TOKEN_VAZIO_2025_AUTOMATION
- TOKEN_VAZIO_HISTORICAL_FOLLOW_COUNTS
- TOKEN_VAZIO_DELETED_EVENTS
- TOKEN_VAZIO_PAYMENT_ROUTE
- TOKEN_VAZIO_CANONICALIZATION_COLLISION

## Next

Preserve historical event/media identities, locate historical account-activity snapshots, establish upstream LLM first-parent provenance, and test raw-event -> canonicalization -> event-ID/dedup independently from cryptographic hashing.


## Step 2 — primary visual evidence

Drive image `1XJYEel67Ipe1js9sTanZn3_927ld3kqL` is a 99,086-byte PNG (Drive metadata: created 2026-08-06, updated 2026-08-03). Visual inspection shows a GitHub Actions Copilot job with **Failure**, total duration **5s**, and this annotation:

> The job was not started because recent account payments have failed or your spending limit needs to be increased. Please check the 'Billing & plans' section in your settings.

Raw fetched image SHA-256:

`0c1e61b682aedfa16e08477566474ea8fad0666cfd5699e5d6ba5f66a5913725`

Additional preserved visual pointers:

- `1-487AMcbXcSMScSOjFvtRFx6Pg7wuTRZ` — "Screenshot (28 de jul de 2026 23:23:10)" — SHA-256 `d6f6688247242b7019601c5e5451ec074bcb26e658eac00493d5a81c40139243`.
- `172FHFwe42_5Q4-Ae5qx07U5X4zsBJBfQ` — GitHub mobile menu showing Copilot — SHA-256 `d24a2a2103442584a6ef94560cf4f0de406bc00fd21d5878be21d7dd3acbe306`.
- `10dQFH0SZVBMYjJK4P_uc9AjNA1Zqg8q-` — GitHub branch view showing `copilot/*` branches — SHA-256 `e4554844c304674c65e642215124e62893a683050e6aad077612232c2daaa089`.

**Boundary:** this proves that a billing/spending gate prevented at least one Copilot job from starting. It does not identify the root cause among failed payment, spending-limit configuration, entitlement/account mapping, or any intentional intervention. No BLAKE3 digest is asserted here because one was not computed in this environment.
