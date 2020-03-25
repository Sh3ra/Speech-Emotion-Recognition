from tkinter import *
from tkinter import filedialog

import Predict

# my function can be used as follows: indexOfEmotion = Predict.predictGivenFileName(filename) filename is a string with full file location "D//abc//1.wav"   ranges from 1 to 8

root = Tk()
myLabel = Label(root, text="You Think NO One Cares About Your Feelings!", bg="red", fg="white", font=("Helvetica", 16))
myLabel2 = Label(root, text="You Think You Will Die Alone!", fg="#CCCC00", bg="white", font=("Helvetica", 16))
myLabel3 = Label(root, text="We Got You Covered", fg="white", bg="black", font=("Helvetica", 16))
myLabel4 = Label(root, text="Just Talk To US :)", fg="black", bg="green", font=("Helvetica", 16))
myLabel.pack(fill=X)
myLabel2.pack(fill=X)
myLabel3.pack(fill=X)
myLabel4.pack(fill=X)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

audioFile = ''
indexOfEmotion = ''


def printPrediction():
    pass


def filebrowser():
    global audioFile
    global indexOfEmotion
    audioFile = filedialog.askopenfilename(initialdir="/", title="Select Your Audio File",
                                           filetypes=(("Audio Files", ".wav "), ("All Files", "*.*")))
    indexOfEmotion = Predict.predictGivenFileName(audioFile)
    printPrediction()


browseButton = Button(bottomFrame, text="Browse", fg="red", command=filebrowser)
browseButton.pack(side=LEFT)
recordButton = Button(bottomFrame, text="Record", fg="blue")
recordButton.pack(side=LEFT)
root.mainloop()
