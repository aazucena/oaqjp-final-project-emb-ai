from requests import post
import operator

def emotion_detector(text_to_analyse):
  print(f'Analyzing text: "{text_to_analyse}"')
  url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
  json = { "raw_document": { "text": text_to_analyse } }
  headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  response = post(url, json=json, headers=headers)


  data = response.json()

  print(data)
  predictions = data['emotionPredictions']
  emotion = predictions[0]['emotion']
  anger_score = emotion['anger'] or 0
  disgust_score = emotion['disgust'] or 0
  fear_score = emotion['fear'] or 0
  joy_score = emotion['joy'] or 0
  sadness_score = emotion['sadness'] or 0
  dominant_emotion = max(emotion.items(), key=operator.itemgetter(1))[0] or 'unknown'
  
  if response.status_code == 400:
    anger_score = None
    disgust_score = None
    fear_score = None
    joy_score = None
    sadness_score = None
    dominant_emotion = None
    
  result = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
  }
  print(result)

  return result
