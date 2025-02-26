# T-Mobile Sentimental Analysis API

This project performs tweet collection and sentiment analysis specifically for tweets related to T-Mobile and the Super Bowl. It consists of two primary components:

1. **Tweet Retrieval** – Uses the Twitter API via Tweepy to retrieve tweets with specific keywords and saves them in CSV format inside a `Temp` folder.
2. **Sentiment Analysis** – Uses NLTKs VADER to evaluate and categorize the sentiment of the collected tweets and outputs the results.

## Folder Structure

```
.
├── Main
│   ├── RetrieveTweets_To_CSV.py
│   ├── Sentimenta_Analysis_Method_1.py
│   └── Sentimenta_Analysis_Method_2.py
├── convert_txt_to_csv.py
└── twitter.txt
```


## Requirements

- Python 3.10+
- Tweepy
- Pandas
- NLTK

> **Note:** The sentiment analysis script downloads NLTK’s VADER lexicon during its first run.

## Setup

1. **Set Environment Variables:**  
   Set your Twitter API Bearer Token as an environment variable named `TWITTER_BEARER_TOKEN`.

2. **Install Dependencies:**  
   Install the required Python packages using pip from `requirements.txt`

3. **Temp Folder Creation:**
    The scripts will automatically create the Temp folder if it does not already exist.

## Sample

> **Note:** `The twitter.txt` file is a sample file that contains the Tweets and that can be converted to CSV format with `convert_txt_to_csv.py`, then can be used as input for the sentiment analysis scripts( `_2` is Recommended).
