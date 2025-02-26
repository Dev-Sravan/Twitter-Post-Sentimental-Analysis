# T-Mobile Sentiment Analysis Web Interface

A modern web interface for analyzing and visualizing sentiment in T-Mobile related tweets, built with Flask and Chart.js

## Features

- Clean, modern UI with gradient background design
- Real-time CSV file upload and preview
- Interactive pie chart visualization of sentiment distribution
- Tweet preview with masked handles for privacy
- Responsive design that works across devices

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualization**: Chart.js
- **Styling**: Custom CSS with modern gradients and animations

## Project Structure

```
.
├── app.py
├── processed
│   └── results.csv
├── static
│   ├── script.js
│   └── styles.css
└── templates
    └── index.html
```

## Key Components
**Backend (app.py)**
- Flask server handling file uploads
- NLTK-based sentiment analysis
- Data processing with pandas
- JSON API endpoints for frontend communication
  
**Frontend (index.html)**
- File upload interface
- Tweet preview section
- Sentiment distribution chart
- Clean, intuitive layout
  
**Styling (styles.css)**
- Modern gradient background
- Responsive containers
- Custom animations
- Professional color scheme
  
**Interactivity (script.js)**
- Real-time file preview
- Chart.js integration
- Dynamic data updates
- Loading animations
  
## Features in Detail
1. File Upload

    - Supports CSV files
    - Instant preview of uploaded tweets
    - Handle masking for privacy

2. Sentiment Analysis

    - Real-time processing
    - Three-way classification (Positive, Negative, Neutral)
    - Compound score calculation

3. Visualization

    - Interactive pie chart
    - Color-coded sentiment categories
    - Responsive chart sizing

4. User Experience

    - Loading indicators
    - Error handling
    - Smooth animations
    - Intuitive layout

## Usage
1. Click "Choose File" to select your CSV file
2. Preview the tweets in the preview section
3. Click "Analyze Sentiment" to process
4. View the sentiment distribution in the pie chart