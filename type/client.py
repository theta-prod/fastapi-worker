from typing import NewType, TypedDict

corpus = NewType("corpus", str)


class Body(TypedDict):
    corpus: corpus
    max_len: int
