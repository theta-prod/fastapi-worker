from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
from transformers.models.bert.tokenization_bert_fast import BertTokenizerFast
from transformers.models.bert.modeling_bert import BertForTokenClassification
import re
from typing import Any


def cleanStr(content: str) -> str:
  content = content.replace("\n", "")
  return re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]', "", content)


# # type
# class Letter(TypedDict):
#     entity: str
#     word: str
#     score: int
#     index: int
#     start: int
#     end: int

# class SimpleLetter(TypedDict):
#     entity: str
#     word: str


##
def getTokenizer(tag: str) -> BertTokenizerFast:
  return AutoTokenizer.from_pretrained(tag)


def getModel(tag: str):  # -> BertForTokenClassification:
  return AutoModelForSequenceClassification.from_pretrained(tag)


##
tokenizer: BertTokenizerFast = getTokenizer("bert-base-chinese")
model: BertForTokenClassification = getModel("theta/MBTI-ckiplab-bert")
classifier: Any = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True)


def runModel(data: str, batchSize: int = 450) :  #-> List[SimpleLetter]:

  modelResult = None
  for startIdx in range(0, len(data), batchSize):
    if modelResult is None:
      modelResult = classifier(cleanStr(data[startIdx: startIdx+batchSize]))
    else:
      modelTempResult = classifier(cleanStr(data[startIdx: startIdx+batchSize]))
      for unitNum in range(4):
        modelResult[0][unitNum]['score'] = (modelTempResult[0][unitNum]['score'] +  modelResult[0][unitNum]['score'])/2
  return modelResult




# ts: List[Letter] = classifier("據了解台南市警二分局民權所警員凃明誠曹瑞傑慘遭割喉殉職嫌犯林信吾經過18小時的逃亡23日清晨4時36分在新竹的和欣客運站落網人被帶回台南市警三分局接受調查全案依殺人等罪偵辦台南市警方根據警車行車記錄器影片調查凃員與曹員接獲機車竊盜案循線追蹤林嫌至案發地僅看到車牌369-PGB機車未見到林男凃員見雜草叢生不易搜索與曹員分頭搜索結果凃員先遇到林嫌持彈簧刀突襲並奪槍後挾持受重傷凃員隨後在警車旁遇到曹員林嫌涉嫌向曹員開六槍疑未擊中曹員也遭林嫌持彈簧刀砍殺林嫌涉嫌殺2警後帶著警槍2彈匣18顆子彈騎該部贓車逃亡並將該贓車棄置在土城高中而後搭計程車離去")

# for t in ts:
#     print(t["word"], end="")
#     if t["entity"] == '|':
#         print(" ", end="")
#     if t["entity"] == '/':
#         print(" / ", end="")
#     if t["entity"] == '。':
#         print()
print(
  runModel("我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！我又感覺到我沒有被尊重，最終我選擇不想再繼續這樣的關係了！"))
