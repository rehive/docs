Rehive Docs
===========
Quickstart:
----------
### Preview Docs:  
Run the follwing command:  
> docker compose up
  
As described in the docker-compose file, middleman will run on [127.0.0.1:4567](http://127.0.0.1:4567).

### Build and release:
Commit all changes and then run:  
> inv release {config} {bump}
  
`{config}` is the name of the deployment config YAML file in the server directory.  
E.g. `staging` or `production.`  
  
`{bump}`is the type of semantic versioning increment to be used for this release.  
Options are:  `prerelease`, `patch`, `minor` or `major.`  
 
### Deployment:
To update the live deployment on kubernetes, run:
> inv deploy {config} {version_tag}  

where `{config}` is the value used for the release command above and `{version_tag}` is the version tag output by the release command.

Once-off setup:
--------------
1. Create a Kubernetes Cluster, Install GCloud SDK, PIP install invoke
2. Athenticate gcloud:  
	`gcloud auth login`  
	`gcloud config set project zapgo-1273`  
3. Connect to kubernetes cluster:  
	`gcloud container clusters get-credentials hosting-cluster --zone us-west1-a --project zapgo-1273`  
4. Letsencrypt SSL setup:  
	`kubectl apply -f server/kubernetes/lego/00-namespace.yaml && kubectl apply -f server/kubernetes/lego/configmap.yaml && kubectl apply -f server/kubernetes/lego/deployment.yaml`  
5. Webserver setup:
	- Create deploment configurations from template (if not already created):
	  `inv templater staging.yaml`  
	  `inv templater production.yaml` 
   - Staging:
   	  `kubectl apply -f server/kubernetes/docs-server-staging/all-in-one.yaml`  
   	- Production:
     `kubectl apply -f server/kubernetes/docs-server/all-in-one.yaml`. 
6. Check the external IP address and setup DNS:  
    `kubectl get ingress --namespace docs-server docs-server`  
