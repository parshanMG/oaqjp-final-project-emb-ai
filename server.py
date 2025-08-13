"""Flask web app for detecting emotions in text."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as detect_emotion

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze emotions for given text via the emotion_detector function."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = detect_emotion(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
