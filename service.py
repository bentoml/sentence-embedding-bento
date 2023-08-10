from __future__ import annotations

import bentoml
import numpy as np
from bentoml.io import JSON, NumpyNdarray
from pydantic import RootModel

from typing import List, TYPE_CHECKING, Dict

from numpy._typing import NDArray

from st_runnable import SentenceTransformerRunnable

if TYPE_CHECKING:
    import numpy.typing as npt


st_runner = bentoml.Runner(
    SentenceTransformerRunnable,
    name='all-minilm-l6-v2',
    max_batch_size=32,
    max_latency_ms=300
)
svc = bentoml.Service(
    "sentence-transformer-svc",
    runners=[st_runner],
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
    return await st_runner.encode.async_run(docs.dict()) 
