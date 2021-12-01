from TikTokApi import TikTokApi
import pprint
import sys

api = TikTokApi.get_instance()

device_id = api.generate_device_id()

if (len(sys.argv) > 1):
    count = sys.argv[1]
    search = sys.argv[2]
else:
    count = 3
    search = 'triggerwarning'

tiktoks = api.by_hashtag(hashtag=search, count=count)

for tiktok in tiktoks:
    video_bytes = api.get_video_by_tiktok(tiktok, custom_device_id=device_id)
    with open(f"downloaded_vids/{tiktok['author']['uniqueId']}_{tiktok['id']}.mp4", "wb") as out:
        out.write(video_bytes)
