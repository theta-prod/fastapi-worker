import uvicorn
from fastapi import FastAPI
from type.response import JsonResponMsg
from type.client import Body
from typing import List
from model import runModel, Letter

app = FastAPI()


@app.post("/model", response_model=JsonResponMsg)
async def newUserById(body: Body) -> JsonResponMsg:
    print(body)
    threshold = body['threshold'] if 0.999 > body['threshold'] > 0.3 else 0.85
    result: List[Letter] = runModel(data=body['corpus'],threshold=threshold) 
    return JsonResponMsg(status=200, result=result)


uvicorn.run(app, host="0.0.0.0", port=8080)
