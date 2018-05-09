import pytube
import os
import subprocess   #터미널 실행 하기 위해서

yt = pytube.YouTube("https://www.youtube.com/watch?v=wowAOdTYqw8") #다운받을 url 지정
#yt = pytube.YouTube("https://www.youtube.com/watch?v=CTRO5NXmAp8") #다운받을 url 지정

videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) : #range(1, 6) 1 이상 6미만 1,2,3,4,5
    print(i, " , ", videos[i])

cNum = int(input("다운 받을 화질은?(0~19)"))


down_dir = "E:/acuyo/python/inflearn/resource/download"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName)
])

print("동영상 파일 다운로드 완료/ 컴버팅")
