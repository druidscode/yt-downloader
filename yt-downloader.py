# Before importing YouTube, first install 'pytube' library using 'pip install pytube'.

from os import link
from pytube import YouTube
from sys import argv

# To take user's input of the video URL in the variable 'link'. 

link=input("Enter the URL of the Video : ")
yt=YouTube(link)

# Before downloading, it's to show user what they're downloading, whether if they have copied the right link or not.

print("\n"+"------------------------------------------")
print("Title: ",yt.title)
print("Channel: ",yt.author)
print("Publish Date: ",yt.publish_date)
print("Views: ",yt.views)
print("Length: ",yt.length//60,"Minutes")
print("\n"+"------------------------------------------")

# This is to get the highest video resolution.

yd=yt.streams.get_highest_resolution()

# IF ELSE based on users decision after seeing the above video information.

yesno=input("Press "+"y"+" to download and "+"n"+" to cancel."+"\n")

if yesno=="y":
    print("Download started in the background, do not close the program.")
    yd.download('/Users/Abhishek/Videos')
    print("Download Completed!")
elif yesno=="n":
    print("Download Terminated.")
else:
    print("Please restart the program.")
