from kubernetes import client, config

def kubernetes_agent(state):

    try:
        config.load_kube_config()

        v1 = client.CoreV1Api()
        pods = v1.list_pod_for_all_namespaces()

        pod_names = []

        for pod in pods.items:
            pod_names.append(pod.metadata.name)

        state["pods"] = pod_names
        state["k8s_status"] = "Healthy"

    except Exception as e:
        state["pods"] = []
        state["k8s_status"] = f"Unavailable: {str(e)}"

    return state