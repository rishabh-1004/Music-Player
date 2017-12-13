
#Libraries used 
#Pygame
#Tkinter
#mutagen

import os
import pygame
from Tkinter import *
import tkFileDialog
#from mutagen.id3 import ID3

root=Tk()
root.minsize(400,400)

listofsongs = []
realnames=[]
index=0


def nextsong(event):
	global index
	index =index+1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()


def previoussong(event):
	global index
	index -=1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()

def stopsong(event):
	pygame.mixer.music.stop()


def directorychooser():
	directory = tkFileDialog.askdirectory()
	os.chdir(directory)


	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			realdir=os.path.realpath(files) #C:/user/data/song.mp3
			#audio=ID3(realdir)
			#realnames.append(audio["TIT2"].text[0])
			listofsongs.append(files)

			

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	pygame.mixer.music.play()

directorychooser()
print listofsongs

label=Label(root,text="Music Player")
label.pack()

listbox=Listbox(root)
listbox.pack()

listofsongs.reverse()
for items in listofsongs:
	listbox.insert(0,items)



nextbutton= Button(root,text='Next Song')
nextbutton.pack()

previousbutton=Button(root,text='Previous Song')
previousbutton.pack()

stopbutton=Button(root,text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)
stopbutton.bind("<Button-1>",stopsong)


root.mainloop()
