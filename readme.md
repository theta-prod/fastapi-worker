# [Tutoial] fastapi-worker with transformer Model

- **Metadata** : `type: Tutoial` `scope: API, Backend, fastapi` 
- **Techs Need** : `python` `fastapi`
- **Status**: `need-review`
<br/><br/>

## ✨ You should already know
- huggingface
- transformer
- FastAPI

👩‍💻 👨‍💻

## ✨ About the wiki
- `Situation:` 提供NLU的服務接口，方便與各服務進行串接。
- `Target:` 提供API接口和文件方便對接。
- `Index:`

| Sub title | decription | memo |
| ------ | ------ | ------ |
| API | 使用FastAPI來建置API | 包含文件使用和定義 |
| MODEL | 從huggingface上下載服務來實現API服務 | 包含載入模型與驅動模型 |


---
<br>

### **API**
> 使用FastAPI來建置API

####  📝 定義API輸入與輸出的內容
這邊請要好好定義，之後FastAPI會根據這些定義來產生線上文件，線上文件可以協助直接透過網頁來打出請求、測試API

- Input(Body)
```
from typing import NewType, TypedDict

corpus = NewType("corpus", str)
class Body(TypedDict):
    corpus: corpus
```


- Output(JsonResponMsg)
```
from typing import TypedDict, NewType, List, Dict

class modelResult(TypedDict):
    word: str
    entity: str

class JsonResponBase(TypedDict):
    status: int

class JsonResponMsg(JsonResponBase):
    result: List[modelResult]
```

####  📝 服務本體

- 設定伺服器基本內容
```
import uvicorn
from fastapi import FastAPI
from type.response import JsonResponMsg
from type.client import Body
from typing import List
from model import runModel, ModelResult

app = FastAPI()


@app.post("/model", response_model=JsonResponMsg)
async def newUserById(body: Body) -> JsonResponMsg:
    print(body)
    result: List[ModelResult] = runModel(data=body['corpus'])
    return JsonResponMsg(status=200, result=result)


uvicorn.run(app, host="0.0.0.0", port=8080)
```

- 啟動伺服器(測試用，正式使用時建議使用docker來建置)
```
python main.py
```

- 啟動伺服器(docker)
```
sudo docker-compose up -d
```

- 線上文件
```
http://127.0.0.1:8080/docs/
```

### **MODEL**
> 從huggingface上下載服務來實現API服務。

這邊我們用[斷句模型: theta/sentcore](https://huggingface.co/theta/sentcore)進行示範。


####  📝 載入模型
這邊我們載入模型和相關配套套件。並使用`TokenClassificationPipeline`來驅動模型
```
from transformers import AutoTokenizer, AutoModelForTokenClassification, TokenClassificationPipeline
from transformers.models.bert.tokenization_bert_fast import BertTokenizerFast
from transformers.models.bert.modeling_bert import BertForTokenClassification

##
def getTokenizer(tag: str) -> BertTokenizerFast:
    return AutoTokenizer.from_pretrained(tag)


def getModel(tag: str, num_labels: int = 4) -> BertForTokenClassification:
    return AutoModelForTokenClassification.from_pretrained(
        tag, num_labels=num_labels)


##
tokenizer: BertTokenizerFast = getTokenizer("bert-base-chinese")
model: BertForTokenClassification = getModel("theta/sentcore")
classifier: TokenClassificationPipeline = TokenClassificationPipeline(
    model=model, tokenizer=tokenizer)
```

####  📝 模型處理
載入完模型，建議根據模型的輸出去定義物件，增加系統穩定性

- 建立驅動模型的方法 
```
# type
class Letter(TypedDict):
    entity: str
    word: str
    score: int
    index: int
    start: int
    end: int


class ModelResult(TypedDict):
    entity: str
    word: str

def runModel(data: str) -> List[ModelResult]:
    modelResult: List[Letter] = classifier(data)
    return [{
        "word": row["word"],
        "entity": row["entity"]
    } for row in modelResult]
```

- 測試模型

```
runModel("據了解台南市警二分局民權所警員凃明誠曹瑞傑慘遭割喉殉職嫌犯林信吾經過18小時的逃亡23日清晨4時36分在新竹的和欣客運站落網")

>>> [
	{"word": "據" , "entity": "|"},
	{"word": "了" , "entity": ""},
	{"word": "解" , "entity": "|"},
	...
]

```

