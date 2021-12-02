from difflib import SequenceMatcher
import jellyfish




text1 = open("Transcripts/Video1/VideoTransciptGCloudSpeech1.txt").read()
text2 = open("Transcripts/Video1/VideoTranscriptReal1.txt").read()
print(jellyfish.jaro_distance(text1, text2))

m = SequenceMatcher(None, text1.lower(), text2.lower())

print(m.ratio())
print("\n")

text3 = open("Transcripts/Video1/VideoTranscriptHoundify1.txt").read()
text4 = open("Transcripts/Video1/VideoTranscriptReal1.txt").read()
n = SequenceMatcher(None, text3, text4)

print(n.ratio())
print("\n")

text5 = open("Transcripts/Video1/VideoTranscriptIBM1.txt").read()
text6 = open("Transcripts/Video1/VideoTranscriptReal1.txt").read()
o = SequenceMatcher(None, text5, text6)

print(o.ratio())
print("\n")