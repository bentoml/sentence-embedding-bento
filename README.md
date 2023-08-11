# Serving SentenceEmbedding Model with BentoML

This is a sentence embedding API service built with [BentoML](https://github.com/bentoml/BentoML). 
It comes with the [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
sentence embedding model and provides a high-performance model
server for generating text embeddings over a REST API endpoint.

Looking For Image Embeddings? Check out [CLIP-API-service](https://github.com/bentoml/CLIP-API-service).

# Usage: Docker

The pre-built Docker Images for this project can be found on GitHub Container
registry [here](https://github.com/bentoml/sentence-embedding-bento/pkgs/container/sentence-embedding-bento).

Ensure you have [Docker](https://docs.docker.com/engine/install/) installed and running,
launch the embedding service with the following command:

```bash
docker run --rm -p 3000:3000 ghcr.io/bentoml/sentence-embedding-bento:latest
```

Open http://0.0.0.0:3000 from your browser to send test requests from the Web UI.

Alternatively, run the API client with Python or CURL command:

```python
from bentoml.client import Client

client = Client.from_url("http://localhost:4000")

samples = [
  "The dinner was great!",
  "The weather is great today!",
  "I love fried chiclken sandwich!"
]
print(client.encode(samples))
``` 

```bash
curl -X POST http://localhost:3000/encode \
   -H 'Content-Type: application/json' \
   -d '["hello world, how are you?", "I love fried chiclken sandwich!"]'
```


# Usage: Build Your Own

It is meant to be hackable and educational
for building your own text embedding service with BentoML.

Get started by cloning this repository:

```bash
git clone https://github.com/bentoml/sentence-embedding-bento.git
```

## Install Dependencies

You will need Python 3.8 or above to run this example. Download dependencies via `pip`:

```bash
pip install -U -r ./requirements.txt
```

## Import Model

```bash
python import_model.py
```

This saves and versions the `all-MiniLM-L6-v2` in your local BentoML model store.

## Run Embedding Service locally

Start the embedding service:
```
bentoml serve
```

## Building Bento

Bento is the standardize distribution format, which is supported by an array of downstream
deployment tools provided in the BentoML eco-system. It captures your service code, models, and
configurations in one place, version control it automatically, and ensures reproducibility across
yoru development and production environments.

```bash
> bentoml build

██████╗ ███████╗███╗   ██╗████████╗ ██████╗ ███╗   ███╗██╗
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║██║
██████╔╝█████╗  ██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║██║
██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║██║
██████╔╝███████╗██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗
╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝

Successfully built Bento(tag="sentence-embedding-svc:scyvqxrxlc4rduqj").

Possible next steps:

 * Containerize your Bento with `bentoml containerize`:
    $ bentoml containerize sentence-embedding-svc:scyvqxrxlc4rduqj  [or bentoml build --containerize]

 * Push to BentoCloud with `bentoml push`:
    $ bentoml push sentence-embedding-svc:scyvqxrxlc4rduqj [or bentoml build --push]
```

# Production Deployment

BentoML provides a number of [deployment options](https://docs.bentoml.com/en/latest/concepts/deploy.html).
The easiest way to set up a production-ready endpoint of your text embedding service is via BentoCloud,
the serverless cloud platform built for BentoML, by the BentoML team.

Next steps:

1. Sign up for a BentoCloud account [here](https://www.bentoml.com/).
2. Get an API Token, see instructions [here](https://docs.bentoml.com/en/latest/bentocloud/getting-started/ship.html#acquiring-an-api-token).
3. Push your Bento to BentoCloud: `bentoml push sentence-embedding-svc:latest`
4. Deploy via Web UI, see [Deploying on BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/getting-started/ship.html#deploying-your-bento)


# Customization

Looking to use a different embedding model? Check out the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)
and decide which embedding model works best for your use case. Modify code in the
`import_model.py`, `embedding_runnable.py`, and `service.py` file to replace the model used.
See [BentoML docs](https://docs.bentoml.org/) for advanced topics such as
performance optimization, runtime configurations, serving with GPU, and adaptive
batching.

# Community

👉 Join our [AI Application Developer community!](https://l.bentoml.com/join-slack)

