---
title: "Docker"
date: 2019-12-11T11:13:00+05:30
 
weight: 50
---

{{% children depth="3" sort="weight" %}}


Check docker version

    docker version

Docker container

    #get runnig and non running docker container 
    docker ps
    docker ps -a 
    
    # remove docker container
    docker rm $(docker ps -aq)

Docker images 

    docker images 
    
    #delete all docker images
    sudo docker kill $(sudo docker ps -aq)
    docker rmi $(docker images -q)

Docker build

    docker build -t {name}  .

Docker run

    docker run -it {image} -p expose_port:internal_port

Exec in Docker container

    docker exec -it {container} /bin/sh

Docker run 

    docker run  --mount type=bind,source="$(pwd)"/data,target=/home/data -it <name_of_container>
