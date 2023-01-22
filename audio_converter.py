from pydub import AudioSegment
import os
import time
myPath = r'C:\Users\username\Downloads\Telegram Desktop'

skip = '__MACOSX'
for root, dirs, files in os.walk(myPath):
    if skip in dirs:
        dirs.remove(skip)
    for name in files:
        filepath = root + os.sep + name
        if filepath.endswith(".m4a") or filepath.endswith(".aiff"):
            unconverted = (os.path.join(root, name))
            print("Converting" + unconverted)
            AudioSegment.from_file(unconverted).export(myPath + unconverted, format='mp3')

        else:
            print('.', end="")
            
print('\nNo Covertible Files Found')

