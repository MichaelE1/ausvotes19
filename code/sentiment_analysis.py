from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

tweets = [line.rstrip() for line in open("tweets.txt")]
sia = SentimentIntensityAnalyzer()

summary = {"positive": 0, "neutral": 0, "negative": 0}
for x in tweets:
    ps = sia.polarity_scores(x)
    if ps["compound"] == 0.0:
        summary["neutral"] += 1
    elif ps["compound"] > 0.0:
        summary["positive"] += 1
    else:
        summary["negative"] += 1

print(summary)
