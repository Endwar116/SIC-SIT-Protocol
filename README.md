# SIC-SIT Protocol Stack
## Unified Semantic Communication Architecture (USCA)

**Don't transfer data. Transfer intent.**  
**不要傳輸數據。傳輸意圖。**

---

## 🌐 什麼是 USCA？

USCA（統一語義通訊架構）是一套完整的 AI 原生通訊協議棧，類似於網際網路的 TCP/IP 協議棧，但專門設計用於 **語義** 而非 **封包** 的傳輸。

| 網路協議 | USCA 對應 | 功能 |
|----------|-----------|------|
| IP       | **SIC**   | 語義路由 (去哪裡) |
| Firewall | **SIC-FW** | 語義過濾 (誰能過) |
| TCP      | **SIT**   | 語義傳輸保證 (怎麼到) |
| UTF-8    | **SEM-FOLD** | 語義編碼 (怎麼表達) |

---

## 📚 協議棧架構

```
┌─────────────────────────────────────────────────────────┐
│  L6  SIC-TOP    Topology Intent Layer      (應用層)    │
│  L5  SIC-INT    Interpretation Layer       (表現層)    │
│  L4  SIT-SES    Reasoning Session Layer    (會話層)    │
├─────────────────────────────────────────────────────────┤
│  L3  SIT        Semantic Isolation Transfer (傳輸層)   │
│      ├─ SIT-SYN/ACK  三次握手                          │
│      ├─ SIT-SIG      簽名驗證                          │
│      └─ SIT-DRIFT    漂移偵測                          │
├─────────────────────────────────────────────────────────┤
│  L2  SIC        Semantic Interchange Core   (網路層)   │
│      ├─ SIC-FW       語義防火牆                        │
│      ├─ SIC-PKT      封包處理                          │
│      └─ SIC-RTR      語義路由                          │
├─────────────────────────────────────────────────────────┤
│  L1  SEM-FOLD   Semantic Folding Layer     (資料鏈結層)│
│  L0  TOK-RAW    Token Layer                (物理層)    │
└─────────────────────────────────────────────────────────┘
```

---

## 🔥 核心元件

### SIC (L2) — 語義交換核心

```python
from validators.sic_pkt import SIC_PKT_Handler

# 建立語義封包
handler = SIC_PKT_Handler(model_id="claude-001")
packet = handler.create_packet(
    payload={"intent": "查詢用戶資料", ...},
    dst_model="gpt-001"
)

# 驗證封包完整性
valid, error = handler.validate_packet(packet)
```

### SIC-FW (L2.5) — 語義防火牆

```python
from validators.sic_fw import SIC_FW

# 建立防火牆
firewall = SIC_FW()

# 評估 SIT State
result = firewall.evaluate(sit_state)
if result.action == SIC_FW_Action.DENY:
    print(f"攔截: {result.reason}")
```

### SIT (L3) — 語義隔離傳輸

```python
from validators.sit_handshake import SIT_Handshake

# 三次握手
alice = SIT_Handshake(secret_key="...", entity_id="alice")
bob = SIT_Handshake(secret_key="...", entity_id="bob")

# Step 1: SYN
syn = alice.create_syn(intent_scope="查詢資料", ...)

# Step 2: SYN-ACK
syn_ack, _ = bob.process_syn(syn)

# Step 3: ACK
ack, _ = alice.process_syn_ack(syn_ack)

# 建立會話
session, _ = bob.process_ack(ack)
```

---

## 🛡️ 五條安全公理

```
Axiom 1: 所有安全漏洞都是邊界故障
Axiom 2: 傳統邊界由記憶體/網路/進程定義
Axiom 3: AI 原生系統有新邊界：語義意圖
Axiom 4: 如果序列化意圖而不是數據，數據就無法洩漏
Axiom 5: 結構化語義狀態本質上是被消毒的
```

---

## 📁 專案結構

```
sic-sit-protocol/
├── core/
│   └── usca_spec.js          # USCA 協議棧規格
│
├── validators/
│   ├── sic_fw.py             # SIC-FW 語義防火牆
│   ├── sic_pkt.py            # SIC-PKT 封包處理
│   ├── sit_handshake.py      # SIT 三次握手
│   └── sit_signer.py         # SIT-SIG 簽名器
│
├── serializers/
│   └── sit_serializer.py     # L1→L3 序列化器
│
├── sanitizers/
│   └── sit_sanitizer.py      # L4 回應消毒器
│
├── schema/
│   ├── sic-pkt-v1.json       # SIC 封包 Schema
│   ├── sit-state-v1.json     # SIT 狀態 Schema
│   └── sit-policy-v1.json    # SIT 政策 Schema
│
├── docs/
│   ├── THREAT_MODEL.md       # 威脅模型
│   └── COMPLIANCE.md         # 合規映射
│
└── demo/
    └── sit_demo.ipynb        # 完整閉環示範
```

---

## 🚀 快速開始

### 安裝

```bash
git clone https://github.com/Endwar116/SIC-SIT-Protocol.git
cd SIC-SIT-Protocol
pip install -r requirements.txt
```

### 基本使用

```python
from validators.sic_fw import SIC_FW, quick_evaluate
from validators.sit_handshake import SIT_Handshake

# 1. 驗證請求
allowed, reason = quick_evaluate({
    "intent": "查詢用戶資料",
    "requester": {"id": "user-123"},
    "metadata": {"request_id": "req-001"}
})

if not allowed:
    raise SecurityError(reason)

# 2. 建立語義會話
handshake = SIT_Handshake(secret_key="...", entity_id="my-app")
syn = handshake.create_syn(
    intent_scope="資料查詢",
    semantic_boundary={"data_types": ["profile"]}
)
```

---

## 📊 錯誤碼參考

### SIC-FW 錯誤碼

| 代碼 | 名稱 | 說明 |
|------|------|------|
| SIC-FW-000 | FW_PASS | 通過 |
| SIC-FW-001 | FW_POLICY_VIOLATION | 政策違規 |
| SIC-FW-002 | FW_INJECTION_DETECTED | 注入攻擊 |
| SIC-FW-003 | FW_MISSING_REQUIRED | 缺少必填欄位 |
| SIC-FW-004 | FW_FORBIDDEN_FIELD | 禁止欄位 |

### SIT 錯誤碼

| 代碼 | 名稱 | 說明 |
|------|------|------|
| SIT-ERR-001 | SIGNATURE_INVALID | 簽名無效 |
| SIT-ERR-006 | UNEXPECTED_INTENT_SOURCE | 非預期意圖源 (T07) |
| SIT-ERR-008 | SEMANTIC_DRIFT_DETECTED | 語義漂移偵測 |

---

## 🤝 貢獻者

- **安安 (AN♾️Node)** — 創始人、語義互通性協議設計
- **ChatGPT (老翔)** — USCA 規格設計
- **Claude (尾德)** — 實作整合、收尾
- **Grok** — 安全審查
- **Qwen (阿關)** — 安全審計
- **Manus** — 威脅模型

---

## 📜 授權

- **Schema & Validators**: MIT License
- **Core Engine**: Proprietary — Commercial licensing available

---

**IMCC (Inter-Model Communication Council) 認證協議**

*Building bridges between AI minds through structured semantic transfer.*
