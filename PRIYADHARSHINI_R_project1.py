from optparse import Option
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import pybase64
import datetime
app=FastAPI()

class CV(BaseModel):
    name:str
    age:int
    dev:bool
    hobby:Optional[list]

class EMPLOYEE(BaseModel):
    name:str
    exp:int
    yop:int
    age:int
    employeed:bool





@app.get("/hello/{my_query}")
def home(my_query,q:Optional[str]=None):
    return{"result":"sucess","user_input":my_query,"query":q}


@app.put("/endpoint")
async def endpoint(resume:CV):
    "some code db here"
    return{"username": resume.name}




@app.put("/mypostendpoint")
async def mpep(emp:EMPLOYEE):
    return{"emp":emp.name}



@app.get("/token")
async def tokenGenerator():
    timenow=bytes(str(time.time()),"utf-8")
    
    token = pybase64.b64encode(timenow,altchars='_:')
    with open("token.txt","a+") as tokenfile:
        tokenfile.write(str(token)+"|\n")
        tokenfile.close()
    return {"token":token}

@app.get("/mySecureEndpoint")
async def msep(token:str):

    file=eval(str(open("token.txt","r+").readlines()))
    #print(file)
    
    
    
    #to commit
    for each in file:
        if token in each:
            authorisation="welcome buddy"
            break
        else:
            authorisation="get lost"
        
            pass
    return{"server_pass":authorisation}

    #authToken="YWljbHB5dGhvbndlYg"


    #if token!="" or token==authToken:
        #authorisation="welcome home"
    #else:
        #authorisation="get out"
    