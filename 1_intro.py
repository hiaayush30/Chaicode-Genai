# tokenization

import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

# Vocab size => how many unique tokens to acommodate all the languages
# example for english it can be 53 (26 upper, 26 lower and 1 space)

print("Vocab size:",encoder.n_vocab) # possible unique tokens in the gpt-4o encoder
# every model has its own vocab size

text = "The cat sat on the mat"
tokens = encoder.encode(text)

print("Tokens:",tokens)

decoded = encoder.decode(tokens)
print("Decoded:",decoded) 

# vector embeddings of these tokens are generated
# vector embeddings bring about the symantic meaning (how they are related) behind these tokens    
# In practice embeddings are high-dimensional vectors — often with hundreds or thousands of dimensions.
# go to 2_embedding.py