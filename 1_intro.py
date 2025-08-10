# tokenization

import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

# Vocab size => how many unique tokens to acommodate all the languages
# example for english it can be 53 (26 upper, 26 lower and 1 space)

print("Vocab size:",encoder.n_vocab) # possible unique tokens in the gpt-4o encoder
# every model has its own vocab size

text = "The cat sat on the mat"
tokens = encoder.encode(text)

print(tokens)