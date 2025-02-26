import tweepy
import os
import pandas as pd
from datetime import datetime, timedelta

# Configuration
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
MAX_RESULTS = 1 # Adjust this variable for number of tweets
KEYWORDS = ["T-Mobile", "Super-Bowl"]

class TweetFetcher:
    def __init__(self, bearer_token):
        self.client = tweepy.Client(
            bearer_token=bearer_token,
            wait_on_rate_limit=True
        )

    def build_query(self, keywords):
        """Constructs an optimized search query with keyword combinations"""
        base_operators = ["lang:en -is:retweet -is:reply"]
        keyword_group = " OR ".join([f'"{k}"' for k in keywords])
        end_query=f"({keyword_group}) {' '.join(base_operators)}"
        print("End_Query:", end_query)
        return end_query

    def fetch_tweets(self, query, max_results=10):
        """Retrieves tweets with pagination handling"""
        tweets = []
        next_token = None
        
        while len(tweets) < max_results:
            try:
                response = self.client.search_recent_tweets(
                    query=query,
                    max_results=min(100, max_results - len(tweets)),
                    tweet_fields=['created_at', 'public_metrics', 'entities'],
                    user_fields=['username', 'name', 'verified'],
                    expansions='author_id',
                    next_token=next_token
                )
                
                if not response.data:
                    break
                    
                users = {u.id: u for u in response.includes.get('users', [])}
                
                for tweet in response.data:
                    user = users.get(tweet.author_id, None)
                    tweets.append({
                        'TwitterID': f"@{user.username}" if user else 'None',
                        'Content': tweet.text,
                        'Hashtag': ', '.join(
                            [tag['tag'] for tag in (tweet.entities or {}).get('hashtags', [])]
                        ) or 'None',
                        'Date': tweet.created_at.strftime('%Y-%m-%d') if tweet.created_at else 'None',
                        'Time': tweet.created_at.strftime('%H:%M:%S') if tweet.created_at else 'None',
                        'Verified': user.verified if user else 'None'
                    })

                next_token = response.meta.get('next_token')
                if not next_token:
                    break
                    
            except tweepy.TweepyException as e:
                print(f"API Error: {e}")
                break
                
        return tweets[:max_results]


    def save_to_csv(self, tweets, filename="Temp/Twitter_Real_Time_Tweets.csv"):
        """Saves tweets to CSV with proper formatting"""

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        df = pd.DataFrame(tweets)
        # Ensure proper ordering of columns
        df = df[['TwitterID', 'Content', 'Hashtag', 'Date', 'Time', 'Verified']]
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Successfully saved {len(df)} tweets to {filename}")

if __name__ == "__main__":
    fetcher = TweetFetcher(BEARER_TOKEN)
    search_query = fetcher.build_query(KEYWORDS)
    results = fetcher.fetch_tweets(search_query)
    
    if results:
        fetcher.save_to_csv(results)
        print("\nSample Output:")
        print(pd.read_csv("Temp/Twitter_Real_Time_Tweets.csv").head(3))
    else:
        print("No tweets found matching criteria")
