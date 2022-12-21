import uvicorn
from fastapi import FastAPI
from type.response import JsonResponMsg
from type.client import Body
from typing import List, Any
from model import runModel

app = FastAPI()


@app.post("/model", response_model=JsonResponMsg)
async def newUserById(body: Body) -> JsonResponMsg:
    print(body)
    result: List[Any] = runModel(data=body['corpus'])
    return JsonResponMsg(status=200, result=result)


uvicorn.run(app, host="0.0.0.0", port=8080)
