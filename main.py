import uvicorn
from fastapi import FastAPI
from type.response import JsonResponMsg
from type.client import Body
from typing import List
from model import runModel, modelOutput

app = FastAPI()


@app.post("/chatGPT", response_model=JsonResponMsg)
async def newUserById(body: Body) -> JsonResponMsg:
    print(body)
    result: modelOutput = runModel(body['corpus'])
    return JsonResponMsg(status=200, result=result)


uvicorn.run(app, host="0.0.0.0", port=8080)
