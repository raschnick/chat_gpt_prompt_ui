import requests
import json
import os

url = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.environ["OPENAI_API_KEY"]}',
}


def generate_response(message, role):
    data = {
        'messages': [{'role': f'{role}', 'content': f'{message}'}],
        'model': 'gpt-3.5-turbo',
        'temperature': 0.5,
        'max_tokens': 500,
        'n': 1,
        'stop': None,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    return response_json['choices'][0]['message']['content'].strip()


def get_sentiment(answer, role):
    sentiment_question = 'Do a sentiment analysis for the following text:' + answer
    return generate_response(sentiment_question, role)
