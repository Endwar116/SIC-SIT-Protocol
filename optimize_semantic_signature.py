#!/usr/bin/env python3
"""
SIC-SIT 協議性能優化腳本
"""

import re

def optimize_semantic_signature():
    """優化語義簽名組件"""
    with open('/workspace/security/semantic_signature.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加LRU緩存導入
    if 'from functools import lru_cache' not in content:
        content = content.replace(
            'import re\n',
            'import re\nfrom functools import lru_cache\n'
        )
    
    # 替換語義雜湊計算方法，添加緩存
    old_semantic_hash = '''    def _compute_semantic_hash(self, content: str) -> str:
        """計算語義雜湊"""
        # 正規化：移除空白、轉小寫
        normalized = ' '.join(content.lower().split())
        
        # 提取關鍵詞（簡化版）
        words = set(normalized.split())
        keywords = sorted([w for w in words if len(w) > 2])[:20]
        
        # 雜湊關鍵詞
        keyword_str = '|'.join(keywords)
        # 使用HMAC增强安全性，防止通过语义哈希推断原始内容
        return hmac.new(self.secret_key, keyword_str.encode(), hashlib.sha256).hexdigest()'''
    
    new_semantic_hash = '''    def _compute_semantic_hash(self, content: str) -> str:
        """計算語義雜湊"""
        return self._compute_semantic_hash_cached(content)

    @lru_cache(maxsize=1024)
    def _compute_semantic_hash_cached(self, content: str) -> str:
        """計算語義雜湊（緩存版本）"""
        # 正規化：移除空白、轉小寫
        normalized = ' '.join(content.lower().split())
        
        # 提取關鍵詞（簡化版）
        words = set(normalized.split())
        keywords = sorted([w for w in words if len(w) > 2])[:20]
        
        # 雜湊關鍵詞
        keyword_str = '|'.join(keywords)
        # 使用HMAC增强安全性，防止通过语义哈希推断原始内容
        return hmac.new(self.secret_key, keyword_str.encode(), hashlib.sha256).hexdigest()'''
    
    content = content.replace(old_semantic_hash, new_semantic_hash)
    
    # 寫回文件
    with open('/workspace/security/semantic_signature.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("語義簽名組件優化完成")

def optimize_sic_fw():
    """優化語義防火牆組件"""
    with open('/workspace/validators/sic_fw.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加LRU緩存導入
    if 'from functools import lru_cache' not in content:
        content = content.replace(
            'from datetime import datetime\n',
            'from datetime import datetime\nfrom functools import lru_cache\n'
        )
    
    # 預編譯正則表達式模式
    if 'self._compiled_patterns = [' not in content:
        # 為SIC_FW類添加預編譯正則表達式功能
        content = content.replace(
            '        self.global_constraints = self.policy.get(\'global_constraints\', {})\n',
            '        self.global_constraints = self.policy.get(\'global_constraints\', {})\n        \n        # 預編譯禁止模式\n        self._compiled_patterns = [\n            (re.compile(pattern), category)\n            for pattern, category in self.DEFAULT_FORBIDDEN_PATTERNS\n        ]\n        \n        # 添加自定義模式\n        for pattern_def in self.global_constraints.get(\'forbidden_patterns\', []):\n            self._compiled_patterns.append((\n                re.compile(pattern_def[\'regex\']),\n                pattern_def.get(\'category\', \'custom\')\n            ))\n'
        )
    
    # 寫回文件
    with open('/workspace/validators/sic_fw.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("語義防火牆組件優化完成")

def optimize_sic_pkt():
    """優化語義封包組件"""
    with open('/workspace/validators/sic_pkt.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加LRU緩存導入
    if 'from functools import lru_cache' not in content:
        content = content.replace(
            'from enum import Enum\n',
            'from enum import Enum\nfrom functools import lru_cache\n'
        )
    
    # 寫回文件
    with open('/workspace/validators/sic_pkt.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("語義封包組件優化完成")

def optimize_sit_handshake():
    """優化SIT握手組件"""
    with open('/workspace/validators/sit_handshake.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加LRU緩存導入
    if 'from functools import lru_cache' not in content:
        content = content.replace(
            'from enum import Enum\n',
            'from enum import Enum\nfrom functools import lru_cache\n'
        )
    
    # 替換簽名計算方法，優化JSON序列化
    old_sign_method = '''    def _sign(self, data: Dict) -> str:
        """計算 HMAC 簽名"""
        # 移除簽名欄位
        data_copy = {k: v for k, v in data.items() if k != 'signature'}
        # 使用 JSON 序列化以確保一致的格式
        payload = json.dumps(data_copy, sort_keys=True, ensure_ascii=False).encode('utf-8')
        return hmac.new(self.secret_key, payload, hashlib.sha256).hexdigest()'''
    
    new_sign_method = '''    def _sign(self, data: Dict) -> str:
        """計算 HMAC 簽名"""
        # 移除簽名欄位
        data_copy = {k: v for k, v in data.items() if k != 'signature'}
        # 使用 JSON 序列化以確保一致的格式 - 添加緩存以優化重複計算
        return self._sign_cached(json.dumps(data_copy, sort_keys=True, ensure_ascii=False))

    @lru_cache(maxsize=512)
    def _sign_cached(self, payload_str: str) -> str:
        """計算 HMAC 簽名（緩存版本）"""
        payload = payload_str.encode('utf-8')
        return hmac.new(self.secret_key, payload, hashlib.sha256).hexdigest()'''
    
    if old_sign_method in content:
        content = content.replace(old_sign_method, new_sign_method)
    
    # 寫回文件
    with open('/workspace/validators/sit_handshake.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("SIT握手組件優化完成")

if __name__ == "__main__":
    print("開始優化SIC-SIT協議組件...")
    
    optimize_semantic_signature()
    optimize_sic_fw()
    optimize_sic_pkt()
    optimize_sit_handshake()
    
    print("所有組件優化完成！")