# Serving SentenceEmbedding Model with BentoML

This is a sentence embedding service built with BentoML. It is meant to be hackable and educational
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

Open http://0.0.0.0:3000 from your browser to send test requests from the Web UI.

Alternatively, run the API client with `python client.py`


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

Successfully built Bento(tag="sentence-transformer-svc:scyvqxrxlc4rduqj").

Possible next steps:

 * Containerize your Bento with `bentoml containerize`:
    $ bentoml containerize sentence-transformer-svc:scyvqxrxlc4rduqj  [or bentoml build --containerize]

 * Push to BentoCloud with `bentoml push`:
    $ bentoml push sentence-transformer-svc:scyvqxrxlc4rduqj [or bentoml build --push]
```

## Deployment

BentoML provides a number of [deployment options](https://docs.bentoml.com/en/latest/concepts/deploy.html).
Here we demonstrate the easiest way to set up a production-ready BentoML deployment via BentoCloud.

1. Sign up for a BentoCloud account [here](https://www.bentoml.com/).
2. Get an API Token, see instructions [here](https://docs.bentoml.com/en/latest/bentocloud/getting-started/ship.html#acquiring-an-api-token).
3. Push your Bento to BentoCloud: `bentoml push sentence-transformer-svc:latest`
4. Deploy via Web UI, see [Deploying on BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/getting-started/ship.html#deploying-your-bento)
