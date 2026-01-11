# SIC/SIT Canon - Interfaces

## Purpose

This document defines the key interfaces and data structures in the SIC-SIT system. All interfaces are traced to source files.

---

## 1. Skeleton JSON Schema

**Purpose:** The canonical format for capturing semantic state at a specific round.

**Trace:** `SIC-Semantic-Infinite-Context/skeleton-schema.json`

### Required Root Fields

```json
{
  "entity": { ... },    // Entity metadata
  "memory": { ... },    // Memory state
  "state": { ... },     // Current state
  "meta": { ... }       // Metadata
}
```

### Validation

- **Python Validator:** `SIC-Semantic-Infinite-Context/tests/validate_skeleton.py`
- **JavaScript Validator:** `SIC-Semantic-Infinite-Context/validate_skeleton.js`

### Examples

- **Simple:** `example-01-simple.json`
- **Medium:** `example-02-medium.json`

---

## 2. SIC Packet Format

**Purpose:** Internal packet format for semantic interchange at network layer (L2 in USCA stack).

**Trace:** `SIC-SIT-Protocol/validators/sic_pkt.py`

**Status:** ✅ EXISTS (TRL3_PROTOTYPE)

**Implementation:** Python dataclass in `sic_pkt.py`

### Structure

```python
@dataclass
class SIC_Packet:
    header: SIC_Header
    payload: SIC_Payload
    shv: str  # Semantic-Hash-Vector
```

### Packet Types

- `REQUEST`: Request packet
- `RESPONSE`: Response packet
- `CONTROL`: Control packet
- `ERROR`: Error packet

### Relationship to Skeleton JSON

**Skeleton JSON** (I1) is the **external interface** (what users submit).

**SIC Packet** (I2) is the **internal format** (how data is transmitted in the network).

**Conversion Chain:**
```
Skeleton JSON → validate_skeleton.py → [Processing] → SIC Packet → [Routing] → Destination
```

**Note:** SIC Packet is NOT exposed to external users. It is used internally for semantic routing and transmission.

**Resolution:** U001 and U002 are now RESOLVED. SIC Packet exists as an internal format, separate from Skeleton JSON (external interface).

---

## 3. Constitution JSON

**Purpose:** Machine-readable representation of the constitutional axioms.

**Trace:** `SIC-SIT-Protocol/sic-sit-constitution/constitution/CONSTITUTION.json`

### Structure

```json
{
  "version": "1.1.3",
  "axioms": [ ... ],
  "enforcement": { ... }
}
```

---

## 4. Semantic Folding API

**Purpose:** Topology-based compression interface.

**Trace:** `SIC-SIT-Protocol/folding/semantic_folding.py`

### Key Methods

```python
class SemanticFolding:
    def fold(self, semantic_state):
        # Compress semantic state
        pass
    
    def unfold(self, compressed_state):
        # Decompress semantic state
        pass
```

**Status:** TRL3_PROTOTYPE

---

## 5. SWAT Protocol API

**Purpose:** Adaptive threshold management.

**Trace:** `SIC-SIT-Protocol/sic-sit-constitution/security/swat_protocol.py`

### Key Methods

```python
class SWAT:
    def adjust_threshold(self, load):
        # Adjust semantic weight threshold based on system load
        pass
    
    def throttle(self, request):
        # Throttle requests based on semantic weight
        pass
```

**Status:** TRL3_PROTOTYPE

---

## 6. Byzantine FT API

**Purpose:** Byzantine fault tolerance consensus.

**Trace:** `SIC-SIT-Protocol/sic-sit-constitution/governance/byzantine_ft.py`

### Key Methods

```python
class ByzantineFT:
    def consensus(self, proposals):
        # Achieve consensus among nodes (f < n/3 tolerance)
        pass
```

**Status:** TRL3_PROTOTYPE

---

## 7. Semantic Signature API

**Purpose:** Cryptographic signing of semantic states.

**Trace:** `SIC-SIT-Protocol/security/semantic_signature.py`

### Key Methods

```python
class SemanticSignature:
    def sign(self, semantic_state, private_key):
        # Sign semantic state with Ed25519
        pass
    
    def verify(self, semantic_state, signature, public_key):
        # Verify signature
        pass
```

**Status:** TRL3_PROTOTYPE

---

## Unknowns

~~⚠️ **UNKNOWN-003:** No canonical schema for "SIC packet" format (only validators exist).~~ **RESOLVED (2026-01-09):** SIC Packet is defined in `sic_pkt.py` as a Python dataclass.

~~⚠️ **UNKNOWN-004:** The relationship between "Skeleton JSON" and "SIC packet" is not explicitly defined.~~ **RESOLVED (2026-01-09):** Skeleton JSON is external interface, SIC Packet is internal format. See Section 2 for details.

---

**End of Interfaces Canon**
