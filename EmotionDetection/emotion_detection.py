import requests
import json

def emotion_detector(text_to_analyze):
    # Check if input text is blank or contains only spaces
    if not text_to_analyze or not text_to_analyze.strip():  # Fix here: check if it's empty or just spaces
        return None

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make a POST request to Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)

    # Handle API error (status code 400)
    if response.status_code == 400:
        return None  # Return None for API error

    # Parse the response data
    emotion_data = response.json()
    emotions = emotion_data['emotionPredictions'][0]['emotion']

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return dominant_emotion  # Only return the dominant emotion
