#!/bin/bash
docker exec -d spark-master /spark/sbin/start-history-server.sh
docker exec -d spark-worker-1 /spark/sbin/start-slave.sh spark://spark-master:7077
docker exec -d spark-worker-2 /spark/sbin/start-slave.sh spark://spark-master:7077