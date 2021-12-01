#!/usr/bin/env python3

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import speech_recognition as sr
import sys

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "SampleAudio/TikTokSample15.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

original_stdout = sys.stdout  
# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

r.adjust_for_ambient_noise = 50
print('\n')

# recognize speech using Sphinx
try:
    with open('Transcripts/sphinx/VideoTransciptSphinx15.txt', 'w') as f:
        sys.stdout = f 
        print(r.recognize_sphinx(audio))
        sys.stdout = original_stdout 
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

print('\n')

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    with open('Transcripts/googlespeech/VideoTransciptGoogleSpeech15.txt', 'w') as f:
        sys.stdout = f 
        print(r.recognize_google(audio))
        sys.stdout = original_stdout 
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print(r.recognize_google(audio))
print('\n')
# # recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "central-hangar-333703",
  "private_key_id": "e8f2e45a260fce1015c2a73b251339d18aa1532b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1fbDXn87hJ9mQ\ntQrHSj9Y9HNo6vcRjNm/jOtUoaoDTPSBC43sRIb1mGYqkQ3Ts3k5CPIAOwWJ+Ybh\nQylPcR3JCM/K+oLnL9yAZ8vbIbAk/9ql6pe/NiwQjx1T+/lBR/9+nmT2GcymgJaj\nsFa8IAI1/9V5+nwn7q4ejAHISHd3lmy6Dj7GzTo5Kn1nSdhMAE4A5AE1SGLHhGqI\nngs/DSbDcDjFl8tCDa+6A4YBsTCrl8nHcoe2REqPS53ZPwdhUf2/L4ZLmh4j90/l\nCjMnMCnGpBMIfLspb64P20UrYC9nf/gG8BVvZ3Gg4Ac1t9eccEDo2Gp0xIjesYgX\nvOH92XgVAgMBAAECggEAIYtesSvfX+wuoTllCZqmhLmBz0WGbt76rBXOtTDALKX/\nlw5cp+uuihwl3f47cQJ+CFWn7PT7vBm7nUz9iKpel/ah+WE96p8FAVKt8g2S8fO8\nJOhsLbJEiLb687fhxPgat/tsq7PvCGNB9HU2QsUjw3lKqqXqZrMNyaWU+sCyHA8I\nKRcEFldbr+TohfP/Lf3vUSV9nePcSSm9uB8n5MSR9Hjs5jgtBejdIhTOEF5MXSKY\nqUOFdVMZ7UQXI4Inx0O/6IE1FSHMWhKWBWsPh8xQfNSeR2P+gGSWuhRGgia/7Lv1\nOOWzyDaC5YBjAhhFMvJOPhdrsvCbz2I1PcQAfGmNTQKBgQD1FH8eAStiX5Ew1YI8\nKxnn19LHp/2eGj0whKqZ/2ZKRDpPnOtHyxGI++SZbeaeP/BK6nk8EVWrwbL5xTLz\ngB/gcEaJkwOw6Lqw5BQXvOnbA0uAG8ln4krQnFmPYC0D/HtgS3IVJHZ8VWNFitRO\nSuEYH0NcN1lkITisrMRt4kajZwKBgQC9k92uN2jy8FkQJjzBLV3oOCPeywlVK/Tu\nnHAMzICSYMIxSYlBoSvkkoA5NOlkNjTYn6NehT1sxToJAM8JInKHOmLgpcJrCUFl\nPlrVlx/8MC98iw3d8//rcvpwJauiNC1G9chAtkFO/Rgap2q59xf6mb3Dxq3u6UMU\nBCAzrno3IwKBgD4iByQtObmD7wRJbO4iIzwy7D4v6c12a4Lsb3ABXwZ/C6V5a/DU\nm8p1yfvX7/q4zQvBLCE9Z9HWlrBZ/VPcbLhy3n8sZWgpaINGH43xF/ytdiuxX7tV\nlJAUw2PlBySWkxTTq8WOa/eTkkpkKvT6aNy7uFEduyz2ey7T0izli/ELAoGAF0NP\nzpMKE9WeeDbY+bOBdH9/F1W+3W65bZZQwaFOnae17KpjZ2RJqJC5n0t44E0uiu57\n85tSAEjraDNrNGm/uAxYGcz9YHkQR0Yxi0gyKpYXHadKmlPYsaG4TY6x0wOoEq8S\nVa6HsROpo4urswo5LQ00lhOJQGnrS0d+VBky8hUCgYEA8sBTVqNp55YV4pDu5R9f\n9m8wzi5iGrtZh2PcqjdEWWqW4d1nu/rSHqTCwgVM53x9tUOXMW5UwZdk8Yjp1NQS\nhosNjQldPIYL6S9oMpt1CUTIOLrGvNLK7uTSjtid/dpTbj3UKCl7OReyBvCn6hUZ\n5bzllUK/vROQunrSs+44DDg=\n-----END PRIVATE KEY-----\n",
  "client_email": "tiktokcloud@central-hangar-333703.iam.gserviceaccount.com",
  "client_id": "110193573904094277009",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tiktokcloud%40central-hangar-333703.iam.gserviceaccount.com"
}"""
try:
    with open('Transcripts/Video15/VideoTransciptGCloudSpeech15.txt', 'w') as f:
        sys.stdout = f 
        print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
        sys.stdout = original_stdout 
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
# # recognize speech using Wit.ai
# WIT_AI_KEY = "DLN5VNNDCK2KBY2Q4JX2NMSQ4DVUF3AB"  # Wit.ai keys are 32-character uppercase alphanumeric strings
# try:
#     with open('Transcripts/VideoTranscriptWitAI1.txt', 'w') as f:
#         sys.stdout = f 
#         print(r.recognize_wit(audio, key=WIT_AI_KEY))
#         sys.stdout = original_stdout 
# except sr.UnknownValueError:
#     print("Wit.ai could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Wit.ai service; {0}".format(e))

print('\n')
# # recognize speech using Microsoft Azure Speech
# AZURE_SPEECH_KEY = "34feb73f-62d6-4866-ba11-005dab60a894"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
# except sr.UnknownValueError:
#     print("Microsoft Azure Speech could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

# # recognize speech using Microsoft Bing Voice Recognition
# BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
# except sr.UnknownValueError:
#     print("Microsoft Bing Voice Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# # recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "nt8BIyFxK4j-pBpLd4y9RQ=="  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "Nd9sfmOzaOTys7-bqcV-XD0N73h0hc2ZrC4UfEqBVMF4jaiOEQce7MkWvzkN84x1-0DdkMEwLeQecuVEST0Nww=="  # Houndify client keys are Base64-encoded strings
try:
     with open('Transcripts/Video15/VideoTranscriptHoundify15.txt', 'w') as f:
        sys.stdout = f 
        print(r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
        sys.stdout = original_stdout
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

print(r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
print('\n')

# # recognize speech using IBM Speech to Text
apikey = "q2KvlsrAPFJuEmmso8DUxM400leEmbIfUYnlGeJbpJWP"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
url = "https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/1c3bc4c1-0bb3-4a3f-9bba-804e091749c5"  # IBM Speech to Text passwords are mixed-case alphanumeric strings

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url)


with open(AUDIO_FILE, 'rb') as f:
    res = stt.recognize(audio = f, content_type = 'audio/wav', model='en-US_BroadbandModel').get_result()

print(res)

text = res['results'][0]['alternatives'][0]['transcript']

with open('Transcripts/Video15/VideoTranscriptIBM15.txt', 'w') as f:
    sys.stdout = f 
    print(res)
    sys.stdout = original_stdout

print(text)
print('\n')
# try: 
#     print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
# except sr.UnknownValueError:
#     print("IBM Speech to Text could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from IBM Speech to Text service; {0}".format(e))