
import pandas as pd
from textblob import TextBlob

# Sample data
data = {'tweet': [
    'I love this product!',
    'This is the worst experience ever.',
    'Not bad, could be better.',
    'Absolutely fantastic service!',
    'I will never buy this again.'
]}
df = pd.DataFrame(data)

# Sentiment analysis
df['polarity'] = df['tweet'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['sentiment'] = df['polarity'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

print(df)

# Insights
print("\nSentiment counts:")
print(df['sentiment'].value_counts())
