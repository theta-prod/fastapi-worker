from typing import TypedDict, NewType, List, Dict




class JsonResponBase(TypedDict):
    status: int


class JsonResponMsg(JsonResponBase):
    result: List[List[str]]
