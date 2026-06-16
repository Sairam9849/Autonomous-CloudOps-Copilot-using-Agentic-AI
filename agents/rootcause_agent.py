def rootcause_agent(state):
    
    if state["incident"] == "Deployment Failed":
        state["root_cause"] = "Docker image missing"

    elif state["incident"] == "CPU High":
        state["root_cause"] = "High CPU utilization"

    else:
        state["root_cause"] = "No issues found"

    return state