from typing import TypedDict, NewType, List, Dict, Any
from model import ModelOutput




class JsonResponBase(TypedDict):
    status: int


class JsonResponMsg(JsonResponBase):
    result: ModelOutput
