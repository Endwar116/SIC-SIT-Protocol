"""
SIC-SIT Protocol
================
Semantic Internet Protocol / Semantic Isolation Transfer

Building the 'Semantic Internet' for AI.
Don't transfer data. Transfer intent.

Core Components:
- SIC (L2): Semantic Interchange Core - Addressing, Routing, Identity
- SIT (L3): Semantic Isolation Transfer - Transmission, Consistency, Flow Control
- SEM-FOLD (L1): Semantic Folding - Encoding, Compression
- SEM-SIG: Semantic Signature - Integrity, Hallucination Detection

Constants:
- S★ (S_STAR) = 2.76: Semantic Density Constant

Usage:
    from sic_sit import quickstart
    quickstart.run()

Author: Andwar Cheng (AN♾️Node) + 老翔宇宙
License: MIT
"""

__version__ = "0.4.0"
__author__ = "Andwar Cheng"

S_STAR = 2.76  # 語義密度常數

# Layer definitions
USCA_STACK = {
    "L6": "SIC-TOP (Topology Intent)",
    "L5": "SIC-INT (Interpretation)",
    "L4": "SIT-SES (Reasoning Session)",
    "L3": "SIT (Semantic Isolation Transfer)",
    "L2": "SIC (Semantic Interchange Core)",
    "L1": "SEM-FOLD (Semantic Folding)",
    "L0": "TOK-RAW (Token Layer)",
}

# Five Axioms
AXIOMS = {
    1: "所有安全漏洞都是邊界故障",
    2: "傳統邊界由記憶體/網路/進程定義",
    3: "AI 原生系統有新邊界：語義意圖",
    4: "如果序列化意圖而不是數據，數據就無法洩漏",
    5: "結構化語義狀態本質上是被消毒的",
}
