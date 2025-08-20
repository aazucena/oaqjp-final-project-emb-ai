"""
This server listens for GET requests on the /emotionDetector endpoint, extracts
the text from the request, executes the sentiment analysis on the text and
returns the result as a string.

The sentiment analysis is executed by the emotion_detector() function in the
EmotionDetection module. The function takes a string as an argument and
returns a dictionary with the scores for the different emotions and the
dominant emotion.

The returned string is a simple text that describes the emotions detected in
the text and the dominant emotion.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Renders the index page.

    Returns:
        The rendered index page.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def sentiment_analyzer():
    """This function takes a text as an argument and analyzes it to identify the
    emotions expressed in the text. It returns a string that describes the
    emotions detected in the text and the dominant emotion.

    Parameters:
    text (string): The text to be analyzed.

    Returns:
    string: A string that describes the emotions detected in the text and
    the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        result = "Invalid text! Please try again!.<br>"
    else:
        result = (
            f'For the given statement, the system response is '
            f'"anger": {anger}, "disgust": {disgust}, "fear": {fear}, "joy": {joy} and '
            f'"sadness": {sadness}. The dominant emotion is {dominant_emotion}.'
        )
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
