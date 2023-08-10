#!/bin/bash
set -e

export VERSION=${VERSION?"Need to set release VERSION, e.g. VERSION=0.1 ./release.sh"}
GIT_ROOT=$(git rev-parse --show-toplevel)

if (! docker version >/dev/null 2>&1); then
	echo "Make sure Docker is running."
	exit 1
fi

echo "🍱 Building Bento.."
bentoml build $GIT_ROOT -f $GIT_ROOT/bentofile.yaml --version $VERSION

echo "🐳 Containerizing Bento.."
bentoml containerize \
	sentence-transformer-svc:$VERSION \
	--opt label='org.opencontainers.image.source=https://github.com/bentoml/sentence-embedding-bento' \
	--opt label='org.opencontainers.image.description="Sentence Transformer Model Serving"' \
	--opt label='org.opencontainers.image.licenses="Apache 2"' \
	-t ghcr.io/bentoml/sentence-embedding-bento:$VERSION \
	-t ghcr.io/bentoml/sentence-embedding-bento:latest

echo "🚀 Publishing Docker Image to Github.."
docker push ghcr.io/bentoml/sentence-embedding-bento:$VERSION
docker push ghcr.io/bentoml/sentence-embedding-bento:latest

echo "✅ Package $VERSION has been released!"
