from tkinter import*
from tkinter import ttk
from tkinter.font import ITALIC
from PIL import Image,ImageTk
from numpy import place

class Face_Recognition_System:
    def __init__(Self,root):
        Self.root=root
        Self.root.geometry("1540x780+0+0")
        Self.root.title("Face_Recognition_System")

        img=Image.open(r"C:\Users\asus\3D Objects\python_project\images\a.jpeg")
        img=img.resize((510,130),Image.ANTIALIAS)
        Self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(Self.root,image=Self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)


        img1=Image.open(r"C:\Users\asus\3D Objects\python_project\images\a.jpeg")
        img1=img1.resize((510,130),Image.ANTIALIAS)
        Self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(Self.root,image=Self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=130)

        img2=Image.open(r"C:\Users\asus\3D Objects\python_project\images\a.jpeg")
        img2=img2.resize((510,130),Image.ANTIALIAS)
        Self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(Self.root,image=Self.photoimg2)
        f_lbl.place(x=1020,y=0,width=510,height=130)

        img3=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img3=img3.resize((1550,730),Image.ANTIALIAS)
        Self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(Self.root,image=Self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=730)

        title_lbl =Label(bg_img,text="FACE RECOGNITION AND ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
#button start
        img4=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        Self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=Self.photoimg4,cursor="hand2")
        b1.place(x=250,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Students Details",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=250,y=300,width=220,height=40)

        img5=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        Self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=Self.photoimg5,cursor="hand2")
        b1.place(x=520,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=520,y=300,width=220,height=40)


        img6=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        Self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=Self.photoimg6,cursor="hand2")
        b1.place(x=790,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=790,y=300,width=220,height=40)

        img7=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        Self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=Self.photoimg7,cursor="hand2")
        b1.place(x=1060,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1060,y=300,width=220,height=40)

        img8=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        Self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=Self.photoimg8,cursor="hand2")
        b1.place(x=370,y=370,width=220,height=220)
        b1_1=Button(bg_img,text="photos",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=370,y=570,width=220,height=40)

        img9=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        Self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=Self.photoimg9,cursor="hand2")
        b1.place(x=640,y=370,width=220,height=220)
        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=640,y=570,width=220,height=40)

        img10=Image.open(r"C:\Users\asus\3D Objects\python_project\images\data.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        Self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=Self.photoimg10,cursor="hand2")
        b1.place(x=910,y=370,width=220,height=220)
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=910,y=570,width=220,height=40)


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()