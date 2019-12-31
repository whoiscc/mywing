#!/bin/bash

action=$1
version="1.0"

case $action in
	clean)
		docker rmi mywing/server-container:${version} 2> /dev/null
		echo "Pleas make sure you remove container first."
		;;
    build)
        docker build -t mywing/server-container:${version} .
        echo "Build over"
        ;;
    exec)
        docker run -it --rm mywing/server-container:${version} /bin/sh
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
