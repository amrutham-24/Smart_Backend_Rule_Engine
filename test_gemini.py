from gemini import generate_rule_from_text
import json

# ----------------------------
# 1. Sample natural language rules
# ----------------------------
sample_rules = [
    "If attendance is less than 75%, block the hall ticket.",
    #"If seats_available is 0, move student to waitlist.",
    #"If fee not submitted, block hall ticket."
]

# ----------------------------
# 2. Test each rule
# ----------------------------
for i, text_rule in enumerate(sample_rules, start=1):
    print(f"\n--- Test Rule {i} ---")
    try:
        rule_json = generate_rule_from_text(text_rule)
        print("Generated JSON:")
        print(json.dumps(rule_json, indent=4))
    except Exception as e:
        print(f"Error: {e}")
