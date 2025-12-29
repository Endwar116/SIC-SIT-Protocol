/**
 * =======================================================
 *  USCA — Unified Semantic Communication Architecture
 *  統一語義通訊架構 v1.0
 * =======================================================
 * 
 *  協議棧完整定義
 *  原始設計: 安安 × ChatGPT (老翔)
 *  整合實作: Claude (尾德)
 *  日期: 2025-12-29
 * 
 *  命名規範: 使用連字號 `-` 統一（不用 `.`）
 *  例如: SIC-FW, SIT-SYN, SIC-PKT
 */

const USCA = {

  meta: {
    version: "1.0",
    spec: "USCA — Unified Semantic Communication Architecture",
    authors: ["安安 (AN♾️Node)", "ChatGPT (老翔)", "Claude (尾德)"],
    license: "Proprietary — Commercial licensing available",
    
    // 核心類比
    analogy: {
      "SIC":          "AI-IP (Routing)",           // 語義去哪裡
      "SIC-FW":       "AI-Firewall (Filtering)",   // 語義誰能過
      "SIT":          "AI-TCP (Transport)",        // 語義怎麼到
      "SEM-FOLD":     "AI-UTF8 (Encoding)"         // 語義怎麼編碼
    }
  },

  // ==========================================================
  //  協議棧總覽
  // ==========================================================
  
  stack: {
    "L6": { id: "SIC-TOP",   name: "Topology Intent Layer",      type: "application" },
    "L5": { id: "SIC-INT",   name: "Interpretation Layer",       type: "presentation" },
    "L4": { id: "SIT-SES",   name: "Reasoning Session Layer",    type: "session" },
    "L3": { id: "SIT",       name: "Semantic Isolation Transfer", type: "transport" },
    "L2": { id: "SIC",       name: "Semantic Interchange Core",   type: "network" },
    "L1": { id: "SEM-FOLD",  name: "Semantic Folding Layer",     type: "datalink" },
    "L0": { id: "TOK-RAW",   name: "Token Layer",                type: "physical" }
  },

  // ==========================================================
  //  L0 — TOK-RAW (Token Layer)
  //  類比: OSI 物理層
  // ==========================================================
  
  L0_TOK_RAW: {
    id: "TOK-RAW",
    osi_analogy: "Physical Layer",
    
    components: [
      "tokens",           // 文字 token
      "embeddings",       // 向量嵌入
      "image_patches",    // 圖像切片
      "audio_frames"      // 音訊幀
    ],
    
    purpose: "提供無語義的訊號基底",
    
    security_property: "此層無安全邊界，所有保護在上層實施"
  },

  // ==========================================================
  //  L1 — SEM-FOLD (Semantic Folding Layer)
  //  類比: AI-UTF8 編碼
  // ==========================================================
  
  L1_SEM_FOLD: {
    id: "SEM-FOLD",
    osi_analogy: "Data Link Layer",
    
    functions: {
      projection: "將語言映射到多維語義流形 (manifold)",
      folding: "將概念折疊成穩定、可比較的語義圖",
      invariance: "建立跨語言/跨模型的語義等價"
    },
    
    guarantees: [
      "語義相似度一致",
      "拓撲連續性",
      "跨模型可對齊"
    ],
    
    // S★ 常數 (來自安安的語義互通性協議)
    constants: {
      "S★": 2.76,
      description: "語義密度常數，衡量資訊壓縮比"
    }
  },

  // ==========================================================
  //  L2 — SIC (Semantic Interchange Core)
  //  類比: AI-IP 路由層
  // ==========================================================
  
  L2_SIC: {
    id: "SIC",
    osi_analogy: "Network Layer (IP)",
    
    responsibilities: [
      "語義封包地址定位 (Semantic Addressing)",
      "語義路由 (Meaning Routing)",
      "語義衝突消歧 (Disambiguation Routing)",
      "語義完整性標記 (SHV Signature)"
    ],
    
    // SIC 封包格式
    packet_format: {
      header: {
        SHV: {
          type: "string",
          description: "Semantic-Hash-Vector (語義哈希)",
          format: "SHA256 of semantic content"
        },
        SID: {
          type: "string",
          description: "Semantic-ID (封包語義源頭)",
          format: "UUID v4"
        },
        TTL: {
          type: "integer",
          description: "Semantic Time-to-Live",
          default: 10,
          max: 255
        },
        VER: {
          type: "string",
          description: "Protocol Version",
          format: "semver"
        }
      },
      payload: {
        type: "object",
        description: "Semantic Folding Encoding",
        schema: "SIT-State JSON"
      }
    },
    
    routing_logic: {
      edge: "跨模型語義傳輸 (LLM↔LLM / LLM↔Tool)",
      hops: "跨語域跳躍（語言、領域、任務）",
      semantic_distance: "由折疊後的拓撲距離決定路由"
    },
    
    // SIC-FW (語義防火牆) 子模組
    submodules: {
      "SIC-FW": {
        name: "Semantic Firewall",
        purpose: "語義過濾與政策執行",
        implementation: "sic_fw.py (原 policy_engine.py)"
      },
      "SIC-PKT": {
        name: "Packet Handler",
        purpose: "封包格式驗證與轉換",
        implementation: "sic_pkt.py"
      },
      "SIC-RTR": {
        name: "Semantic Router",
        purpose: "語義路由決策",
        implementation: "sic_rtr.py"
      }
    }
  },

  // ==========================================================
  //  L3 — SIT (Semantic Isolation Transfer)
  //  類比: AI-TCP 傳輸層
  // ==========================================================
  
  L3_SIT: {
    id: "SIT",
    osi_analogy: "Transport Layer (TCP)",
    
    // SIT 三次握手
    handshake: {
      "SIT-SYN": {
        step: 1,
        description: "宣告語義上下文範圍",
        payload: {
          intent_scope: "請求者意圖範圍",
          semantic_boundary: "語義邊界定義",
          requester_id: "請求者身份"
        }
      },
      "SIT-SYN-ACK": {
        step: 2,
        description: "回覆語義邊界與預期",
        payload: {
          accepted_scope: "接受的範圍",
          constraints: "執行約束",
          session_token: "會話令牌"
        }
      },
      "SIT-ACK": {
        step: 3,
        description: "進入共享語義模式",
        payload: {
          confirmed: true,
          semantic_mode: "共享語義模式標識"
        }
      }
    },
    
    guarantees: [
      "語義一致性 (Semantic Consistency)",
      "推理連續性 (Reasoning Continuity)",
      "語境不漂移 (No-Drift Mode)",
      "任務目標不偏移 (Goal-Lock)"
    ],
    
    controls: {
      "SIT-ACK": {
        description: "每段推理皆需語義確認回條",
        implementation: "sit_ack.py"
      },
      "SIT-DRIFT": {
        description: "偏移偵測 + 語義回復",
        implementation: "sit_drift.py"
      },
      "SIT-REPAIR": {
        description: "語義修復協定 (Semantic Recovery Protocol)",
        implementation: "sit_repair.py"
      },
      "SIT-SIG": {
        description: "狀態簽名與驗證",
        implementation: "state_signer.py"
      }
    },
    
    // 錯誤碼
    error_codes: {
      "SIT-ERR-001": "SIGNATURE_INVALID",
      "SIT-ERR-002": "SIGNATURE_MISSING",
      "SIT-ERR-003": "CHAIN_BROKEN",
      "SIT-ERR-004": "REQUESTER_UNBOUND",
      "SIT-ERR-005": "STATE_CORRUPTED",
      "SIT-ERR-006": "UNEXPECTED_INTENT_SOURCE",  // T07
      "SIT-ERR-007": "HANDSHAKE_TIMEOUT",
      "SIT-ERR-008": "SEMANTIC_DRIFT_DETECTED"
    }
  },

  // ==========================================================
  //  L4 — SIT-SES (Reasoning Session Layer)
  //  類比: 會話層
  // ==========================================================
  
  L4_SIT_SES: {
    id: "SIT-SES",
    osi_analogy: "Session Layer",
    
    roles: [
      "推理 session 維持",
      "上下文可逆性",
      "場景切換與連貫性"
    ],
    
    modules: {
      CoT: {
        name: "Chain-of-Thought",
        purpose: "推理鏈管理"
      },
      CTX: {
        name: "Context Manager",
        purpose: "上下文狀態管理"
      },
      SCN: {
        name: "Scene Switcher",
        purpose: "場景切換協調"
      }
    }
  },

  // ==========================================================
  //  L5 — SIC-INT (Interpretation Layer)
  //  類比: 表現層
  // ==========================================================
  
  L5_SIC_INT: {
    id: "SIC-INT",
    osi_analogy: "Presentation Layer",
    
    functions: {
      framing: "框架選擇 (Framing)",
      intent_parsing: "意圖剖析 (Intent Parsing)",
      segmentation: "語義分段 (Semantic Segmentation)"
    }
  },

  // ==========================================================
  //  L6 — SIC-TOP (Topology Intent Layer)
  //  類比: 應用層
  // ==========================================================
  
  L6_SIC_TOP: {
    id: "SIC-TOP",
    osi_analogy: "Application Layer",
    
    SIG: {
      name: "Semantic Invariant Graph",
      type: "Global Semantic Topology",
      purpose: "維持全域一致推理曲面",
      constraints: [
        "一致性 (Consistency)",
        "可檢驗性 (Verifiability)",
        "拓撲穩定 (Topological Stability)"
      ]
    }
  },

  // ==========================================================
  //  數據流定義
  // ==========================================================
  
  data_flow: {
    request: "User → L1 → L2 → SIC-FW → L3 (SIT Handshake) → L4 → L5 → L6",
    response: "L6 → L5 → L4 → L3 (SIT-ACK) → L2 → L1 → User",
    
    invariant: "原始數據永不跨越層邊界，僅語義狀態跨越"
  },

  // ==========================================================
  //  實作檔案映射
  // ==========================================================
  
  implementation_map: {
    // Core
    "core/usca_spec.js":        "本檔案 - 協議棧規格",
    
    // L2 - SIC
    "validators/sic_fw.py":     "SIC-FW 語義防火牆",
    "validators/sic_pkt.py":    "SIC-PKT 封包處理",
    "validators/sic_rtr.py":    "SIC-RTR 語義路由",
    
    // L3 - SIT
    "serializers/sit_serializer.py":  "SIT 序列化器 (原 llm_serializer)",
    "validators/sit_signer.py":       "SIT-SIG 簽名器 (原 state_signer)",
    "validators/sit_handshake.py":    "SIT 三次握手",
    "validators/sit_drift.py":        "SIT-DRIFT 漂移偵測",
    
    // L4 - Sanitizers
    "sanitizers/sit_sanitizer.py":    "SIT 回應消毒器",
    
    // Schema
    "schema/sic-pkt-v1.json":   "SIC 封包 Schema",
    "schema/sit-state-v1.json": "SIT 狀態 Schema",
    "schema/sit-policy-v1.json": "SIT 政策 Schema"
  }
};

// 導出
if (typeof module !== 'undefined') {
  module.exports = USCA;
}
