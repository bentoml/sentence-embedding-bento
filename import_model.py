import bentoml
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

bentoml.transformers.save_model("all-MiniLM-L6-v2", model)
bentoml.transformers.save_model("all-MiniLM-L6-v2-tokenizer", tokenizer)
