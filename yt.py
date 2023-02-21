# from pytube import Playlist, YouTube


# def Youtube_program (x):
#     p=Playlist(str(x))
#     y=YouTube(str(x))
#     titles=y.title
#     lengthseconds=y.length
#     vid=y.streams.get_highest_resolution().download()

#     print(titles)
#     print(lengthseconds)
#     open(vid)

#     links= open("link.html", "w").write(str(y))
import subprocess
subprocess.run('ffmpeg -i interstellar.mp4 audio.mp3', shell=True)


# def beginning ():
#     enter=input("Are you entering a video or a playlist: ")

#     if enter == "video":
#         x=input("Enter your link: ")
#         Youtube_program(x)


#     elif enter == "playlist":
#         print("deal with this later")

#     else:
#         print("""
# Make sure you type 'video' or 'playlist'!
#         """)
#         beginning()

# beginning()
