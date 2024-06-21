''' Deployed on localhost:5000.
'''
from flask import request, render_template, Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/emotionDetector")
def sent_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion_detector over it using emotion_detector()
        function. The output returned shows the emotion socres and
        dominant emotion.
    '''
    text = request.args.get('textToAnalyze')
    emo = emotion_detector(text)
    if emo['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    # server.py:19:0: C0301: Line too long (143/100) (line-too-long)
    # response = "For the given statement, the system response is " + ", ".join(f"'{k}': {v}" for k, v in emo.items() if k != "dominant_emotion")
    # response += f". The dominant emotion is {emo['dominant_emotion']}."
    response_parts = [
        "For the given statement, the system response is ",
        ", ".join(f"'{k}': {v}" for k, v in emo.items() if k != "dominant_emotion"),
        f". The dominant emotion is {emo['dominant_emotion']}."
    ]
    response = "".join(response_parts)
    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
