import json
from kubernetes import client, config
from openpyxl import Workbook

# Load kubeconfig file
config.load_kube_config()

# Create Kubernetes API client
api = client.AppsV1Api()
core_api = client.CoreV1Api()

# Read namespaces from config file
with open("config.json") as f:
    config_data = json.load(f)
    namespaces = config_data.get("namespaces")

# Create workbook
workbook = Workbook()

# Loop through each namespace
for ns_name in namespaces:
    # Create worksheet for this namespace
    worksheet = workbook.create_sheet(ns_name)

    # Write header to worksheet
    worksheet.append(["Namespace", "Deployment", "Image", "Replicas", "Pod", "CPU Limits", "CPU Requests", "Memory Limits", "Memory Requests", "Start Time"])

    # Get list of all deployments in the namespace
    deployment_list = api.list_namespaced_deployment(ns_name).items

    # Loop through each deployment
    for deploy in deployment_list:
        # Get deployment details
        image = deploy.spec.template.spec.containers[0].image
        cpu_limits = deploy.spec.template.spec.containers[0].resources.limits.get("cpu")
        cpu_requests = deploy.spec.template.spec.containers[0].resources.requests.get("cpu")
        memory_limits = deploy.spec.template.spec.containers[0].resources.limits.get("memory")
        memory_requests = deploy.spec.template.spec.containers[0].resources.requests.get("memory")
        replicas = deploy.spec.replicas

        # Get list of all pods for this deployment
        pod_list = core_api.list_namespaced_pod(namespace=ns_name, label_selector="app=" + deploy.metadata.name).items

        # Loop through each pod
        for pod in pod_list:
            # Get pod details
            pod_name = pod.metadata.name
            start_time = pod.status.start_time

            # Write deployment and pod details to worksheet
            worksheet.append([ns_name, deploy.metadata.name, image, replicas, pod_name, cpu_limits, cpu_requests, memory_limits, memory_requests, start_time])

# Remove default sheet
workbook.remove(workbook["Sheet"])

# Save workbook to file
workbook.save("deployment_report.xlsx")
