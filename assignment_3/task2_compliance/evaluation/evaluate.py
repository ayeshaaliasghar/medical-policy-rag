import pandas as pd
from agent_workflow import evaluate_rule, rules

results = []

for r in rules:
    out = evaluate_rule(r)
    results.append({
        "rule_id": r["id"],
        "rule_title": r["title"],
        "evaluation": out
    })

df = pd.DataFrame(results)
df.to_csv("evaluation/compliance_results.csv", index=False)

print("Saved evaluation to evaluation/compliance_results.csv")
