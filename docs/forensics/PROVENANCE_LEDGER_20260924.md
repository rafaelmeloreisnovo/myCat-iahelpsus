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
