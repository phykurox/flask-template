#!/bin/bash -xe
#This script will build a local docker image running on your local machine
clear

# Get an initial name from the builder
if [ -z "$1" ]; then
    echo "bash scripts/build-docker.sh <your-initial>" >&2
    exit 1
else
    NAME=$1
fi

# Optional: for building alternative image for debugging purposes
if [ -z "$2" ]; then
    DOCKERFILE=Dockerfile
    DEBUGFILE=""
else
    DOCKERFILE=$2
    DEBUGFILE="-debug"
fi

# main settings
VERSION=0.1.0
LATEST=latest 
PACKAGE=$NAME-movies-api$DEBUGFILE
REGISTRY=dojocracr.azurecr.io
PORT=8080

if ! docker images -q $PACKAGE:$VERSION; then
    docker image rm $PACKAGE:$VERSION #remove old image         
fi   

docker build -t $PACKAGE:$VERSION -f $DOCKERFILE .    
docker tag $PACKAGE:$VERSION $PACKAGE:$LATEST
docker image ls $PACKAGE

echo "For Azure Container Registry (ACR)"
echo "TEST RUN: docker run -it -u 1000 -p $PORT:$PORT $PACKAGE:$LATEST"
echo "TAG: docker tag $PACKAGE:$LATEST $REGISTRY/$PACKAGE:$LATEST"
echo "PUSH: docker push $REGISTRY/$PACKAGE:$LATEST"