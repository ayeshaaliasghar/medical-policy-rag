import gradio as gr
from agent_workflow import evaluate_rule, rules

def run(rule_id):
    rule = next((r for r in rules if r["id"] == rule_id), None)
    if not rule:
        return "Rule not found"
    return evaluate_rule(rule)

ui = gr.Interface(
    fn=run,
    inputs=gr.Dropdown([r["id"] for r in rules], label="Select Rule"),
    outputs="text",
    title="Policy Compliance Checker (RAG + FLAN-T5)"
)

ui.launch()
