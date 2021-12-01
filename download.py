from TikTokApi import TikTokApi
import pprint
import sys

api = TikTokApi.get_instance()

device_id = api.generate_device_id()

if (len(sys.argv) > 1):
    count = sys.argv[1]
    search = sys.argv[2]
else:
    count = 6
    search = 'domesticabuseawareness'

tiktoks = api.by_hashtag(hashtag=search, count=count)

video_bytes = api.get_video_by_tiktok(tiktoks[0], custom_device_id=device_id)

pprint.pp(tiktoks[0])

with open("video.mp4", "wb") as out:
    out.write(video_bytes)


