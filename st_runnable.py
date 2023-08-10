from __future__ import annotations

import bentoml

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    import numpy.typing as npt

MODEL_TAG="all-MiniLM-L6-v2:latest"
TOKENIZER_TAG="all-MiniLM-L6-v2-tokenizer:latest"

class SentenceTransformerRunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("nvidia.com/gpu", "cpu")
    SUPPORTS_CPU_MULTI_THREADING = True
    
    def __init__(self):
        import torch
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.tokenizer = bentoml.transformers.load_model(TOKENIZER_TAG)
        self.model = bentoml.transformers.load_model(MODEL_TAG)
        self.model.to(self.device)

    
    @bentoml.Runnable.method(batchable=True, batch_dim=0)
    def encode(self, sentences: List[str]) -> npt.NDArray[float]:
        import torch
        
        # Tokenize sentences
        encoded_input = self.tokenizer(
            sentences, padding=True, truncation=True, return_tensors='pt'
        ).to(self.device)

        # Compute token embeddings
        with torch.no_grad():
            model_output = self.model(**encoded_input)

        # Perform pooling
        sentence_embeddings = self.mean_pooling(
            model_output, encoded_input['attention_mask']
        )

        # Optional: Normalize embeddings if needed
        # sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
        
        return sentence_embeddings.cpu().numpy()


    @staticmethod
    def mean_pooling(model_output, attention_mask):
        import torch

        # Mean Pooling - Take attention mask into account for correct averaging
        token_embeddings = model_output[0] #First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
