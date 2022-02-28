import os
import shutil
from pytube import YouTube

print("cabanchik-py inspired by https://github.com/Cactus-0/cabanchik")
print('loading кабанчик...')
try:
    YouTube('https://youtu.be/lxWkk1bvOPE').streams.get_highest_resolution().download(filename='source.mp4')
except:
    print('loading failed')
    input('press enter to exit...')
    raise
print('кабанчик loaded, writing files')

for dir in [x[0] for x in os.walk(os.getcwd())]:
    print('writing кабанчик into ' + dir)
    try:
        shutil.copy('source.mp4', dir + '/кабанчик.mp4')
    except:
        print('failed. skipped.')
os.remove('source.mp4')

print('done')
input('press enter to exit...')
