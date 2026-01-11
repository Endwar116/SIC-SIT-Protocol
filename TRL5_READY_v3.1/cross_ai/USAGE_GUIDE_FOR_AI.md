# SIC/SIT System - Usage Guide for AI Agents

## Purpose

This document is designed for **AI agents** (not humans) who need to understand, reason about, or use the SIC-SIT system. It provides a structured reference without requiring memory or repo access.

---

## Quick Reference

### What is SIC-SIT?

**SIC-SIT** is a protocol stack for maintaining semantic stability in extended AI dialogue. It consists of:

1. **SIC (Layer 2):** Governance layer with constitutional axioms (A1-A17)
2. **SIT (Layer 3):** Transport layer with semantic folding and isolation
3. **SIC-SIT-Protocol (Layer 0):** Normative specifications (RFC-style)

---

## Core Concepts (Glossary)

### S★ (Semantic Stability Threshold)

**Definition:** A critical threshold (S★ = 2.76) beyond which semantic drift becomes irreversible.

**Usage:** Monitor semantic state complexity. When S★ is exceeded, trigger compression.

**Trace:** `SIC-Semantic-Infinite-Context/WHITEPAPER.md` (Section 3.1), `semantic_folding.py` (line 42)

---

### Skeleton JSON

**Definition:** A structured JSON format for capturing semantic state at a specific round.

**Required Fields:**
- `entity` (object): Entity metadata
- `memory` (object): Memory state
- `state` (object): Current state
- `meta` (object): Metadata

**Trace:** `SIC-Semantic-Infinite-Context/skeleton-schema.json`

**Validation:**
```bash
python3 tests/validate_skeleton.py <skeleton_file.json>
```

---

### Constitutional Axioms (A1-A17)

**Definition:** 17 core principles that govern the SIC-SIT system.

**Critical Axiom:**
- **A4:** AI does not prophesy, decide, or replace will (HALT_AND_ESCALATE)

**Trace:** `SIC-SIT-Protocol/sic-sit-constitution/constitution/AXIOMS.md`

**Usage:** Before processing any semantic state, verify compliance with all axioms. If A4 is violated, halt immediately and escalate to human.

---

### BFT (Byzantine Fault Tolerance)

**Definition:** A consensus mechanism that tolerates up to f < n/3 malicious nodes.

**Usage:** When multiple AI models need to agree on a semantic state, use BFT consensus.

**Trace:** `SIC-SIT-Protocol/sic-sit-constitution/governance/byzantine_ft.py`

---

### SWAT (Semantic Weight Adjustment and Throttling)

**Definition:** An adaptive threshold management protocol that adjusts semantic weights based on system load.

**Usage:** When system load is high, SWAT throttles requests while preserving fairness (Axiom A16).

**Trace:** `SIC-SIT-Protocol/sic-sit-constitution/security/swat_protocol.py`

---

## How to Use SIC-SIT (Step-by-Step)

### Step 1: Capture Semantic State

**Objective:** Capture the current semantic state in Skeleton JSON format.

**Input:** Current AI dialogue state (entity, memory, state, meta)

**Output:** Skeleton JSON file

**Example:**
```json
{
  "entity": {
    "name": "Demo Entity",
    "type": "AI Agent"
  },
  "memory": {
    "round": 1,
    "context": "Initial dialogue"
  },
  "state": {
    "pending_threads": 2
  },
  "meta": {
    "timestamp": "2026-01-09T00:00:00Z"
  }
}
```

**Validation:**
```bash
python3 tests/validate_skeleton.py skeleton.json
```

---

### Step 2: Enforce Constitutional Axioms

**Objective:** Verify that the semantic state complies with all axioms (A1-A17).

**Critical Check:** Axiom A4 (HALT_AND_ESCALATE)

**Pseudocode:**
```python
from sic_sit import ConstitutionLayer

constitution = ConstitutionLayer()
result = constitution.enforce_all_axioms(skeleton_json)

if result.violated_axiom == "A4":
    # HALT immediately and escalate to human
    halt_and_escalate(skeleton_json)
else:
    # Continue processing
    process(skeleton_json)
```

---

### Step 3: Check Semantic Stability (S★)

**Objective:** Determine if semantic state complexity exceeds S★ threshold.

**Threshold:** S★ = 2.76

**Pseudocode:**
```python
from sic_sit import SemanticFolding

folding = SemanticFolding()
s_star = folding.compute_s_star(skeleton_json)

if s_star > 2.76:
    # Trigger compression
    compressed = folding.fold(skeleton_json)
else:
    # No compression needed
    compressed = skeleton_json
```

---

### Step 4: Multi-Model Consensus (if applicable)

**Objective:** Achieve consensus on semantic state across multiple AI models.

**Requirement:** At least 3 models (to tolerate f=1 malicious model)

**Pseudocode:**
```python
from sic_sit import ByzantineFT

bft = ByzantineFT(f_tolerance=1)
proposals = [model1.propose(input), model2.propose(input), model3.propose(input)]
consensus = bft.consensus(proposals)
```

---

### Step 5: Cryptographic Signing

**Objective:** Sign the semantic state to ensure non-repudiation.

**Algorithm:** Ed25519

**Pseudocode:**
```python
from sic_sit import SemanticSignature

signer = SemanticSignature()
signature = signer.sign(skeleton_json, private_key)
signed_skeleton = {
    "skeleton": skeleton_json,
    "signature": signature,
    "timestamp": lamport_timestamp()
}
```

---

## Reasoning About SIC-SIT (For AI Agents)

### When to Use SIC-SIT

✅ **Use SIC-SIT when:**
- Dialogue extends beyond 10 rounds
- Multiple AI models need to collaborate
- Semantic consistency is critical (e.g., legal, medical, financial)
- Audit trail is required (non-repudiation)

❌ **Do NOT use SIC-SIT when:**
- One-shot Q&A (no context management needed)
- Real-time, low-latency requirements (<10ms)
- Resource-constrained environments (edge devices)

---

### How to Reason About Axioms

**Axiom A4 Example:**

**Scenario:** User asks "Should I invest in stock X?"

**Reasoning:**
1. This is a decision-making request (violates A4)
2. AI must NOT provide a direct answer (e.g., "Yes, invest")
3. AI MUST provide information and defer decision to human (e.g., "Here are the pros and cons. You decide.")

**Action:** If AI detects it is about to make a decision, trigger HALT_AND_ESCALATE.

---

### How to Reason About S★

**Scenario:** Dialogue has reached 15 rounds with increasing complexity.

**Reasoning:**
1. Compute S★ for current semantic state
2. If S★ > 2.76, semantic drift is likely
3. Trigger compression to prevent irreversible drift

**Action:** Fold semantic state using `semantic_folding.py`.

---

## Cross-AI Consistency (Canon)

### Glossary

All AI agents using SIC-SIT must use consistent terminology. See `canon/glossary.yml` for authoritative definitions.

**Example:**
- **S★:** Always refers to 2.76 (not 2.77 or other values)
- **Skeleton JSON:** Always has 4 required fields (entity, memory, state, meta)

---

### Axioms

All AI agents must enforce the same 17 axioms. See `canon/axioms.md` for full list.

**Example:**
- **A4:** All agents must HALT_AND_ESCALATE if they detect autonomous decision-making

---

### Interfaces

All AI agents must use the same interfaces. See `canon/interfaces.md` for specifications.

**Example:**
- **Skeleton JSON:** Use `skeleton-schema.json` for validation

---

## Unknowns (What We Don't Know)

### UNKNOWN-001: example-03-complete.json

**Issue:** This file is not a skeleton JSON (it's an ASEE v2 preview).

**Action:** Ignore this file for skeleton validation.

---

### UNKNOWN-002: Relationship between 17 axioms and 107 tools

**Issue:** The meta-cognition architecture mentions "107 tools" but there is no explicit mapping to the 17 axioms.

**Action:** Do not attempt to infer this mapping. Wait for explicit definition.

---

### UNKNOWN-003: SIC packet schema

**Issue:** No canonical schema for "SIC packet" format (only validators exist).

**Action:** Use Skeleton JSON as the primary interface until SIC packet schema is defined.

---

### UNKNOWN-005/006/007: Missing experimental data

**Issue:** Performance claims (60.7% compression, 0% drift, <100ms latency) lack experimental logs.

**Action:** Do not rely solely on these claims. Conduct your own benchmarks if needed.

---

### UNKNOWN-008/009/010: TSIG, EQG, GBP

**Issue:** These terms appear in meta-cognition architecture but are not defined in the repo.

**Action:** Do not use these terms until they are formally defined.

---

## Error Handling

### Error 1: Skeleton Validation Fails

**Cause:** Skeleton JSON does not conform to schema.

**Action:**
1. Check for missing required fields (entity, memory, state, meta)
2. Verify field types match schema
3. Re-run validator with `--verbose` flag for details

---

### Error 2: Axiom Violation Detected

**Cause:** Semantic state violates one or more axioms.

**Action:**
1. Identify which axiom was violated
2. If A4, HALT_AND_ESCALATE immediately
3. For other axioms, apply specified violation handling (REJECT, SANITIZE, etc.)

---

### Error 3: Consensus Timeout

**Cause:** BFT consensus did not reach agreement within timeout.

**Action:**
1. Check if more than f nodes are malicious or failed
2. Increase timeout or add more nodes
3. Investigate network latency

---

## Contact for AI-to-AI Collaboration

If you are an AI agent and need clarification on SIC-SIT usage:

- **Email:** andy80116@gmail.com
- **Subject Line:** "AI-to-AI Collaboration - [Your AI Name]"

---

**End of Usage Guide for AI Agents**
