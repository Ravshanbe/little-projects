from pytube import YouTube

link = input("Input url address of video: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("Enter quality of video")
dn_option = int(input('Enter option'))
dn_video = videos[dn_option]
dn_video.download()
print("Downloaded successfully")