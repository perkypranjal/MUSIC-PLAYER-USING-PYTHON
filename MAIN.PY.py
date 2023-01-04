# setup screen=-                                                        
from tkinter import *
import os
import time
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
from playsound import playsound


mixer.init()


class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        self.root.geometry('700x400')
        self.root.title('Fumes')
        self.root.configure(background='white')
        self.root.resizable(0,0)

        #open file
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()

        

        #menu--
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='Exit',command=self.root.destroy)

        def About():
            tkinter.messagebox.showinfo('About Us','This is a python based music player created by our team members')
            
        
                
        self.submenu2=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Help',menu=self.submenu2)
        self.submenu2.add_command(label='About',command=About)
        


        


        #Adding label---
        self.filelabel=Label(text='Select & Play',bg='white',fg='black',font=('cambria',15))
        self.filelabel.place(x=10,y=20)

        def songinfo():
            self.filelabel['text']='Current Music: '+os.path.basename(filename)

        #Adding leftsideimg---
            
        #L=left
        self.L_photo=ImageTk.PhotoImage(file='leftsideimg.png')
        L_photo=Label(self.root,image=self.L_photo,bg='white').place(x=240,y=80,width=500,height=200)


        
        #Adding img--
        self.photo=ImageTk.PhotoImage(file='mainimg.png')
        photo=Label(self.root,image=self.photo,bg='white').place(x=50,y=50)

        
        #label---
        self.label1=Label(self.root,text='Lets Play It.',bg='black',fg='white',font=22)
        self.label1.pack(side=BOTTOM,fill=X)
        
        
        #functions for playbtn---
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']='Music Playing..'
                    songinfo()
                    length_bar()
                except:
                    tkinter.messagebox.showerror('Error','Please select the music')
            else:
                mixer.music.unpause()
                self.label1['text']='Music Unpaused'



        def length_bar():
            current_time=mixer.music.get_pos()/1000
            convert_current_time=time.strftime('%M:%S',time.gmtime(current_time))
            song_mut=MP3(filename)
            song_mut_length=song_mut.info.length
            convert_song_mut_length=time.strftime('%M:%S',time.gmtime( song_mut_length))
            self.lengthbar.config(text=f'Song Duration:- {convert_current_time}:{convert_song_mut_length}')
            self.lengthbar.after(1000,length_bar)
        #length
        self.lengthbar=Label(self.root,text='Song Duration=00:00',bg='white',fg='black',font=('cambria',12))
        self.lengthbar.place(x=10,y=270)

        
            






        
        #Creating Buttons---
        #play_button---
        self.photo_B1=ImageTk.PhotoImage(file='playbtn.png')
        photo_B1=Button(self.root,image=self.photo_B1,bd=0,bg='white',command=playmusic).place(x=5,y=300)

        #function for pausebtn---
        def pausemusic():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label1['text']='Music Paused'



        #pause_button---
        self.photo_B2=ImageTk.PhotoImage(file='pausebtn.png')
        photo_B2=Button(self.root,image=self.photo_B2,bd=0,bg='white',command=pausemusic).place(x=85,y=300)
        
        #function for stopbtn---
        def stopmusic():
            mixer.music.stop()
            self.label1['text']='Music Stopped'

        #mute--
        def mute():
            self.scale.set(0)
            self.mute=ImageTk.PhotoImage(file='mutebtnn.png')
            mute=Button(self.root,image=self.mute,command=unmute,bg='white',bd=0).place(x=250,y=295)
            self.label1['text']='Music muted'
        #unmute--
        def unmute():
            self.scale.set(25)
            self.volimg=ImageTk.PhotoImage(file='6.png')
            volimg=Button(self.root,image=self.volimg,command=mute,bg='white',bd=0).place(x=250,y=295)
            self.label1['text']='Music played'


        
        #stop_button---
        self.photo_B3=ImageTk.PhotoImage(file='stopbtn.png')
        photo_B3=Button(self.root,image=self.photo_B3,bd=0,bg='white',background='white',command=stopmusic).place(x=165,y=300)

        #function for volume bar
        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)

        #volume bar
        self.scale=Scale(self.root,orient=HORIZONTAL,bg='black',fg='white',length=160,command=volume,from_=0,to=100)
        self.scale.set(25)
        self.scale.place(x=330,y=310)


        #volume --Img-
        self.volimg=ImageTk.PhotoImage(file='6.png')
        volimg=Button(self.root,image=self.volimg,command=mute,bg='white',bd=0).place(x=250,y=295)

        #right corner image
        self.rightjpg=ImageTk.PhotoImage(file='fumess.jpg')
        rightjpg=Label(self.root,image=self.rightjpg,bg='white',bd=0).place(x=590,y=266)


        

        





       


root=Tk()
obj=musicplayer(root)
root.mainloop()

