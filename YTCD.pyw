import shutil
from cgitb import text
from importlib.resources import path
import os
from os import link
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pytube import YouTube
import random
import time
import pathlib




mp3_ertek=False
mp4_ertek=False


def mappavalaszto():
    global pathdir
    pathdir="./"
    pathdir=filedialog.askdirectory()
    

#mp3\mp4 buttons| mp3\mp4 gombok
def mp3():
    global mp3_ertek
    global mp4_ertek
    mp3_ertek=True
    mp4_ertek=False
    mp3_gomb.config(text="MP3",command=mp3,background="red",font="Arial 10",fg="white")
    mp4_gomb.config(text="MP4",command=mp4,background="white",font="Arial 10",fg="black")

def mp4():
    global mp4_ertek
    global mp3_ertek
    mp4_ertek=True
    mp3_ertek=False
    mp3_gomb.config(text="MP3",command=mp3,background="white",font="Arial 10",fg="black")
    mp4_gomb.config(text="MP4",command=mp4,background="red",font="Arial 10",fg="white")



def main():
    
    try:
        #Collect url|url begyűjtése
        linkurl=linkdoboz.get()
        yt=YouTube(linkurl)

        #mp4 video download| mp4 videó letöltése
        if mp4_ertek:
            bar["value"]=0
            mp4=yt.streams.get_highest_resolution().download(pathdir)
            bar["value"]+=100

        #download audio| hang letöltése
        if mp3_ertek:
            
            bar["value"]+=10
            mp3=yt.streams.filter(only_audio=True).first()
            bar["value"]+=10
            mp3.download()
            bar["value"]+=10
            #rewrite file extension |fájl kiterjesztés átírása
            fileok=os.listdir()
            bar["value"]+=10
            for file in fileok:
                if ".mp4" in file:
                    os.rename(file,str(file).replace(".mp4","")+".mp3")
            bar["value"]+=10
            time.sleep(1)    
            #copy the mp3 file to the destination folder|mp3 file célmappába másolása
            fileok=os.listdir()
            bar["value"]+=10  
            localdirectory=pathlib.Path(__file__).parent.resolve()
            bar["value"]+=10
            for mp3_file in fileok:
                if ".mp3" in mp3_file:
                    shutil.copy(str(localdirectory) + "\\" + mp3_file,pathdir)
                    time.sleep(1)        
                    os.remove(str(localdirectory) + "\\"+ mp3_file)
            bar["value"]+=30
        else:
            pass


        

        text["state"]=NORMAL
        text.delete(1.0,END)
        text.insert(END,f"Sikeres letöltés!")
        text["state"]=DISABLED
        text.config(fg="white")
        text.place(x=0,y=220)
        
    except:
        text["state"]=NORMAL
        text.delete(1.0,END)
        text.insert(END,"File vagy tipus hiba! Nem adtál meg célhelyet/file-tipust! \n")
        text["state"]=DISABLED
        text.config(fg="red")
        text.place(x=0,y=220)





win=Tk()


win.geometry("400x600")
win.title("YTCD")
win.resizable(False,False)
win.iconbitmap(r'ikon.ico')
hatter=PhotoImage(file="hatter.png")
backgroundlabel=Label(win,image=hatter)
backgroundlabel.place(x=0,y=0,relheight=1,relwidth=1)
kep=PhotoImage(file="kep.png")
kep=kep.subsample(12,12)
hatterlogo=Label(win,image=kep)
hatterlogo.place(x=105,y=15)


#text box|szövegdoboz
text=Text(win,font="arial 10 bold",state=DISABLED,width=100,height=3,fg="red",border=0,background="black")
#progressbar
bar=Progressbar(orient=HORIZONTAL,length=380)

bar.place(x=10,y=530)


#Linkbox
linkdoboz=Entry(width=40)
linkdoboz.place(x=90,y=200)
#Download button|Letöltésgomb\\\\\
letoltesgomb=Button(text="Letöltés")
letoltesgomb.place(x=90,y=380)
letoltesgomb.config(font="Arial 40",fg="white",background="red",activebackground="red",activeforeground="white",command=main)
#destination folder selector|célmappa választó\\\\\\
valaszto=Button(text="könyvtár",command=mappavalaszto,font="Arial 20",background="red",fg="white")
valaszto.place(x=160,y=270)
#url-label
urlbox_megnevezese=Label(text="Add meg a videó url-jét!",background="black",fg="white",font="Arial 13")
urlbox_megnevezese.place(x=90,y=170)
#mp3/mp4 buttons|mp3/mp4 választó\\\\
mp3_gomb=Button(text="MP3",command=mp3,background="white",font="Arial 10")
mp4_gomb=Button(text="MP4",command=mp4,background="white",font="Arial 10")
mp3_gomb.place(x=105,y=269)
mp4_gomb.place(x=105,y=300)

win.mainloop()