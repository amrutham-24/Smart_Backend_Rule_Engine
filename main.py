from fastapi import FastAPI
from pydantic import BaseModel
#from engine import evaluate_rules
#from gemini import generate_rule_from_text
#from firebase import save_rule, get_all_rules, save_trace

app = FastAPI()
class RuleRequest(BaseModel):
    text: str


class EventRequest(BaseModel):
    event: str
    data: dict

@app.post("/create-rule")
def create_rule(req: RuleRequest):

    rule = generate_rule_from_text(req.text)
    save_rule(rule)

    return {
        "message": "Rule created successfully",
        "rule": rule
    }


@app.post("/evaluate-event")
def evaluate_event(req: EventRequest):

    rules = get_all_rules()

    result = evaluate_rules(
        req.event,
        rules,
        req.data
    )

    save_trace({
        "event": req.event,
        "input": req.data,
        "result": result
    })

    return result