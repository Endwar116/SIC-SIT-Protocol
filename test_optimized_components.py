#!/usr/bin/env python3
"""
測試優化後的SIC-SIT協議組件
"""

def test_semantic_routing():
    """測試語義路由組件"""
    print("測試語義路由組件...")
    try:
        from core.semantic_routing import SIC_Router, SemanticNode
        router = SIC_Router()
        
        # 添加一個測試節點
        node = SemanticNode(
            node_id="test-node",
            model_type="test",
            capabilities=["test"],
            semantic_profile={},
            domains=["test"],
            languages=["en"]
        )
        router.register_node(node)
        
        # 測試路由功能
        decision = router.route("test intent")
        print(f"  ✓ 路由功能正常: {decision.strategy_used}")
        
        return True
    except Exception as e:
        print(f"  ✗ 路由組件測試失敗: {e}")
        return False

def test_semantic_signature():
    """測試語義簽名組件"""
    print("測試語義簽名組件...")
    try:
        from security.semantic_signature import SemanticIntegrity
        integrity = SemanticIntegrity(secret_key="test-key")
        
        # 測試簽名功能
        content = "test content for signing"
        signature = integrity.sign(content, model_source="test")
        report = integrity.verify(content, signature)
        
        print(f"  ✓ 簽名功能正常: {report.status}")
        
        return True
    except Exception as e:
        print(f"  ✗ 簽名組件測試失敗: {e}")
        return False

def test_sic_firewall():
    """測試語義防火牆組件"""
    print("測試語義防火牆組件...")
    try:
        from validators.sic_fw import SIC_FW
        fw = SIC_FW()
        
        # 測試防火牆評估功能
        test_state = {
            "intent": "test intent",
            "requester": {"id": "test-user"},
            "metadata": {"request_id": "test-request"}
        }
        
        result = fw.evaluate(test_state)
        print(f"  ✓ 防火牆功能正常: {result.action}")
        
        return True
    except Exception as e:
        print(f"  ✗ 防火牆組件測試失敗: {e}")
        return False

def test_sit_handshake():
    """測試SIT握手組件"""
    print("測試SIT握手組件...")
    try:
        from validators.sit_handshake import SIT_Handshake
        handshake = SIT_Handshake(secret_key="test-key", entity_id="test-entity")
        
        # 測試SYN創建功能
        syn = handshake.create_syn(
            intent_scope="test scope",
            semantic_boundary={"type": "test"},
            constraints={"max_tokens": 100}
        )
        
        print(f"  ✓ 握手功能正常: {syn.requester_id}")
        
        return True
    except Exception as e:
        print(f"  ✗ 握手組件測試失敗: {e}")
        return False

def main():
    """主測試函數"""
    print("開始測試優化後的SIC-SIT協議組件...\n")
    
    tests = [
        test_semantic_routing,
        test_semantic_signature,
        test_sic_firewall,
        test_sit_handshake
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"測試完成: {passed}/{total} 個組件通過測試")
    
    if passed == total:
        print("✓ 所有組件測試通過！")
        return True
    else:
        print("✗ 部分組件測試失敗")
        return False

if __name__ == "__main__":
    main()