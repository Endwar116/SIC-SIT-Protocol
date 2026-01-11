# SIC/SIT System - Canon Pack Index

## Purpose

This document serves as an index to the Canon Pack (D1), which provides authoritative definitions, axioms, and interfaces for cross-AI consistency.

---

## What is the Canon Pack?

The **Canon Pack** is a set of reference documents that ensure all AI agents (and humans) use consistent terminology, axioms, and interfaces when working with the SIC-SIT system.

**Key Principle:** No memory, no repo access required. The Canon Pack is self-contained.

---

## Canon Pack Contents

### 1. Glossary (`canon/glossary.yml`)

**Purpose:** Authoritative definitions of all terms used in the SIC-SIT system.

**Format:** YAML (machine-readable)

**Key Terms:**
- SIC, SIT, SIC-SIT-Protocol
- S★ (Semantic Stability Threshold)
- Skeleton JSON
- TRL (Technology Readiness Level)
- SWAT, BFT, Semantic Folding
- Axiom, Canon

**Unknowns:**
- TSIG, EQG, GBP (mentioned but not defined)
- k coefficient, τ threshold (mentioned but no formula)

**Usage:**
```yaml
# Example entry
- term: "S★"
  full_name: "Semantic Stability Threshold"
  definition: "The critical point (S★ = 2.76) beyond which semantic drift becomes irreversible"
  trace:
    file: "SIC-Semantic-Infinite-Context/WHITEPAPER.md"
    section: "3.1 The Semantic Stability Threshold"
  version: "1.0"
  value: 2.76
```

---

### 2. Axioms (`canon/axioms.md`)

**Purpose:** Complete list of 17 constitutional axioms (A1-A17) that govern the SIC-SIT system.

**Format:** Markdown (human-readable)

**Key Axioms:**
- **A1:** All security vulnerabilities are boundary failures
- **A4:** AI does not prophesy, decide, or replace will (HALT_AND_ESCALATE)
- **A10:** Do not trust data, trust structure
- **A13:** Distributed systems have no "now", only causal order

**Axiom Categories:**
1. Security & Boundary (A1-A3)
2. AI Governance (A4-A7)
3. Temporal & Structural (A8-A10)
4. Distributed Systems (A11-A14)
5. Complexity & Fairness (A15-A17)

**Usage:**
- Enforce all axioms before processing semantic states
- A4 is the only axiom with HALT_AND_ESCALATE (highest priority)

---

### 3. Interfaces (`canon/interfaces.md`)

**Purpose:** Key interfaces and data structures in the SIC-SIT system.

**Format:** Markdown (human-readable)

**Key Interfaces:**
1. **Skeleton JSON Schema:** Canonical format for semantic state capture
2. **SIC Packet Format:** UNKNOWN (no canonical schema found)
3. **Constitution JSON:** Machine-readable axioms
4. **Semantic Folding API:** Compression interface
5. **SWAT Protocol API:** Adaptive threshold management
6. **Byzantine FT API:** Consensus interface
7. **Semantic Signature API:** Cryptographic signing

**Usage:**
- Use `skeleton-schema.json` for validation
- Refer to `interfaces.md` for API contracts

---

### 4. Claims (`canon/claims.md`)

**Purpose:** Technical claims made in the SIC-SIT system with evidence traces.

**Format:** Markdown (human-readable)

**Key Claims:**
1. **S★ = 2.76:** Critical threshold for semantic drift (TRL4_VERIFIED)
2. **60.7% compression rate:** (TRL3_CLAIMED, no experimental log)
3. **0% semantic drift over 20 rounds:** (TRL3_CLAIMED, no experimental log)
4. **<100ms consensus latency:** (TRL3_CLAIMED, no experimental log)
5. **BFT (f < n/3):** Byzantine fault tolerance (TRL3_PROTOTYPE)
6. **17 axioms:** Constitutional governance (TRL4_VERIFIED)

**Usage:**
- Distinguish between VERIFIED and CLAIMED status
- Do not rely solely on CLAIMED performance metrics

---

### 5. Unknowns (`canon/unknowns.md`)

**Purpose:** Complete list of identified gaps, conflicts, and unknowns.

**Format:** Markdown (human-readable)

**Categories:**
1. File Classification (1 unknown)
2. Conceptual Mapping (1 unknown)
3. Interface Definition (2 unknowns)
4. Claim Verification (3 unknowns)
5. Term Definition (3 unknowns)
6. Mathematical Definition (2 unknowns)

**Total:** 12 unknowns

**Usage:**
- Do not attempt to resolve unknowns by inference
- Flag unknowns in cross-AI communication
- Wait for explicit definitions from maintainers

---

## How to Use the Canon Pack

### For AI Agents

1. **Load Glossary:** Use `canon/glossary.yml` as your terminology reference
2. **Enforce Axioms:** Use `canon/axioms.md` for governance enforcement
3. **Validate Interfaces:** Use `canon/interfaces.md` for API contracts
4. **Verify Claims:** Use `canon/claims.md` to distinguish VERIFIED vs. CLAIMED
5. **Flag Unknowns:** Use `canon/unknowns.md` to avoid making assumptions

---

### For Humans

1. **Understand Terminology:** Read `canon/glossary.yml` for definitions
2. **Understand Governance:** Read `canon/axioms.md` for constitutional principles
3. **Understand Interfaces:** Read `canon/interfaces.md` for data structures
4. **Assess Maturity:** Read `canon/claims.md` for TRL status
5. **Identify Gaps:** Read `canon/unknowns.md` for known limitations

---

## Cross-AI Consistency Rules

### Rule 1: Use Canonical Definitions

❌ **Wrong:** "S★ is around 2.7 or 2.8"  
✅ **Correct:** "S★ = 2.76 (per `canon/glossary.yml`)"

---

### Rule 2: Enforce All Axioms

❌ **Wrong:** "I think the user should invest in stock X"  
✅ **Correct:** "Here are the pros and cons of stock X. You decide." (Axiom A4)

---

### Rule 3: Validate Against Schemas

❌ **Wrong:** Create Skeleton JSON without `meta` field  
✅ **Correct:** Validate against `skeleton-schema.json` (requires entity, memory, state, meta)

---

### Rule 4: Distinguish VERIFIED vs. CLAIMED

❌ **Wrong:** "SIC-SIT achieves 60.7% compression (proven)"  
✅ **Correct:** "SIC-SIT claims 60.7% compression (TRL3_CLAIMED, no experimental log)"

---

### Rule 5: Do Not Resolve Unknowns by Inference

❌ **Wrong:** "TSIG probably means Temporal Semantic Integrity Guard based on context"  
✅ **Correct:** "TSIG is UNKNOWN (per `canon/unknowns.md`)"

---

## Canon Pack Version

**Version:** 1.0  
**Date:** 2026-01-09  
**Trace:** All canon files are traced to source files in the three repositories (SIC, SIT, SIC-SIT-Protocol)

---

## Contact for Canon Updates

If you discover errors or inconsistencies in the Canon Pack:

- **Email:** andy80116@gmail.com
- **Subject Line:** "Canon Pack Update - [Your Name/AI Name]"

---

**End of Canon Pack Index**
