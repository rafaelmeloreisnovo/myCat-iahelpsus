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


## Step 3 — exact provider chain for the Copilot billing gate

The visual billing-gate screenshot can now be bound to provider metadata in the private producer repository `rafaelmeloreisnovo/Rafaelia_Private`.

- PR: `#35`, title `[WIP] Unify technical structure of RAFAELIA repositories`.
- Head: `copilot/integrate-repositories-structure`.
- Head SHA: `e68a4fdb28781448009e4d9b67482aa01aaa4ada` (`Initial plan`, Copilot bot, 2025-11-25 06:05:28Z).
- Exact dynamic run: `19659988066`, `Running Copilot`, created 06:05:33Z, completed 06:05:38Z, conclusion `failure`.
- Exact job: `56304280175`, name `copilot`, 06:05:34Z..06:05:37Z, `steps=[]`, `runner_id=0`, empty runner name.
- The preserved screenshot for this run states that the job was not started because recent account payments had failed **or** the spending limit needed to be increased.
- Two owner comments invoking `@copilot` generated two more dynamic runs on the same head SHA:
  - `19660076585`: 06:09:54Z..06:09:59Z; job `56304547676`; failure; `steps=[]`; `runner_id=0`.
  - `19660127113`: 06:12:18Z..06:12:23Z; job `56304697794`; failure; `steps=[]`; `runner_id=0`.
- Current job-log downloads for all three return HTTP 410; the run/job metadata remains available.
- PR #35 was later merged on 2025-12-03 with merge SHA `94d0776d25bd856cc8150557ec04d802c6659a3b`; provider metadata reports one commit and zero changed files/additions/deletions.
- The historical head branch is absent from the current branch list; PR/run metadata proves that it existed. Its current absence does not establish when or why it was deleted.

**Date correction:** the underlying Copilot billing/spending event is **2025-11-25**. The August-2026 Drive timestamps belong to preservation/archive of the screenshot, not the original failure.

**Boundary:** repeated failure before runner steps is observable. The screenshot binds a billing/spending precondition to the first run. This does not establish deliberate targeting, deletion of logs, or any BLAKE3 collision.


## Step 4 — empty commit and explicit branch deletion

Git object identity resolves the apparent zero-diff lifecycle of `Rafaelia_Private#35`.

- Head `e68a4fdb28781448009e4d9b67482aa01aaa4ada` has tree `4ad3f38889d32e67b508154a34bfa05fb56ee1c1`, zero additions/deletions and no files.
- Its parent `bf3822b6ad8546f1e36b8534318307de512653f4` has **the same tree SHA**. The Copilot `Initial plan` commit was therefore an empty/no-op Git commit by tree identity.
- Merge `94d0776d25bd856cc8150557ec04d802c6659a3b` has tree `a13e9664a0fe1eab8c70e602d09e9f6247f83582`.
- Its first parent `844d966e5542959032704b781e4841ff0584f38e` has **the same merge tree SHA**. The merge introduced no file-tree delta into `main`.
- PR timeline: ready-for-review 09:36:05Z → merged/closed 09:36:11Z → `head_ref_deleted` 09:36:19Z on 2025-12-03.
- The provider attributes `head_ref_deleted` to `rafaelmeloreisnovo`. That identifies the authority/account attributed to the event, not the human/UI mechanism that caused it.
- Timeline also preserves `copilot_work_finished_failure` events matching all three 2025-11-25 dynamic Copilot attempts.

This specific branch deletion was **not silent**, and the object graph shows there was no file payload in the head commit to erase. It is not evidence of cryptographic collision or content replacement.


## Step 4 — Git object closure for linked PR #35

The linked `Rafaelia_Private#35` head `e68a4fdb28781448009e4d9b67482aa01aaa4ada` and its parent share the same tree `4ad3f38889d32e67b508154a34bfa05fb56ee1c1`; the head reports zero additions/deletions and no changed files.

The merge `94d0776d25bd856cc8150557ec04d802c6659a3b` and its first parent share tree `a13e9664a0fe1eab8c70e602d09e9f6247f83582`.

The PR timeline explicitly records `head_ref_deleted` at 2025-12-03T09:36:19Z, eight seconds after merge/close. Therefore this specific lifecycle is a provider-visible empty/no-op commit followed by an explicitly recorded branch removal, not evidence of a removed file-tree delta.


## Step 5 — public contact, AI chronology, and social automation boundary

### Contact and public access route

- 2025-10-23 17:46:10Z — `rafaelmeloreisnovo` commented on upstream commit `d2c9c04...`: “Hi how are you. How you find me”.
- 17:55:12Z — `yumiaura` replied on that commit that they were “watching” the account and thanked it for following. The reply is independently preserved in a GitHub notification email.
- 17:58:29Z — `rafaelmeloreisnovo` posted a long public technical plan on upstream commit `1ff5862...`, covering license/governance, CONTRIBUTING/SECURITY/CODEOWNERS, lint/type/pre-commit, CI/CD, packaging, docs/GIF and tests.
- Later that day DatMayo committed contribution/documentation work and opened PR #5; it was merged at 21:58Z. The upstream added a license the next day. These are generic engineering topics; timing and overlap are recorded, not promoted to derivation.

### AI path

- PR #25 by `king-tri-ton`, merged 2025-11-01, introduced an **OpenAI API** chat companion.
- Upstream commit `2d894ecccd5b6af30fee7e1995debb4fd27a1d44` by `yumiaura`, dated 2025-11-13, added `llm_ollama.py` together with the split LLM modules. This is the earliest exact myCat Ollama-path evidence found in this audit.
- User-side public evidence predates it:
  - `RafNet-Core@d5ace6d0...` — 2025-07-02 — local API + generated RafaelIA script.
  - `publicacientiespiritual@bdad5083...` — 2025-07-29 — LLM/RafaelIA material.
- Targeted pre-2025-11-13 commit searches found no exact user-side marker for `Ollama`, `llama`, `11434`, `GGUF`, or `llama.cpp`. The supported precedence claim is therefore **public AI/local-API material**, not an Ollama-specific implementation.

### Current social automation

On 2026-09-24 the public `yumiaura` profile displays roughly 7k followers, 18.6k following and 3.5k stars. Its README links the sentence about following a visitor because their project “caught my interest” to `yumiaura/followme`. That sentence entered the profile in commit `ad732a49016d2eec6d51be7290dece5276156c8b` on 2026-05-29.

`followme` is a later public mechanism that uses local Ollama scoring and can automatically follow profiles and star repositories, including repeated/infinite operation.

**Boundary:** this proves a public contact/access path and a later mass-social automation mechanism. It does not prove that `followme` or an equivalent bot was operating in October 2025, nor that later myCat AI work was derived from RafaelIA.
