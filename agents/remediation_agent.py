def remediation_agent(state):
    
    if state["root_cause"] == "Docker image missing":
        state["fix"] = "Push image and restart deployment"

    elif state["root_cause"] == "High CPU utilization":
        state["fix"] = "Scale EC2 instances"

    else:
        state["fix"] = "Manual investigation required"

    return state