"""
Flask server for Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Returns:
        str: Formatted response string or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    response = (
        "For the given statement, the system response is "
        f"'anger': {result.get('anger')}, "
        f"'disgust': {result.get('disgust')}, "
        f"'fear': {result.get('fear')}, "
        f"'joy': {result.get('joy')} and "
        f"'sadness': {result.get('sadness')}. "
        f"The dominant emotion is {result.get('dominant_emotion')}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
