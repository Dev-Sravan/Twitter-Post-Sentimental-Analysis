# Twitter API Setup Guide

## Step 1: Sign Up for a Twitter Developer Account

1. Visit the Twitter Developer Portal
2. Click "Apply for access"
3. Log in with your Twitter/X account
4. Select access tier:
   - Basic (Free)
   - Elevated (Recommended for full access)
   - Academic
5. Complete application:
   - Describe your usage plans (sentiment analysis, research)
   - Accept terms
   - Submit application

## Step 2: Create a Twitter App

1. Access Twitter Developer Dashboard
2. Create Project:
   - Click "Create Project"
   - Name it "TMobile Sentiment Analysis"
3. Create App:
   - App Name: "SuperBowlNetworkAnalysis"
   - Add description
   - Website URL (e.g., https://yourproject.com)
   - Callback URL (optional)
   - Set Permissions to "Read-Only"
4. Generate Keys

## Step 3: Get Your API Keys

Navigate to: Dashboard → App → Keys & Tokens

Collect the following credentials:
- API Key
- API Secret Key
- Bearer Token (required for Tweepy)

> Note: Store these credentials securely and never commit them to version control.
