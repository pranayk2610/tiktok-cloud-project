from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

text1 = open("Transcripts/Video30/VideoTransciptGCloudSpeech30.txt").read()
text2 = open("Transcripts/Video30/VideoTranscriptHoundify30.txt").read()
text3 = open("Transcripts/Video30/VideoTranscriptIBM30.txt").read()
text4 = open("Transcripts/Video30/VideoTranscriptReal30.txt").read()


analyzer = SentimentIntensityAnalyzer()
vs = analyzer.polarity_scores(text1)
print("\n GCS")
print("{:-<65} {}".format(text1, str(vs)))
print("\n")

vs = analyzer.polarity_scores(text2)
print("\n Houndify")
print("{:-<65} {}".format(text2, str(vs)))
print("\n")

vs = analyzer.polarity_scores(text3)
print("\n IBM")
print("{:-<65} {}".format(text3, str(vs)))
print("\n")

vs = analyzer.polarity_scores(text4)
print("\n Real")
print("{:-<65} {}".format(text4, str(vs)))
print("\n")