import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
import PIL
from gtts import gTTS
import os
import texttospeech
import webbrowser
import convert
import Readrandom


def GetStarted():
    win = tk.Tk()
    win.geometry("200x150")

    win.title('Inflection Booster')

    def lowlevel():
        win.destroy()
        window = tk.Tk()
        window.geometry("400x300")


        def results():
            window.destroy()
            win1 = tk.Tk()
            win1.geometry("300x300")
            win1.title('Inflection Booster')
            frame = tk.Frame(win1)
            frame.grid(row = 0,column = 0,sticky = "nsew")
            frame.place(x = 0,y = 0)
            frame.configure(height = 300,width = 300)
            string.lower()
            readtext.lower()
            print(readtext)
            if string == readtext:
                speak_text = 'Hurray!! you read it correct'
            elif string in readtext:
                speak_text = 'oh!! you extra words'
            else:
                speak_text = 'It is pronounced as ' + string

                
            speakimage = tk.PhotoImage(file =r'C:\Users\Srinivas\Pictures\Saved Pictures\speak.png')
            speak = tk.Button(frame,text = 'speak',command =  lambda :texttospeech.speaknow(speak_text))
            #speak.image = speakimage
            speak.place(x = 100,y = 100)

        string = Readrandom.ReadRandom(1,'lowlevel.txt')
        namevalue = tk.StringVar()
        name = tk.Entry(window,textvariable = namevalue,width = 20,bd = 2,font =('Times',15,"italic"))
        name.insert(0,string)
        name.place(x = 130,y = 110)

        readvalue = tk.StringVar()
        read = tk.Entry(window,textvariable = readvalue,width = 20,bd = 2,font =('Times',15,"italic"))
        read.place(x = 130,y = 170)
             
        recordbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Record',command = lambda:read.insert(0,convert.SpeechToText()))
        
        recordbutton.place(x = 100,y = 250)
        readtext = read.get()

        #result
        resultbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Results',command = results)
        resultbutton.place(x = 200,y = 250)

    label = tk.Label(win,font  = ("Times",15,"italic"),text = 'Confirm to start test')
    label.place(x = 20,y = 10)
    button = tk.Button(win,font = ("Times",10,"italic"),text = 'start',command = lowlevel,width = 12)
    button.place(x = 90,y = 90)
  

def GetStarted1():
    win = tk.Tk()
    win.geometry("200x150")

    win.title('Inflection Booster')

    def mediumlevel():
        win.destroy()
        window = tk.Tk()
        window.geometry("400x300")


        def results():
            window.destroy()
            win1 = tk.Tk()
            win1.geometry("300x300")
            win1.title('Inflection Booster')
            frame = tk.Frame(win1)
            frame.grid(row = 0,column = 0,sticky = "nsew")
            frame.place(x = 0,y = 0)
            frame.configure(height = 300,width = 300)
            string.lower()
            readtext.lower()
            print(readtext)
            if string == readtext:
                speak_text = 'Hurray!! you read it correct'
            elif string in readtext:
                speak_text = 'oh!! you extra words'
            else:
                speak_text = 'It is pronounced as ' + string

                
            speakimage = tk.PhotoImage(file = r'C:\Users\Srinivas\Pictures\Saved Pictures\speak.png')
            speak = tk.Button(frame,text = 'speak',command =  lambda :texttospeech.speaknow(speak_text))
            #speak.image = speakimage
            speak.place(x = 100,y = 100)

        string = Readrandom.ReadRandom(1,'mediumlevel.txt')
        namevalue = tk.StringVar()
        name = tk.Entry(window,textvariable = namevalue,width = 20,bd = 2,font =('Times',15,"italic"))
        name.insert(0,string)
        name.place(x = 130,y = 110)

        readvalue = tk.StringVar()
        read = tk.Entry(window,textvariable = readvalue,width = 20,bd = 2,font =('Times',15,"italic"))
        read.place(x = 130,y = 170)
        
        recordbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Record',command = lambda:read.insert(0,convert.SpeechToText()))
        recordbutton.place(x = 100,y = 250)
        readtext = read.get()

        #result
        resultbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Results',command = results)
        resultbutton.place(x = 200,y = 250)

    label = tk.Label(win,font  = ("Times",15,"italic"),text = 'Confirm to start test')
    label.place(x = 20,y = 10)
    button = tk.Button(win,font = ("Times",10,"italic"),text = 'start',command = mediumlevel,width = 12)
    button.place(x = 90,y = 90)
      



def GetStarted2():
    win = tk.Tk()
    win.geometry("200x150")

    win.title('Inflection Booster')

    def highlevel():
        win.destroy()
        window = tk.Tk()
        window.geometry("400x300")


        def results():
            window.destroy()
            win1 = tk.Tk()
            win1.geometry("300x300")
            win1.title('Inflection Booster')
            frame = tk.Frame(win1)
            frame.grid(row = 0,column = 0,sticky = "nsew")
            frame.place(x = 0,y = 0)
            frame.configure(height = 300,width = 300)
            string.lower()
            readtext.lower()
            print(readtext)
            if string == readtext:
                speak_text = 'Hurray!! you read it correct'
            elif string in readtext:
                speak_text = 'oh!! you extra words'
            else:
                speak_text = 'It is pronounced as ' + string

                
            speakimage = tk.PhotoImage(file = r'C:\Users\Srinivas\Pictures\Saved Pictures\speak.png')
            speak = tk.Button(frame,text = 'speak',command =  lambda :texttospeech.speaknow(speak_text))
            #speak.image = speakimage
            speak.place(x = 100,y = 100)

        string = Readrandom.ReadRandom(1,'highlevel.txt')
        namevalue = tk.StringVar()
        name = tk.Entry(window,textvariable = namevalue,width = 20,bd = 2,font =('Times',15,"italic"))
        name.insert(0,string)
        name.place(x = 130,y = 110)

        readvalue = tk.StringVar()
        read = tk.Entry(window,textvariable = readvalue,width = 20,bd = 2,font =('Times',15,"italic"))
        read.place(x = 130,y = 170)
        
        recordbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Record',command = lambda:read.insert(0,convert.SpeechToText()))
        recordbutton.place(x = 100,y = 250)
        readtext = read.get()

        #result
        resultbutton = tk.Button(window,width = 10,font = ('Times',14,'italic'),text = 'Results',command = results)
        resultbutton.place(x = 200,y = 250)

    label = tk.Label(win,font  = ("Times",15,"italic"),text = 'Confirm to start test')
    label.place(x = 20,y = 10)
    button = tk.Button(win,font = ("Times",10,"italic"),text = 'start',command = highlevel,width = 12)
    button.place(x = 90,y = 90)


def Game():
    window = tk.Tk()
    window.geometry('600x500')
    window.title('Inflection booster')
    def Convert():
        string1 = convert.SpeechToText()
        print(string1)
        if string1 in stringlist:
            print(dict1[string1])
            dict1[string1].pack_forget()
    stringlist = ['Hello','welcome','inflection','booster']
    label1 = tk.Label(window,font = ("Times",15,"italic"),text = stringlist[0])
    label1.place(x = 20, y = 80)

    label2 = tk.Label(window,font = ("Times",15,"italic"),text = stringlist[1])
    label2.place(x = 40,y = 100)

    label3 = tk.Label(window,font = ("Times",15,"italic"),text = stringlist[2])
    label3.place(x = 60,y = 120)

    label4 = tk.Label(window,font = ("Times",15,"italic"),text  = stringlist[3])
    label4.place(x = 80,y = 140)

    dict1 = {stringlist[0]:label1,stringlist[1]:label2,stringlist[2]:label3,stringlist[3]:label4}

    button = tk.Button(window,font = ("Times",10,"italic"),text = 'start',command = lambda: Convert(),width = 12)
    button.place(x = 100,y = 200)

    
  
def Course(name):
    string = "welcome to tutor" + name
    texttospeech.speaknow(string)
    master.destroy()
    window = tk.Tk()
    window.geometry("600x500")
    menu_frame = tk.Frame(window,bg = "#c3c3c3")
    window.title("Inflection booster")

    img = tk.PhotoImage(file = r'C:\Users\Srinivas\Downloads\noun-reading-book-1997764.png')
    window.iconphoto(False,img)

    
    menu_frame.pack(side = tk.LEFT)
    menu_frame.pack_propagate(False)
    menu_frame.configure(width = 120,height = 500)

    frame = tk.Frame(window)
    frame.pack(side = tk.LEFT)
    frame.pack_propagate(False)
    frame.configure(height = 500 ,width = 480)


    def improve():
        label = tk.Label(frame,text = 'Know the inflection of words',font = ("Times",20,'bold italic'))
        label.place(x = 20,y = 50)
        namelabel = tk.Label(frame,text = 'Enter letter or word ',font = ("Times",12,"italic"))
        namelabel.place(x = 50,y = 110)
        namevalue = tk.StringVar()
        name = tk.Entry(frame,textvariable = namevalue,width = 20,bd = 2,font =20)
        name.place(x = 200,y = 110)

        speakimage = tk.PhotoImage(file = r'C:\Users\Srinivas\Pictures\Saved Pictures\speak.png')

        speak = tk.Button(frame,command =  lambda :texttospeech.speaknow(name.get()),image = speakimage)
        speak.image = speakimage
        speak.place(x = 250,y = 150)
        


    def Tutorial():

        ver_label = tk.Label(frame,text = "Youtube Tutorials",font = ("Times",20," bold italic"))
        ver_label.place(x = 0,y =  30)

        
        my_link1 = tk.Label(frame,text = " EngFluent ",fg = 'blue',cursor = 'hand2',font = ('Times new Roman',15,'underline'))
        my_link1.bind('<Button-1>',lambda x:webbrowser.open_new("https://youtu.be/5l-fo-d0gt8"))
        my_link1.place(x = 50,y = 100)

        my_link2 = tk.Label(frame,text = " mmmenglish ",fg = 'blue',cursor = 'hand2',font = ('Times new Roman',15,'underline'))
        my_link2.bind('<Button-1>',lambda x:webbrowser.open_new("https://youtu.be/-P-5RC17BHw"))
        my_link2.place(x = 50,y = 150)

        my_link3 = tk.Label(frame,text = " Rachel's English ",fg = 'blue',cursor = 'hand2',font = ('Times new Roman',15,'underline'))
        my_link3.bind('<Button-1>',lambda x:webbrowser.open_new("https://youtu.be/2W-KUSb3DTM"))
        my_link3.place(x = 50,y = 200)

        my_link3 = tk.Label(frame,text = " Easy english with james",fg = 'blue',cursor = 'hand2',font = ('Times new Roman',15,'underline'))
        my_link3.bind('<Button-1>',lambda x:webbrowser.open_new("https://youtu.be/LjrhyKV6ALQ"))
        my_link3.place(x = 50,y = 250)

        my_link4 = tk.Label(frame,text = "5 Steps to improve fluency",fg = 'blue',cursor = 'hand2',font = ('Times new Roman',15,'underline'))
        my_link4.bind('<Button-1>',lambda x:webbrowser.open_new("https://youtu.be/KaA_mxga3PQ"))
        my_link4.place(x = 50,y = 300)


        my_link5 = tk.Label(frame,text = "Use alternate words for Advanced English",fg = 'blue',cursor = 'hand2',font = ('Times new Roman',15,'underline'))
        my_link5.bind('<Button-1>',lambda x:webbrowser.open_new("https://youtu.be/5f_4Wx50Qjk"))
        my_link5.place(x = 50,y = 350)
        
    
        
    def Test_page():
        #low level

        lowimage = ImageTk.PhotoImage(Image.open(r'C:\Users\Srinivas\Pictures\Saved Pictures\lowinflection.png'))
        low_label = tk.Button(frame,image = lowimage,command = GetStarted)
        low_label.image = lowimage
        low_label.place(x = 50,y =  60)

        normalimage = ImageTk.PhotoImage(Image.open(r'C:\Users\Srinivas\Pictures\Saved Pictures\normalinflection.png'))
        normal_label = tk.Button(frame,image = normalimage,command = GetStarted1)
        normal_label.image = normalimage
        normal_label.place(x = 50,y =  180)

        highimage = ImageTk.PhotoImage(Image.open(r'C:\Users\Srinivas\Pictures\Saved Pictures\highinflection.png'))
        high_label = tk.Button(frame,image = highimage,command = GetStarted2)
        high_label.image = highimage
        high_label.place(x = 50,y =  300)


    def game():


        ballimage = ImageTk.PhotoImage(Image.open(r'C:\Users\Srinivas\Pictures\Saved Pictures\ball.jpg'))
        ball_label = tk.Label(frame,image = ballimage)
        ball_label.image = ballimage
        ball_label.place(x = 50,y =  60)


        circleimage = ImageTk.PhotoImage(Image.open(r'C:\Users\Srinivas\Pictures\Saved Pictures\Circle.jpg'))
        circle_label = tk.Label(frame,image = circleimage)
        circle_label.image = circleimage
        circle_label.place(x = 50,y =  180)

        cloudimage = ImageTk.PhotoImage(Image.open(r'C:\Users\Srinivas\Pictures\Saved Pictures\cloud.jpg'))
        cloud_label = tk.Label(frame,image = cloudimage)
        cloud_label.image = cloudimage
        cloud_label.place(x = 50,y =  300)
        
        
        ball_button = tk.Button(frame,font= ("Times", "12", "bold italic"),text = "Ball words",command = lambda :Game(),bd = 0,bg = "#c3c3c3")
        ball_button.place(x = 200,y = 90)

        ball_button = tk.Button(frame,font= ("Times", "12", "bold italic"),text = "circle words",command = None,bd = 0,bg = "#c3c3c3")
        ball_button.place(x = 200,y = 210)

        ball_button = tk.Button(frame,font= ("Times", "12", "bold italic"),text = "Clouds words",command = None,bd = 0,bg = "#c3c3c3")
        ball_button.place(x = 200,y = 330)
        


    def information_page():


        def display():
            text = tk.Text(frame,height = 3,width = 40,bg= "#c3c3c3")
            text.place(x = 130,y = 200)
            text.insert(tk.END,information)

        information = "It helps to improve your inflection skills. There are related tutorials to enhance pronounciation.Courses menu says how the words are inflected."
        infor_label = tk.Label(frame,text = "Information",font = ("Times",18," bold italic"))
        infor_label.place(x = 100,y =  30)

        versi_label = tk.Label(frame,text = "version",font = ("Times",15," bold italic"))
        versi_label.place(x = 130,y =  60)

        ver_label = tk.Label(frame,text = "1.000",font = ("Times",15,"italic"))
        ver_label.place(x = 250,y =  60)

        lic_label = tk.Label(frame,text = "License",font = ("Times",15,"bold italic"))
        lic_label.place(x = 130,y =  90)

        license_label = tk.Label(frame,text = "Not Yet Issued",font = ("Times",15,"italic"))
        license_label.place(x = 250,y =  90)

        copy_label = tk.Label(frame,text = "Copy Rights",font = ("Times",15,"bold italic"))
        copy_label.place(x = 130,y =  150)

        right_label = tk.Label(frame,text = "Bhavani",font = ("Times",15,"italic"))
        right_label.place(x = 250,y =  150)

        moreinfor_label = tk.Button(frame,text = " More Information",command = lambda :display(),font = ("Times",15," bold italic"))
        moreinfor_label.place(x = 130,y =  200)
        

    def delete_pages():
        for frame1 in frame.winfo_children():
            frame1.destroy()

            
    def hidelabel():
        course_indicate.configure(bg = "#c3c3c3")
        tut_indicate.configure(bg = "#c3c3c3")
        test_indicate.configure(bg = "#c3c3c3")
        game_indicate.configure(bg = "#c3c3c3")
        statistics_indicate.configure(bg = "#c3c3c3")
        information_indicate.configure(bg = "#c3c3c3")


    def indicate(lb,page):
        hidelabel()
        lb.configure(bg = '#158aff')
        delete_pages()
        page()


    #tutorial button
    course_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Course",command = lambda: indicate(course_indicate,improve),fg = "Black",bd = 0,bg = "#c3c3c3")
    course_button.place(x = 10,y = 50)

    course_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    course_indicate.place(x = 2,y = 50,width = 5,height = 40)


    
    #tutorial button
    tut_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Tutorial",command = lambda: indicate(tut_indicate,Tutorial),fg = "Black",bd = 0,bg = "#c3c3c3")
    tut_button.place(x = 10,y = 100)

    tut_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    tut_indicate.place(x = 2,y = 100,width = 5,height = 40)
    

    #test button
    test_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Inflection Test",command = lambda : indicate(test_indicate,Test_page),fg = "Black",bd = 0,bg = "#c3c3c3")
    test_button.place(x = 10,y = 150)

    test_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    test_indicate.place(x = 2,y = 150,width = 5,height = 40)


    #Games button
    game_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Games",command = lambda: indicate(game_indicate,game),fg = "Black",bd = 0,bg = "#c3c3c3")
    game_button.place(x = 10,y =200)

    game_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    game_indicate.place(x = 2,y = 200,width = 5,height = 40)


    #statistics button
    statistics_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Statistics",command = None,fg = "Black",bd = 0,bg = "#c3c3c3")
    statistics_button.place(x = 10,y =250)

    statistics_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    statistics_indicate.place(x = 2,y = 250,width = 5,height = 40)


    #information button
    information_button = tk.Button(menu_frame,font= ("Times", "12", "bold italic"),text = "Information",command = lambda: indicate(information_indicate,information_page),fg = "Black",bd = 0,bg = "#c3c3c3")
    information_button.place(x = 10,y = 300)

    information_indicate = tk.Label(menu_frame,text = " ",bg = '#c3c3c3')
    information_indicate.place(x = 2,y = 300,width = 5,height = 40)
    

    
def OpenWindow():


    master.geometry("600x400")
    master.title("Inflection booster")

    frame1 = tk.Frame(master)
    frame1.grid(row = 0,column = 0,sticky = "nsew")
    frame1.place(x = 0,y = 0)
    frame1.configure(height = 100,width = 600)
    
    frame = tk.Frame(master)
    frame.grid(row = 1,column = 1,sticky = "nsew")
    frame.place(x = 125,y = 100)
    frame.pack_propagate(False)
    frame.configure(height = 400,width = 400)


    img = tk.PhotoImage(file = '\\Users\\Srinivas\\Downloads\\noun-reading-book-1997764.png')
    master.iconphoto(False,img)

    #img1 = tk.PhotoImage(file = r'C:\Users\Srinivas\Pictures\Saved Pictures\homepage.jpg')
    #imglabel = tk.Label(frame1)
    #imglabel.config(image = img1)
    #imglabel.image = img1
    #imglabel.place(x= 150,y = 0)


    title = tk.Label(frame1,font = ("Times", "24", "bold italic"),text = "Inflection Booster")
    title.place(x = 250,y = 0)

    subtitle = tk.Label(frame1,font = ("Times", "12", "italic"),text = "Pronunication tutor")
    subtitle.place(x = 310,y = 35)

    
    #label
    label = tk.Label(frame,font = ("Times", "22", "italic"),text = "Welcome to Inflection Booster")
    label.place(x = 30,y = 50)

    namelabel = tk.Label(frame,text = 'Enter Your Name ',font = ("Times",12,"italic"))
    namelabel.place(x = 50,y = 110)
    namevalue = tk.StringVar()
    name = tk.Entry(frame,textvariable = namevalue,width = 20,bd = 2,font =20)
    name.place(x = 200,y = 110)

    button = tk.Button(frame,font = ("Times",10,"italic"),text = 'start',command = lambda :Course(name.get()),width = 15)
    button.place(x = 120,y = 160)



master = tk.Tk()
OpenWindow()


