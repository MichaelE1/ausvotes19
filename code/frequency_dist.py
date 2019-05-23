import nltk

f = open("tweets.txt", "r")
raw = f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
f.close()

fdist = nltk.FreqDist(text)
stopwords = set(nltk.corpus.stopwords.words("english"))
stopwords.add("RT")
stopwords.add("ausvotes")
stopwords.add("https")
stopwords.add("co")
stopwords.add("auspol")
stopwords.add("I")

fdist_no_stopwords = nltk.FreqDist(dict((word, freq)
                                        for word, freq in fdist.items() if word not in stopwords and word.isalpha()))
fdist_no_stopwords.plot(50, title="50 most common words (no stop words)")
