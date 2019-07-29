#!/usr/bin/env python3

import youtube_dl
import re
#ydl_opts = {
#    'simulate'
#}
#
#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    ydl.download(['https://www.youtube.com/playlist?list=UUzQUP1qoWDoEbmsQxvdjxgQ&playnext=1&index=1'])

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/playlist?list=PLk1Sqn_f33KuS7ZSVMJqzFaqOyyl-esmG',
        download=False # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

titles=[]
for t in range(len(result['entries'])):
    titles.append(result['entries'][t]['title'])
print(titles)

p=re.compile(r'^.*?- (?P<name>.*)$')
for title in titles:
    print(p.search(title).group('name'))
