from engine import evaluate_rules # type: ignore
import json

rules = json.load(open("rules.json"))

event = "attendance_updated"

data = {
    "attendance": 68
}

result = evaluate_rules(event, rules, data)

print(result)
