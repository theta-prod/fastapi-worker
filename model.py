import requests as rq
from typing import TypedDict, List
import re
import os
# 
def cleanStr(content: str)-> str:
  content = content.replace("\n","")
  return re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]', "", content)



class modelOutput(TypedDict):
    result: str


header = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {os.environ.get('APIKEY','')}"
}


def runModel(text: str) -> modelOutput:
  url: str= "https://api.openai.com/v1/completions"
  body = {
    "model": "text-davinci-003",#"text-ada-001",#,
    "prompt": text,
    "max_tokens": 300,
    "temperature": 0
  }
  x = rq.post(url=url, json=body, headers=header)
  print(x.json())
  return {
    "result": x.json()["choices"][0]["text"]
  }

print(runModel("""別人對我的好會放在心中很久很久，也會時常想要為他們做點什麼原來在別人眼中我是勇敢的，在我的記憶中，常常記得別人對我的傷害，其實我也是有把別人對我的好記在心中。

請務必選擇下列一個心情

1. 掙扎
2. 開心
3. 迷惘
4. 虧欠 """))