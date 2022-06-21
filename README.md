# Berkeley Project
## Development
### Requirements
- Python 3
- Docker

### Setup Dev Environment
Create and activate virtual environment & install apps required.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Setup Redis
```
docker network create -d bridge redisnet

docker run --rm -d -p 6379:6379 -e REDIS_PASSWORD=redis --name redis --network redisnet redis /bin/sh -c 'redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}'
```

### Building Image
```
docker build --tag berk .
```

### Deploying on Docker
Running Python container
```
docker run -d -p 5000:5000 -e REDIS_HOST='redis' -e REDIS_PASS='redis' --name berk --network redisnet berk
```