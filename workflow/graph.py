from langgraph.graph import StateGraph, END

def planner(state):
    state["plan"] = "Investigation Started"
    return state

def aws(state):
    state["aws"] = "EC2 Healthy"
    return state

def kubernetes(state):
    state["k8s"] = "ImagePullBackOff"
    return state

def rootcause(state):
    if state["k8s"] == "ImagePullBackOff":
        state["root_cause"] = "Docker image missing"

    return state

def remediation(state):
    state["fix"] = "Push image and restart deployment"
    return state


graph = StateGraph(dict)

graph.add_node("planner", planner)
graph.add_node("aws", aws)
graph.add_node("kubernetes", kubernetes)
graph.add_node("rootcause", rootcause)
graph.add_node("remediation", remediation)

graph.set_entry_point("planner")

graph.add_edge("planner", "aws")
graph.add_edge("aws", "kubernetes")
graph.add_edge("kubernetes", "rootcause")
graph.add_edge("rootcause", "remediation")
graph.add_edge("remediation", END)

app = graph.compile()

result = app.invoke({
    "incident": "Deployment Failed"
})

print(result)