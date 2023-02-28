# IDS721_Project2
## Introduction
This is the second project for the course IDS721, it is a flask application which can search for 10 similar songs on Spotify based on the song name you provide. I used the Docker image to deploy this application and created a repository in DockerHub so that everyone could run it easily without cloning the whole project. Also, I depolyed this app on the Kubernetes by implementing Minikube.

## Function Display
___Search Page:___   

<img src="https://github.com/Gary-Zhigang/IDS721_Project2/blob/main/images/p1.png" alt="Your image description" width="300" height="100">

___Results Page:___  

<img src="https://github.com/Gary-Zhigang/IDS721_Project2/blob/main/images/p2.png" alt="Your image description" width="500" height="300"> 

## Implementation 
___Docker:___   

* After you clone this project, to build the Docker in local, you could type ``docker build -t get-songs``, and then type ``docker image ls`` to verify the images you get, finally, typing ``docker run -p 8080:8080 get-songs`` to run the application.
* You could also run the Docker without cloning this project, you could pull the image from the **DockerHub** by typing ``docker pull zhiw803/get-songs:latest``, and then typing ``docker run -p 8080:8080 zhiw803/get-songs:latest`` to run the application.

___Kubernetes:___  

1. Start the minikube: `minikube start`
2. Create a deployment: `kubectl create deployment get-songs --image=registry.hub.docker.com/zhiw803/get-songs`
3. View deployment: `kubectl get deployments`
4. Create service and expose it: `kubectl expose deployment get-songs --type=LoadBalancer --port=8080`
5. View services:  `kubectl get service get-songs`
6. View URL: `minikube service get-songs --url`
7. Curl web service: i.e. `curl http://192.168.49.2:31174`
8. Cleanup and stop: 
```bash
kubectl delete service get-songs
kubectl delete deployment get-songs
minikube stop
````
**Example:**  
<img src="https://github.com/Gary-Zhigang/IDS721_Project2/blob/main/images/minikube_image.png" alt="Your image description" width="850" height="750"> 

