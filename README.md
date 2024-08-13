# Neo4j Kubernetes Resource Relationships

This project visualizes Kubernetes resource relationships using Neo4j. The data represents the connections between Deployments and Pods in a Kubernetes environment.

## Project Structure

- `relationships.csv`: A CSV file containing the relationship data between Deployments and Pods.
- `README.md`: This documentation file.
- `.gitignore`: Files and directories to ignore in the repository.
- `LICENSE`: The project's license file.

## Prerequisites

- [Neo4j Desktop](https://neo4j.com/download/) or Neo4j Community Edition.
- Python (for any additional scripts you may use).

## Setup Instructions

### 1. Install Neo4j

Ensure you have Neo4j installed on your system. You can download and install it from [here](https://neo4j.com/download/).

### 2. Prepare the Data

The `relationships.csv` file contains the deployment and pod relationships:

```csv
deployment,pod
argocd-redis,argocd-redis-c6b47cdbd-f6lbp
nginx,nginx-bf5d5cf98-rkzv2
