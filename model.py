import requests as rq
from typing import TypedDict, NamedTuple
import json
import re
import os
# 
def cleanStr(content: str)-> str:
  content = content.replace("\n","")
  return re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]', "", content)



class ModelOutput(TypedDict):
    result: str
    
class TaskObj(TypedDict):
  question: str
  reply: str



header = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {os.environ.get('APIKEY','')}"
}


def runModel(taskObj: TaskObj) -> ModelOutput:
  url: str= "https://api.openai.com/v1/completions"


  body = {
    "model": "davinci:ft-voiss-co-ltd:ensemble-base-2023-01-23-08-42-12",#"text-ada-001",#,
    "prompt": f"{taskObj['question']} -ques;ans- {taskObj['reply']} ->",
    "max_tokens": 3,
    "temperature": 0
  }
  x = rq.post(url=url, json=body, headers=header).json()
  if 'choices' in x:
    return {
      "result": str(x['choices'][0]['text'])
    }
  else:
    return {
      "result": json.dumps(x)
    }

print(runModel(TaskObj(
  question = "我護理專科肄業，現年30歲，為連鎖店門市正職人員,最近一直思考是否要回學校補齊專科學歷，但補齊學歷真的會對工作選擇更多嗎，工作經驗一直以來都是服務業性質，想跳脫這種性質但又發現自己能做的也只有這類型工作，有上赫綵設計相關課程喜歡畫畫但目前感覺好像都是在繳錢實質上對工作轉職目前還無成效！不知道是否要繼續這一塊，也喜歡烘焙！有想說是不是可以考取相關證照增加轉職或工作機會！但好像還是逃離不了服務業性質！，還是什麼都不要想，安份於現況好好工作與生活呢？望各位前輩或朋友們曾有相似之處的或疑慮過的能提供我一些建議或意見！謝謝大家",
  reply= "您好，我是阿邱，很高興有機會回答您的問題     首先，現在這個時代，永遠不會有一個正確答案是 安於現狀 的 您的癥結點應該在於，看不到補齊學歷或考取證照的實質效益，反正現在的狀態一樣可以持續從事服務業；但是，請不要忘記，當經濟動盪或所待的企業營運出問題時，第一批會被淘汰掉的很可能就是基層人員；即使一路平順，隨著年紀增長，從事服務業可能也會更加吃力，屆時要轉職 提升職涯等，都會更加困難重重     學歷跟證照，在一種情況下可以不用補，即是您在目前從事的工作上已經完全變成熟手，您的技能不管在哪家公司都炙手可熱，公司非常依賴您的能力，那您就可以憑藉這份技能持續維生 否則，若經濟與時間允許，還是建議可以將學歷與（跟您工作直接相關的）證照補足，有備無患     相信您會詢問這個問題也代表您已產生一定程度的危機意識，持續進步的動力在職涯發展上是很重要的喔！若回答對您有幫助，請不吝點個 拍手 及 肯定 唷，謝謝！"
)))