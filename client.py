if __name__ == "__main__":
    from bentoml.client import Client
    client = Client.from_url("http://localhost:3000")

    samples = [
        "The dinner was great!",
        "The weather is great today!",
        "I love fried chiclken sandwich!"
    ]
    print(client.encode(samples))
