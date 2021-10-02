import speech_recognition as sr
import pyttsx3 
from tkinter import *
from tkinter.font import Font,Font
from tkinter.ttk import Combobox
from tkinter import messagebox,filedialog
from PIL import Image,ImageTk


import os


root = Tk()

root.geometry("750x450")
root.title("Ultitled.txt  -Notepade".center(200))
root.maxsize(root.winfo_screenwidth(),root.winfo_screenheight())
# root.wm_iconbitmap("ico.ico")


#############################################-: Adding Menu Bar :-###################################################
def CreatingMainMenu():
    global status_bar
    all = BooleanVar()    
    all.set(True)
    Scroll_bar = BooleanVar()
    status_bar = StringVar()
    

    mainmenu = Menu(root)
#####################################-: Adding File Menu Bar :-###############################################################################
   
    m1  = Menu(mainmenu)
    m1 = Menu(mainmenu,tearoff=0)

    m1.add_command(label="New",activebackground="silver",command=NewFile)
    m1.add_command(label="New Window",activebackground="silver",command=CreateNewWindow)
    m1.add_command(label="Save",command=SaveFile,activebackground="silver")
    m1.add_command(label="Save as",command=SaveasFileName,activebackground="silver")
    m1.add_command(label="Open",activebackground="silver",command=OpenFileName)
    
    
    m1.add_separator()
    

    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="File",menu=m1)

###########-: Adding Edite Menu Bar :-###########

    m2  = Menu(mainmenu)
    m2 = Menu(mainmenu,tearoff=0)

    m2.add_command(label="Undo")
    m2.add_separator()
    m2.add_command(label="Cut",command=CutText)
    m2.add_command(label="Copy",command=CopyText)
    m2.add_command(label="Paste",command=PasteText)
    m2.add_command(label="Delete")
    
    m2.add_command(label="Find And Replace",command= create_main_window)

    m2.add_separator()
    m2.add_command(label="Select All..")
    m2.add_command(label="TIme/Date")
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Edit",menu=m2)

###########-: Adding Formate Menu Bar :-###########
    m3  = Menu(mainmenu)
    m3 = Menu(mainmenu,tearoff=0)
    m3.add_command(label="Fonts",command=setfont)
   

    # ////////////////////////////// Adding the color option ////////////////////////////////////////////////
    m3.add_command(label="Colors",command=setcolor)
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Edit",menu=m3)



    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Formate",menu=m3,background="blue")

    
###########-: Adding View Menu Bar :-###########
   
    m4 = Menu(mainmenu,tearoff=0)
    m4.add_checkbutton(label="Monu",onvalue=1,offvalue=2,command=showstatus,variable=status_bar)

    m4.add_radiobutton(label="Vertical Bar",variable=Scroll_bar)
    m4.add_radiobutton(label="Horizontal Bar", variable=Scroll_bar)
    
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="View",menu=m4,background="blue")
    
###########-: Adding Help Menu Bar :-###########
    

    m5  = Menu(mainmenu,font=("Arial",10))
    m5 = Menu(mainmenu,tearoff=0)
    m5.add_command(label="View Help",command=ViewHelp)
    m5.add_command(label="Send Feedback",command=feedback)
    m5.add_command(label="About Notpade",command=about)
    
    
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="Help",menu=m5,background="blue")
    
    mainmenu.add_cascade(label="Exit",command=ExitWindow)
    mainmenu.add_cascade(label="Speech",command=Text2Speech)
    mainmenu.add_command(label='Mic',compound=LEFT,command=Speech2Text)
    
def Text2Speech():
    import pyttsx3
    engine = pyttsx3.init()  
    engine.say(Text1.get(1.0,END))  
    
    engine.runAndWait()

def Speech2Text():

    r = sr.Recognizer() 
    
    try:
            
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print('Say...') 
            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            # MyText = MyText.lower()

            print("Did you say "+MyText)
            Text1.insert(END,MyText)
        
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
            
    except sr.UnknownValueError:
        print("unknown error occured")
    
    
###########-: Adding Exit Menu Button :-###########



#############################################-: Configure all Help Options :-######################################

def about():
    messagebox.showinfo("About Notepade","hello i am Monu Saini this is my first software as a text editer like Notepade.i create it by taking 'codewithharry' Classses from yourtube at the time")

def feedback():
    a = messagebox.askyesno("Feedback","If you want to send feedback")
    if a:
        f = Tk()
        var = IntVar()
        f.geometry("200x150")
        f.title("Feedback")
        f.resizable(0,0)
        f.wm_iconbitmap("1.ico")
        
        varList = StringVar(f)
        varList.set("Good")
        def submits():
            messagebox.showinfo("Feedback","Thanks for your Feedback..")
            f.destroy()
        om = OptionMenu(f, varList, "Nice", "SO Nice", "Good", "Very Nive", "Venderful", "So Good")
        om.place(width=120,height=50)
        Label(f,text="Rate Us.. ",font=("Arial BLock",13)).place(x=2,y=80)
        sc1  =Scale(f,from_=0,to=10,orient=HORIZONTAL,tickinterval=2).place(x=70,y=60)
        Button(f,text="Submit..",font=("Arial Black",12),command=submits).place(x=90,y=120)



        

        
        f.mainloop()
    else:
        messagebox.showinfo("Feedback","OK! No Problem..")

def ViewHelp():   
    helproot= Tk()
    helproot.geometry("750x450")
    helproot.title("Help Support")
    helproot.wm_iconbitmap("3.ico")
    
    scroll=Scrollbar(helproot)
    scroll.pack(side=RIGHT,fill=Y)
    
    
    Text2 = Text(helproot,yscrollcommand=scroll.set)
    Text2.pack(expand=True, fill=BOTH)
    scroll.config(command=Text2.yview)
    help = open("help.txt","r")    
    Text2.insert(1.0,help.read())
    Text2.configure(state='disabled')
    help.close()

    Text2.config()
    helproot.mainloop()

#############################################-: Configure all View Options :-######################################
##############    Status Bar     ??/
def showstatus():
    pass

cordinates = StringVar()
word = StringVar()
frm = Frame(root,width=1366,height=17,bg='#E6E6FA')
frm.pack(side=BOTTOM)

# lable = Label(root,bg="gray",relief=SUNKEN,anchor="w",textvariable=bar).pack(fill="y",side=LEFT)
entry = Entry(frm,font=("Arian",10),bg='#E6E6FA',textvariable=cordinates)
entry.place(height=15)
entry.configure(state='disabled')
# entry.pack()
def motion(event):
    cordinates.set("")
    x, y = event.x, event.y
    cordinates.set(f"Cordinates {x}::{y}")

root.bind('<Motion>', motion)

##### ///////////// counting the words ///////////////////////////////
word.set("words:0")
def check(event):
    os.system('cls')
   
    word.set(f"words:{len(Text1.get(1.0,END))-1}")


########################## Defyning the line numbers ##############################
def lines(event):
    final_index = str(Text3.index(END))
    num_of_lines = final_index.split('.')[0]
    line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
    width = len(str(num_of_lines))
    Text3.configure(state='normal', width=width)
    Text3.delete(1.0, END)
    Text3.insert(1.0, line_numbers_string)
    Text3.configure(state='disabled')


words = Entry(frm,width=40,font=("Arian",10),bg='#E6E6FA',textvariable=word)
words.pack(side=TOP)
words.configure(state='disabled')

words.place(x=585,width=80,height=15)

# ///////////// Zoom Bar //////////////////////////////
zoom_bar = IntVar()
font1 = Font(family="Courier", size=zoom_bar.get())
def zoomwindow(size):
    global Text1
    font1.config(size=size)
    Text1.config(font=font1)

sc1 = Scale(root,width=10,from_=5,to=150,variable=zoom_bar,command=zoomwindow)
sc1.place(x=1)
sc1.pack(fill='y',side=RIGHT)

   
#############################################-: Configure all Font Options :-######################################


def setfont():
    font = Tk()
    font.geometry("450x150")
    font.title("Costomize Font")
    # font.wm_iconbitmap('font.ico')
    font.config(background='White')
    font.attributes('-toolwindow', True)
    var = StringVar()
  
# /////////////////////////////////////////   Set The Text Font ////////////////////////////////////////////////////
    def change_font(event):
        
        Text1.config(font=(f"{opt.get()}",fsize.get()))
        Text1.update()
        demo.config(font=(f"{opt.get()}"))

    fonts = ("Arial","Courier","Verdana","Georgia","Palatino","Courier New","Times New Roman","Sylfaen","Stencil","Script MT")
    opt = Combobox(font, textvariable=var)
    opt.set("Arial")
    opt['values'] = fonts
    opt['state'] = 'readonly'  # normal
    

    opt.place(x=5,y=35,width=100)
    opt.bind('<<ComboboxSelected>>',change_font)
  
    Label(font,text="Set Font",font=("Arial Black",12),bg="white").place(x=5,y=1)
    Button(font,text="Save",font=("Georgia",13),bg='#008000').place(x=360,y=110,width=80)

# /////////////////////////////////////////   Set The Text Font size  ////////////////////////////////////////////////////
    def change_font_size():
            Text1.config(font=("",fsize.get()))
            Text1.update()
            for i in list1.curselection():
                demo.config(font=(f"{opt.get()}",fsize.get(),f'{list1.get(i).lower()}'))
                demo.update()



    fsize = StringVar()
    fsize.set("Giorgia")
    data = []
    for i in range(11,72):
        data.append(i)
    Label(font,text="Font Size",font=("Arial Black",12),bg="white").place(x=5,y=70)
    fsize= Spinbox(font,values= data,font=("Algerian",15),textvariable= fsize,command=change_font_size)
    
    fsize.place(x=1,y=100,width=70,height=20)

    
# /////////////////////////////////////////   Set The Text Font Style  ////////////////////////////////////////////////////
    def selected_item():
        for i in list1.curselection():
            
            Text1.configure(font=("",fsize.get(),f'{list1.get(i).lower()}'))
            Text1.update()
            demo.config(font=(f"{opt.get()}",fsize.get(),f'{list1.get(i).lower()}'))
            demo.update()

    scroll=Scrollbar(font)
    scroll.place(height=80,x=260,y=30)
    
   

    Label(font,text="Font Style",font=("Arial Black",12),bg="white").place(x=170,y=3)

    list1  = Listbox(font,yscrollcommand=scroll.set)
    list1.place(x=140,y=28,height=80)

    scroll.config(command=list1.yview)
    fontStyles = ["Regular","Italic","Bold Italic","Light Oblique"," Light",
    " Light Italic "," Oblique","Medium Oblique "," Bold Oblique"," Semibold Oblique"]

    for item in fontStyles:
        list1.insert(END,item)


    Button(font,text="Select",font=("Arial Black",10),command=selected_item).place(x=180,y=120)
   
############################ Creating Fint Demo window #############################################################################
  
# FLAT.
# RAISED.
# SUNKEN.
# GROOVE.
# RIDGE.
# ,f"{list1.get(i)}"
# ,f"{fsize.get()}"
    demo  = Label(font,text="AbcdABCD",bg="white",width=14,height=5,relief=RIDGE)
    demo.place(x=300,y=16)

    sample = Label(font,font=("Arial Black",10),text="Sample",bg="white")
    sample.place(x=300,y=3)
    
        

    font.mainloop()
    
#################################  Set The Text Font color  ////////////////////////////////////////////////////



def setcolor():
    color = Tk()
    color.geometry("250x100")
    color.title("Set Color")
    color.attributes('-toolwindow', True)
    bg1 = StringVar()
    fg1 = StringVar()
    colors = ("Blue","Green","Red","Cyan","Black","Magenta","Yellow","Black","White")

    def setbg():
        Text1.config(bg=f"{bg.get().lower()}")
        Text1.update()
        bg1.set(f"{bg1.get()}")




    def setfg():
        Text1.config(fg=f"{fg.get().lower()}")
        Text1.update()
        fg1.set(f"{fg.get()}")




    bg = Spinbox(color,font=("Rockwell",12),textvariable=bg1,values=colors,command=setbg)
    bg.place(x=110,y=8,width=110,height=30)

    fg = Spinbox(color,font=("Rockwell",12),textvariable=fg1,values=colors,command=setfg)
    fg.place(x=110,y=50,width=110,height=30)

    lab1 = Label(color,text="Set Back color",font=("Latin",12))
    lab1.place(x=1,y=8)

    lab2 = Label(color,text="Set text color",font=("Latin",12))
    lab2.place(x=1,y=50)
    
    color.mainloop()
# #############################################-: Configure all File Options :-######################################

def SaveFile():
    global file
    if file == None:
        
        file = filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None
        else:
            f = open(file, "w")
            f.write(Text1.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-  Notepade")
    else:
        f = open(file, "w")
        f.write(Text1.get(1.0, END))
        f.close()


def SaveasFileName():

    global file
    
                            
    file = filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    
    f = open(file, "w")
    f.write(Text1.get(1.0, END))
    f.close()
    root.title(os.path.basename(file) + "-  Notepade")

def ExitWindow():
    root.destroy()


def OpenFileName():#Complete
    global file
    def openfile():
        file = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All file","*.*"),("Text Document",".txt")])
        
       
        if file=="":
            file = None
        else:
            root.title(os.path.basename(file)+ "   -Notepade")
            Text1.delete(1.0,END)
            with open(file,"r") as filetext:
                
                Text1.insert(1.0,filetext.read())
                filetext.close()

    if len(Text1.get(1.0,END)) ==1:
      openfile()
    else:
        YESNO = filedialog.askyesno("Save File","Save Curret Text as a file")
        if YESNO:
                filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
                Text1.delete(1.0,END)
                openfile()
        else:
            Text1.delete(1.0,END)
            openfile()



    ###########################

def  NewFile():
    global file
    
    if len(Text1.get(1.0,END)) ==1:
      pass
    else:
        YESNO = filedialog.askyesno("Save File","Save Curret Text as a file")
        if YESNO:
            filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        else:
            Text1.delete(1.0,END)

#############################################-: Configure all Edid Options :-######################################

def CopyText():
    Text1.event_generate(("<>"))


def CutText():
    Text1.event_generate(("<>"))


def PasteText():
    Text1.event_generate(("<>"))
# ////////////////////////////////////////  Find and Replace   ////////////////////////////////////////////////////////////////////

def create_input_frame(container):

    frame = Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    Label(frame, text='Find with:').grid(column=0, row=0, sticky=W)
    keyword = Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=W)

    # Replace with:
    Label(frame, text='Replace with:').grid(column=0, row=1, sticky=W)
    replacement = Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=W)

    # Match Case checkbox
    match_case =StringVar()
    match_case_check = Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=W)

    # Wrap Around checkbox
    wrap_around = StringVar()
    wrap_around_check = Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame


def create_button_frame(container):
    frame = Frame(container)

    frame.columnconfigure(0, weight=1)

    Button(frame, text='Find Next').grid(column=0, row=0)
    Button(frame, text='Replace').grid(column=0, row=1)
    Button(frame, text='Replace All').grid(column=0, row=2)
    Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame


def create_main_window():

    # root window
    root = Tk()
    root.geometry('400x150')
    root.title('Find and Replace'.center(120))
    # root.wm_iconbitmap("3.ico")
    root.resizable(0, 0)
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
def CreateNewWindow():
    
    pass
#############################################################################################################

if __name__=="__main__":

    file = None
        
###########-: Adding Scroll Bar :-###########F
    # frame1 = Frame(root)
    bar  = StringVar()
    bar.set("1")
    bar.set("2")

    Text3 = Text(root,width=1,height=400)
    Text3.pack(fill="x",side=LEFT)

    Text3.configure(state='disabled')

    scroll=Scrollbar(root)
    scroll.pack(side=RIGHT,fill=Y)
    
    fm = Frame(root).pack()
    Text1 = Text(fm,font="Arial",yscrollcommand=scroll.set)
    Text1.pack(expand=True, fill=BOTH,padx=10)
    scroll.config(command=Text1.yview)
    Text1.bind('<KeyRelease>',check)
    Text1.bind('<KeyPress>',check)
    Text1.bind('<BackSpace>',check)
    Text1.bind('<Return>',lines)
    
    CreatingMainMenu()
    
    root.mainloop()
