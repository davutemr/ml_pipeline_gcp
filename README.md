## Branching Strategy

This project uses two main branches:

- **main:**  
  Contains production-ready code. Only tested and verified changes are merged into this branch. Pushes to this branch trigger automatic deployment to the GCP virtual machine.

- **dev:**  
  Contains ongoing development work. All new features and updates are first pushed to this branch for testing and verification. No deployment is performed from this branch.

## Workflow

1. Development and testing are performed in the **dev** branch.  
2. After successful testing, changes are merged from **dev** into **main**.  
3. Changes merged into **main** trigger deployment of the latest code and model to the GCP virtual machine.

