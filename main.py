
# import subprocess

# n = input()
# while
# subprocess.run('ffmpeg -i rickroll.mp4 nic.mp3', shell = True)

# # with stuff open
    # write original starting HTML CODE

    # define TitleVideo/TitleAudio
    # write new starting HTML CODE

    # yt.streams.get_highest_resolution().download()
    # subprocess.run('ffmpeg -i' + "\""+titleV + "\"" + " " + "\"" + titleA + "\"", shell=True)

    # file.write("<td><a href=" + "\"" + u + "\">" + title")
               
    # add ending string for <tr>
    # use import os, os.listdir instead to get correct file names
    # alkfjnalkfnalkf
    # alskdnaskld
    

def Youtube_program (x):
    p=Playlist(str(x))
    y=YouTube(str(x))
    titles=y.title
    lengthseconds=y.length
    vid=y.streams.get_highest_resolution().download()

    print(titles)
    print(lengthseconds)
    open(vid)

    links= open("link.html", "w").write(str(y))
import subprocess
subprocess.run('ffmpeg -i interstellar.mp4 audio.mp3', shell=True)
