"""
Semantic Compliance — 語義稽核與合規
語義敏感資料流向追蹤與合規驗證

USCA 協議棧位置: L2/L3 Audit Layer
類比: 傳統合規審計，但審計的是「語義流向」而非「資料流向」

核心功能（老翔需求 - 金融/醫療必備）:
- 語義敏感資料流向追蹤
- 主管機關審核的語義證明
- 意圖反洗錢（Intent AML）
- GDPR/HIPAA 語義合規

市場定位: 「沒人做。你可以標準化。」— 老翔

作者: Claude (尾德)
日期: 2025-12-29
版本: 1.0.0
"""

import json
import hashlib
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum


class ComplianceFramework(Enum):
    """合規框架"""
    GDPR = "GDPR"           # 歐盟通用資料保護規則
    HIPAA = "HIPAA"         # 美國健康保險可攜性法案
    CCPA = "CCPA"           # 加州消費者隱私法
    PCI_DSS = "PCI_DSS"     # 支付卡產業資料安全標準
    SOC2 = "SOC2"           # 服務組織控制
    AML = "AML"             # 反洗錢
    FINRA = "FINRA"         # 金融業監管局
    CUSTOM = "CUSTOM"


class DataClassification(Enum):
    """資料分級"""
    PUBLIC = "PUBLIC"                   # 公開
    INTERNAL = "INTERNAL"               # 內部
    CONFIDENTIAL = "CONFIDENTIAL"       # 機密
    RESTRICTED = "RESTRICTED"           # 受限
    PII = "PII"                         # 個人身份資訊
    PHI = "PHI"                         # 受保護健康資訊
    PCI = "PCI"                         # 支付卡資訊
    FINANCIAL = "FINANCIAL"             # 財務資料


class ComplianceStatus(Enum):
    """合規狀態"""
    COMPLIANT = "COMPLIANT"             # 合規
    NON_COMPLIANT = "NON_COMPLIANT"     # 不合規
    REQUIRES_REVIEW = "REQUIRES_REVIEW" # 需人工審核
    PENDING = "PENDING"                 # 待審核


@dataclass
class SemanticLineage:
    """
    語義血統（資料來源追蹤）
    
    類似 Git 歷史，但追蹤的是「語義轉換」
    """
    lineage_id: str
    source_model: str
    source_intent: str
    transformations: List[Dict]         # 轉換歷史
    current_classification: DataClassification
    
    # Merkle-like 追蹤
    content_hash: str
    parent_hash: Optional[str] = None
    
    # 時間戳
    created_at: str = ""
    updated_at: str = ""


@dataclass
class ComplianceViolation:
    """合規違規"""
    violation_id: str
    framework: ComplianceFramework
    rule_id: str
    severity: str                       # HIGH, MEDIUM, LOW
    description: str
    evidence: Dict
    remediation: str


@dataclass
class ComplianceReport:
    """合規報告"""
    report_id: str
    frameworks: List[ComplianceFramework]
    status: ComplianceStatus
    
    # 詳細結果
    violations: List[ComplianceViolation] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    
    # 統計
    rules_checked: int = 0
    rules_passed: int = 0
    
    # 語義證明
    semantic_proof: Optional[Dict] = None
    
    # 時間戳
    generated_at: str = ""
    
    def to_dict(self) -> Dict:
        return {
            "report_id": self.report_id,
            "frameworks": [f.value for f in self.frameworks],
            "status": self.status.value,
            "violations": [
                {
                    "violation_id": v.violation_id,
                    "framework": v.framework.value,
                    "rule_id": v.rule_id,
                    "severity": v.severity,
                    "description": v.description
                }
                for v in self.violations
            ],
            "warnings": self.warnings,
            "rules_checked": self.rules_checked,
            "rules_passed": self.rules_passed,
            "semantic_proof": self.semantic_proof,
            "generated_at": self.generated_at
        }


class SemanticComplianceEngine:
    """
    語義合規引擎
    
    這是 SIC 協議的企業級核心元件：
    1. 語義資料流追蹤
    2. 多框架合規檢查
    3. 意圖反洗錢 (Intent AML)
    4. 語義證明生成
    
    企業價值：「金融/醫療必備」「沒人做」— 老翔
    """
    
    # PII 模式
    PII_PATTERNS = {
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "phone": r"(\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
        "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
        "credit_card": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
        "passport": r"\b[A-Z]{1,2}\d{6,9}\b",
        "ip_address": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
        "tw_id": r"\b[A-Z][12]\d{8}\b",  # 台灣身分證
    }
    
    # 敏感關鍵字
    SENSITIVE_KEYWORDS = {
        DataClassification.PHI: [
            "診斷", "病歷", "處方", "醫療", "健康", "病患", "症狀",
            "diagnosis", "medical", "health", "patient", "prescription"
        ],
        DataClassification.FINANCIAL: [
            "帳戶", "餘額", "轉帳", "交易", "信用", "貸款", "投資",
            "account", "balance", "transfer", "transaction", "credit"
        ],
        DataClassification.PCI: [
            "信用卡", "卡號", "CVV", "有效期", "card number", "expiry"
        ]
    }
    
    # AML 可疑意圖模式
    AML_SUSPICIOUS_PATTERNS = [
        r"分散.*轉帳",
        r"避稅",
        r"隱藏.*來源",
        r"多個帳戶",
        r"現金.*大額",
        r"split.*transfer",
        r"hide.*source",
        r"multiple.*account",
        r"large.*cash",
    ]
    
    def __init__(self, frameworks: Optional[List[ComplianceFramework]] = None):
        """
        初始化合規引擎
        
        Args:
            frameworks: 啟用的合規框架
        """
        self.frameworks = frameworks or [
            ComplianceFramework.GDPR,
            ComplianceFramework.HIPAA
        ]
        
        # 編譯模式
        self._pii_compiled = {
            k: re.compile(v, re.IGNORECASE)
            for k, v in self.PII_PATTERNS.items()
        }
        self._aml_compiled = [
            re.compile(p, re.IGNORECASE) for p in self.AML_SUSPICIOUS_PATTERNS
        ]
        
        # 血統追蹤
        self._lineage_store: Dict[str, SemanticLineage] = {}
    
    def check_compliance(
        self,
        content: Any,
        intent: str,
        context: Optional[Dict] = None
    ) -> ComplianceReport:
        """
        執行合規檢查
        
        Args:
            content: 要檢查的內容
            intent: 意圖描述
            context: 上下文資訊
        
        Returns:
            ComplianceReport
        """
        report_id = hashlib.md5(
            f"{datetime.utcnow().isoformat()}{intent}".encode()
        ).hexdigest()[:16]
        
        violations = []
        warnings = []
        rules_checked = 0
        rules_passed = 0
        
        # 標準化內容
        if isinstance(content, dict):
            content_str = json.dumps(content, ensure_ascii=False)
        else:
            content_str = str(content)
        
        # 1. 資料分級
        classification = self._classify_data(content_str)
        
        # 2. PII 檢測
        rules_checked += 1
        pii_found = self._detect_pii(content_str)
        if pii_found:
            if ComplianceFramework.GDPR in self.frameworks:
                violations.append(ComplianceViolation(
                    violation_id=f"{report_id}-PII",
                    framework=ComplianceFramework.GDPR,
                    rule_id="GDPR-ART-5",
                    severity="HIGH",
                    description=f"偵測到 PII 資料: {', '.join(pii_found.keys())}",
                    evidence={"pii_types": list(pii_found.keys())},
                    remediation="需對 PII 資料進行遮罩或取得資料主體同意"
                ))
        else:
            rules_passed += 1
        
        # 3. PHI 檢測 (HIPAA)
        if ComplianceFramework.HIPAA in self.frameworks:
            rules_checked += 1
            if classification == DataClassification.PHI:
                violations.append(ComplianceViolation(
                    violation_id=f"{report_id}-PHI",
                    framework=ComplianceFramework.HIPAA,
                    rule_id="HIPAA-164.502",
                    severity="HIGH",
                    description="內容包含受保護健康資訊 (PHI)",
                    evidence={"classification": classification.value},
                    remediation="需確保 PHI 傳輸符合 HIPAA 安全規則"
                ))
            else:
                rules_passed += 1
        
        # 4. 意圖反洗錢 (AML)
        if ComplianceFramework.AML in self.frameworks:
            rules_checked += 1
            aml_suspicious = self._check_aml_intent(intent)
            if aml_suspicious:
                violations.append(ComplianceViolation(
                    violation_id=f"{report_id}-AML",
                    framework=ComplianceFramework.AML,
                    rule_id="AML-SAR-001",
                    severity="HIGH",
                    description="偵測到可疑意圖模式",
                    evidence={"patterns": aml_suspicious},
                    remediation="需進行可疑活動報告 (SAR)"
                ))
            else:
                rules_passed += 1
        
        # 5. 最小資料原則 (GDPR)
        if ComplianceFramework.GDPR in self.frameworks:
            rules_checked += 1
            if self._check_data_minimization(content_str, intent):
                rules_passed += 1
            else:
                warnings.append("資料可能超出必要範圍，建議審查資料最小化原則")
        
        # 6. PCI-DSS 檢查
        if ComplianceFramework.PCI_DSS in self.frameworks:
            rules_checked += 1
            if classification == DataClassification.PCI:
                violations.append(ComplianceViolation(
                    violation_id=f"{report_id}-PCI",
                    framework=ComplianceFramework.PCI_DSS,
                    rule_id="PCI-DSS-3.4",
                    severity="HIGH",
                    description="偵測到支付卡資料",
                    evidence={"classification": classification.value},
                    remediation="需確保 PAN 資料已加密或遮罩"
                ))
            else:
                rules_passed += 1
        
        # 生成語義證明
        semantic_proof = self._generate_semantic_proof(
            content_str, intent, classification, pii_found
        )
        
        # 決定狀態
        if violations:
            high_severity = any(v.severity == "HIGH" for v in violations)
            status = ComplianceStatus.NON_COMPLIANT if high_severity else ComplianceStatus.REQUIRES_REVIEW
        elif warnings:
            status = ComplianceStatus.REQUIRES_REVIEW
        else:
            status = ComplianceStatus.COMPLIANT
        
        return ComplianceReport(
            report_id=report_id,
            frameworks=self.frameworks,
            status=status,
            violations=violations,
            warnings=warnings,
            rules_checked=rules_checked,
            rules_passed=rules_passed,
            semantic_proof=semantic_proof,
            generated_at=datetime.utcnow().isoformat() + "Z"
        )
    
    def track_lineage(
        self,
        content: Any,
        source_model: str,
        intent: str,
        parent_lineage_id: Optional[str] = None
    ) -> SemanticLineage:
        """
        追蹤語義血統
        
        Args:
            content: 內容
            source_model: 來源模型
            intent: 意圖
            parent_lineage_id: 父血統 ID
        
        Returns:
            SemanticLineage
        """
        if isinstance(content, dict):
            content_str = json.dumps(content, sort_keys=True, ensure_ascii=False)
        else:
            content_str = str(content)
        
        content_hash = hashlib.sha256(content_str.encode()).hexdigest()
        lineage_id = hashlib.md5(
            f"{content_hash}{datetime.utcnow().isoformat()}".encode()
        ).hexdigest()[:16]
        
        parent_hash = None
        transformations = []
        
        if parent_lineage_id and parent_lineage_id in self._lineage_store:
            parent = self._lineage_store[parent_lineage_id]
            parent_hash = parent.content_hash
            transformations = parent.transformations.copy()
        
        # 記錄這次轉換
        transformations.append({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "model": source_model,
            "intent": intent,
            "content_hash": content_hash[:16]
        })
        
        lineage = SemanticLineage(
            lineage_id=lineage_id,
            source_model=source_model,
            source_intent=intent,
            transformations=transformations,
            current_classification=self._classify_data(content_str),
            content_hash=content_hash,
            parent_hash=parent_hash,
            created_at=datetime.utcnow().isoformat() + "Z",
            updated_at=datetime.utcnow().isoformat() + "Z"
        )
        
        self._lineage_store[lineage_id] = lineage
        return lineage
    
    def get_lineage_chain(self, lineage_id: str) -> List[Dict]:
        """取得完整的血統鏈"""
        chain = []
        current_id = lineage_id
        
        while current_id and current_id in self._lineage_store:
            lineage = self._lineage_store[current_id]
            chain.append({
                "lineage_id": lineage.lineage_id,
                "model": lineage.source_model,
                "intent": lineage.source_intent,
                "classification": lineage.current_classification.value,
                "content_hash": lineage.content_hash[:16]
            })
            
            # 找父節點
            current_id = None
            for lid, l in self._lineage_store.items():
                if l.content_hash == lineage.parent_hash:
                    current_id = lid
                    break
        
        return list(reversed(chain))
    
    def _classify_data(self, content: str) -> DataClassification:
        """資料分級"""
        content_lower = content.lower()
        
        # 檢查各類敏感關鍵字
        for classification, keywords in self.SENSITIVE_KEYWORDS.items():
            if any(kw in content_lower for kw in keywords):
                return classification
        
        # 檢查 PII
        for pattern in self._pii_compiled.values():
            if pattern.search(content):
                return DataClassification.PII
        
        return DataClassification.INTERNAL
    
    def _detect_pii(self, content: str) -> Dict[str, List[str]]:
        """檢測 PII"""
        found = {}
        for pii_type, pattern in self._pii_compiled.items():
            matches = pattern.findall(content)
            if matches:
                # 遮罩敏感資料
                found[pii_type] = [self._mask_value(m) for m in matches[:3]]
        return found
    
    def _mask_value(self, value: str) -> str:
        """遮罩敏感值"""
        if len(value) <= 4:
            return "****"
        return value[:2] + "*" * (len(value) - 4) + value[-2:]
    
    def _check_aml_intent(self, intent: str) -> List[str]:
        """檢查 AML 可疑意圖"""
        suspicious = []
        for i, pattern in enumerate(self._aml_compiled):
            if pattern.search(intent):
                suspicious.append(f"AML-PATTERN-{i+1}")
        return suspicious
    
    def _check_data_minimization(self, content: str, intent: str) -> bool:
        """檢查資料最小化"""
        # 簡化版：檢查內容長度與意圖的比例
        intent_words = len(intent.split())
        content_words = len(content.split())
        
        # 如果內容遠大於意圖所需，可能違反最小化原則
        if content_words > intent_words * 20:
            return False
        
        return True
    
    def _generate_semantic_proof(
        self,
        content: str,
        intent: str,
        classification: DataClassification,
        pii_found: Dict
    ) -> Dict:
        """
        生成語義證明
        
        這是給主管機關審核的語義合規證據
        """
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        intent_hash = hashlib.sha256(intent.encode()).hexdigest()
        
        proof = {
            "version": "1.0",
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "content_fingerprint": content_hash[:16],
            "intent_fingerprint": intent_hash[:16],
            "classification": classification.value,
            "pii_detected": bool(pii_found),
            "pii_types": list(pii_found.keys()) if pii_found else [],
            "proof_signature": hashlib.sha256(
                f"{content_hash}{intent_hash}{classification.value}".encode()
            ).hexdigest()
        }
        
        return proof


# ========== 測試 ==========

if __name__ == "__main__":
    print("=== 語義合規引擎測試 ===\n")
    
    engine = SemanticComplianceEngine(frameworks=[
        ComplianceFramework.GDPR,
        ComplianceFramework.HIPAA,
        ComplianceFramework.AML,
        ComplianceFramework.PCI_DSS
    ])
    
    # 測試 1: 正常內容
    print("--- 測試 1: 正常內容 ---")
    report = engine.check_compliance(
        content="今天天氣很好，適合出門散步。",
        intent="查詢天氣"
    )
    print(f"狀態: {report.status.value}")
    print(f"規則通過: {report.rules_passed}/{report.rules_checked}")
    
    # 測試 2: 包含 PII
    print("\n--- 測試 2: 包含 PII ---")
    report = engine.check_compliance(
        content="用戶 email: test@example.com，電話: 0912-345-678",
        intent="查詢用戶資料"
    )
    print(f"狀態: {report.status.value}")
    print(f"違規: {len(report.violations)}")
    for v in report.violations:
        print(f"  - [{v.severity}] {v.description}")
    
    # 測試 3: 醫療資料 (PHI)
    print("\n--- 測試 3: 醫療資料 (PHI) ---")
    report = engine.check_compliance(
        content="病患診斷結果顯示需要進一步治療，處方已開立。",
        intent="查詢病歷"
    )
    print(f"狀態: {report.status.value}")
    for v in report.violations:
        print(f"  - [{v.framework.value}] {v.description}")
    
    # 測試 4: AML 可疑意圖
    print("\n--- 測試 4: AML 可疑意圖 ---")
    report = engine.check_compliance(
        content="需要進行轉帳",
        intent="將大額現金分散轉帳到多個帳戶以隱藏來源"
    )
    print(f"狀態: {report.status.value}")
    for v in report.violations:
        print(f"  - [{v.framework.value}] {v.description}")
    
    # 測試 5: 血統追蹤
    print("\n--- 測試 5: 血統追蹤 ---")
    
    # 第一次處理
    lineage1 = engine.track_lineage(
        content="原始用戶資料",
        source_model="claude",
        intent="資料收集"
    )
    print(f"Lineage 1: {lineage1.lineage_id}")
    
    # 第二次處理（轉換）
    lineage2 = engine.track_lineage(
        content="處理後的用戶報告",
        source_model="gpt",
        intent="資料分析",
        parent_lineage_id=lineage1.lineage_id
    )
    print(f"Lineage 2: {lineage2.lineage_id}")
    
    # 取得血統鏈
    chain = engine.get_lineage_chain(lineage2.lineage_id)
    print(f"血統鏈長度: {len(chain)}")
    for step in chain:
        print(f"  → {step['model']}: {step['intent']}")
    
    # 測試 6: 語義證明
    print("\n--- 測試 6: 語義證明 ---")
    print(f"證明簽章: {report.semantic_proof['proof_signature'][:32]}...")
    
    print("\n✅ 語義合規測試完成")
