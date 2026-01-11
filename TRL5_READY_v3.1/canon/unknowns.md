# SIC/SIT Canon - Unknowns

## Purpose

This document lists all identified gaps, conflicts, and unknowns in the SIC-SIT system. **No resolution is attempted**—only flagging.

---

## UNKNOWN-001: example-03-complete.json is not a skeleton

**Category:** File Classification

**Description:** The file `example-03-complete.json` is listed in the TRL4 minimal set, but it is not a skeleton JSON file. It is a structural preview of the ASEE v2 document.

**Trace:**
- `SIC-Semantic-Infinite-Context/example-03-complete.json`
- Validation result: FAILED (missing entity, memory, state, meta fields)

**Impact:** Does not affect TRL4 status (2/2 skeleton examples passed).

**Status:** Flagged, no action needed.

---

## UNKNOWN-002: Relationship between 17 axioms and 107 tools

**Category:** Conceptual Mapping

**Description:** The meta-cognition architecture mentions "107 tools" (超高維腦袋邏輯學習地圖), but there is no explicit mapping between these tools and the 17 constitutional axioms (A1-A17) in the repo.

**Trace:**
- Source A: `107_tools_extracted.md` (from PDF)
- Source B: `SIC-SIT-Protocol/sic-sit-constitution/constitution/AXIOMS.md`

**Impact:** Cross-AI reasoning may be inconsistent if the relationship is not defined.

**Status:** Flagged, requires manual mapping.

---

## UNKNOWN-003: No canonical schema for "SIC packet"

**Category:** Interface Definition

**Description:** The term "SIC packet" appears in validators (`sic_pkt.py`) and other files, but there is no canonical schema definition like `skeleton-schema.json`.

**Trace:**
- `SIC-SIT-Protocol/validators/sic_pkt.py`
- No corresponding `sic-packet-schema.json` found

**Impact:** Unclear what constitutes a valid "SIC packet" vs. a "skeleton JSON".

**Status:** Flagged, schema missing.

---

## UNKNOWN-004: Relationship between Skeleton JSON and SIC packet

**Category:** Interface Definition

**Description:** It is unclear whether "Skeleton JSON" and "SIC packet" are the same thing, or if one is a subset/superset of the other.

**Trace:**
- `skeleton-schema.json` defines Skeleton JSON
- `sic_pkt.py` validates SIC packets
- No documentation explicitly relates the two

**Impact:** Ambiguity in interface definitions.

**Status:** Flagged, requires clarification.

---

## UNKNOWN-005: No experimental data for 60.7% compression rate

**Category:** Claim Verification

**Description:** The whitepaper claims a 60.7% compression rate, but no experimental log or trace data is found in the repo.

**Trace:**
- Claim: `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (Section 7.3)
- Evidence: None found

**Impact:** Claim cannot be independently verified.

**Status:** Flagged, experimental data missing.

---

## UNKNOWN-006: No experimental data for 0% semantic drift over 20 rounds

**Category:** Claim Verification

**Description:** The whitepaper claims 0% semantic drift over 20 rounds, but no experimental log or trace data is found in the repo.

**Trace:**
- Claim: `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (Section 7.1)
- Evidence: None found

**Impact:** Claim cannot be independently verified.

**Status:** Flagged, experimental data missing.

---

## UNKNOWN-007: No experimental data for <100ms consensus latency

**Category:** Claim Verification

**Description:** The whitepaper claims multi-model consensus in <100ms, but no experimental log or trace data is found in the repo.

**Trace:**
- Claim: `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (Section 7.2)
- Evidence: None found

**Impact:** Claim cannot be independently verified.

**Status:** Flagged, experimental data missing.

---

## UNKNOWN-008: TSIG definition missing

**Category:** Term Definition

**Description:** The term "TSIG" (Temporal Semantic Integrity Guard) appears in the meta-cognition architecture but has no definition or implementation in the repo.

**Trace:**
- Mentioned in: `meta_cognition_clean.md`
- Implementation: Not found

**Impact:** Cannot use TSIG in cross-AI reasoning without definition.

**Status:** Flagged, definition missing.

---

## UNKNOWN-009: EQG definition missing

**Category:** Term Definition

**Description:** The term "EQG" (Entropy Quantification Gate) appears in the meta-cognition architecture but has no definition or implementation in the repo.

**Trace:**
- Mentioned in: `meta_cognition_clean.md`
- Implementation: Not found

**Impact:** Cannot use EQG in cross-AI reasoning without definition.

**Status:** Flagged, definition missing.

---

## UNKNOWN-010: GBP definition missing

**Category:** Term Definition

**Description:** The term "GBP" (Governance Boundary Protocol) appears in the meta-cognition architecture but has no definition or implementation in the repo.

**Trace:**
- Mentioned in: `meta_cognition_clean.md`
- Implementation: Not found

**Impact:** Cannot use GBP in cross-AI reasoning without definition.

**Status:** Flagged, definition missing.

---

## UNKNOWN-011: k coefficient formula missing

**Category:** Mathematical Definition

**Description:** The whitepaper mentions a "k coefficient" (k = 0.1) but does not provide the formula or derivation.

**Trace:**
- Mentioned in: `SIC-Semantic-Infinite-Context/WHITEPAPER.md`
- Formula: Not found

**Impact:** Cannot reproduce or verify k = 0.1 value.

**Status:** Flagged, formula missing.

---

## UNKNOWN-012: τ (tau) threshold value missing

**Category:** Mathematical Definition

**Description:** The whitepaper mentions a "τ threshold" (τ = 0.7) but does not provide context or formula.

**Trace:**
- Mentioned in: `SIC-Semantic-Infinite-Context/WHITEPAPER.md`
- Formula: Not found

**Impact:** Cannot reproduce or verify τ = 0.7 value.

**Status:** Flagged, formula missing.

---

## Summary

| Category | Count |
|----------|-------|
| File Classification | 1 |
| Conceptual Mapping | 1 |
| Interface Definition | 2 |
| Claim Verification | 3 |
| Term Definition | 3 |
| Mathematical Definition | 2 |
| **Total** | **12** |

---

**End of Unknowns Canon**
