import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyze } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)  

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    formatted_response = json.loads(response.text)

    try:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
    except (KeyError, IndexError, TypeError):
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
    result = {
        "anger": emotions.get('anger', 0.0),
        "disgust": emotions.get('disgust', 0.0),
        "fear": emotions.get('fear', 0.0),
        "joy": emotions.get('joy', 0.0),
        "sadness": emotions.get('sadness', 0.0),
    }
    result["dominant_emotion"] = max(result, key=result.get)
    return result
    
        