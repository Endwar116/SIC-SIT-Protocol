# SIC/SIT System - Architecture Overview

## Purpose

This document provides a high-level architecture overview of the SIC-SIT system for technical stakeholders.

---

## System Architecture

### Layer Model

```
┌─────────────────────────────────────────┐
│  Application Layer (User Applications)  │
├─────────────────────────────────────────┤
│  SIC (Semantic Infinite Context)        │  ← Layer 2: Governance
│  - Constitutional Axioms (A1-A17)       │
│  - Semantic Stability (S★ = 2.76)       │
│  - Cryptographic Enforcement            │
├─────────────────────────────────────────┤
│  SIT (Semantic Isolation & Transport)   │  ← Layer 3: Transport
│  - Semantic Folding                     │
│  - Conflict Resolution                  │
│  - Session Management                   │
├─────────────────────────────────────────┤
│  SIC-SIT-Protocol (Specification)       │  ← Layer 0: Standards
│  - RFC-style Specifications             │
│  - Validators & Reference Impl          │
└─────────────────────────────────────────┘
```

---

## SIC (Layer 2: Governance)

**Repository:** `SIC-Semantic-Infinite-Context`

### Core Components

1. **Constitutional Layer** (`governance/constitution_layer.py`)
   - Enforces 17 axioms (A1-A17)
   - Violation handling (REJECT, HALT, ESCALATE, etc.)

2. **Security Layer** (`security/non_repudiation.py`)
   - Ed25519 cryptographic signing
   - Non-repudiation guarantees

3. **Skeleton JSON** (`skeleton-schema.json`)
   - Canonical format for semantic state capture
   - Required fields: entity, memory, state, meta

### Key Algorithms

- **S★ Threshold:** S★ = 2.76 (semantic stability critical point)
- **SWAT Protocol:** Adaptive threshold management
- **BFT Consensus:** Byzantine fault tolerance (f < n/3)

---

## SIT (Layer 3: Transport)

**Repository:** `SIT-Protocol`

### Core Components

1. **Semantic Folding** (`folding/semantic_folding.py`)
   - Topology-preserving compression
   - Dimensionality reduction

2. **LLM Serializer** (`serializer/llm_serializer.py`)
   - Model-specific serialization
   - Cross-model compatibility

3. **Session State Signer** (`session/state_signer.py`)
   - Session-level cryptographic signing
   - State integrity verification

---

## SIC-SIT-Protocol (Layer 0: Standards)

**Repository:** `SIC-SIT-Protocol`

### Core Components

1. **SPEC/** (RFC-style specifications)
   - Normative protocol definitions
   - Interface contracts

2. **reference-impl/** (Reference implementations)
   - Non-normative code examples
   - Validation tools

3. **validators/** (Protocol validators)
   - `sic_pkt.py`: SIC packet validator
   - `validate_sit.py`: SIT protocol validator

---

## Data Flow

### 1. Semantic State Capture

```
User Input → Skeleton JSON → Validator → Constitutional Layer
```

**Files:**
- `skeleton-schema.json`: Schema definition
- `validate_skeleton.py`: Python validator
- `constitution_layer.py`: Axiom enforcement

### 2. Semantic Folding

```
Skeleton JSON → Semantic Folding → Compressed State → Storage
```

**Files:**
- `semantic_folding.py`: Folding algorithm
- S★ = 2.76: Compression trigger threshold

### 3. Multi-Model Consensus

```
Model A → Proposal → BFT Consensus ← Proposal ← Model B
                ↓
            Agreed State
```

**Files:**
- `byzantine_ft.py`: BFT implementation
- f < n/3: Fault tolerance bound

### 4. Cryptographic Signing

```
Semantic State → Ed25519 Sign → Signed State → Verification
```

**Files:**
- `semantic_signature.py`: Signature generation
- `non_repudiation.py`: Non-repudiation layer

---

## Key Metrics

| Metric | Value | Status | Trace |
|--------|-------|--------|-------|
| S★ (Stability Threshold) | 2.76 | TRL4_VERIFIED | WHITEPAPER.md, semantic_folding.py |
| Compression Rate | 60.7% | TRL3_CLAIMED | WHITEPAPER.md (no experimental log) |
| Semantic Drift (20 rounds) | 0% | TRL3_CLAIMED | WHITEPAPER.md (no experimental log) |
| Consensus Latency | <100ms | TRL3_CLAIMED | WHITEPAPER.md (no experimental log) |
| BFT Tolerance | f < n/3 | TRL3_PROTOTYPE | byzantine_ft.py |
| Axiom Count | 17 | TRL4_VERIFIED | AXIOMS.md |

---

## Technology Stack

### Languages
- **Python:** 3.11+ (primary implementation)
- **JavaScript:** Node.js 22+ (validators)

### Dependencies
- **jsonschema:** JSON schema validation
- **cryptography:** Ed25519 signing (Python)

### Operating System
- **Ubuntu:** 22.04 LTS (tested)
- **Linux:** Any modern distribution (expected to work)

---

## TRL Status

| Component | TRL Level | Status |
|-----------|-----------|--------|
| Skeleton JSON Schema | TRL4 | ✅ VERIFIED |
| Validators (Python/JS) | TRL4 | ✅ VERIFIED |
| Constitutional Layer | TRL3 | 🔄 PROTOTYPE |
| Semantic Folding | TRL3 | 🔄 PROTOTYPE |
| BFT Consensus | TRL3 | 🔄 PROTOTYPE |
| SWAT Protocol | TRL3 | 🔄 PROTOTYPE |
| Cryptographic Signing | TRL3 | 🔄 PROTOTYPE |

**Overall System:** TRL4 → TRL5 transition

---

## Integration Points

### For Existing AI Systems

1. **LangChain Integration**
   - Use `llm_serializer.py` for model-specific serialization
   - Wrap LangChain agents with constitutional layer

2. **LlamaIndex Integration**
   - Use Skeleton JSON as storage format
   - Apply semantic folding for compression

3. **Custom AI Systems**
   - Implement Skeleton JSON schema
   - Enforce axioms via `constitution_layer.py`

---

## Security Model

### Threat Model

1. **Semantic Drift:** Prevented by S★ threshold and axiom enforcement
2. **Byzantine Nodes:** Tolerated up to f < n/3 via BFT consensus
3. **Replay Attacks:** Prevented by Lamport timestamps (Axiom A13)
4. **Forgery:** Prevented by Ed25519 signatures

### Trust Assumptions

- **A10:** Do not trust data, trust structure
- **A11:** Do not trust nodes, trust the network
- **A14:** Honest nodes can be misjudged, malicious nodes can disguise as honest

---

## Unknowns & Limitations

See `canon/unknowns.md` for a full list. Key limitations:

1. **No experimental logs** for performance claims (60.7% compression, 0% drift, <100ms latency)
2. **Missing schemas** for SIC packet format
3. **Undefined terms** (TSIG, EQG, GBP) from meta-cognition architecture
4. **No formal verification** of semantic folding topology preservation

---

## Next Steps

### For TRL5 Readiness
1. Conduct real-world pilot tests
2. Generate experimental logs for performance claims
3. Define missing schemas (SIC packet)
4. Formal verification of critical algorithms

### For Production (TRL7+)
1. Security audit by third-party firm
2. Performance optimization at scale
3. Enterprise-grade deployment tools
4. Comprehensive documentation

---

**End of Architecture Overview**
