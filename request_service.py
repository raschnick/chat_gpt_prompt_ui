import requests
import json
import os

from nltk.sentiment.vader import SentimentIntensityAnalyzer

url = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.environ["OPENAI_API_KEY"]}',
}

analyzer = SentimentIntensityAnalyzer()


def generate_response(message, role, response_length):
    data = {
        'messages': [{'role': f'{role}', 'content': f'{message}'}],
        'model': 'gpt-3.5-turbo',
        'temperature': 0.5,
        'max_tokens': response_length,
        'n': 1,
        'stop': None,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    return response_json['choices'][0]['message']['content'].strip()


def get_sentiment_gpt(answer, role, response_length):
    sentiment_question = 'Do a sentiment analysis for the following text:' + answer
    return generate_response(sentiment_question, role, response_length)


def get_sentiment_vader(answer):
    scores = analyzer.polarity_scores(answer)

    if scores['compound'] >= 0.05:
        sentiment = "Sentiment: Positive"
    elif scores['compound'] <= -0.05:
        sentiment = "Sentiment: Negative"
    else:
        sentiment = "Sentiment: Neutral"

    return sentiment
