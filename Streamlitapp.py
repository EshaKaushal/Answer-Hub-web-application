import streamlit as st
import pandas as pd
import requests
import json
import os

#Get URL from Git env variables
#url = "https://mgmt590-restapi-es7glm5rsq-uc.a.run.app"
url = format(os.environ.get('REST_API_URL'))

st.title("Answers Hub - Question Answering App")

def getModelList():
    payload_modellist = ""
    headers_modellist = {}
    getModelURL = url + "/models"
    response = requests.request("GET", getModelURL, headers=headers_modellist, data=payload_modellist)
    modelResp = json.loads(response.text)
    modelList = []
    for i in range(0,len(modelResp)):
        modelList.append(modelResp[i]["name"])
    print("Models received from Database",len(modelResp))
    print(modelList)
    return modelList, modelResp

#Section 1 - Add/Delete Model List

ModelSec = st.beta_expander("Add a Model")
ModelSec.title("Add a model")
MName = ModelSec.text_input('Model Nick Name')
MModel = ModelSec.text_input('Model')
MTokenizer = ModelSec.text_input('Tokenizer')
AddModelURL = url + "/models"
if ModelSec.button('Add Model'):
    #Trigger PUT request to add model
    payload = json.dumps({
        "name": MName,
        "tokenizer": MTokenizer,
        "model": MModel
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", AddModelURL, headers=headers, data=payload)
    print(response.text)
    ModelSec.success('Model has been Added')

#Section 2 - Delete a Model
ModelSec2 = st.beta_expander("Delete a Model")
ModelSec2.title("Delete a model")
modelList, modelResp = getModelList()
DelModel = ModelSec2.selectbox('Select Model to delete',modelList)
if ModelSec2.button('Delete Model'):
    #Trigger Delete request
    payload = ""
    headers = {}
    DelURL = url + "/models?model="+DelModel
    response = requests.request("DELETE", DelURL, headers=headers, data=payload)
    ModelSec2.success('Model has been Deleted')

#Section 3 - Answer a Question
AnswerSec = st.beta_expander("Answer a Question")
question = AnswerSec.text_input('Question')
Context = AnswerSec.text_area ('Context')
modelList2, modelResp = getModelList()
ModelName = AnswerSec.selectbox('Select Model',modelList2)
if AnswerSec.button('Get Answer'):
    #Trigger POST request
    if ModelName == None:
        AnswerURL = url + "/answer"
    else:
        AnswerURL = url + "/answer?model=" + ModelName
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "question": question,
        "context": Context
    })
    response = requests.request("POST", AnswerURL, headers=headers, data=payload)
    Answer = json.loads(response.text)
    print(Answer["answer"])
    AnswerSec.success("Answer is "+Answer["answer"])

#Section 3
BulkUploadSec = st.beta_expander("Bulk Upload Question and Context")
file = BulkUploadSec.file_uploader("Upload a csv questions and context file")
if (file is not None) and BulkUploadSec.button('Fetch Answer'):
    df = pd.read_csv(file)
    answer_list = []
    print("length of file is ",len(df))
    #print(df)
    for i in range(0,len(df)):
        question = df['question'][i]
        context = df['context'][i]
        #trigger API to get answer
        AnswerURL = url + "/answer"
        headers = {
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "question": question,
            "context": context
        })
        response = requests.request("POST", AnswerURL, headers=headers, data=payload)
        Answer = json.loads(response.text)
        answer_list.append(Answer["answer"])
        print(Answer["answer"])
        #BulkUploadSec.success("Answer is " + Answer["answer"])
    df['Answer'] = answer_list
    BulkUploadSec.table(df)

#Sidebar
# sidebar = st.beta_expander("List of available models")
# modelList, modelResp = getModelList()
# sidebar.table(modelResp)

st.title("List of available models")
modelList, modelResp = getModelList()
st.table(modelResp)
