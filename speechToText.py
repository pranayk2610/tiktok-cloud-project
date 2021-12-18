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
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "SampleAudio/TikTokSample16-2.wav")
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
    with open('Transcripts/sphinx/VideoTransciptSphinx16-2.txt', 'w') as f:
        sys.stdout = f 
        print(r.recognize_sphinx(audio))
        sys.stdout = original_stdout 
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# print('\n')

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    with open('Transcripts/googlespeech/VideoTransciptGoogleSpeech16-2.txt', 'w') as f:
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
}"""
try:
    with open('Transcripts/Video30/VideoTransciptGCloudSpeech30.txt', 'w') as f:
        sys.stdout = f 
        print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
        sys.stdout = original_stdout 
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
# # # recognize speech using Wit.ai
# # WIT_AI_KEY = "DLN5VNNDCK2KBY2Q4JX2NMSQ4DVUF3AB"  # Wit.ai keys are 32-character uppercase alphanumeric strings
# # try:
# #     with open('Transcripts/VideoTranscriptWitAI1.txt', 'w') as f:
# #         sys.stdout = f 
# #         print(r.recognize_wit(audio, key=WIT_AI_KEY))
# #         sys.stdout = original_stdout 
# # except sr.UnknownValueError:
# #     print("Wit.ai could not understand audio")
# # except sr.RequestError as e:
# #     print("Could not request results from Wit.ai service; {0}".format(e))

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
HOUNDIFY_CLIENT_ID = ""  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = ""  # Houndify client keys are Base64-encoded strings
try:
     with open('Transcripts/Video30/VideoTranscriptHoundify30.txt', 'w') as f:
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
apikey = ""  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
url = ""  # IBM Speech to Text passwords are mixed-case alphanumeric strings

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url)


with open(AUDIO_FILE, 'rb') as f:
    res = stt.recognize(audio = f, content_type = 'audio/wav', model='en-US_BroadbandModel').get_result()

print(res)

text = res['results'][0]['alternatives'][0]['transcript']

with open('Transcripts/Video30/VideoTranscriptIBM30.txt', 'w') as f:
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
