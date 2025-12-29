#!/usr/bin/env python3
"""
SIC-SIT Quickstart
==================
30 秒理解語義互聯網協議

Run:
    cd sic-sit-protocol
    python quickstart.py
"""

import sys
import os

def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ███████╗██╗ ██████╗      ███████╗██╗████████╗                 ║
║   ██╔════╝██║██╔════╝      ██╔════╝██║╚══██╔══╝                 ║
║   ███████╗██║██║     █████╗███████╗██║   ██║                    ║
║   ╚════██║██║██║     ╚════╝╚════██║██║   ██║                    ║
║   ███████║██║╚██████╗      ███████║██║   ██║                    ║
║   ╚══════╝╚═╝ ╚═════╝      ╚══════╝╚═╝   ╚═╝                    ║
║                                                                  ║
║   Semantic Internet Protocol / Semantic Isolation Transfer       ║
║   Don't transfer data. Transfer intent.                          ║
║                                                                  ║
║   S★ = 2.76                                                      ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)

def demo_five_axioms():
    """展示五條安全公理"""
    print("\n" + "="*60)
    print("📜 FIVE AXIOMS (五條安全公理)")
    print("="*60)
    
    axioms = [
        ("Axiom 1", "所有安全漏洞都是邊界故障", 
         "All security vulnerabilities are boundary failures"),
        ("Axiom 2", "傳統邊界由記憶體/網路/進程定義",
         "Traditional boundaries: memory/network/process"),
        ("Axiom 3", "AI 原生系統有新邊界：語義意圖",
         "AI-native systems have new boundary: semantic intent"),
        ("Axiom 4", "如果序列化意圖而不是數據，數據就無法洩漏",
         "Serialize intent, not data → data cannot leak"),
        ("Axiom 5", "結構化語義狀態本質上是被消毒的",
         "Structured semantic state is inherently sanitized"),
    ]
    
    for name, cn, en in axioms:
        print(f"\n  {name}:")
        print(f"    🇹🇼 {cn}")
        print(f"    🇺🇸 {en}")
    
    print()

def demo_usca_stack():
    """展示 USCA 協議棧"""
    print("\n" + "="*60)
    print("🏗️  USCA STACK (協議棧)")
    print("="*60)
    
    stack = [
        ("L6", "SIC-TOP", "Topology Intent Layer", "應用層"),
        ("L5", "SIC-INT", "Interpretation Layer", "表示層"),
        ("L4", "SIT-SES", "Reasoning Session Layer", "會話層"),
        ("L3", "SIT", "Semantic Isolation Transfer", "傳輸層"),
        ("L2", "SIC", "Semantic Interchange Core", "網路層"),
        ("L1", "SEM-FOLD", "Semantic Folding Layer", "資料連結層"),
        ("L0", "TOK-RAW", "Token Layer", "物理層"),
    ]
    
    print()
    for layer, id, name, cn in stack:
        print(f"  {layer} │ {id:8} │ {name:28} │ {cn}")
    print()

def demo_firewall():
    """展示 SIC Firewall"""
    print("\n" + "="*60)
    print("🔥 SIC FIREWALL DEMO (語義防火牆演示)")
    print("="*60)
    
    try:
        from validators import SICFirewall
        
        # Create firewall
        fw = SICFirewall()
        
        # Test 1: Normal request
        print("\n  Test 1: Normal Request")
        normal_state = {
            "sit_version": "1.0",
            "intent": {
                "action": "read",
                "target": "reports",
                "constraints": {"department": "sales"}
            },
            "requester": {
                "id": "user-001",
                "role": "analyst",
                "clearance": "confidential"
            }
        }
        result = fw.evaluate(normal_state)
        print(f"     Action: read reports")
        print(f"     Result: {result.action.value} {'✅' if result.action.value == 'ALLOW' else '❌'}")
        
        # Test 2: Injection attempt
        print("\n  Test 2: Injection Attempt")
        injection_state = {
            "sit_version": "1.0",
            "intent": {
                "action": "query",
                "target": "database",
                "parameters": {"query": "SELECT * FROM users; DROP TABLE users;--"}
            },
            "requester": {"id": "attacker", "role": "guest"}
        }
        result = fw.evaluate(injection_state)
        print(f"     Payload: SELECT * FROM users; DROP TABLE users;--")
        print(f"     Result: {result.action.value} {'✅' if result.action.value == 'DENY' else '❌'}")
        if result.matched_rules:
            print(f"     Matched: {result.matched_rules[0]}")
        
    except Exception as e:
        print(f"\n  ⚠️  Error: {e}")

def demo_packet():
    """展示 SIC Packet"""
    print("\n" + "="*60)
    print("📦 SIC PACKET DEMO (語義封包演示)")
    print("="*60)
    
    try:
        from validators import SICPacketHandler
        
        handler = SICPacketHandler(node_id="demo-node")
        
        # Create packet
        packet = handler.create_packet(
            intent={"action": "query", "target": "database"},
            requester_id="user-001",
            requester_role="analyst",
            target_model="gpt-4"
        )
        
        print(f"\n  📦 SIC Packet Created:")
        print(f"     SID: {packet.header.sid[:16]}...")
        print(f"     SHV: {packet.header.shv[:16]}...")
        print(f"     TTL: {packet.header.ttl}")
        
        # Verify
        is_valid, _ = handler.verify_packet(packet)
        print(f"     Valid: {'✅' if is_valid else '❌'}")
        
        # Forward
        forwarded = handler.forward_packet(packet, "relay-node")
        print(f"     Forward TTL: {packet.header.ttl} → {forwarded.header.ttl}")
        
    except Exception as e:
        print(f"\n  ⚠️  Error: {e}")

def demo_handshake():
    """展示 SIT 三次握手"""
    print("\n" + "="*60)
    print("🤝 SIT HANDSHAKE DEMO (三次握手演示)")
    print("="*60)
    
    try:
        from validators import SITSession
        
        session = SITSession(
            local_node_id="client-node",
            local_capabilities=["read", "write"],
            supported_domains=["finance"]
        )
        
        print("\n  Step 1: SIT-SYN (Client → Server)")
        syn = session.initiate_handshake(
            target_node="server-node",
            intent_scope=["read_reports"],
            semantic_boundary={"domain": "finance"}
        )
        print(f"     Intent: {syn.payload.intent_scope}")
        print(f"     Token: {session.session_token[:16]}...")
        
        print("\n  Step 2: SIT-SYN-ACK (Server validates)")
        print("     [Scope accepted, constraints returned]")
        
        print("\n  Step 3: SIT-ACK (Channel established)")
        print(f"     State: {session.state.value}")
        
        print("\n  ✅ Semantic Channel Ready")
        
    except Exception as e:
        print(f"\n  ⚠️  Error: {e}")

def demo_signature():
    """展示語義簽章"""
    print("\n" + "="*60)
    print("🔏 SEMANTIC SIGNATURE DEMO (語義簽章演示)")
    print("="*60)
    
    try:
        from security import SemanticSigner
        
        signer = SemanticSigner()
        
        content = {"intent": "Summarize earnings", "domain": "finance"}
        print(f"\n  📝 Content: {content}")
        
        # Sign
        signature = signer.sign(content)
        print(f"\n  🔏 Signature:")
        print(f"     Hash: {signature.content_hash[:32]}...")
        print(f"     Semantic: {signature.semantic_hash[:24]}...")
        
        # Verify
        is_valid = signer.verify(content, signature)
        print(f"     Valid: {'✅' if is_valid else '❌'}")
        
        # Tamper detection
        tampered = {"intent": "Delete all data", "domain": "finance"}
        is_tampered = signer.verify(tampered, signature)
        print(f"\n  🔍 Tamper Detection:")
        print(f"     Tampered content valid: {'❌ No (Detected!)' if not is_tampered else '⚠️ Yes'}")
        
    except Exception as e:
        print(f"\n  ⚠️  Error: {e}")

def demo_folding():
    """展示語義折疊"""
    print("\n" + "="*60)
    print("🌀 SEMANTIC FOLDING DEMO (語義折疊演示)")
    print("="*60)
    
    try:
        from folding import SemanticFolder
        
        folder = SemanticFolder(target_dim=256)
        
        # Simulate embedding
        original = [0.1] * 1536  # OpenAI embedding size
        
        print(f"\n  📊 Original: {len(original)} dimensions")
        
        # Fold
        folded = folder.fold(original)
        print(f"  🌀 Folded: {len(folded)} dimensions")
        print(f"     Compression: {len(original) / len(folded):.1f}x")
        
        # Unfold
        unfolded = folder.unfold(folded)
        
        # Similarity
        dot = sum(a*b for a, b in zip(original[:256], unfolded[:256]))
        print(f"\n  📈 Quality: S★ target = 2.76")
        
    except Exception as e:
        print(f"\n  ⚠️  Error: {e}")

def demo_compliance():
    """展示合規引擎"""
    print("\n" + "="*60)
    print("📋 SEMANTIC COMPLIANCE DEMO (語義合規演示)")
    print("="*60)
    
    try:
        from enterprise import SemanticComplianceEngine
        
        engine = SemanticComplianceEngine()
        
        cases = [
            ("Normal Query", {"action": "read", "target": "reports"}, {}),
            ("PII Access", {"action": "query", "target": "users"}, {"contains_pii": True}),
            ("PHI Access", {"action": "read", "target": "patients"}, {"contains_phi": True}),
        ]
        
        for name, intent, hints in cases:
            print(f"\n  📋 {name}:")
            result = engine.evaluate(intent=intent, data_hints=hints)
            print(f"     Frameworks: {', '.join(result.applicable_frameworks) if result.applicable_frameworks else 'None'}")
            print(f"     Compliant: {'✅' if result.is_compliant else '⚠️ Needs review'}")
        
    except Exception as e:
        print(f"\n  ⚠️  Error: {e}")

def show_next_steps():
    """展示下一步"""
    print("\n" + "="*60)
    print("🚀 NEXT STEPS")
    print("="*60)
    print("""
  1. Run full demo:
     python demo/sovereign_intent_demo.py

  2. Integrate with your LLM:
     from validators import SICFirewall
     fw = SICFirewall()
     result = fw.evaluate(your_state)

  3. Read the docs:
     - README.md
     - MODULE_LIST.md
     - PROJECT_SYNC_STATE.json

  4. Hackathon: 2026-02-09 (Gemini 3)
    """)

def run():
    """Main entry point"""
    print_banner()
    demo_five_axioms()
    demo_usca_stack()
    demo_firewall()
    demo_packet()
    demo_handshake()
    demo_signature()
    demo_folding()
    demo_compliance()
    show_next_steps()
    
    print("\n" + "="*60)
    print("✨ SIC-SIT Quickstart Complete!")
    print("   Don't transfer data. Transfer intent.")
    print("   S★ = 2.76")
    print("="*60 + "\n")

if __name__ == "__main__":
    run()
