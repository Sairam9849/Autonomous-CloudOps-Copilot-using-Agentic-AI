def planner_agent(incident):

    return {
        "incident": incident,
        "plan": [
            "Check Jenkins",
            "Check Kubernetes",
            "Check AWS"
        ]
    }