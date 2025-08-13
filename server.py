from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(emotion_detector)

app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "No text provided for emotion detection.", 400
    
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Error in emotion detection. Please try again.", 500
    
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    