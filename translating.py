import requests
from docx import document
import os

subscription_key = 'apikey'
endpoint = 'https://api.cognitive.microsofttranslator.com'
location = 'eastus'
language_destination = 'pt-br'

def translatorDocument(text, target_language):
  path  = '/translate'
  constructed_url = endpoint + path
  headers = {
      'Ocp-Apim-Subscription-Key': subscription_key,
      'Ocp-Apim-Subscription-Region': location,
      'Content-type': 'application/json',
      'X-ClientTraceId' : str(os.urandom(16))
  }

  body = [{
      'text': text
  }]

  params = {
      'api-version': '3.0',
      'from': 'en',
      'to': target_language
  }
  request = requests.post(constructed_url, params=params, headers=headers, json=body)
  response = request.json()
  return response[0]["translations"][0]["text"]

