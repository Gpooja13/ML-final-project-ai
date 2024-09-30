# from flask import Flask, render_template, request, jsonify
# from EmotionDetection.emotion_detection import emotion_detector

# app = Flask(__name__)

# @app.route("/emotionDetector")
# def sent_detector():
#     text_to_analyze = request.args.get('textToAnalyze')
#     dominant_emotion = emotion_detector(text_to_analyze)

#     if dominant_emotion is None:
#         return "Invalid text! Please try again."
#     else:
#         return "The given text has been identified as {}.".format(dominant_emotion)

# @app.route("/")
# def render_index_page():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5005)


"""
Server for emotion detection application.
Provides endpoints to analyze text emotion and render the homepage.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotions in the input text.
    
    Returns:
        str: The dominant emotion or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    dominant_emotion = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None, which indicates invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again.", 400

    # Otherwise, return the detected emotion
    return "The given text has been identified as {}.".format(dominant_emotion)


@app.route("/")
def render_index_page():
    """
    Endpoint to render the home page.
    
    Returns:
        str: Rendered HTML page for the index.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
