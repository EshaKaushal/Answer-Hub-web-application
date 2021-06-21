# Answers Hub web application
### Submission Details


## Application Description
The application can be accessed using the URL - https://mgmt590-webapp-es7glm5rsq-uc.a.run.app

Our application **'Answers Hub'** allows user to ask questions by providing context and utilizing various AI models. 

### Application Architecture
Our application's is a python based application with its front end created using Streamlit. The application uses REST API to make calls to the service hosted on google cloud.<br>
A user can access the application hosted on cloud using the public URL. Each user action triggers a request to API. When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint. The service then interacts with application's PostgreSQL database hosted on Google Cloud= to generate a response.

Here is our architecture diagram. <br>

<img src="/images/ApplicationArchitecture.PNG">

### Application Functionalities
A user can perform the following operations using the app -<br>
1)  **Action 1 - Add a model** - This functionality allows a user to add a new model into the server and make it available for question answering.
      
    <img src="/images/AddModel.PNG">

2)  **Action 2 - Delete a model** - This functionality allows a user to delete a model stored in the server.The dropdown will show all current models in the database.

    <img src="/images/DeleteModel.PNG">

3)  **Action 3 - Answer a question** - This functionality allows a user to enter a question, context and choose a model to finally get the answer.

    <img src="/images/AnswerQues.PNG">

4)  **Action 4 - Bulk Upload of questions** - This functionality allows a user to enter upload a csv file containing multiple questions and context. The application generates answers using the default model.
    <img src="/images/BulkUpload.PNG">

### Dependencies
The application uses a lot of python packages and libraries to ensure that both the REST API and application UI are functional. Packages currently in use are -
|Packages|Function|installation|
|----|----|----|
|streamlit|Use to render the UI|pip install streamlit|
|pandas|Used to work with data files |pip install pandas
|requests|Used to get and send requests to API |pip install requests
|transformers==4.2.2|Used to get Huggingface's transformers|pip install transformers==4.2.2|
|flask|Used to create a flask application|pip install flask
|torch|Used to access pyTorch based model in Higgingface models |pip install torch
|pytest==6.2.2|Used to run unit test suit|pip install pytest
|psycopg2-binary|Used to access Postgre sql database hosted on google cloud |pip install psycopg2

A user can simply executing the following command -
```$ pip install -r requirements.txt``` and voila! all the program's dependencies will be downloaded, installed and ready to be used by the application.

### Build and Run the WebApp locally via Docker
To build and run the application locally a user would need to follow the below process - <br>
1) **Get the application** - To run the application locally, one needs to get the application source code onto their local machine. Our application is already developed and the code can be accessed in 'Streamlitapp.py'. User can start by cloning our repo command and using the following command to run the app. <br>
``` streamlit run <app.py> ```.
The application would be active on the local host. Application can be closed using Ctrl+C.<br>

2) **Build a Docker image for app with Docker engine** - Here image refers to the bundle that includes your app and dependencies (listed in requirements.txt). We will specify the details of how to build an image in a file called 'Dockerfile'. A Dockerfile is simply a text-based script of instructions that is used to create a container image. Below is one sample of DockerFile - <br>

```
FROM python:3.7-slim

EXPOSE 8080
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

COPY requirements.txt . 

RUN pip install -r requirements.txt 

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "Streamlitapp.py"]
```
Please check that the file Dockerfile has no file extension like ```.txt.``` Some editors may append this file extension automatically and this would result in an error in the next step.

3) **Building Docker image in the Active Directory/Folder** - After we have added the dependencies, we will run the docker container using the command - <br>
``` sudo docker build -t <image-name> . ```
The . at the end of the docker build command tells that Docker should look for the Dockerfile in the current directory.

4) **Start the app container** - Now we run the docker image with ports defined for communication between local machine and docker image . User can use the following command <br>
``` sudo docker run -it -p 8080:8080 <image-name> /app/<aap-name>.py ```
