from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import os
# Load data with explicit handling for Hashtag column
df = pd.read_csv("Temp/sample_twitter_data.csv", dtype={'Hashtag': 'str'})

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Compute Sentiment Scores
df["Sentiment_Score"] = df["Content"].apply(
    lambda x: analyzer.polarity_scores(str(x))["compound"]
)

# Categorize Sentiment
df["Sentiment_Label"] = df["Sentiment_Score"].apply(
    lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral")
)

# Save results while preserving 'None' values
# df.to_csv("tmobile_sentiment_results.csv", index=False, na_rep='None')
os.makedirs("Assests", exist_ok=True)
df.to_csv("Assests/sample_twitter_data_Results.csv", index=False, na_rep='None')
print("Sentiment analysis complete. Results saved to tmobile_sentiment_results.csv")



