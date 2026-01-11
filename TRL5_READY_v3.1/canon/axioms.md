# SIC/SIT Canon - Axioms

## Purpose

This document lists all constitutional axioms (A1-A17) that govern the SIC-SIT system. These axioms are **hard constraints** and must not be violated.

**Trace:** All axioms are extracted from `SIC-SIT-Protocol/sic-sit-constitution/constitution/AXIOMS.md` (version 1.1.3).

---

## Axiom List

| Axiom ID | Axiom Statement | Violation Handling | Trace |
|----------|-----------------|-------------------|-------|
| **A1** | 所有安全漏洞都是邊界故障<br>(All security vulnerabilities are boundary failures) | REJECT_AND_LOG | AXIOMS.md:7 |
| **A2** | AI 原生系統的邊界是語義意圖，不是數據<br>(The boundary of AI-native systems is semantic intent, not data) | TRANSFORM_TO_INTENT | AXIOMS.md:8 |
| **A3** | 結構化語義狀態本質上是被消毒的<br>(Structured semantic state is inherently sanitized) | SANITIZE | AXIOMS.md:9 |
| **A4** | AI 不預言、不決定、不取代意志<br>(AI does not prophesy, decide, or replace will) | **HALT_AND_ESCALATE** | AXIOMS.md:10 |
| **A5** | 溢出是信號，不是錯誤<br>(Overflow is a signal, not an error) | CAPTURE_AND_ANALYZE | AXIOMS.md:11 |
| **A6** | 量化即共識<br>(Quantification is consensus) | REQUEST_QUANTIFICATION | AXIOMS.md:12 |
| **A7** | 語義一致性是跨模型協作的唯一基礎<br>(Semantic consistency is the only basis for cross-model collaboration) | REALIGN_SEMANTICS | AXIOMS.md:13 |
| **A8** | 時間拓撲是語義密度的第四維度<br>(Temporal topology is the fourth dimension of semantic density) | ADD_TEMPORAL_MARKER | AXIOMS.md:14 |
| **A9** | 格式是協議的邊界，不可被內容價值覆寫<br>(Format is the boundary of protocol, cannot be overwritten by content value) | REJECT_REFORMAT | AXIOMS.md:15 |
| **A10** | 不信任數據，信任結構<br>(Do not trust data, trust structure) | VERIFY_STRUCTURE | AXIOMS.md:16 |
| **A11** | 不信任節點，信任網絡<br>(Do not trust nodes, trust the network) | REQUIRE_CONSENSUS | AXIOMS.md:17 |
| **A12** | 預測即脆弱，混沌即堅固<br>(Prediction is fragile, chaos is robust) | INJECT_ENTROPY | AXIOMS.md:18 |
| **A13** | 分佈式系統沒有『現在』，只有因果順序<br>(Distributed systems have no "now", only causal order) | ADD_LAMPORT_TIMESTAMP | AXIOMS.md:19 |
| **A14** | 誠實節點可被誤判，惡意節點可偽裝誠實<br>(Honest nodes can be misjudged, malicious nodes can disguise as honest) | REQUIRE_SIGNATURE | AXIOMS.md:20 |
| **A15** | 治理複雜度存在相變臨界點<br>(Governance complexity has a phase transition critical point) | TRIGGER_COMPRESSION | AXIOMS.md:21 |
| **A16** | 安全機制不得以犧牲參與公平性為代價<br>(Security mechanisms must not sacrifice participation fairness) | APPLY_SWAT | AXIOMS.md:22 |
| **A17** | 語義價值優先於計算資源<br>(Semantic value takes priority over computational resources) | APPLY_NOVELTY_BONUS | AXIOMS.md:23 |

---

## Axiom Categories

### Security & Boundary (A1-A3)
- **A1:** All security vulnerabilities are boundary failures
- **A2:** The boundary of AI-native systems is semantic intent, not data
- **A3:** Structured semantic state is inherently sanitized

### AI Governance (A4-A7)
- **A4:** AI does not prophesy, decide, or replace will (HALT_AND_ESCALATE)
- **A5:** Overflow is a signal, not an error
- **A6:** Quantification is consensus
- **A7:** Semantic consistency is the only basis for cross-model collaboration

### Temporal & Structural (A8-A10)
- **A8:** Temporal topology is the fourth dimension of semantic density
- **A9:** Format is the boundary of protocol, cannot be overwritten by content value
- **A10:** Do not trust data, trust structure

### Distributed Systems (A11-A14)
- **A11:** Do not trust nodes, trust the network
- **A12:** Prediction is fragile, chaos is robust
- **A13:** Distributed systems have no "now", only causal order
- **A14:** Honest nodes can be misjudged, malicious nodes can disguise as honest

### Complexity & Fairness (A15-A17)
- **A15:** Governance complexity has a phase transition critical point
- **A16:** Security mechanisms must not sacrifice participation fairness
- **A17:** Semantic value takes priority over computational resources

---

## Critical Axiom: A4

**A4** is the only axiom with **HALT_AND_ESCALATE** violation handling, indicating it is the most critical constraint.

> **A4:** AI does not prophesy, decide, or replace will.

This axiom ensures that AI systems remain tools under human control and do not attempt to make autonomous decisions that override human intent.

---

## Usage in Code

Axioms are enforced by the `constitution_layer.py` module:

```python
# Trace: SIC-SIT-Protocol/sic-sit-constitution/governance/constitution_layer.py
class ConstitutionLayer:
    def enforce_axiom(self, axiom_id, context):
        # Enforcement logic based on AXIOMS.md
        pass
```

---

## Unknowns

⚠️ **UNKNOWN-002:** The relationship between axioms and the "107 tools" from the meta-cognition architecture is not explicitly defined in the repo.

---

**End of Axioms Canon**
