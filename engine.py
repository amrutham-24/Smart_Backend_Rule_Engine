def evaluate_condition(condition, data):
    field = condition["field"]
    operator = condition["operator"]
    expected = condition["value"]
    actual = data.get(field)

    if operator == "<":
        return actual < expected
    if operator == ">":
        return actual > expected
    if operator == "==":
        return actual == expected
    if operator == "!=":
        return actual != expected
    if operator == "<=":
        return actual <= expected
    if operator == ">=":
        return actual >= expected

    return False

def evaluate_rule(rule, data):
    trace = []

    for cond in rule["conditions"]:
        actual = data.get(cond["field"])

        result = evaluate_condition(cond, data)

        trace.append({
            "field": cond["field"],
            "operator": cond["operator"],
            "expected": cond["value"],
            "actual": actual,
            "result": result
        })

        if not result:
            return {
                "rule_id": rule["rule_id"],
                "triggered": False,
                "trace": trace
            }

    return {
        "rule_id": rule["rule_id"],
        "triggered": True,
        "action": rule["action"],
        "trace": trace
    }

def evaluate_rules(event, rules, data):
    results = []

    for rule in rules:
        if rule["event"] != event:
            continue

        result = evaluate_rule(rule, data)
        if result["triggered"]:
            results.append(result)

    return results
