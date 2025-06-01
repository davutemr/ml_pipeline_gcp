## Branching Strategy

This project uses two main branches:

- **main:**  
  Contains production-ready code. Only tested and verified changes are merged into this branch. Pushes to this branch trigger automatic deployment to the GCP virtual machine.

- **dev:**  
  Used for ongoing development. All feature additions, bug fixes, and updates are first pushed to this branch.
CI workflows run automated tests and training here, but no deployment is performed from dev.

## Workflow

1. Code is developed and tested on the **dev** branch. 
2. GitHub Actions runs the CI pipeline (ci.yml) to ensure everything works (training, testing, etc.).
3. Once verified, changes are merged from dev into main.
4. The main branch triggers the deployment pipeline (deploy.yml) to:
	- SSH into the GCP VM
	- Pull the latest code
	- Restart the Flask app to serve the updated model.
