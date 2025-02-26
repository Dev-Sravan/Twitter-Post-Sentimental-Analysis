from flask import Flask, render_template, request, jsonify
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os
import re

nltk.download('vader_lexicon')

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "csv_file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files["csv_file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read and clean data
        df = pd.read_csv(file)
        df = df.drop(columns=["TwitterID"], errors='ignore')
        
        if "Content" not in df.columns:
            return jsonify({"error": "CSV must contain 'Content' column"}), 400

        # Remove hashtags and mentions
        df["Content"] = df["Content"].apply(
            lambda x: re.sub(r'[#@]\w+', '', str(x))
        )

        # Sentiment analysis
        analyzer = SentimentIntensityAnalyzer()
        df["sentiment"] = df["Content"].apply(
            lambda x: analyzer.polarity_scores(x)["compound"]
        )
        df["sentiment_label"] = df["sentiment"].apply(
            lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral")
        )

        # Save processed data
        processed_path = os.path.join(PROCESSED_FOLDER, "results.csv")
        df.to_csv(processed_path, index=False)
        
        return jsonify({
            "sentiment_counts": df["sentiment_label"].value_counts().to_dict(),
            "sample_tweets": df["Content"].head(5).tolist()
        })
        
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
