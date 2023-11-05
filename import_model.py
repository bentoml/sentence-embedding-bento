import bentoml
import fire
from transformers import AutoTokenizer, AutoModel


def hf_to_bentoml(hf: str = "sentence-transformers/all-MiniLM-L6-v2",
                  model_name: str = None,
                  tokenizer_name: str = None):
    tokenizer = AutoTokenizer.from_pretrained(hf)
    model = AutoModel.from_pretrained(hf)

    if not model_name:
        model_name = hf.split("/")[1]

    if not tokenizer_name:
        tokenizer_name = f"{model_name}-tokenizer"

    bentoml.transformers.save_model(model_name, model)
    bentoml.transformers.save_model(tokenizer_name, tokenizer)
    print(f"{model_name}")


if __name__ == '__main__':
    fire.Fire(hf_to_bentoml)
