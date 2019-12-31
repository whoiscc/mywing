#!/bin/bash

action=$1
version="1.0"

case $action in
	clean)
		docker rmi mywing/server:${version} 2> /dev/null
		echo "Pleas make sure you remove container first."
		;;
    build)
        docker build -t mywing/server:${version} .
        echo "Build over"
        ;;
    exec)
        docker run -it --rm mywing/server:${version} /bin/sh
        echo "Quit."
        ;;
    run)
        docker-compose up
        echo "Container stop and removed."
        ;;
    *)
        echo "Action not found: $action"
        ;;
esac
