from typing import TypedDict, NewType, List, Dict
from model import ModelResult


class JsonResponBase(TypedDict):
    status: int


class JsonResponMsg(JsonResponBase):
    result: List[ModelResult]
