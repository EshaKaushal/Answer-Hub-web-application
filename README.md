# Mgmt590-Assignment3 - Creating web application
### Submission Details
|Name|PUID|
|----|----|
|Esha Kaushal| 0032356932|

### Application Description
The application can be accessed using the URL - https://mgmt590-webapp-es7glm5rsq-uc.a.run.app

Our application **'Answers Hub'** allows user to ask questions by providing context and utilizing various AI models. A user can perform the following operations using the app -<br>
1)  **Action 1 - Add a model** - This functionality allows a user to add a new model into the server and make it available for question answering.
      
    <img src="/images/AddModel.PNG">

2)  **Action 2 - Delete a model** - This functionality allows a user to delete a model stored in the server.

    <img src="/images/DeleteModel.PNG">

3)  **Action 3 - Answer a question** - This route allows a user to delete an existing model on the server such that it is no longer available for inference.
      Method and path; DELETE /models?model=<model name>
      Sample request paramaters & respones -
    <img src="/images/AnswerQuestion.PNG">

4)  **Action 4 - Bulk Upload of questions** - This route uses one of the available models to answer a question, given the context provided in the JSON payload.
     Method and path: POST /answer?model=<model name>     <model name> is optional
      Sample request paramaters & respones -
    <img src="/images/BulkUpload.PNG">

### Dependencies
The application uses a lot of python packages and libraries. All the required packages are listed in the file **requirements.txt**. A user can simply executing the following command -
```$ pip install -r requirements.txt``` and voila! all the program's dependencies will be downloaded, installed and ready to be used by the application.

### Build and RUn the API locally via Docker or Flask
A user can download this repository and after installing all the dependencies listed in requirement.txt, they can trigger the python code. Requests can be sent using application like 'Postman', instead of the application url, the user can hit their localhost and can continue to send the request following the routes specified above.
