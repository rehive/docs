Rehive Docs
===========
Documentation:
----------
1. Build the middleman container:  
	`docker build -t docs_app .`  
2. Build HTML:  
	`docker run --rm -v $PWD/source:/usr/src/app/source -v $PWD/build:/usr/src/app/build -w /usr/src/app docs_app bundle exec middleman build --clean` 
- Preview Docs:  
	`docker-compose up`  
	
Deployment:
-----------
### Push to container registry:
1. Build the docker image to deploy:  
   `docker build -f server/Dockerfile -t docs-server .`  
2. Push to Container Registry:  
   `docker tag docs-server gcr.io/zapgo-1273/docs-server:v`  
   `gcloud docker -- push gcr.io/zapgo-1273/docs-server:production`  
   
### Once-off setup:
1. Create a Kubernetes Cluster
2. Athenticate gcloud:  
	`gcloud auth login`  
	`gcloud config set project zapgo-1273`  
3. Connect to kubernetes cluster:  
	`gcloud container clusters get-credentials hosting-cluster --zone us-west1-a --project zapgo-1273`  
4. Letsencrypt SSL setup:  
	`kubectl apply -f server/kubernetes/lego/00-namespace.yaml && kubectl apply -f server/kubernetes/lego/configmap.yaml && kubectl apply -f server/kubernetes/lego/deployment.yaml`  
5. Webserver setup:  
   - Staging:
   	  `kubectl apply -f server/kubernetes/docs-server-staging/all-in-one.yaml`  
   	- Production:
     `kubectl apply -f server/kubernetes/docs-server/all-in-one.yaml`. 
6. Check the external IP address and setup DNS:  
   - `kubectl get ingress --namespace docs-server docs-server`  
