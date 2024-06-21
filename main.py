from pytube import YouTube

SavePath = "/Users/kemalozyon/Downloads/YoutubeVideosDownloaded"
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=SavePath)
    except Exception as e:
        print(f"An error was occured! {e}")

link = input("Enter the link of the video you want to download: ")
Download(link)
