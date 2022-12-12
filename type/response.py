from typing import TypedDict, NewType, List, Dict

class modelResult(TypedDict):
    word: str
    entity: str


class JsonResponBase(TypedDict):
    status: int


class JsonResponMsg(JsonResponBase):
    result: List[modelResult]
