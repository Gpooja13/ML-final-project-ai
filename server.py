from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text = request.json.get('text', '')
    if text:
        result = emotion_detector(text)

        # Format the output message
        response_message = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify(result=result, message=response_message)
    else:
        return jsonify(error="No text provided"), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
