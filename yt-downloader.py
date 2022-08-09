from os import link
from pytube import YouTube
from sys import argv


link=input("Enter the URL of the Video : ")
yt=YouTube(link)

print("\n"+"------------------------------------------")
print("Title: ",yt.title)
print("Channel: ",yt.author)
print("Publish Date: ",yt.publish_date)
print("Views: ",yt.views)
print("Length: ",yt.length//60,"Minutes")
print("\n"+"------------------------------------------")

yd=yt.streams.get_highest_resolution()

yesno=input("Press "+"y"+" to download and "+"n"+" to cancel."+"\n")

if yesno=="y":
    print("Download started in the background, do not close the program.")
    yd.download('/Users/Abhishek/Videos')
    print("Download Completed!")
elif yesno=="n":
    print("Download Terminated.")
else:
    print("Please restart the program.")
