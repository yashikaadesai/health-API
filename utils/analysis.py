from textblob import TextBlob
import numpy as np

blob = TextBlob("This is a great project!")
print(blob.sentiment)