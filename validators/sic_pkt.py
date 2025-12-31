"""
SIC-PKT — Semantic Interchange Core Packet Handler
語義交換核心封包處理器

USCA 協議棧位置: L2 (Network Layer)
類比: IP 封包處理

功能:
- SIC 封包格式定義
- 封包建立與解析
- SHV (Semantic-Hash-Vector) 計算
- TTL 管理

設計來源: 老翔 USCA 規格
實作: Claude (尾德) Round 10+
日期: 2025-12-29
版本: 1.0.0
"""

import json
import uuid
import hashlib
from datetime import datetime
from typing import Any, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache


class SIC_PKT_Type(Enum):
    """封包類型"""
    REQUEST = "REQUEST"       # 請求封包
    RESPONSE = "RESPONSE"     # 回應封包
    CONTROL = "CONTROL"       # 控制封包
    ERROR = "ERROR"           # 錯誤封包


class SIC_PKT_Error(Enum):
    """封包錯誤碼"""
    OK = "SIC-PKT-000"
    INVALID_FORMAT = "SIC-PKT-001"
    MISSING_HEADER = "SIC-PKT-002"
    INVALID_SHV = "SIC-PKT-003"
    TTL_EXPIRED = "SIC-PKT-004"
    PAYLOAD_TOO_LARGE = "SIC-PKT-005"
    VERSION_MISMATCH = "SIC-PKT-006"


@dataclass
class SIC_Header:
    """
    SIC 封包標頭
    
    類比 IP Header，但處理的是語義而非網路地址
    """
    # 核心欄位
    SHV: str                    # Semantic-Hash-Vector (語義哈希)
    SID: str                    # Semantic-ID (封包語義源頭)
    TTL: int = 10               # Semantic Time-to-Live
    VER: str = "1.0.0"          # Protocol Version
    
    # 路由欄位
    src_model: str = ""         # 源模型
    dst_model: str = ""         # 目標模型
    hop_count: int = 0          # 跳躍次數
    
    # 元數據
    pkt_type: SIC_PKT_Type = SIC_PKT_Type.REQUEST
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    
    def to_dict(self) -> Dict:
        return {
            "SHV": self.SHV,
            "SID": self.SID,
            "TTL": self.TTL,
            "VER": self.VER,
            "src_model": self.src_model,
            "dst_model": self.dst_model,
            "hop_count": self.hop_count,
            "pkt_type": self.pkt_type.value,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "SIC_Header":
        return cls(
            SHV=data.get("SHV", ""),
            SID=data.get("SID", ""),
            TTL=data.get("TTL", 10),
            VER=data.get("VER", "1.0.0"),
            src_model=data.get("src_model", ""),
            dst_model=data.get("dst_model", ""),
            hop_count=data.get("hop_count", 0),
            pkt_type=SIC_PKT_Type(data.get("pkt_type", "REQUEST")),
            timestamp=data.get("timestamp", "")
        )


@dataclass
class SIC_Packet:
    """
    SIC 封包
    
    完整的語義交換封包，包含標頭和載荷
    """
    header: SIC_Header
    payload: Dict               # SIT State JSON
    
    # 驗證資訊
    valid: bool = True
    error: Optional[SIC_PKT_Error] = None
    
    def to_dict(self) -> Dict:
        return {
            "header": self.header.to_dict(),
            "payload": self.payload
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)
    
    @classmethod
    def from_dict(cls, data: Dict) -> "SIC_Packet":
        header = SIC_Header.from_dict(data.get("header", {}))
        payload = data.get("payload", {})
        return cls(header=header, payload=payload)
    
    @classmethod
    def from_json(cls, json_str: str) -> "SIC_Packet":
        data = json.loads(json_str)
        return cls.from_dict(data)


class SIC_PKT_Handler:
    """
    SIC 封包處理器
    
    提供封包的建立、解析、驗證和路由功能
    """
    
    # 配置
    MAX_PAYLOAD_SIZE = 1024 * 1024  # 1MB
    SUPPORTED_VERSIONS = ["1.0.0", "1.0.1"]
    
    def __init__(self, model_id: str):
        """
        初始化封包處理器
        
        Args:
            model_id: 本模型的識別碼
        """
        self.model_id = model_id
    
    def create_packet(
        self,
        payload: Dict,
        dst_model: str = "",
        pkt_type: SIC_PKT_Type = SIC_PKT_Type.REQUEST,
        ttl: int = 10
    ) -> SIC_Packet:
        """
        建立 SIC 封包
        
        Args:
            payload: SIT State JSON
            dst_model: 目標模型
            pkt_type: 封包類型
            ttl: Time-to-Live
        
        Returns:
            SIC_Packet
        """
        # 計算 SHV (Semantic-Hash-Vector)
        shv = self._compute_shv(payload)
        
        # 生成 SID
        sid = str(uuid.uuid4())
        
        header = SIC_Header(
            SHV=shv,
            SID=sid,
            TTL=ttl,
            src_model=self.model_id,
            dst_model=dst_model,
            pkt_type=pkt_type
        )
        
        return SIC_Packet(header=header, payload=payload)
    
    def parse_packet(self, data: Any) -> Tuple[Optional[SIC_Packet], Optional[SIC_PKT_Error]]:
        """
        解析封包
        
        Args:
            data: JSON 字串或字典
        
        Returns:
            (SIC_Packet, None) 成功
            (None, error) 失敗
        """
        try:
            if isinstance(data, str):
                pkt = SIC_Packet.from_json(data)
            elif isinstance(data, dict):
                pkt = SIC_Packet.from_dict(data)
            else:
                return None, SIC_PKT_Error.INVALID_FORMAT
        except json.JSONDecodeError:
            return None, SIC_PKT_Error.INVALID_FORMAT
        except Exception:
            return None, SIC_PKT_Error.INVALID_FORMAT
        
        return pkt, None
    
    def validate_packet(self, pkt: SIC_Packet) -> Tuple[bool, Optional[SIC_PKT_Error]]:
        """
        驗證封包
        
        Args:
            pkt: 要驗證的封包
        
        Returns:
            (True, None) 有效
            (False, error) 無效
        """
        header = pkt.header
        
        # 檢查必要欄位
        if not header.SHV or not header.SID:
            return False, SIC_PKT_Error.MISSING_HEADER
        
        # 驗證 SHV
        expected_shv = self._compute_shv(pkt.payload)
        if header.SHV != expected_shv:
            return False, SIC_PKT_Error.INVALID_SHV
        
        # 檢查 TTL
        if header.TTL <= 0:
            return False, SIC_PKT_Error.TTL_EXPIRED
        
        # 檢查版本
        if header.VER not in self.SUPPORTED_VERSIONS:
            return False, SIC_PKT_Error.VERSION_MISMATCH
        
        # 檢查載荷大小
        payload_size = len(json.dumps(pkt.payload))
        if payload_size > self.MAX_PAYLOAD_SIZE:
            return False, SIC_PKT_Error.PAYLOAD_TOO_LARGE
        
        return True, None
    
    def forward_packet(self, pkt: SIC_Packet, next_model: str) -> SIC_Packet:
        """
        轉發封包（減少 TTL，更新路由資訊）
        
        Args:
            pkt: 要轉發的封包
            next_model: 下一跳模型
        
        Returns:
            更新後的封包
        """
        # 減少 TTL
        pkt.header.TTL -= 1
        
        # 增加跳躍計數
        pkt.header.hop_count += 1
        
        # 更新目標
        pkt.header.dst_model = next_model
        
        return pkt
    
    def create_error_packet(
        self,
        original_pkt: SIC_Packet,
        error: SIC_PKT_Error,
        message: str = ""
    ) -> SIC_Packet:
        """
        建立錯誤回應封包
        
        Args:
            original_pkt: 原始封包
            error: 錯誤碼
            message: 錯誤訊息
        
        Returns:
            錯誤封包
        """
        error_payload = {
            "error_code": error.value,
            "message": message,
            "original_sid": original_pkt.header.SID
        }
        
        return self.create_packet(
            payload=error_payload,
            dst_model=original_pkt.header.src_model,
            pkt_type=SIC_PKT_Type.ERROR
        )
    
    def _compute_shv(self, payload: Dict) -> str:
        """
        計算 Semantic-Hash-Vector
        
        這是語義內容的唯一識別碼，類似於 IP 封包的校驗碼
        但這裡雜湊的是「語義內容」而非「位元組」
        """
        # 正規化 JSON
        normalized = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        
        # 計算 SHA-256
        return hashlib.sha256(normalized.encode('utf-8')).hexdigest()
    
    def compute_semantic_distance(self, pkt1: SIC_Packet, pkt2: SIC_Packet) -> float:
        """
        計算兩個封包的語義距離
        
        用於路由決策：選擇語義距離最近的路徑
        
        Returns:
            0.0 = 完全相同
            1.0 = 完全不同
        """
        # 簡化版：比較 intent 字串的相似度
        intent1 = pkt1.payload.get("intent", "")
        intent2 = pkt2.payload.get("intent", "")
        
        if not intent1 or not intent2:
            return 1.0
        
        # 使用字符級別的 Jaccard 相似度
        set1 = set(intent1)
        set2 = set(intent2)
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        if union == 0:
            return 1.0
        
        similarity = intersection / union
        return 1.0 - similarity


# ========== Schema 定義 ==========

SIC_PKT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://sic-protocol.dev/schema/sic-pkt-v1.json",
    "title": "SIC Packet Schema",
    "type": "object",
    "required": ["header", "payload"],
    "properties": {
        "header": {
            "type": "object",
            "required": ["SHV", "SID", "TTL", "VER"],
            "properties": {
                "SHV": {
                    "type": "string",
                    "description": "Semantic-Hash-Vector",
                    "pattern": "^[a-f0-9]{64}$"
                },
                "SID": {
                    "type": "string",
                    "description": "Semantic-ID (UUID)",
                    "format": "uuid"
                },
                "TTL": {
                    "type": "integer",
                    "description": "Semantic Time-to-Live",
                    "minimum": 0,
                    "maximum": 255
                },
                "VER": {
                    "type": "string",
                    "description": "Protocol Version",
                    "pattern": "^\\d+\\.\\d+\\.\\d+$"
                },
                "src_model": {"type": "string"},
                "dst_model": {"type": "string"},
                "hop_count": {"type": "integer", "minimum": 0},
                "pkt_type": {
                    "type": "string",
                    "enum": ["REQUEST", "RESPONSE", "CONTROL", "ERROR"]
                },
                "timestamp": {"type": "string", "format": "date-time"}
            }
        },
        "payload": {
            "type": "object",
            "description": "SIT State JSON"
        }
    }
}


# ========== 測試 ==========

if __name__ == "__main__":
    print("=== SIC-PKT 封包處理器測試 ===\n")
    
    handler = SIC_PKT_Handler(model_id="claude-001")
    
    # 測試 1: 建立封包
    print("--- 測試 1: 建立封包 ---")
    payload = {
        "intent": "查詢用戶資料",
        "requester": {"id": "user-123", "role": "user"},
        "constraints": {"max_tokens": 1000}
    }
    
    pkt = handler.create_packet(
        payload=payload,
        dst_model="gpt-001",
        ttl=5
    )
    
    print(f"SHV: {pkt.header.SHV[:32]}...")
    print(f"SID: {pkt.header.SID}")
    print(f"TTL: {pkt.header.TTL}")
    print(f"路由: {pkt.header.src_model} → {pkt.header.dst_model}")
    
    # 測試 2: 驗證封包
    print("\n--- 測試 2: 驗證封包 ---")
    valid, error = handler.validate_packet(pkt)
    print(f"有效: {valid}")
    print(f"錯誤: {error}")
    
    # 測試 3: 篡改檢測
    print("\n--- 測試 3: 篡改檢測 ---")
    pkt.payload["intent"] = "惡意意圖"  # 篡改
    valid, error = handler.validate_packet(pkt)
    print(f"篡改後有效: {valid}")
    print(f"錯誤碼: {error}")
    
    # 測試 4: 轉發封包
    print("\n--- 測試 4: 轉發封包 ---")
    # 恢復原始內容
    pkt.payload["intent"] = "查詢用戶資料"
    pkt.header.SHV = handler._compute_shv(pkt.payload)
    
    forwarded = handler.forward_packet(pkt, "gemini-001")
    print(f"新 TTL: {forwarded.header.TTL}")
    print(f"跳躍次數: {forwarded.header.hop_count}")
    print(f"新目標: {forwarded.header.dst_model}")
    
    # 測試 5: 序列化/反序列化
    print("\n--- 測試 5: 序列化/反序列化 ---")
    json_str = pkt.to_json()
    print(f"JSON 長度: {len(json_str)} bytes")
    
    parsed, error = handler.parse_packet(json_str)
    print(f"解析成功: {error is None}")
    print(f"SID 匹配: {parsed.header.SID == pkt.header.SID}")
    
    print("\n✅ SIC-PKT 測試完成")
