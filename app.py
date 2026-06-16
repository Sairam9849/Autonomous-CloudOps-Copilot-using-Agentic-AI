from agents.planner_agent import planner_agent
from agents.aws_agent import aws_agent
from agents.kubernetes_agent import kubernetes_agent
from agents.jenkins_agent import jenkins_agent
from agents.rootcause_agent import rootcause_agent
from agents.remediation_agent import remediation_agent
from agents.severity_agent import severity_agent

incident = input("Enter Incident: ")

state = planner_agent(incident)

state = aws_agent(state)
state = kubernetes_agent(state)
state = jenkins_agent(state)

state = rootcause_agent(state)
state = remediation_agent(state)
state = severity_agent(state)

print("\n========== INCIDENT REPORT ==========")
print("Incident:", state["incident"])
print("Plan:", state["plan"])
print("AWS Status:", state["aws_status"])
print("Kubernetes Status:", state["k8s_status"])
print("Pods:", state["pods"])
print("Jenkins Status:", state["jenkins_status"])
print("Severity:", state["severity"])
print("Root Cause:", state["root_cause"])
print("Recommended Fix:", state["fix"])
print("====================================")