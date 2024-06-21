'''
This module defines a function to analyze emotion using Watson's
EmotionPredict analysis service.
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' This code receives the text to analysis
    '''
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    my_object = { "raw_document": { "text": text_to_analyze } }
   
    # print(result)
    try:
        resp = requests.post(url, json = my_object, headers = header, timeout=10)
        formatted_response = json.loads(resp.text)
        if 200 == resp.status_code:
            result = formatted_response['emotionPredictions'][0]['emotion']
            result['dominant_emotion'] =  max(result, key=result.get)
            return result
        elif 400 == resp.status_code:
            return  { "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, 'dominant_emotion': None }
    except requests.exceptions.Timeout:
        return "The request timed out"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"