from __future__ import annotations

import bentoml
from bentoml.io import JSON, NumpyNdarray
from pydantic import RootModel

from typing import List, TYPE_CHECKING

from embedding_runnable import SentenceEmbeddingRunnable

if TYPE_CHECKING:
    import numpy.typing as npt


embed_runner = bentoml.Runner(
    SentenceEmbeddingRunnable,
    name='sentence_embedding_model',
    max_batch_size=32,
    max_latency_ms=300
)
svc = bentoml.Service(
    "sentence-embedding-svc",
    runners=[embed_runner],
)

Documents = RootModel[List[str]]
samples = [
    "The dinner was great!",
    "The weather is great today!",
    "I love fried chiclken sandwich!"
]

@svc.api(
    input=JSON.from_sample(samples, pydantic_model=Documents),
    output=NumpyNdarray()
)
async def encode(docs: Documents) -> npt.NDArray[float]:
    return await embed_runner.encode.async_run(docs.dict()) 
