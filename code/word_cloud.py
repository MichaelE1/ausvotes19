import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
import numpy as np
from PIL import Image

f = open("tweets.txt", "r")
raw = f.read()
f.close()

stopwords = set(STOPWORDS)
stopwords.add("RT")
stopwords.add("ausvotes")
stopwords.add("https")
stopwords.add("co")
stopwords.add("auspol")

img = Image.open("australia.png")
mask = np.array(img)

wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords).generate(raw)
plt.figure(figsize=(20, 10), facecolor="k")
plt.imshow(wc)
plt.axis("off")
plt.show()
