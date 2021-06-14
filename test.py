import youtube_dl

url = 'https://www.youtube.com/watch?v=QSH2PkL61sg'

opts =  {
   'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192'
   }],
   'ffmpeg_location': 'ffmpeg-4.2.1/ffmpeg',
      'youtube_include_dash_manifest': 'False'
}

with youtube_dl.YoutubeDL(opts) as ytdl:
   ytdl.download([url])