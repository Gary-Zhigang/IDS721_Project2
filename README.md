# IDS721_Project2
## Introduction
This is the second project for the course IDS721, it is a flask application which can search for 10 similar songs on Spotify based on the song name you provide. In the future, I will apply more techniques in this project to make it more powerful.

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

would finish in next week


## Project2 Requirements

* Create a customized Docker container from the current version of Python that deploys a simple python script.
* Push image to DockerHub, or Cloud based Container Registery (ECR)
* Project should deploy automatically to Kubernetes cluster
* Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)
