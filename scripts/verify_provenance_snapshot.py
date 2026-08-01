#!/usr/bin/env python3
"""Valida o snapshot de proveniência sem dependências externas."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ALLOWED_STATES = {
    "PROVADO",
    "EVIDENCIADO",
    "HIPÓTESE",
    "MODELO_ANALÓGICO",
    "PARÁBOLA",
    "REFUTADO",
    "TOKEN_VAZIO",
}
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    raise ValueError(message)


def require_mapping(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{field} must be an object")
    return value


def require_list(value: Any, field: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{field} must be an array")
    return value


def validate(path: Path) -> str:
    raw = path.read_bytes()
    data = require_mapping(json.loads(raw), "root")

    if data.get("schema") != "rafaelia.github-upstream-provenance.v1":
        fail("unsupported schema")
    if data.get("privacy_class") != "PUBLIC_METADATA_ONLY":
        fail("privacy_class must remain PUBLIC_METADATA_ONLY")

    relation = require_mapping(data.get("pre_application_relation"), "pre_application_relation")
    for field in ("merge_base_commit", "upstream_head_commit", "fork_head_commit"):
        value = relation.get(field)
        if not isinstance(value, str) or not SHA40.fullmatch(value):
            fail(f"{field} must be a lowercase 40-character Git SHA")
    for field in ("ahead_by", "behind_by"):
        value = relation.get(field)
        if not isinstance(value, int) or value < 0:
            fail(f"{field} must be a non-negative integer")

    classifications = require_list(data.get("classifications"), "classifications")
    if not classifications:
        fail("at least one classification is required")

    seen_claims: set[str] = set()
    for index, item in enumerate(classifications):
        claim = require_mapping(item, f"classifications[{index}]")
        claim_id = claim.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id.startswith("CLM-"):
            fail(f"invalid claim_id at index {index}")
        if claim_id in seen_claims:
            fail(f"duplicate claim_id: {claim_id}")
        seen_claims.add(claim_id)
        if claim.get("epistemic_state") not in ALLOWED_STATES:
            fail(f"invalid epistemic_state for {claim_id}")
        if claim.get("claim_allowed") is not False:
            fail(f"claim_allowed must remain false for {claim_id}")

    controls = require_mapping(data.get("risk_controls"), "risk_controls")
    if controls.get("automatic_upstream_sync") is not False:
        fail("automatic_upstream_sync must remain false")

    legal = require_mapping(data.get("legal_posture"), "legal_posture")
    required_legal = {
        "no_identity_accusation",
        "no_personal_data_enrichment",
        "no_circumvention",
        "evidence_minimization",
    }
    for field in required_legal:
        if legal.get(field) is not True:
            fail(f"legal_posture.{field} must remain true")

    tokens = require_list(data.get("tokens_vazios"), "tokens_vazios")
    if not tokens:
        fail("unresolved gaps must be explicit TOKEN_VAZIO entries")
    for index, item in enumerate(tokens):
        token = require_mapping(item, f"tokens_vazios[{index}]")
        if not str(token.get("token", "")).startswith("TOKEN_VAZIO_"):
            fail(f"invalid TOKEN_VAZIO at index {index}")
        if not token.get("next_gate"):
            fail(f"missing next_gate at index {index}")

    return hashlib.sha256(raw).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "snapshot",
        nargs="?",
        default="provenance/upstream_snapshot_2026-08-01.json",
        type=Path,
    )
    args = parser.parse_args()

    try:
        digest = validate(args.snapshot)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"PROVENANCE_VALIDATION=FAIL: {exc}", file=sys.stderr)
        return 1

    print("PROVENANCE_VALIDATION=PASS")
    print(f"SNAPSHOT_SHA256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
