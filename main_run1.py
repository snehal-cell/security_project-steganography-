from tkinter import*
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox
from tkinter import font as tkFont


def encode():
    main.destroy()
    enc=Tk()
    enc.title("encode")
    enc.geometry("500x400+300+150")

    def go_back():
        enc.destroy()
        main.deiconify()

    fontl = tkFont.Font(family='Algerian', size=32)

    Label1 =Label(text="Secrate message")
    Label1.place(relx=0.1, rely=0.1, height=20, width=100)

    entry=Entry()
    entry.place(relx=0.4, rely=0.1)

    Label2 =Label(text="File Name")
    Label2.place(relx=0.1, rely=0.2, height=20, width=100)

    entrysave=Entry()
    entrysave.place(relx=0.4, rely=0.2)

    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg files, png file","*jpg *png"),("all files","*.*"))) 

        Label3=Label(text=fileopen)
        Label3.place(relx=0.3,rely=0.3)

    def encode():
        response=messagebox.askyesno("pop up","do you want to encode")
        if response==1:
            stg.hide(fileopen,entrysave.get()+'.jpg',entry.get())
            messagebox.showinfo("pop up","successfully encode")

        else:
            messagebox.showinfo("pop up","unsuccessfully ")



    Buttonselect=Button(text="Select File",command=openfile)
    Buttonselect.place(relx=0.1,rely=0.3)

    Buttonencode=Button(text="Encode",command=encode)
    Buttonencode.place(relx=0.4,rely=0.5)

    back_button=Button(text="Back",command=go_back)
    back_button.place(relx=0.2,rely=0.5)
    enc.mainloop()


def decode():
    main.destroy()
    dnc=Tk()
    dnc.title("decode")
    dnc.geometry("500x400+300+150") 
    
    def go_back():
        dnc.destroy()
        main.deiconify()

    fontl = tkFont.Font(family='Algerian', size=32)

    def openfile():
        global fileopen
        #global imagee
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg files, png file","*jpg *png"),("all files","*.*"))) 

    def decode():
        message=stg.reveal(fileopen)
        Label4=Label(text=message)
        Label4.place(relx=0.3,rely=0.3)


    Buttonselect=Button(text="Select File",command=openfile)
    Buttonselect.place(relx=0.1,rely=0.3)

    Buttonencode=Button(text="Decode",command=decode)
    Buttonencode.place(relx=0.4,rely=0.5)

    back_button=Button(text="Back",command=go_back)
    back_button.place(relx=0.2,rely=0.5)
    
    dnc.mainloop()


main=Tk()
main.title("img stegano")
main.geometry("500x400")
fontl = tkFont.Font(family='Algerian', size=32)




encbutton=Button(text='Encode',fg="white",bg="black",width=20,command=encode)
encbutton['font'] =fontl 
encbutton.place(relx=0.1,rely=0.3)


decbutton=Button(text='Decode',fg="white",bg="black",width=20,command=decode)
decbutton['font'] =fontl 
decbutton.place(relx=0.1,rely=0.5)


def exit():
	main.destroy()

closebutton=Button(text='EXIT',fg="white",bg="red",width=20,command=exit)
closebutton['font'] =fontl 
closebutton.place(relx=0.1,rely=0.7)

main.mainloop()