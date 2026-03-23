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


# """
# Emotion Detection Module

# This module sends a POST request to the Watson NLP Emotion Predict
# API, processes the response, and returns structured emotion scores.
# """

# import requests
# import json


# def emotion_detector(text_to_analyze):
#     """
#     Analyze emotions in the given text using Watson NLP API.

#     Args:
#         text_to_analyze (str): The input text to analyze.

#     Returns:
#         dict: A dictionary containing emotion scores and dominant emotion.
#     """

#     url = (
#         "https://sn-watson-emotion.labs.skills.network/"
#         "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
#     )

#     headers = {
#         "grpc-metadata-mm-model-id":
#         "emotion_aggregated-workflow_lang_en_stock",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "raw_document": {
#             "text": text_to_analyze
#         }
#     }

#     response = requests.post(url, headers=headers, json=payload)

#     # Convert response text to dictionary
#     response_dict = json.loads(response.text)

#     # Extract emotion scores
#     emotions = response_dict["emotionPredictions"][0]["emotion"]

#     anger = emotions.get("anger", 0)
#     disgust = emotions.get("disgust", 0)
#     fear = emotions.get("fear", 0)
#     joy = emotions.get("joy", 0)
#     sadness = emotions.get("sadness", 0)

#     # Determine dominant emotion
#     emotion_scores = {
#         "anger": anger,
#         "disgust": disgust,
#         "fear": fear,
#         "joy": joy,
#         "sadness": sadness
#     }

#     dominant_emotion = max(emotion_scores, key=emotion_scores.get)

#     # Return formatted output
#     return {
#         "anger": anger,
#         "disgust": disgust,
#         "fear": fear,
#         "joy": joy,
#         "sadness": sadness,
#         "dominant_emotion": dominant_emotion
#     }



# # """
# # Emotion Detection Module

# # This module sends a POST request to the Watson NLP Emotion Predict
# # API and returns the response text.
# # """

# # import requests


# # def emotion_detector(text_to_analyze):
# #     """
# #     Analyze emotions in the given text using Watson NLP API.

# #     Args:
# #         text_to_analyze (str): The input text to analyze.

# #     Returns:
# #         dict or str: The response text from the API.
# #     """

# #     url = (
# #         "https://sn-watson-emotion.labs.skills.network/"
# #         "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
# #     )

# #     headers = {
# #         "grpc-metadata-mm-model-id":
# #         "emotion_aggregated-workflow_lang_en_stock",
# #         "Content-Type": "application/json"
# #     }

# #     payload = {
# #         "raw_document": {
# #             "text": text_to_analyze
# #         }
# #     }

# #     response = requests.post(url, headers=headers, json=payload)

# #     # Return the text attribute of the response object
# #     return response.text

# # # import requests 
# # # import json

# # # def emotion_detector(text_to_analyze): 
# # #     # Define the URL for the sentiment analysis API 
# # #     url = (
# # #         "https://sn-watson-emotion.labs.skills.network/"
# # #         "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
# # #     )

# # #     # Create the payload with the text to be analyzed 
# # #     myobj = {
# # #         "raw_document": {
# # #             "text": text_to_analyze
# # #         }
# # #     }

# # #     # Set the headers with the required model ID for the API 
# # #     header = {
# # #         "grpc-metadata-mm-model-id":
# # #         "emotion_aggregated-workflow_lang_en_stock",
# # #         "Content-Type": "application/json"
# # #     }


# # #     # Make a POST request to the API with the payload and headers 
# # #     response = requests.post(url, json=myobj, headers=header)

# # #     return response.text

# # #     # # Parse the response from the API 
# # #     # formatted_response = json.loads(response.text)

# # #     # # If the response status code is 200, extract the label and score from the response 
# # #     # if response.status_code == 200: 
# # #     #     label = formatted_response['documentSentiment']['label'] 
# # #     #     score = formatted_response['documentSentiment']['score'] 
# # #     # # If the response status code is 500, set label and score to None 
# # #     # elif response.status_code == 500: 
# # #     #     label = None 
# # #     #     score = None

# # #     # Return the label and score in a dictionary 
# # #     # return {'label': label, 'score': score}