from typing import TypedDict, NewType, List, Any

class modelResult(TypedDict):
    word: str
    entity: str


class JsonResponBase(TypedDict):
    status: int


class JsonResponMsg(JsonResponBase):
    result: List[Any]
