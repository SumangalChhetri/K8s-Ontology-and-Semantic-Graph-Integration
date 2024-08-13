from kubernetes import client, config
import yaml

# Load Kubernetes config
config.load_kube_config()

# API clients
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

# Extract relationships
def extract_relationships():
    relationships = []

    # List Deployments
    deployments = apps_v1.list_deployment_for_all_namespaces()
    for deployment in deployments.items:
        namespace = deployment.metadata.namespace
        name = deployment.metadata.name

        # Find Pods belonging to the Deployment
        pods = v1.list_namespaced_pod(namespace, label_selector=f"app={name}")
        for pod in pods.items:
            relationships.append({
                'type': 'Deployment-Pod',
                'deployment': name,
                'pod': pod.metadata.name,
                'namespace': namespace
            })

    # Save relationships to YAML
    with open("relationships.yaml", "w") as f:
        yaml.dump(relationships, f)

extract_relationships()
