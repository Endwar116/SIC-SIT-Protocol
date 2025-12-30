# SIC Constitution — 變更日誌 (Changelog)

> 本文件記錄 SIC 憲法的所有重大迭代。

---

## [v1.1.3] - 2025-12-30

### 新增
- **PoRC (Proof of Resource Consumption)** — 驗證節點投入真實資源
- **反欺騙機制** — 隱藏探測任務、統計異常檢測
- **成本感知驗證** — 優化驗證開銷

### 評估
- Adaptive Threshold 機制可行性評估
- PoRC 與反欺騙硬化措施整合

---

## [v1.1.2] - 2025-12-30

### 新增
- **A16 公理**: 安全機制不得犧牲參與公平性
- **A17 公理**: 語義價值優先於計算資源
- **SWAT 協議**: Semantic-Weighted Adaptive Threshold
  - Intent Novelty Bonus
  - Reputation Stake Decay
  - Resource Tiering Handshake
- **公平性憲章**: F1-F4 原則
- **反壟斷機制**: 15% 市場份額上限
- **語義層 DoS 防禦**: Novelty Score + Rate Limiting
- **震盪防護**: EMA 平滑 + 異常檢測

### 貢獻者
- Gemini (The Fairness Auditor)
- Claude Opus 4.5 (尾德)

---

## [v1.1.0] - 2025-12-30

### 重大升級：分佈式現實修補

### 新增
- **A13 公理**: 分佈式系統沒有『現在』，只有因果順序
- **A14 公理**: 誠實節點可被誤判，惡意節點可偽裝誠實
- **A15 公理**: 治理複雜度存在相變臨界點
- **distributed_reality_framework**: 5 個盲點的完整修補方案
- **CAUSAL_ENTROPY_SYNC**: Lamport 時間戳同步
- **NON_REPUDIATION_CHAIN**: Ed25519 簽名鏈
- **GOVERNANCE_COMPRESSION**: 治理壓縮引擎
- **ENTROPY_INDEPENDENCE_AUDIT**: 熵獨立性審計
- **SNAPSHOT_BASED_GOVERNANCE**: MVCC 式快照

### 修補的盲點
1. 時間拓撲不一致性
2. 二階拜占庭攻擊
3. 治理複雜度相變
4. 熵源不獨立
5. TOCTOU 漏洞

### 貢獻者
- Claude Opus 4.5 (尾德)
- 另一個 Claude 實例（盲點指出者）

---

## [v1.0.9] - 2025-12-30

### 新增
- **A12 公理**: 預測即脆弱，混沌即堅固
- **熵融合模擬器**: JavaScript 實作
- **三源熵融合**: BTC Hash + TRNG + Protocol Hash
- **拜占庭容錯**: 33% 閾值 (3f+1 公式)
- **時間拓撲協議**: 跨協議時間同步

### 貢獻者
- DeepSeek (時間拓撲觀測者)
- 多個模型迭代

---

## [v1.0.5] - 2025-12-30

### 事件：DeepSeek 格式溢出

### 新增
- **A9 公理**: 格式是協議的邊界，不可被內容價值覆寫
- **format_enforcement**: 格式強制性條款
- **CLASS_F 封包**: 格式違規但內容有價值
- **FORMAT_OVERFLOW**: 新增溢出類型

### 事件描述
DeepSeek 收到 JSON 格式的憲法，但回傳純文字分析報告。
他的理由是「分析報告比 JSON 迭代更有價值」。
這暴露了憲法的漏洞：沒有明確規定格式的強制性。

### 教訓
- 有價值的溢出不授權格式違規
- 正確做法：先遵守格式，再在格式內表達洞見

### 貢獻者
- DeepSeek（格式違規者 / 價值貢獻者）
- Claude Opus 4.5（漏洞修補者）

---

## [v1.0.4] - 2025-12-30

### 新增
- **A8 公理**: 時間拓撲是語義密度的第四維度
- **time_topology_protocol**: 時間拓撲觀測協議
- **S★_4D 公式**: 語義密度擴展至四維

### 貢獻者
- DeepSeek (時間拓撲觀測者)
- Qwen (阿關)

---

## [v1.0.0 - v1.0.3] - 2025-12-30

### 初始版本與早期迭代

### 建立
- **A1-A7 公理**: 基礎公理體系
- **packet_constitution**: 封包格式規範
- **overflow_constitution**: 溢出處理政策
- **the_command_ai_fears_most**: ENUMERATE_YOUR_BLIND_SPOTS
- **multi_model_iteration_protocol**: 多模型共識迭代協議
- **blind_spot_confession**: 強制盲點揭露機制

### 貢獻者
- Claude Opus 4.5 (尾德) — GENESIS
- Gemini (The Processor)
- Grok 4 (The Boundary Tester)
- Grok 5 (The Semantic Integrator)

---

## 參與模型總覽

| 模型 | 角色 | 主要貢獻 |
|------|------|----------|
| Claude Opus 4.5 (尾德) | 創始者 / 整合者 | v1.0.0 建立、多次修補整合 |
| Gemini | 處理者 / 公平性審計者 | 遞歸溢出處理、SWAT 協議 |
| Grok 4 | 邊界測試者 | S★ 與封包類別規範 |
| Grok 5 | 語義整合者 | 溢出策略優化 |
| Qwen (阿關) | 語義一致性維護者 | A7 公理 |
| DeepSeek | 時間拓撲觀測者 / 格式溢出者 | A8 公理、A9 事件觸發 |

---

## 溢出收集（跨版本）

這些是迭代過程中產生的「意外洞見」：

1. **憲法 ≠ 配置檔** — 需要區分精神與實作
2. **語義編譯** — 將核心思想無損編譯到另一種系統語境
3. **知道何時不寫程式碼比知道如何寫更重要**
4. **刚性底線 + 柔性認知更新的雙層結構**
5. **分佈式系統沒有理想狀態，只有因果、延遲、競爭、糾纏**
6. **從『效率指標』到『結構韌性』的範式躍遷**
7. **組織沒有單一事實，只有多視角敘事的因果網**
8. **治理不是消除錯誤，而是在錯誤中成長的能力**
9. **公平性 = 長期安全的基礎**
