import sys
import os
from datetime import datetime
import pandas as pd
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.planner_agent import planner_agent
from agents.aws_agent import aws_agent
from agents.kubernetes_agent import kubernetes_agent
from agents.jenkins_agent import jenkins_agent
from agents.severity_agent import severity_agent
from agents.rootcause_agent import rootcause_agent
from agents.remediation_agent import remediation_agent

st.set_page_config(
    page_title="Autonomous CloudOps Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Autonomous CloudOps Copilot")
st.markdown("AI-Powered Incident Analysis Dashboard")

incident = st.text_input("Enter Incident")

if st.button("Analyze"):

    if incident.strip() == "":
        st.warning("Please enter an incident.")
    else:

        try:
            # Run agents
            state = planner_agent(incident)

            state = aws_agent(state)
            state = kubernetes_agent(state)
            state = jenkins_agent(state)

            state = severity_agent(state)
            state = rootcause_agent(state)
            state = remediation_agent(state)

            st.success("Analysis Complete ✅")

            # Metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("AWS", state["aws_status"])

            with col2:
                st.metric("Kubernetes", state["k8s_status"])

            with col3:
                st.metric("Severity", state["severity"])

            st.subheader("📋 Incident Report")

            st.write("**Incident:**", state["incident"])
            st.write("**Plan:**", state["plan"])
            st.write("**Jenkins Status:**", state["jenkins_status"])

            st.error(f"**Root Cause:** {state['root_cause']}")
            st.success(f"**Recommended Fix:** {state['fix']}")

            st.write("🕒 Analyzed at:", datetime.now())

            # Pods Table
            if "pods" in state:
                st.subheader("☸ Kubernetes Pods")

                df = pd.DataFrame({
                    "Pods": state["pods"]
                })

                st.table(df)

            # Download Report
            report = f"""
Incident: {state['incident']}
Plan: {state['plan']}
AWS Status: {state['aws_status']}
Kubernetes Status: {state['k8s_status']}
Jenkins Status: {state['jenkins_status']}
Severity: {state['severity']}
Root Cause: {state['root_cause']}
Recommended Fix: {state['fix']}
"""

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="incident_report.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")