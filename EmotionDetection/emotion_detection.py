"""
Emotion Detection Module with error handling.
"""

import requests
import json


def emotion_detector(text_to_analyze):

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    # ✅ Handle blank input / API error
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Convert response text to dictionary
    response_dict = json.loads(response.text)

    # Extract emotion scores
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    anger = emotions.get("anger")
    disgust = emotions.get("disgust")
    fear = emotions.get("fear")
    joy = emotions.get("joy")
    sadness = emotions.get("sadness")

    # Determine dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }
