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
	sentence-embedding-svc:$VERSION \
	--opt label='org.opencontainers.image.source=https://github.com/bentoml/sentence-embedding-bento' \
	--opt label='org.opencontainers.image.description="Sentence Embedding REST API Service"' \
	--opt label='org.opencontainers.image.licenses="Apache-2.0"' \
	-t ghcr.io/bentoml/sentence-embedding-bento:$VERSION \
	-t ghcr.io/bentoml/sentence-embedding-bento:latest

echo "🍱 Building GPU-enabled Bento.."
bentoml build $GIT_ROOT -f $GIT_ROOT/bentofile-gpu.yaml --version $VERSION-gpu

echo "🐳 Containerizing GPU-enabled Bento.."
bentoml containerize \
	sentence-embedding-svc:$VERSION-gpu \
	--opt label='org.opencontainers.image.source=https://github.com/bentoml/sentence-embedding-bento' \
	--opt label='org.opencontainers.image.description="Sentence Embedding REST API Service"' \
	--opt label='org.opencontainers.image.licenses="Apache-2.0"' \
	-t ghcr.io/bentoml/sentence-embedding-bento-gpu:$VERSION \
	-t ghcr.io/bentoml/sentence-embedding-bento-gpu:latest

echo "🚀 Publishing Docker Image to Github.."
docker push ghcr.io/bentoml/sentence-embedding-bento:$VERSION
docker push ghcr.io/bentoml/sentence-embedding-bento:latest
docker push ghcr.io/bentoml/sentence-embedding-bento-gpu:$VERSION
docker push ghcr.io/bentoml/sentence-embedding-bento-gpu:latest

echo "✅ Package $VERSION has been released!"
