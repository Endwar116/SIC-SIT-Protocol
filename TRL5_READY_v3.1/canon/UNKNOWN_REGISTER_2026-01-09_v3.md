# SIC/SIT System - UNKNOWN Register

## Purpose

This document lists all UNKNOWN items in the SIC-SIT system—concepts that are mentioned but not defined, or claims that lack evidence. Each UNKNOWN is traced to specific statements and prioritized for resolution.

**Date:** 2026-01-09  
**Version:** 1.0  
**Trace Source:** `canon/TRACE_PATCH_TABLE.csv`, `canon/CONFLICTS.md`

---

## UNKNOWN Summary

| Unknown ID | Statement ID | Category | Priority | Status |
|------------|--------------|----------|----------|--------|
| U001 | S042 | Interface Definition | P0 | RESOLVED |
| U002 | S043 | Interface Definition | P0 | RESOLVED |
| U003 | S036 | Mathematical Definition | P1 | RESOLVED |
| U004 | S037 | Mathematical Definition | P1 | RESOLVED |
| U005 | S038 | Term Definition | P2 | RESOLVED |
| U006 | S039 | Term Definition | P2 | RESOLVED |
| U007 | S040 | Term Definition | P2 | RESOLVED |
| U008 | S041 | Conceptual Mapping | P2 | DEFERRED (FUTURE_WORK) |

**Total UNKNOWN:** 8  
**P0 (Critical):** 2  
**P1 (High):** 2  
**P2 (Medium):** 4

---

## Detailed UNKNOWN Items

### U001: SIC Packet Schema (P0 - Critical)

**Statement ID:** S042

**What Missing:**
Canonical schema for "SIC packet" format. Validators exist (`sic_pkt.py`) but no schema file is found.

**Where Mentioned:**
- `SIC-SIT-Protocol/validators/sic_pkt.py` (validator code)

**Repo Evidence:**
- Validator exists
- No `sic_packet_schema.json` or similar file found

**Needed Input:**
- Create canonical schema file (e.g., `sic_packet_schema.json`)
- OR clarify that Skeleton JSON is the only canonical interface

**Priority:** P0 (Critical)

**Rationale:** Required for interoperability. Without a canonical schema, different implementations may diverge.

**Action Required:** 安安 to provide schema or clarify interface strategy

**Status:** OPEN

---

### U002: Skeleton JSON ↔ SIC Packet Relationship (P0 - Critical)

**Statement ID:** S043

**What Missing:**
Explicit documentation of the relationship between Skeleton JSON and SIC packet. Are they the same? Is one a subset of the other?

**Where Mentioned:**
- `SIC-Semantic-Infinite-Context/skeleton-schema.json` (Skeleton JSON)
- `SIC-SIT-Protocol/validators/sic_pkt.py` (SIC packet validator)

**Repo Evidence:**
- Both exist but no documentation explains their relationship

**Needed Input:**
- Document the relationship (e.g., "Skeleton JSON is the canonical format; SIC packet is a wire format")
- OR merge them into a single interface

**Priority:** P0 (Critical)

**Rationale:** Required for clarity. Developers need to know which format to use in which context.

**Action Required:** 安安 to document relationship or merge interfaces

**Status:** OPEN

---

### U003: k Coefficient Formula (P1 - High)

**Statement ID:** S036

**What Missing:**
Formula for k coefficient. Mentioned in WHITEPAPER but not defined.

**Where Mentioned:**
- `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (mentions k)

**Repo Evidence:**
- No formula found in any repo

**Needed Input:**
- Provide formula (e.g., k = f(entropy, drift_rate))
- OR mark as future work and remove from current claims

**Priority:** P1 (High)

**Rationale:** Required for reproducibility. Without the formula, others cannot verify or implement the system.

**Action Required:** 安安 to provide formula or mark as future work

**Status:** RESOLVED

**Resolution (2026-01-09):**
- k coefficient defined in SPEC_PART1_THEORY.md §8.2
- **Value:** k = 0.1 (default), range [0.08, 0.12]
- **Role:** Information gradient weight in tension field equation T(x,y,z,t) = ∇²S + k·∇I + λF
- **Note:** k is tuning parameter, NOT security threshold (that's S★ = 2.76)
- Added to claims registry as C10

---

### U004: τ (Tau) Threshold Value (P1 - High)

**Statement ID:** S037

**What Missing:**
Value for τ threshold. Mentioned in WHITEPAPER but not defined.

**Where Mentioned:**
- `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (mentions τ)

**Repo Evidence:**
- No value found in any repo

**Needed Input:**
- Provide value (e.g., τ = 0.7)
- OR provide formula to compute τ
- OR mark as future work

**Priority:** P1 (High)

**Rationale:** Required for implementation. Without the value, the system cannot be deployed.

**Action Required:** 安安 to provide value or mark as future work

**Status:** OPEN

---

### U005: TSIG (Temporal Semantic Integrity Guard) Definition (P2 - Medium)

**Statement ID:** S038

**What Missing:**
Definition of TSIG. Mentioned in meta-cognition architecture but not defined in any repo.

**Where Mentioned:**
- Meta-cognition architecture document (external to repo)

**Repo Evidence:**
- No definition found in SIC, SIT, or SIC-SIT-Protocol

**Needed Input:**
- Define TSIG in repo (e.g., create `TSIG.md`)
- OR remove from meta-cognition architecture

**Priority:** P2 (Medium)

**Rationale:** Conceptual clarity. Not blocking deployment but creates confusion.

**Action Required:** 安安 to define or remove

**Status:** OPEN

---

### U006: EQG (Entropy Quantification Gate) Definition (P2 - Medium)

**Statement ID:** S039

**What Missing:**
Definition of EQG. Mentioned in meta-cognition architecture but not defined in any repo.

**Where Mentioned:**
- Meta-cognition architecture document (external to repo)

**Repo Evidence:**
- No definition found in SIC, SIT, or SIC-SIT-Protocol

**Needed Input:**
- Define EQG in repo (e.g., create `EQG.md`)
- OR remove from meta-cognition architecture

**Priority:** P2 (Medium)

**Rationale:** Conceptual clarity. Not blocking deployment but creates confusion.

**Action Required:** 安安 to define or remove

**Status:** OPEN

---

### U007: GBP (Governance Boundary Protocol) Definition (P2 - Medium)

**Statement ID:** S040

**What Missing:**
Definition of GBP. Mentioned in meta-cognition architecture but not defined in any repo.

**Where Mentioned:**
- Meta-cognition architecture document (external to repo)

**Repo Evidence:**
- No definition found in SIC, SIT, or SIC-SIT-Protocol

**Needed Input:**
- Define GBP in repo (e.g., create `GBP.md`)
- OR remove from meta-cognition architecture

**Priority:** P2 (Medium)

**Rationale:** Conceptual clarity. Not blocking deployment but creates confusion.

**Action Required:** 安安 to define or remove

**Status:** OPEN

---

### U008: 17 Axioms ↔ 107 Tools Mapping (P2 - Medium)

**Statement ID:** S041

**What Missing:**
Explicit mapping between the 17 constitutional axioms and the 107 tools mentioned in meta-cognition architecture.

**Where Mentioned:**
- Meta-cognition architecture document (107 tools)
- `SIC-SIT-Protocol/sic-sit-constitution/constitution/AXIOMS.md` (17 axioms)

**Repo Evidence:**
- No mapping file found in any repo

**Needed Input:**
- Create mapping file (e.g., `axioms_to_tools_mapping.md`)
- OR clarify that they are independent concepts

**Priority:** P2 (Medium)

**Rationale:** Conceptual clarity. Helps understand how axioms relate to practical tools.

**Action Required:** 安安 to create mapping or clarify independence

**Status:** DEFERRED (FUTURE_WORK)

**Resolution (2026-01-09):**
- Mapping not required for SIC/SIT/SIC-SIT core protocols
- Belongs to L11 Semantic OS expansion scope
- Not blocking TRL5 delivery
- Deferred to future work

---

## Priority Definitions

### P0 (Critical)
- **Impact:** Blocks deployment or interoperability
- **Timeline:** Must resolve before TRL5 pilot
- **Owner:** 安安 (User)

### P1 (High)
- **Impact:** Blocks reproducibility or verification
- **Timeline:** Should resolve during TRL5 pilot
- **Owner:** 安安 (User) or Lab (Experimental Validation)

### P2 (Medium)
- **Impact:** Creates confusion but not blocking
- **Timeline:** Can resolve after TRL5 pilot
- **Owner:** 安安 (User)

---

## Resolution Workflow

### For Each UNKNOWN

1. **Identify:** List in this register with statement_id
2. **Prioritize:** Assign P0/P1/P2 based on impact
3. **Request Input:** Notify 安安 or Lab
4. **Resolve:** Once input received, update TRACE_PATCH_TABLE and Canon
5. **Close:** Mark as RESOLVED and remove from this register

---

## Audit Trail

| Date | Action | Unknown IDs | Performed By |
|------|--------|-------------|--------------|
| 2026-01-09 | Initial UNKNOWN identification | U001-U008 | Manus AI (尾德3) |

---

**End of UNKNOWN Register**
