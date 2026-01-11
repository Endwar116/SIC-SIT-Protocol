# SIC/SIT System - Conflicts Register

## Purpose

This document lists all identified conflicts, contradictions, or ambiguities in the SIC-SIT system documentation. Each conflict is traced to specific statements and resolved with a clear disposition.

**Date:** 2026-01-09  
**Version:** 1.0  
**Trace Source:** `canon/TRACE_PATCH_TABLE.csv`

---

## Conflict Summary

| Conflict ID | Type | Statements Involved | Resolution | Status |
|-------------|------|---------------------|------------|--------|
| C001 | Ownership Ambiguity | S029 | Clarified ownership | RESOLVED |
| C002 | Evidence Gap | S029, S030, S031 | Moved to TRL3_CLAIMED | RESOLVED |
| C003 | Missing Definition | S036, S037 | Moved to UNKNOWN | RESOLVED |
| C004 | Missing Definition | S038, S039, S040 | Moved to UNKNOWN | RESOLVED |
| C005 | Missing Mapping | S041 | Moved to UNKNOWN | RESOLVED |
| C006 | Missing Schema | S042, S043 | Moved to UNKNOWN | RESOLVED |

**Total Conflicts:** 6  
**Resolved:** 6  
**Pending:** 0

---

## Detailed Conflicts

### C001: Compression Rate Ownership Ambiguity

**Type:** Ownership Ambiguity

**Statements Involved:**
- S029: "60.7% compression rate is claimed"

**Issue:**
The 60.7% compression rate is claimed in SIC's WHITEPAPER.md (Section 7.3), but the Semantic Folding algorithm is implemented in SIT's `semantic_folding.py`. This creates ambiguity about which repository owns the claim.

**Where Seen:**
- `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (Section 7.3)
- `SIC-SIT-Protocol/folding/semantic_folding.py` (implementation)

**Repo Evidence:**
- SIC WHITEPAPER: Contains the claim
- SIT folding code: Contains the algorithm

**Resolution:**
- **Claim Ownership:** SIT (algorithm owner)
- **Evidence Location:** SIC WHITEPAPER (documentation)
- **Disposition:** KEEP with clarification in `ownership_split.md`

**Status:** RESOLVED

---

### C002: Performance Claims Lack Experimental Evidence

**Type:** Evidence Gap

**Statements Involved:**
- S029: "60.7% compression rate is claimed"
- S030: "0% semantic drift over 20 rounds is claimed"
- S031: "<100ms consensus latency is claimed"

**Issue:**
All three performance claims are stated in WHITEPAPER.md but lack experimental logs or reproducible benchmarks. This violates the "trace to evidence" requirement.

**Where Seen:**
- `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (Section 7.3)

**Repo Evidence:**
- No `lab/benchmark_results.jsonl` or similar file found
- No experimental setup documentation found

**Resolution:**
- **TRL Binding:** Downgraded from TRL4_EVIDENCE to TRL3_CLAIMED
- **Evidence Strength:** Downgraded from SOFT to NONE
- **Disposition:** KEEP as claims but clearly marked as unverified

**Status:** RESOLVED

---

### C003: Missing Mathematical Definitions (k, τ)

**Type:** Missing Definition

**Statements Involved:**
- S036: "k coefficient is mentioned but formula not defined"
- S037: "τ (tau) threshold is mentioned but value not defined"

**Issue:**
Both k coefficient and τ threshold are mentioned in WHITEPAPER.md but no formulas or values are provided.

**Where Seen:**
- `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (mentions k and τ)

**Repo Evidence:**
- No formula for k found in any repo
- No value for τ found in any repo

**Resolution:**
- **Disposition:** MOVE_TO_UNKNOWN
- **Priority:** P1 (High) - required for reproducibility
- **Action Required:**安安 needs to provide formulas or mark as future work

**Status:** RESOLVED (moved to UNKNOWN_REGISTER.md)

---

### C004: Missing Term Definitions (TSIG, EQG, GBP)

**Type:** Missing Definition

**Statements Involved:**
- S038: "TSIG (Temporal Semantic Integrity Guard) is mentioned but not defined"
- S039: "EQG (Entropy Quantification Gate) is mentioned but not defined"
- S040: "GBP (Governance Boundary Protocol) is mentioned but not defined"

**Issue:**
These terms appear in the meta-cognition architecture document but are not defined in any of the three repositories.

**Where Seen:**
- Meta-cognition architecture document (external to repo)

**Repo Evidence:**
- No definition found in SIC, SIT, or SIC-SIT-Protocol

**Resolution:**
- **Disposition:** MOVE_TO_UNKNOWN
- **Priority:** P2 (Medium) - conceptual clarity but not blocking
- **Action Required:** Either define in repo or remove from meta-cognition

**Status:** RESOLVED (moved to UNKNOWN_REGISTER.md)

---

### C005: Missing Conceptual Mapping (17 Axioms ↔ 107 Tools)

**Type:** Missing Mapping

**Statements Involved:**
- S041: "Relationship between 17 axioms and 107 tools is not defined"

**Issue:**
The meta-cognition architecture mentions "107 tools" but there is no explicit mapping to the 17 constitutional axioms.

**Where Seen:**
- Meta-cognition architecture document (external to repo)
- `SIC-SIT-Protocol/sic-sit-constitution/constitution/AXIOMS.md` (17 axioms)

**Repo Evidence:**
- No mapping file found in any repo

**Resolution:**
- **Disposition:** MOVE_TO_UNKNOWN
- **Priority:** P2 (Medium) - conceptual clarity but not blocking
- **Action Required:** Create mapping or clarify that they are independent

**Status:** RESOLVED (moved to UNKNOWN_REGISTER.md)

---

### C006: Missing Interface Schemas (SIC Packet)

**Type:** Missing Schema

**Statements Involved:**
- S042: "SIC packet schema is not canonically defined"
- S043: "Relationship between Skeleton JSON and SIC packet is not defined"

**Issue:**
Validators exist for "SIC packet" but no canonical schema file is found. The relationship between Skeleton JSON and SIC packet is also unclear.

**Where Seen:**
- `SIC-SIT-Protocol/validators/sic_pkt.py` (validator exists)
- No schema file found

**Repo Evidence:**
- Validator code exists
- No `sic_packet_schema.json` or similar file found

**Resolution:**
- **Disposition:** MOVE_TO_UNKNOWN
- **Priority:** P0 (Critical) - required for interoperability
- **Action Required:** Create canonical schema or clarify that Skeleton JSON is the only interface

**Status:** RESOLVED (moved to UNKNOWN_REGISTER.md)

---

## Resolution Summary

### KEEP (with clarification)
- C001: Compression rate ownership (clarified in `ownership_split.md`)

### DOWNGRADE (TRL binding)
- C002: Performance claims (TRL4_EVIDENCE → TRL3_CLAIMED)

### MOVE_TO_UNKNOWN
- C003: k coefficient, τ threshold
- C004: TSIG, EQG, GBP
- C005: 17 axioms ↔ 107 tools mapping
- C006: SIC packet schema, Skeleton JSON ↔ SIC packet relationship

---

## Action Items

### For 安安 (User)
1. **P0 (Critical):** Provide SIC packet schema or confirm Skeleton JSON is the only interface
2. **P1 (High):** Provide formulas for k coefficient and τ threshold
3. **P2 (Medium):** Define TSIG, EQG, GBP or remove from meta-cognition
4. **P2 (Medium):** Create mapping between 17 axioms and 107 tools or clarify independence

### For Lab (Experimental Validation)
1. **P1 (High):** Conduct benchmarks to verify 60.7% compression rate
2. **P1 (High):** Conduct long-term tests to verify 0% semantic drift
3. **P1 (High):** Measure consensus latency under production load

---

## Audit Trail

| Date | Action | Conflict IDs | Performed By |
|------|--------|--------------|--------------|
| 2026-01-09 | Initial conflict identification | C001-C006 | Manus AI (尾德3) |
| 2026-01-09 | Resolved all conflicts | C001-C006 | Manus AI (尾德3) |

---

**End of Conflicts Register**
