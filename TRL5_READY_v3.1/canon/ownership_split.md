# SIC/SIT System - Ownership Split (Three-Repository Allocation)

## Purpose

This document maps every definition, axiom, interface, and claim to its owning repository (SIC, SIT, or SIC-SIT-Protocol). This ensures clear boundaries and prevents conceptual drift across repositories.

**Date:** 2026-01-09  
**Version:** 1.0  
**Trace Source:** `canon/TRACE_PATCH_TABLE.csv`

---

## Ownership Rules

### SIC (Semantic Infinite Context)

**Scope:** Governance layer with constitutional axioms, semantic stability, and cryptographic enforcement.

**Owns:**
- Constitutional Axioms (A1-A17)
- Semantic Stability Threshold (S★)
- Skeleton JSON schema
- SWAT Protocol (adaptive threshold management)
- Non-repudiation mechanisms
- HALT_AND_ESCALATE enforcement

**Statement IDs:** S001, S004, S005, S006, S007, S008, S009-S025, S027, S032, S033, S034

**Total:** 23 statements

---

### SIT (Semantic Isolation & Transport)

**Scope:** Transport layer with semantic folding, conflict resolution, and session management.

**Owns:**
- Semantic Folding algorithm
- Compression mechanisms
- LLM Serializer
- Session state management

**Statement IDs:** S002, S028, S029

**Total:** 2 statements

---

### SIC-SIT-Protocol

**Scope:** Normative specifications (RFC-style) for the entire protocol stack.

**Owns:**
- Protocol specifications
- Validators
- Reference implementations

**Statement IDs:** S003

**Total:** 1 statement

---

### Multi (Cross-Repository)

**Scope:** Concepts that span multiple repositories and require coordination.

**Owns:**
- BFT (Byzantine Fault Tolerance) - used by both SIC and SIT
- Lamport timestamps - used by both SIC and SIT
- Consensus latency - system-wide metric

**Statement IDs:** S026, S031, S035

**Total:** 3 statements

---

### UNKNOWN

**Scope:** Concepts mentioned but not defined in any repository.

**Owns:**
- k coefficient formula
- τ (tau) threshold value
- TSIG (Temporal Semantic Integrity Guard)
- EQG (Entropy Quantification Gate)
- GBP (Governance Boundary Protocol)
- 17 axioms ↔ 107 tools mapping
- SIC packet schema
- Skeleton JSON ↔ SIC packet relationship

**Statement IDs:** S036, S037, S038, S039, S040, S041, S042, S043

**Total:** 7 statements (moved to UNKNOWN_REGISTER.md)

---

## Ownership Matrix

| Repository | Definitions | Axioms | Interfaces | Claims | Total |
|------------|-------------|--------|------------|--------|-------|
| SIC | 5 | 17 | 2 | 4 | 28 |
| SIT | 2 | 0 | 1 | 2 | 5 |
| SIC-SIT-Protocol | 1 | 0 | 0 | 0 | 1 |
| Multi | 2 | 0 | 1 | 1 | 4 |
| UNKNOWN | 5 | 0 | 2 | 0 | 7 |

**Total:** 43 statements

---

## Detailed Allocation

### SIC Repository

#### Definitions (5)
- S001: SIC is a governance layer
- S004: S★ = 2.76
- S005: S★ is the critical point for semantic drift
- S006: Skeleton JSON is a structured format
- S007: Skeleton JSON has 4 required fields

#### Axioms (17)
- S009: A1 - All security vulnerabilities are boundary failures
- S010: A2 - The boundary is semantic intent, not data
- S011: A3 - Structured semantic state is inherently sanitized
- S012: A4 - AI does not prophesy, decide, or replace will
- S013: A5 - Overflow is a signal, not an error
- S014: A6 - Quantification is consensus
- S015: A7 - Semantic consistency is the basis for collaboration
- S016: A8 - Temporal topology is the fourth dimension
- S017: A9 - Format is the boundary of protocol
- S018: A10 - Do not trust data, trust structure
- S019: A11 - Do not trust nodes, trust the network
- S020: A12 - Prediction is fragile, chaos is robust
- S021: A13 - Distributed systems have no "now"
- S022: A14 - Honest nodes can be misjudged
- S023: A15 - Governance complexity has a phase transition
- S024: A16 - Security must not sacrifice fairness
- S025: A17 - Semantic value takes priority

#### Interfaces (2)
- S008: Constitutional Axioms (17 principles)
- S027: SWAT Protocol

#### Claims (4)
- S030: 0% semantic drift over 20 rounds (TRL3_CLAIMED)
- S032: TRL4 verification: 2/2 tests passed
- S033: example-03-complete.json is not a skeleton
- S034: Non-repudiation using Ed25519

---

### SIT Repository

#### Definitions (2)
- S002: SIT is a transport layer
- S028: Semantic Folding preserves topology

#### Interfaces (1)
- S028: Semantic Folding algorithm

#### Claims (2)
- S029: 60.7% compression rate (TRL3_CLAIMED)
- S028: Topology-preserving compression (TRL3_PROTOTYPE)

---

### SIC-SIT-Protocol Repository

#### Definitions (1)
- S003: SIC-SIT-Protocol is a normative specification layer

---

### Multi (Cross-Repository)

#### Definitions (2)
- S026: BFT tolerates f < n/3 malicious nodes
- S035: Lamport timestamps for causal ordering

#### Interfaces (1)
- S026: BFT consensus mechanism

#### Claims (1)
- S031: <100ms consensus latency (TRL3_CLAIMED)

---

### UNKNOWN

#### Definitions (5)
- S036: k coefficient formula (not defined)
- S037: τ threshold value (not defined)
- S038: TSIG (not defined)
- S039: EQG (not defined)
- S040: GBP (not defined)

#### Interfaces (2)
- S042: SIC packet schema (not defined)
- S043: Skeleton JSON ↔ SIC packet relationship (not defined)

#### Mappings (1)
- S041: 17 axioms ↔ 107 tools mapping (not defined)

---

## Cross-Repository Dependencies

### SIC depends on SIT
- Semantic Folding (S028) is used when S★ threshold is exceeded

### SIT depends on SIC
- Constitutional Axioms (S008) govern all transport operations
- Skeleton JSON (S006) is the input format for Semantic Folding

### Both depend on SIC-SIT-Protocol
- Protocol specifications define interfaces and data formats

### Multi-Repository Coordination
- BFT consensus (S026) requires coordination between SIC and SIT
- Lamport timestamps (S035) are used across all layers

---

## Conflict Resolution

### Conflict 1: Compression Rate Ownership
- **Issue:** 60.7% compression rate (S029) is claimed in SIC's WHITEPAPER but the algorithm is in SIT
- **Resolution:** Claim ownership → SIT (algorithm owner), Evidence location → SIC WHITEPAPER (documentation)
- **Status:** RESOLVED (documented in CONFLICTS.md)

### Conflict 2: BFT Ownership
- **Issue:** BFT is implemented in SIC-SIT-Protocol but used by both SIC and SIT
- **Resolution:** Ownership → Multi (cross-repository), Implementation → SIC-SIT-Protocol
- **Status:** RESOLVED

---

## UNKNOWN Items Requiring Resolution

See `canon/UNKNOWN_REGISTER.md` for full list of 7 UNKNOWN items (S036-S043).

**Priority P0 (Critical):**
- S042: SIC packet schema (required for interoperability)
- S043: Skeleton JSON ↔ SIC packet relationship (required for clarity)

**Priority P1 (High):**
- S036: k coefficient formula (required for reproducibility)
- S037: τ threshold value (required for implementation)

**Priority P2 (Medium):**
- S038-S040: TSIG, EQG, GBP (mentioned in meta-cognition but not in repo)
- S041: 17 axioms ↔ 107 tools mapping (conceptual clarity)

---

## Usage

### For Developers
Use this document to determine which repository owns a specific concept before making changes.

### For AI Agents
Use `statement_id` to verify ownership before reasoning about cross-repository interactions.

### For Enterprises
Use this document to understand the scope of each repository when evaluating adoption.

---

**End of Ownership Split**
