import csv
import requests as rq
import re
from typing import Any, List
def cleanStr(content) -> str : 
  content = content.replace("\n","")
  return re.sub(f'[^\u4e00-\u9fa5^a-z^A-Z^0-9]', "", content) or ""

def getmodel(s: str):
    return rq.post("http://127.0.0.1:8080/userID",json={
        "corpus": cleanStr(s)
    }).json()['result']
def humanParse(res: List[Any])-> str:
    res_human: Literal[''] = ""
    for unit in res:
        res_human+=(unit["word"])
        if unit["entity"] == "/" :
            res_human+=(unit["entity"])
        if unit["entity"] == "|" :
            res_human+=(" ")
    return res_human

with open('data.tsv', newline='\n') as csvfile:
  arrayR = [["user", "第一單元 光和能源 知識內容省思", "res1_human", "單元二 地球的夥伴 日月星辰 知識內容省思", "res2_human"]]
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile,delimiter="\t")

  # 以迴圈輸出每一列
  for row in rows:
    user = row[3]
    source1, source2 = row[4],row[5]
    print(source1,source2) 

    res1 = getmodel(source1)
    res1_human = humanParse(res1)
    
    res2 = getmodel(source2)
    res2_human = humanParse(res2)
    arrayR.append([user,cleanStr(source1), res1_human, cleanStr(source2), res2_human])


print(arrayR)

# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
#   writer.writerow(['姓名', '身高', '體重'])

  # 寫入另外幾列資料
  for r in arrayR:
    writer.writerow(r)