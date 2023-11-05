#!/bin/bash
set -ex

HF_MODEL=${HF_MODEL:-"sentence-transformers/all-MiniLM-L6-v2"}
CUDA=${CUDA:-"11.6.2"}
GPU=${GPU:-"false"}
REPO=${REPO:-"ghcr.io"}

echo "📂 1. Loading model & tokenizer from HuggingFace into cache"
model=$(python import_model.py --hf "$HF_MODEL")

echo "🍱 2. Building Bento.."
if [ "$GPU" == "true" ];
then
  VERSION="${model}-gpu"
  cat bentofile-gpu.yaml | sed -e "s/all-MiniLM-L6-v2/$model/g" -e "s/11\.6\.2/$CUDA/g" > bentofile-copy.yaml
else
  VERSION="$model"
  cat bentofile.yaml | sed -e "s/all-MiniLM-L6-v2/$model/g" > bentofile-copy.yaml
fi

cp embedding_runnable.py _embedding_runnable.py
cat _embedding_runnable.py | sed -e "s/all-MiniLM-L6-v2/$model/g" > embedding_runnable.py
bentoml build . -f bentofile-copy.yaml --version "$VERSION" --force

echo "🐳 3. Containerizing Bento.."
bentoml containerize \
	"sentence-embedding-svc:$VERSION" \
	--opt label='org.opencontainers.image.source=https://github.com/bentoml/sentence-embedding-bento' \
	--opt label='org.opencontainers.image.description="Sentence Embedding REST API Service"' \
	--opt label='org.opencontainers.image.licenses="Apache-2.0"' \
	-t "$REPO/bentoml/sentence-embedding-bento:$VERSION"