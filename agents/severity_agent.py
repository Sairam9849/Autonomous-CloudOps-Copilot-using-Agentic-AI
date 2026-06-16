def severity_agent(state):
    
    if state["incident"] == "Deployment Failed":
        state["severity"] = "High"

    elif state["incident"] == "CPU High":
        state["severity"] = "Medium"

    else:
        state["severity"] = "Low"

    return state