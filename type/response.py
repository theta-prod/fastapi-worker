from typing import TypedDict, NewType, List, Dict, Any




class JsonResponBase(TypedDict):
    status: int


class JsonResponMsg(JsonResponBase):
    result: Dict[str, Any]
