from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

text = "Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall"

response = client.embeddings.create( # will create tokens and then the embedding
    input = text,
    model = "text-embedding-3-small" # the smaller the 3d space , the relationships would be more compact
)

print("Vector Embeddings:",response.data[0].embedding)

# Vector Embeddings: [
#   -0.013826749, 0.012356234, -0.00765323, ... , 0.003412675
# ]

# The output is a 1D array of length 1,536 (because text-embedding-3-small outputs 1,536-dimensional vectors).
# If you run your code, the actual numbers will be different every time for different inputs but deterministic for the same
# text and model — meaning the same input → same embedding.
# go to 2_embedding.md

