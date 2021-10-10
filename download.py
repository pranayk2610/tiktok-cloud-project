import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.tiktok.com/@yulieigaming/video/6765653289909456133?lang=en&is_copy_url=1&is_from_webapp=v1'])