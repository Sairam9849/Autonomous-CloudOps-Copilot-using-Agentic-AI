from llm import analyze_logs

logs = """
Pod status: ImagePullBackOff
Failed to pull image from registry
"""

result = analyze_logs(logs)

print(result)