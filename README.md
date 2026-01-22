┌──────────────────────────────┐
│            UI Layer           │
│  Web App / Postman / Frontend │
│                                │
│ • User enters natural language │
│   or structured JSON           │
└───────────────┬──────────────┘
                │
                │ 1. Request
                ▼
┌──────────────────────────────┐
│           FastAPI Backend     │
│                                │
│  /create-rule                  │
│  /evaluate-event               │
│                                │
│  • Request validation          │
│  • Routing logic               │
└───────────────┬──────────────┘
                │
        ┌───────┴────────┐
        │                 │
        ▼                 ▼
┌──────────────────┐  ┌────────────────────┐
│     Gemini API     │  │   Firebase          │
│                    │  │                     │
│ • Converts natural │  │ • Stores rules      │
│   language → JSON  │  │ • Stores events     │
│ • Suggests fields  │  │ • Stores traces     │
│                    │  │ • Stores results    │
└─────────┬──────────┘  └─────────┬──────────┘
          │                       │
          │ rule JSON             │ rules
          ▼                       ▼
┌────────────────────────────────────────┐
│            Rule Engine Core             │
│                (engine.py)              │
│                                        │
│  • evaluateCondition()                  │
│  • evaluateRule()                       │
│  • evaluateRules()                      │
│                                        │
│  Domain-agnostic evaluation             │
└───────────────┬────────────────────────┘
                │
                │ execution result + trace
                ▼
┌────────────────────────────────────────┐
│             Action Layer                 │
│                                        │
│  • block_account                        │
│  • move_to_waitlist                    │
│  • restrict_exam                       │
│  • block_hall_ticket                   │
│                                        │
│ (mock / simulation for demo)            │
└───────────────┬────────────────────────┘
                │
                ▼
┌────────────────────────────────────────┐
│              Firebase Logs               │
│                                        │
│  • execution_results                    │
│  • rule_traces                          │
│  • audit_history                        │
└────────────────────────────────────────┘
