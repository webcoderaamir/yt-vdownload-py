from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        print("Download is completed successfully")
    except Exception as e:
        print("An error has occurred:", e)

link = input("Enter the YouTube video URL: ")
Download(link)
