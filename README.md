# Usage
## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine

- Git [- Download Git](https://git-scm.com/downloads)
- Docker [- Get Docker](https://docs.docker.com/get-docker/)

## Build a local environment
Start docker container
```
cd [WORK_DIRECTORY]/learning-apache-spark/deployments/local/
docker-compose up -d
```

## To run Apache Spark
Start history server and worker server
```
sh scripts/start.sh
```

Execute spark application
```
docker exec -it spark-master bash
/spark/bin/spark-submit /root/main.py
```