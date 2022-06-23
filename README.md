# Berkeley Project
## Development
### Requirements
- Python 3
- Docker
- Kubernetes (optional)

### Setup Dev Environment
Create and activate virtual environment & install apps required.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Building Image
```
docker build --tag visit-counter .
```

### Deploying on Docker
Setup Redis
```
docker network create -d bridge redisnet

docker run --rm -d -p 6379:6379 -e REDIS_PASSWORD=redis --name redis --network redisnet redis /bin/sh -c 'redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}'
```

Running visit-counter app
```
docker run -d -p 5000:5000 -e REDIS_HOST='redis' -e REDIS_PASS='redis' --name visit-counter --network redisnet visit-counter 
```

### Deploying on Kubernetes
`Note: Make sure to push the visitor-counter image to your container registry, and make sure your cluster have the secrets to pull the image.`
```
docker push <change-to-registry-account>/visitor-counter
```

Setup Redis
```
cd berkeley-project/k8s-sample/redis/base
kubectl kustomize . | kubectl apply -f -
```

Running visit-counter app
```
cd berkeley-project/k8s-sample/visit-counter/base
kubectl create secret generic redis-pass --from-literal=REDIS_PASS=redis
kubectl kustomize . | kubectl apply -f -
```