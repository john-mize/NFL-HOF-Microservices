# NFL-HOF-Microservices
An update/reimagining of the previous Hall of Fame Predictions repo.
- The algorithms have been updated and moved to a script format, rather than a jupyter notebook
- A flask app has been created to query/view the data in a more accessible format, in JSON form
- A Dockerfile has been included to create an image for this app, and helm charts have been included to run this image in kubernetes

Instructions:
1. First, it is recommended you install python, start a python virtual machine, and install the packages listed in the requirements.txt file 
2. In order to run just the HOF Predictions scripts, run either RB_HOF_PREDICT.py or WR_HOF_PREDICT.py in python
3. To run the Flask app, run app.py in python. It is currently set to run on localhost:5000 in your browser, but the port (5000) can be changed in the file. This app runs the scripts and compiles the data in a queryable, readable format
4. To create an image, run a docker build command with the Dockerfile
5. To run this image in kubernetes, podman, minikube, etc., change the helm values.yaml file to point to the docker image you have built, and then install the charts
