from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = "youtube"


#file location
def location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text="You did NOT select Folder!", fg="red")


#donwload video
def download():
    choice = ytdchoices.get()
    url = entry.get()

    if len(url) > 1:
        error.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()

        elif choice == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif choice == choices[2]:
            select = yt.streams.filter(only_audio=True).first()

        else:
            error.config(text="Paste Link again!!", fg="red")


    #download function
    select.download(Folder_Name)
    error.config(text="Download Completed!")


root = Tk()
root.title("YouTube Downloader")
root.geometry("") #set window
root.columnconfigure(0, weight=1)#set all content in center.

#Ytd Link Label
label = Label(root, text="Please Enter URL", font=("verdana", 15))
label.pack()

#Entry Box
EntryVar = StringVar()
entry = Entry(root, width=50, textvariable=EntryVar)
entry.pack()


#Asking save file label
saveLabel = Label(root, text="Save File", font=("verdana", 15, "bold"))
saveLabel.pack()

#btn of save file
saveEntry = Button(root, width=10, fg="red", text="Choose Path", command=location)
saveEntry.pack()


#Download Quality
ytdQuality = Label(root, text="Select Quality", font=("verdana", 15))
ytdQuality.pack()

#combobox
choices = ["720p", "144p", "Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.pack()

#donwload btn
download = Button(root, text="Click to Download", width=15, fg="red", command=download)
download.pack()


#Error Msg
error = Label(root, text="", fg="red", font=("verdana",  10))
error.pack()

# #Error Msg location
locationError = Label(root, text="", fg="red", font=("verdana", 10))
locationError.pack()

root.mainloop()
