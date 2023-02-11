from transformers import AutoTokenizer, AutoModelForTokenClassification, TokenClassificationPipeline
from transformers.models.bert.tokenization_bert_fast import BertTokenizerFast
from transformers.models.bert.modeling_bert import BertForTokenClassification
from typing import TypedDict, List
import re

def cleanStr(content: str)-> str:
  content = content.replace("\n","")
  return re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]', "", content)
# type
class Letter(TypedDict):
    entity: str
    word: str
    score: int
    index: int
    start: int
    end: int





##
def getTokenizer(tag: str) -> BertTokenizerFast:
    return AutoTokenizer.from_pretrained(tag)


def getModel(tag: str, num_labels: int = 4) -> BertForTokenClassification:
    return AutoModelForTokenClassification.from_pretrained(
        tag, num_labels=num_labels)





def runModel(data: str, threshold=0.9) -> List[Letter]:
    modelResult: List[Letter] = classifier(cleanStr(data))
    return toSent(modelResult, threshold)


def toSent(ls: List[Letter], threshold:float) -> List[List[str]]:
    sents:List[List[str]] = []
    words:List[str]=[]
    word:str=""
    for l in ls:
        word+=l['word']
        if l['entity']=="|" or l['entity']=="/":
            words.append(word)
            word=""
        elif l['entity']=="。" and l["score"]>threshold:
            words.append(word)
            sents.append(words)
            word=""
            words = []
        elif l['entity']=="。":
            words.append(word)
            word= ""

    return sents


##
tokenizer: BertTokenizerFast = getTokenizer("bert-base-chinese")
model: BertForTokenClassification = getModel("theta/sentcore")
classifier: TokenClassificationPipeline = TokenClassificationPipeline(
    model=model, tokenizer=tokenizer)

# ts: List[Letter] = classifier("據了解台南市警二分局民權所警員凃明誠曹瑞傑慘遭割喉殉職嫌犯林信吾經過18小時的逃亡23日清晨4時36分在新竹的和欣客運站落網人被帶回台南市警三分局接受調查全案依殺人等罪偵辦台南市警方根據警車行車記錄器影片調查凃員與曹員接獲機車竊盜案循線追蹤林嫌至案發地僅看到車牌369-PGB機車未見到林男凃員見雜草叢生不易搜索與曹員分頭搜索結果凃員先遇到林嫌持彈簧刀突襲並奪槍後挾持受重傷凃員隨後在警車旁遇到曹員林嫌涉嫌向曹員開六槍疑未擊中曹員也遭林嫌持彈簧刀砍殺林嫌涉嫌殺2警後帶著警槍2彈匣18顆子彈騎該部贓車逃亡並將該贓車棄置在土城高中而後搭計程車離去")
# for t in ts:
#     print(t["word"], end="")
#     if t["entity"] == '|':
#         print(" ", end="")
#     if t["entity"] == '/':
#         print(" / ", end="")
#     if t["entity"] == '。':
#         print()
# print(runModel("據了解台南市警二分局民權所警員凃明誠曹瑞傑慘遭割喉殉職嫌犯林信吾經過18小時的逃亡23日清晨4時36分在新竹的和欣客運站落網"))
s:str= "據了解台南市警二分局民權所警員凃明誠曹瑞傑慘遭割喉殉職嫌犯林信吾經過18小時的逃亡23日清晨4時36分在新竹的和欣客運站落網"
s:str= "公司文化跟職位的需求不一樣，有時候就會讓人覺得有些企業喜歡找沒相關經驗的白紙或新鮮人    如果目前公司需要的是一名即戰力，那當然是有經驗的人員一進入職場就可以開始打仗是最好的，但他們已經有既定的作業模式，與公司現行的方式要花時間進行磨合跟溝通，也是需要考量的點 但若公司想要從零開始培養一個符合公司文化，而且不會被以往的框架或作業模式束縛住的，那就會偏向尋找沒相關經驗或是新鮮人 所以兩種有好有壞，主要還是看求職者本身的潛力 條件 跟與公司是否相符"
# print(classifier(s)[0])
es= runModel(s)
print(es)