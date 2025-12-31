"""
SIC-RTR — Semantic Router
語義路由器

USCA 協議棧位置: L2 (Network Layer)
類比: IP Router，但路由依據是「語義距離」而非「網路拓撲」

核心功能（老翔需求）:
- 以語義距離（cosine / KL / HNSW）判斷路徑
- 以"語境相似度"選擇最短語義路徑
- 向量 Mesh routing（像 IP mesh，但以 meaning 走）
- 動態語境路由（context-aware routing）

市場定位: 這個市場完全沒人做 — 老翔

作者: Claude (尾德)
日期: 2025-12-29
版本: 1.0.0
"""

import math
import hashlib
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from functools import lru_cache
import json


class RoutingStrategy(Enum):
    """路由策略"""
    NEAREST = "NEAREST"           # 最近語義距離
    BROADCAST = "BROADCAST"       # 廣播到所有
    MULTIPATH = "MULTIPATH"       # 多路徑
    FAILOVER = "FAILOVER"         # 故障轉移
    CONTEXT_AWARE = "CONTEXT_AWARE"  # 語境感知


@dataclass
class SemanticNode:
    """語義節點（模型/服務端點）"""
    node_id: str
    model_type: str              # claude, gpt, gemini, qwen, etc.
    capabilities: List[str]      # 能力標籤
    semantic_profile: Dict       # 語義特徵向量（簡化版）
    load: float = 0.0            # 當前負載 0-1
    available: bool = True
    latency_ms: float = 0.0
    
    # 語義專長
    domains: List[str] = field(default_factory=list)  # 專長領域
    languages: List[str] = field(default_factory=list)  # 支援語言


@dataclass
class RouteDecision:
    """路由決策結果"""
    selected_nodes: List[SemanticNode]
    strategy_used: RoutingStrategy
    semantic_distance: float
    reasoning: str
    alternatives: List[SemanticNode] = field(default_factory=list)


class SIC_Router:
    """
    SIC 語義路由器
    
    這是 SIC 協議的核心路由元件：
    - 根據語義相似度選擇最佳目標
    - 支援多模型負載均衡
    - 動態語境感知路由
    
    市場價值：「向量世界的 Cisco」— 老翔
    """
    
    def __init__(self):
        self.nodes: Dict[str, SemanticNode] = {}
        self.routing_table: Dict[str, List[str]] = {}  # domain -> [node_ids]
        self.route_cache: Dict[str, RouteDecision] = {}
    
    def register_node(self, node: SemanticNode):
        """註冊語義節點"""
        self.nodes[node.node_id] = node
        
        # 更新路由表
        for domain in node.domains:
            if domain not in self.routing_table:
                self.routing_table[domain] = []
            if node.node_id not in self.routing_table[domain]:
                self.routing_table[domain].append(node.node_id)
    
    def unregister_node(self, node_id: str):
        """註銷語義節點"""
        if node_id in self.nodes:
            node = self.nodes.pop(node_id)
            for domain in node.domains:
                if domain in self.routing_table:
                    self.routing_table[domain] = [
                        n for n in self.routing_table[domain] if n != node_id
                    ]
    
    def route(
        self,
        intent: str,
        context: Optional[Dict] = None,
        strategy: RoutingStrategy = RoutingStrategy.NEAREST,
        required_capabilities: Optional[List[str]] = None
    ) -> RouteDecision:
        """
        執行語義路由
        
        Args:
            intent: 意圖描述
            context: 語境上下文
            strategy: 路由策略
            required_capabilities: 必要能力
        
        Returns:
            RouteDecision 路由決策
        """
        # 計算意圖的語義特徵
        intent_profile = self._compute_intent_profile(intent, context)
        
        # 過濾可用節點
        candidates = [
            node for node in self.nodes.values()
            if node.available and self._meets_requirements(node, required_capabilities)
        ]
        
        if not candidates:
            return RouteDecision(
                selected_nodes=[],
                strategy_used=strategy,
                semantic_distance=float('inf'),
                reasoning="無可用節點"
            )
        
        # 計算語義距離
        scored_nodes = [
            (node, self._compute_semantic_distance(intent_profile, node))
            for node in candidates
        ]
        
        # 按距離排序（距離越小越好）
        scored_nodes.sort(key=lambda x: x[1])
        
        # 根據策略選擇
        if strategy == RoutingStrategy.NEAREST:
            selected = [scored_nodes[0][0]]
            distance = scored_nodes[0][1]
        elif strategy == RoutingStrategy.MULTIPATH:
            # 選擇前 3 個
            selected = [n for n, _ in scored_nodes[:3]]
            distance = sum(d for _, d in scored_nodes[:3]) / min(3, len(scored_nodes))
        elif strategy == RoutingStrategy.BROADCAST:
            selected = [n for n, _ in scored_nodes]
            distance = sum(d for _, d in scored_nodes) / len(scored_nodes)
        elif strategy == RoutingStrategy.FAILOVER:
            # 選擇最近的，但保留備選
            selected = [scored_nodes[0][0]]
            distance = scored_nodes[0][1]
        elif strategy == RoutingStrategy.CONTEXT_AWARE:
            # 綜合考慮語義距離、負載、延遲
            selected = self._context_aware_select(scored_nodes, context)
            distance = scored_nodes[0][1] if scored_nodes else float('inf')
        else:
            selected = [scored_nodes[0][0]]
            distance = scored_nodes[0][1]
        
        return RouteDecision(
            selected_nodes=selected,
            strategy_used=strategy,
            semantic_distance=distance,
            reasoning=self._generate_reasoning(selected, intent, distance),
            alternatives=[n for n, _ in scored_nodes[1:4]]  # 備選方案
        )
    
    def _compute_intent_profile(self, intent: str, context: Optional[Dict]) -> Dict:
        """
        計算意圖的語義特徵
        
        這是簡化版實作。生產環境應該使用：
        - 真正的 embedding 模型
        - 語義折疊 (Semantic Folding)
        """
        # 簡化版：基於關鍵字的特徵提取
        profile = {
            "keywords": set(),
            "domain_hints": set(),
            "complexity": 0,
            "language": "zh"
        }
        
        intent_lower = intent.lower()
        
        # 領域檢測
        domain_keywords = {
            "finance": ["交易", "帳戶", "金融", "投資", "股票", "transaction", "finance"],
            "medical": ["醫療", "健康", "診斷", "病患", "medical", "health"],
            "legal": ["法律", "合約", "訴訟", "legal", "contract"],
            "technical": ["程式", "代碼", "API", "系統", "code", "technical"],
            "creative": ["創作", "故事", "設計", "creative", "story"],
        }
        
        for domain, keywords in domain_keywords.items():
            if any(kw in intent_lower for kw in keywords):
                profile["domain_hints"].add(domain)
        
        # 複雜度估算
        profile["complexity"] = min(len(intent) / 100, 1.0)
        
        # 語言檢測（簡化）
        if any('\u4e00' <= c <= '\u9fff' for c in intent):
            profile["language"] = "zh"
        else:
            profile["language"] = "en"
        
        return profile
    
    def _compute_semantic_distance(self, intent_profile: Dict, node: SemanticNode) -> float:
        """
        計算語義距離
        
        0.0 = 完全匹配
        1.0 = 完全不匹配
        
        生產環境應該使用：
        - Cosine similarity
        - KL divergence
        - HNSW 索引
        """
        distance = 0.5  # 基礎距離
        
        # 領域匹配加分
        intent_domains = intent_profile.get("domain_hints", set())
        node_domains = set(node.domains)
        
        if intent_domains & node_domains:
            # 有領域交集
            overlap = len(intent_domains & node_domains)
            distance -= 0.2 * overlap
        
        # 語言匹配
        if intent_profile.get("language") in node.languages:
            distance -= 0.1
        
        # 負載懲罰
        distance += node.load * 0.2
        
        # 延遲懲罰
        distance += min(node.latency_ms / 1000, 0.2)
        
        return max(0.0, min(1.0, distance))
    
    def _meets_requirements(self, node: SemanticNode, required: Optional[List[str]]) -> bool:
        """檢查節點是否滿足需求"""
        if not required:
            return True
        return all(cap in node.capabilities for cap in required)
    
    def _context_aware_select(
        self,
        scored_nodes: List[Tuple[SemanticNode, float]],
        context: Optional[Dict]
    ) -> List[SemanticNode]:
        """語境感知選擇"""
        if not scored_nodes:
            return []
        
        # 綜合評分：語義距離 + 負載 + 延遲
        def combined_score(node: SemanticNode, distance: float) -> float:
            return (
                distance * 0.5 +
                node.load * 0.3 +
                min(node.latency_ms / 500, 0.2)
            )
        
        best = min(scored_nodes, key=lambda x: combined_score(x[0], x[1]))
        return [best[0]]
    
    def _generate_reasoning(
        self,
        selected: List[SemanticNode],
        intent: str,
        distance: float
    ) -> str:
        """生成路由決策說明"""
        if not selected:
            return "無可用節點"
        
        node = selected[0]
        return (
            f"選擇 {node.model_type} ({node.node_id}) | "
            f"語義距離: {distance:.3f} | "
            f"負載: {node.load:.1%} | "
            f"延遲: {node.latency_ms:.0f}ms"
        )
    
    # ========== 進階功能 ==========
    
    def find_semantic_path(
        self,
        source_intent: str,
        target_intent: str,
        max_hops: int = 3
    ) -> List[SemanticNode]:
        """
        尋找語義路徑
        
        類似 IP 路由的 traceroute，但追蹤的是「語義轉換路徑」
        例如：中文 → 英文 → 專業術語
        """
        path = []
        current_intent = source_intent
        
        for hop in range(max_hops):
            decision = self.route(current_intent, strategy=RoutingStrategy.NEAREST)
            if not decision.selected_nodes:
                break
            
            node = decision.selected_nodes[0]
            path.append(node)
            
            # 檢查是否到達目標
            target_profile = self._compute_intent_profile(target_intent, None)
            if self._compute_semantic_distance(target_profile, node) < 0.2:
                break
        
        return path
    
    def get_routing_stats(self) -> Dict:
        """取得路由統計"""
        return {
            "total_nodes": len(self.nodes),
            "available_nodes": sum(1 for n in self.nodes.values() if n.available),
            "domains": list(self.routing_table.keys()),
            "avg_load": sum(n.load for n in self.nodes.values()) / max(len(self.nodes), 1)
        }


# ========== 測試 ==========

if __name__ == "__main__":
    print("=== SIC-RTR 語義路由器測試 ===\n")
    
    router = SIC_Router()
    
    # 註冊模型節點
    nodes = [
        SemanticNode(
            node_id="claude-001",
            model_type="claude",
            capabilities=["reasoning", "coding", "analysis"],
            semantic_profile={},
            domains=["technical", "creative"],
            languages=["zh", "en"],
            load=0.3,
            latency_ms=150
        ),
        SemanticNode(
            node_id="gpt-001",
            model_type="gpt",
            capabilities=["general", "coding"],
            semantic_profile={},
            domains=["technical", "general"],
            languages=["en"],
            load=0.5,
            latency_ms=200
        ),
        SemanticNode(
            node_id="gemini-001",
            model_type="gemini",
            capabilities=["multimodal", "analysis"],
            semantic_profile={},
            domains=["technical", "medical"],
            languages=["zh", "en"],
            load=0.2,
            latency_ms=100
        ),
        SemanticNode(
            node_id="qwen-001",
            model_type="qwen",
            capabilities=["chinese", "reasoning"],
            semantic_profile={},
            domains=["finance", "legal"],
            languages=["zh"],
            load=0.1,
            latency_ms=80
        ),
    ]
    
    for node in nodes:
        router.register_node(node)
    
    print(f"已註冊 {len(router.nodes)} 個節點")
    print(f"路由表: {router.routing_table}\n")
    
    # 測試路由
    test_cases = [
        ("幫我寫一個 Python 程式", ["coding"]),
        ("分析這份財務報表", None),
        ("翻譯這段醫療文件", None),
        ("Write a creative story", None),
    ]
    
    for intent, caps in test_cases:
        print(f"--- 意圖: {intent} ---")
        decision = router.route(
            intent=intent,
            required_capabilities=caps,
            strategy=RoutingStrategy.CONTEXT_AWARE
        )
        print(f"決策: {decision.reasoning}")
        if decision.alternatives:
            alt_names = [n.model_type for n in decision.alternatives[:2]]
            print(f"備選: {alt_names}")
        print()
    
    # 統計
    print("--- 路由統計 ---")
    stats = router.get_routing_stats()
    print(f"總節點: {stats['total_nodes']}")
    print(f"可用節點: {stats['available_nodes']}")
    print(f"平均負載: {stats['avg_load']:.1%}")
    
    print("\n✅ SIC-RTR 測試完成")
