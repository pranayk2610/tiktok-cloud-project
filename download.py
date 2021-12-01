from TikTokApi import TikTokApi
import sys
import youtube_dl

api = TikTokApi.get_instance()

device_id = api.generate_device_id()

ytdl_opts = {
    'outtmpl': 'downloaded_vids/%(title)s-%(id)s.%(ext)s',
}

if (len(sys.argv) > 1):
    if (sys.argv[1] == '-link'):
        with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
            ydl.download([sys.argv[2]])
        exit()
    else:
        count = int(sys.argv[1])
        search = sys.argv[2]
else:
    count = 3
    search = 'triggerwarning'

tiktoks = api.by_hashtag(hashtag=search, count=count)

for tiktok in tiktoks:
    video_bytes = api.get_video_by_tiktok(tiktok, custom_device_id=device_id)
    with open(f"downloaded_vids/{tiktok['author']['uniqueId']}-{tiktok['id']}.mp4", "wb") as out:
        out.write(video_bytes)
