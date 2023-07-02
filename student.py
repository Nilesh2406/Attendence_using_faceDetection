
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk

class Student:
    def __init__(Self,root):
        Self.root=root
        Self.root.geometry("1540x780+0+0")
        Self.root.title("Student system")
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

        title_lbl =Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width= 1500,height=600)

        left_frame=LabelFrame(main_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="Students details",font=("times new roman",12,"bold"))
        left_frame.place(x=30,y=10,width=660,height=580)
        current_frame=LabelFrame(left_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="Personal details",font=("times new roman",12,"bold"))
        current_frame.place(x=10,y=10,width=600,height=115)
       #department
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_frame,font=("timess now roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","computer science","Information techology","Electronics and communictionn","mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    #course
        course_label=Label(current_frame,text="course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_frame,font=("timess now roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select course","Btech","BE","Mtech","BCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_frame,font=("timess now roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #semester
        sem_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        sem_combo=ttk.Combobox(current_frame,font=("timess now roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select semester","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
#class student info
        student_frame=LabelFrame(left_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="Personal details",font=("times new roman",12,"bold"))
        student_frame.place(x=10,y=130,width=600,height=190)
        #student ID
        studentID_label=Label(student_frame,text="Student id:",font=("times new roman",12,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentID_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
#student_name
        Name_label=Label(student_frame,text="Student Name:",font=("times new roman",12,"bold"))
        Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        Name_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        Name_entry.grid(row=0,column=3,padx=10,sticky=W)
#Roll_no
        studentRoll_label=Label(student_frame,text="RollNo:",font=("times new roman",12,"bold"))
        studentRoll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        studentRoll_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        studentRoll_entry.grid(row=1,column=1,padx=10,sticky=W)
#mobile no
        contact_label=Label(student_frame,text="Contact No:",font=("times new roman",12,"bold"))
        contact_label.grid(row=1,column=2,padx=10,sticky=W,pady=5)
        contact_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        contact_entry.grid(row=1,column=3,padx=10,sticky=W)
#section
        section_label=Label(student_frame,text="Section:",font=("times new roman",12,"bold"))
        section_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        section_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        section_entry.grid(row=2,column=1,padx=10,sticky=W)

#Address
        address_label=Label(student_frame,text="Address:",font=("times new roman",12,"bold"))
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        address_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=2,column=3,padx=10,sticky=W)
        #photos
        photos_label=Label(student_frame,text="Photos:",font=("times new roman",12,"bold"))
        photos_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        photos_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        photos_entry.grid(row=3,column=1,padx=10,sticky=W)
        #cc
         #photos
        cc_label=Label(student_frame,text="Section:",font=("times new roman",12,"bold"))
        cc_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        cc_entry=ttk.Entry(student_frame,width=20,font=("times new roman",12,"bold"))
        cc_entry.grid(row=3,column=3,padx=10,sticky=W)
#radio buttons
        radiobtn1=ttk.Radiobutton(student_frame,text="take a photo sample",value="yes")
        radiobtn1.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        radiobtn2=ttk.Radiobutton(student_frame,text="No photo sample",value="No")
        radiobtn2.grid(row=4,column=1,padx=10,pady=5,sticky=W)
#butto frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="black")
        btn_frame.place(x=10,y=340,width=600,height=40)
#button
        save_btn=Button(btn_frame,text="save",width=14,font=("times new roman",13,"bold"),bg="white",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",width=14,font=("times new roman",13,"bold"),bg="white",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",width=14,font=("times new roman",13,"bold"),bg="white",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",width=14,font=("times new roman",13,"bold"),bg="white",fg="black")
        reset_btn.grid(row=0,column=3)

        btn1_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="black")
        btn1_frame.place(x=10,y=400,width=600,height=40)

        photo_btn=Button(btn1_frame,text="Take photo samples",width=28,font=("times new roman",13,"bold"),bg="white",fg="black")
        photo_btn.grid(row=1,column=0)
        update_photo_btn=Button(btn1_frame,text="update photo samples",width=28,font=("times new roman",13,"bold"),bg="white",fg="black")
        update_photo_btn.grid(row=1,column=2)

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",fg="black",relief=RIDGE,text="class student information",font=("times new roman",12,"bold"))
        Right_frame.place(x=800,y=10,width=660,height=580)
       
        img_right=Image.open(r"C:\Users\asus\3D Objects\python_project\images\e.jpeg")
        img_right=img_right.resize((650,130),Image.ANTIALIAS)
        Self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=Self.photoimg_right)
        f_lbl.place(x=5,y=0,width=650,height=130)
        search_frame=LabelFrame(Right_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="search system",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=140,width=650,height=70)
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        search_combo=ttk.Combobox(search_frame,font=("timess now roman",12,"bold"),width=12,state="readonly")
        search_combo["values"]=("Select","Rollno","phoneNo")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=4,pady=10,sticky=W)
        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=4,sticky=W)

        search_btn=Button(search_frame,text="search",width=12,font=("times new roman",12,"bold"),bg="white",fg="black")
        search_btn.grid(row=0,column=3,padx=4,sticky=W)
        search1_photo_btn=Button(search_frame,text="show All",width=12,font=("times new roman",12,"bold"),bg="white",fg="black")
        search1_photo_btn.grid(row=0,column=4,padx=4)

        table_frame=Frame(Right_frame,bd=2,bg="grey",relief=RIDGE)
        table_frame.place(x=10,y=220,width=650,height=330)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        Self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","rollno","mobno","section","address","photos","cc"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Self.student_table.xview)
        scroll_y.config(command=Self.student_table.yview)
        Self.student_table.heading("dep",text="Department")
        Self.student_table.heading("course",text="Course")
        Self.student_table.heading("year",text="Year")
        Self.student_table.heading("sem",text="Semester")
        Self.student_table.heading("id",text="StudentId")
        Self.student_table.heading("name",text="Name")
        Self.student_table.heading("rollno",text="Rollo")
        Self.student_table.heading("mobno",text="Mobno")
        Self.student_table.heading("section",text="Section")
        Self.student_table.heading("address",text="Address")
        Self.student_table.heading("photos",text="photoSampleStatus")
        Self.student_table.heading("cc",text="CC")
        Self.student_table["show"]="headings"

        Self.student_table.column("dep",width=100)
        Self.student_table.column("course",width=100)
        Self.student_table.column("year",width=100)
        Self.student_table.column("sem",width=100)
        Self.student_table.column("id",width=100)
        Self.student_table.column("name",width=100)
        Self.student_table.column("rollno",width=100)
        Self.student_table.column("mobno",width=100)
        Self.student_table.column("section",width=100)
        Self.student_table.column("address",width=100)
        Self.student_table.column("photos",width=100)
        Self.student_table.column("cc",width=100)

        Self.student_table.pack(fill=BOTH,expand=1)
    



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()