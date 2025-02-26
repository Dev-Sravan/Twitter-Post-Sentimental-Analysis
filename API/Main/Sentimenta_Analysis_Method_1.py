import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime
import os
# Download VADER lexicon (first-time only)
nltk.download('vader_lexicon')

class TweetSentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        
    def _get_sentiment(self, text):
        """Get compound sentiment score using VADER"""
        scores = self.analyzer.polarity_scores(text)
        return {
            'Negative': scores['neg'],
            'Neutral': scores['neu'],
            'Positive': scores['pos'],
            'Compound': scores['compound'],
            'Sentiment': self._categorize_sentiment(scores['compound'])
        }
    
    def _categorize_sentiment(self, compound_score):
        """Categorize based on VADER's recommended thresholds"""
        if compound_score >= 0.05:
            return 'Positive'
        elif compound_score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def analyze_csv(self, input_file, output_file):
        """Analyze tweets and save with sentiment scores"""
        df = pd.read_csv(input_file)
        
        # Apply sentiment analysis
        sentiment_data = df['Content'].apply(self._get_sentiment).apply(pd.Series)
        df = pd.concat([df, sentiment_data], axis=1)
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_file}_{timestamp}.csv"
        df.to_csv(filename, index=False, na_rep='None')
        return df

# Usage
if __name__ == "__main__":
    analyzer = TweetSentimentAnalyzer()
    os.makedirs("Assests", exist_ok=True)
    # Analyze your collected tweets
    results = analyzer.analyze_csv(
        input_file='Temp/Twitter_Real_Time_Tweets.csv',
        output_file='Assests/T-Twitter_Real_Time_Tweets_Sentiment_Analysis'
    )
    
    # Display summary
    if not results.empty:
        print(f"Sentiment Distribution:\n{results['Sentiment'].value_counts()}")
        print("\nSample Analysis:")
        print(results[['Content', 'Sentiment', 'Compound']].head(3))
