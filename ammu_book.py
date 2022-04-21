'''
The Bookshop Automation Software (BAS) is to automate all operations in a bookshop.
Generally it includes the Order Processing, Stock Management and Accounts Management. Also
BAS will provide the ability to search any book using the book title or the name of the author
that are available in the shop and in case where the book is not available in the stock, it will ask
the customer to enter full details of the book for procurement of the book in future and
increment a request field for the book.
BAS will help the manager to periodically view the request field of the books so as to arrive at a
rough estimate regarding the current demand for different books. Also it maintains the price of
various books.
'''



from datetime import date, datetime
from multiprocessing import connection
from re import L
import re
from tkinter import *
from urllib import request
from PIL import ImageTk,Image, ImageSequence
from tkinter import messagebox
from tkinter.font import BOLD
import time

import mysql.connector as connector



# create a database or connect to one 
#connection=connector.connect("Bookshop_database")

#create cursor 

#cursor=connection.cursor() 

# do the related stuff



rootaccess=Tk()
rootaccess.configure(bg="orange")
rootaccess.geometry('800x680')
rootaccess.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    
    # Create Image Widget
Bookshop_img_access=ImageTk.PhotoImage((Image.open("C:Users/smile/Downloads/6.jpg")).resize((320,300)))
#Bookshop_img_access=Bookshop_img_access.resize((300,300))
    # text label-Shop name
text_label_access=Label(rootaccess,text="VS Book Store",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3')
text_label_access.grid(row=0,column=0,columnspan=3,sticky=W+E,padx=20)
    # Image label
Bookshop_img_label_access=Label(rootaccess,image=Bookshop_img_access,anchor=CENTER, relief=SUNKEN,bd=10).grid(row=1,column=1,padx=10,pady=60) 

    # title
rootaccess.title("BOOKSHOP AUTOMATION SYSTEM")
    # frame1
Bookshop_frame1_access=LabelFrame(rootaccess,text="Bookshop Automation Software :)",relief=SUNKEN)
Bookshop_frame1_access.grid(row=1,column=0,padx=10)
    # frame2
Bookshop_frame2_access=LabelFrame(rootaccess, text="Bookshop Automation Software :)",relief=SUNKEN)
Bookshop_frame2_access.grid(row=1,column=2,padx=8)
    # Label
Bookshop_label1_access=Label(Bookshop_frame1_access, text="Bookshops are the places of\n magical discoveries and\n the rediscovery of past pleasures", padx=10, pady=20, fg="darkred", bg="skyblue").pack()
Bookshop_label2_access=Label(Bookshop_frame2_access, text="That's the thing about books.\nThey let you travel without\n moving your feet", padx=20, pady=20, fg="darkred", bg="skyblue").pack()

def cart_frame_clear():
    global frame_label,serial_no,global_increment,storing_books
    for widget in frame_label.winfo_children():
        widget.destroy()
    
    frame_label=Frame(root6,highlightcolor="ivory",highlightbackground="ivory3",highlightthickness=3,height=575,width=725)
    frame_label.grid(row=1,column=0,padx=15,pady=10,columnspan=5)

    frame_heading1=Label(frame_label,text="serial no",bg="ivory3",relief=SUNKEN)
    frame_heading1.place(x=12,y=5)

    frame_heading2=Label(frame_label,text=" Title and Author of the book ",bg="ivory3",relief=SUNKEN , width=25)
    frame_heading2.place(x=87,y=5)

    frame_heading3=Label(frame_label,text="No of books",bg="ivory3",relief=SUNKEN)
    frame_heading3.place(x=300,y=5)
    
    frame_heading4=Label(frame_label,text="Cost of each book ",bg="ivory3",relief=SUNKEN)
    frame_heading4.place(x=375,y=5)

    frame_heading4=Label(frame_label,text="Total cost ",bg="ivory3",relief=SUNKEN)
    frame_heading4.place(x=500,y=5)

    frame_heading4=Label(frame_label,text="proceed ",bg="ivory3",relief=SUNKEN)
    frame_heading4.place(x=575,y=5)
    global_increment=50
    serial_no=1
    storing_books.clear()



def cart():
    global root6,x,root1,root5,Bookshop_img,Bookshop_img_label,isbn_entry,frame_label,total_book_cost
    root1.withdraw()
    root5.withdraw()
    root6=Toplevel()
    root6.configure(bg="orange")
    root6.geometry('800x680')
    root6.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root6.title("Cart||BOOKSHOP AUTOMATION SYSTEM")

    cart_text_label=Label(root6,text="MyCart",font=('Helvatical bold',20),relief=SUNKEN,bg='ivory3',padx=10,anchor=W,width=40)
    cart_text_label.grid(row=0,column=0,columnspan=10,sticky=W+E,padx=10)

    frame_label=Frame(root6,highlightcolor="ivory",highlightbackground="ivory3",highlightthickness=3,height=575,width=725)
    frame_label.grid(row=1,column=0,columnspan=5,padx=15,pady=10)

    #Bookshop_img=ImageTk.PhotoImage((Image.open("C:Users/smile/Downloads/book1.jpg")).resize((70,100)))
    #Bookshop_img_label=Label(frame_label,image=Bookshop_img,anchor=CENTER, relief=SUNKEN,bd=10)
    #Bookshop_img_label.grid(row=1,column=1,padx=10,pady=60) 

    frame_heading1=Label(frame_label,text="serial no",bg="ivory3",relief=SUNKEN)
    frame_heading1.place(x=12,y=5)

    frame_heading2=Label(frame_label,text=" Title and Author of the book ",bg="ivory3",relief=SUNKEN , width=25)
    frame_heading2.place(x=87,y=5)

    frame_heading3=Label(frame_label,text="No of books",bg="ivory3",relief=SUNKEN)
    frame_heading3.place(x=300,y=5)
    
    frame_heading4=Label(frame_label,text="Cost of each book ",bg="ivory3",relief=SUNKEN)
    frame_heading4.place(x=375,y=5)

    frame_heading4=Label(frame_label,text="Total cost ",bg="ivory3",relief=SUNKEN)
    frame_heading4.place(x=500,y=5)

    frame_heading4=Label(frame_label,text="proceed ",bg="ivory3",relief=SUNKEN)
    frame_heading4.place(x=575,y=5)

    back_button=Button(root6,text="back",command=lambda:backy(root6,root1))
    back_button.grid(row=9,column=4)

    add_book=Button(root6,text="Add to Cart" ,command=add_cart,bg="green")
    add_book.grid(row=9,column=3,padx=5)
     
    clear_cart=Button(root6,text="clear cart" ,command=cart_frame_clear,bg="ivory3")
    clear_cart.grid(row=9,column=2)
    total_book_cost=0

cart_no=1

def add_cart():
    global cart_no
    cart_no=cart_no+1
    cart_function()
    
    return

global_increment=50
serial_no=1
storing_books=[]

def cart_items():
    global global_increment,serial_no,isbn_entry,no_entry,storing_books,list_of_cart_books,storing_books1
    query="SELECT * from inventory where ISBN=(%s);"
    mycursor.execute(query,(isbn_entry.get(),))
    list_of_cart_books=mycursor.fetchone()
    
    frame_heading1=Label(frame_label,text=f"{serial_no}",bg="ivory3",relief=SUNKEN)
    frame_heading1.place(x=12,y=5+global_increment)
    
    title_lable=Label(frame_label,text=f"{list_of_cart_books[1]} \n {list_of_cart_books[2]}",padx=5)
    title_lable.place(x=87,y=5+global_increment)
    
    books_need=Label(frame_label,text=f"{int(no_entry.get())}",padx=5)
    books_need.place(x=300,y=5+global_increment)
    
    book_cost=Label(frame_label,text=f"{int(list_of_cart_books[5])}",padx=5)
    book_cost.place(x=375,y=5+global_increment)

    total_cost=Label(frame_label,text=f"{(int(list_of_cart_books[5]))*(int(no_entry.get()))}",padx=5)
    total_cost.place(x=500,y=5+global_increment)

    buy_button=Button(frame_label,text="buy",command=buy,bg="green")
    buy_button.place(x=575,y=5+global_increment)
    
    storing_books1=[(list_of_cart_books[1] ,list_of_cart_books[2],int(no_entry.get()),int(list_of_cart_books[5]),(int(list_of_cart_books[5]))*(int(no_entry.get())))]
    storing_books+=storing_books1
    global_increment=global_increment+50
    serial_no=serial_no+1

def buy():
    
    global list_of_cart_books,storing_books,no_entry,isbn_entry,total_book_cost
    total_book_cost=0
    for i in storing_books:
        total_book_cost=i[4]+total_book_cost
    print(total_book_cost)
    
def isbn_enter():
    global isbn_entry,no_entry,x,cart_no
    query='SELECT * from inventory'
    mycursor.execute(query)
    list_of_books=(mycursor.fetchall())
    len_list=len(list_of_books)
   
    s=0
    for i in list_of_books:
        digit_check=no_entry.get().isdigit()

        if no_entry.get()=="" or no_entry.get()==" " :
            messagebox.showwarning('Warning',"Sorry,incorrect input")
            no_entry.delete(0,END)
            isbn_entry.delete(0,END)

        elif digit_check==False :
            messagebox.showwarning('Warning',"Sorry,Incorrect input")
            no_entry.delete(0,END)
            break
        
        elif int(no_entry.get())>i[4]:
            messagebox.showwarning('Warning',"Sorry,Out of stock")
            no_entry.delete(0,END)
            break

        elif (isbn_entry.get().lower()==i[0].lower())and int(no_entry.get())<=i[4]:
            x=i
            if cart_no==1:
                cart()
                cart_items()
                break
            elif cart_no>1:
                cart_items()
                break

        elif s==len_list-1:
            if(isbn_entry.get().lower()!=i[0].lower()):
                
                messagebox.showerror("Error","Incorrect ISBN pin")
                isbn_entry.delete(0,END)
                break
            elif  int(no_entry.get())>i[4]:
                messagebox.showwarning('Warning',"Sorry,Out of stock")
                no_entry.delete(0,END)
                break
        else:
            s=s+1
            pass

def backy(present,past):
    global rootaccess,root,root1,root3,root5,root6
    present.withdraw()
    past.wm_deiconify()    

def cart_function():
    global isbn_entry,no_entry,root5
    root5=Toplevel()
    #root5.configure(bg="orange")
    root5.geometry('300x200')
    root5.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root5.title("BOOKSHOP AUTOMATION SYSTEM")
    isbn_lable=Label(root5,text="Enter ISBN :",bg="ivory3",padx=10)
    isbn_lable.grid(row=0,column=0)
    isbn_entry=Entry(root5,width="25",borderwidth=5)
    isbn_entry.grid(row=0,column=1,columnspan=2)

    no_lable=Label(root5,text="No of books:",bg="ivory3",padx=10)
    no_lable.grid(row=1,column=0,padx=5)
    no_entry=Entry(root5,width="25",borderwidth=5)
    no_entry.grid(row=1,column=1,padx=5,columnspan=2)

    isbn_button=Button(root5,text="Enter",command=isbn_enter)
    isbn_button.grid(row=5,column=2)


def frame_clear():
    global Frame_box,Frame_box1
    for widget in Frame_box.winfo_children():
        widget.destroy()
    Frame_box1=Frame(root1,highlightcolor="ivory",height=575,width=725,highlightbackground="ivory3",highlightthickness=3)
    Frame_box1.grid(row=2,column=1,rowspan=9,columnspan=5,padx=5,pady=10)
    frame_label1=Label(Frame_box1,text=" ISBN no ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label1.place(x=12,y=5)
    frame_label2=Label(Frame_box1,text=" Name of the book/Title of the book ",bd=5,relief=SUNKEN,padx=2,justify='center',bg='ivory3')
    frame_label2.place(x=87,y=5)
    frame_label3=Label(Frame_box1,text="Author of the book ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label3.place(x=312,y=5)
    frame_label4=Label(Frame_box1,text=" Rack number ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label4.place(x=442,y=5)
    frame_label5=Label(Frame_box1,text=" No of books ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label5.place(x=537,y=5)
    frame_label6=Label(Frame_box1,text=" cost/book ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label6.place(x=632,y=5)
    searching_enter()


def query():
    global name_entry,contact_entry,address_entry
    #print(curr_name+" "+curr_add+" "+curr_no)
    query1="INSERT INTO customer_details(full_name,contact_no,address) values(%s,%s,%s);"
    mycursor.execute(query1,(name_entry.get(),contact_entry.get(),address_entry.get()))
    query2="SELECT * FROM customer_details;"
    mycursor.execute(query2)
    list1=mycursor.fetchall()
    print(list1)


def update_stock():
    global Search_entry
    query3="INSERT INTO stock_update(stock_to_update) values ({});".format(Search_entry.get())
    mycursor.execute(query3)
    query4="SELECT * FROM stock_update;"
    mycursor.execute(query4)
    list2=mycursor.fetchall()
    print(list2)
    

def searching_enter():
    global Search_entry,Frame_box1
    query2="SELECT * from inventory  ;"
    mycursor.execute(query2)
    list_of_selected_books=(mycursor.fetchall())
    list_length=len(list_of_selected_books)
    if Search_entry.get()==" " or Search_entry.get()=="":
        messagebox.showwarning("Warning","Null entry, please enter vaild text")
        Search_entry.delete(0,END)

    elif Search_entry.get()!=" " or Search_entry.get()!="":
        sum=50
        s=1
        for i in list_of_selected_books:
            
            if (i!=list_of_selected_books[list_length-1]) and ((Search_entry.get().lower() in i[1].lower())or(Search_entry.get().lower() in i[2].lower())):
                frame_label11=Label(Frame_box1,text=i[0],bd=5,padx=2,justify='left')
                frame_label11.place(x=12,y=5+sum)
                frame_label2=Label(Frame_box1,text=i[1],bd=5,padx=2,justify='center')
                frame_label2.place(x=87,y=5+sum)
                frame_label3=Label(Frame_box1,text=i[2],bd=5,padx=2,justify='left',)
                frame_label3.place(x=312,y=5+sum)
                frame_label4=Label(Frame_box1,text=i[3],bd=5,padx=2,justify='left')
                frame_label4.place(x=442,y=5+sum)
                frame_label5=Label(Frame_box1,text=i[4],bd=5,padx=2,justify='left')
                frame_label5.place(x=537,y=5+sum)
                frame_label6=Label(Frame_box1,text=i[5],bd=5,padx=2,justify='left')
                frame_label6.place(x=632,y=5+sum)
                sum=sum+50
                
                

            elif (i==list_of_selected_books[list_length-1])and((Search_entry.get().lower() in i[1].lower())or(Search_entry.get().lower() in i[2].lower())):               
                frame_label11=Label(Frame_box1,text=i[0],bd=5,padx=2,justify='left')
                frame_label11.place(x=12,y=5+sum)
                frame_label2=Label(Frame_box1,text=i[1],bd=5,padx=2,justify='center')
                frame_label2.place(x=87,y=5+sum)
                frame_label3=Label(Frame_box1,text=i[2],bd=5,padx=2,justify='left',)
                frame_label3.place(x=312,y=5+sum)
                frame_label4=Label(Frame_box1,text=i[3],bd=5,padx=2,justify='left')
                frame_label4.place(x=442,y=5+sum)
                frame_label5=Label(Frame_box1,text=i[4],bd=5,padx=2,justify='left')
                frame_label5.place(x=537,y=5+sum)
                frame_label6=Label(Frame_box1,text=i[5],bd=5,padx=2,justify='left')
                frame_label6.place(x=632,y=5+sum)
                sum=sum+50
                
                break  
            elif i==list_of_selected_books[list_length-1]: 
                break
            
            elif(s==list_length-1):
                k= messagebox.showinfo("Information","Sorry,we cant find any thing related to your query")            
                break
            else:
                s=s+1
                pass
    else:
        messagebox.showwarning("Warning","Something went wrong please try again later")

def request_field():
    global root1,request_win,req_author_name_entry,req_book_title_entry,req_contact_no_entry,req_customer_name_entry
    request_win=Toplevel()
    root1.withdraw()
    request_win.geometry('800x680') 

    request_field_label=Label(request_win,text="Enter details fro procurement",bg='violet',padx=20,relief=SUNKEN,borderwidth=5)
    request_field_label.place(x=5,y=120)

    text_label_access=Label(request_win,text="VS Book Store",font=('Helvatical bold',30),relief=SUNKEN,bg='ivory3',padx=120)
    text_label_access.grid(row=0,column=0,columnspan=3,sticky=W+E,padx=40)

    customer_name=Label(request_win,text="Name",relief=SUNKEN,padx=14,pady=5)
    customer_name.place(x=5,y=150)
    contact_no=Label(request_win,text="Contact",relief=SUNKEN,padx=9,pady=5)
    contact_no.place(x=5,y=190)
    book_title=Label(request_win,text="Title",relief=SUNKEN,padx=18,pady=5)
    book_title.place(x=5,y=230)
    author_name=Label(request_win,text="Author",relief=SUNKEN,padx=11,pady=5)
    author_name.place(x=5,y=270)
    
    req_customer_name_entry=Entry(request_win,width=80,borderwidth=5)
    req_customer_name_entry.place(x=80,y=150)
    req_contact_no_entry=Entry(request_win,width=80,borderwidth=5)
    req_contact_no_entry.place(x=80,y=190)
    req_book_title_entry=Entry(request_win,width=80,borderwidth=5)
    req_book_title_entry.place(x=80,y=230)
    req_author_name_entry=Entry(request_win,width=80,borderwidth=5)
    req_author_name_entry.place(x=80,y=270)
    
    insert_button=Button(request_win,text="Submit",relief=SUNKEN,padx=15,pady=8,bd=5,fg="green",command=request_checking)
    insert_button.place(x=250,y=370) 



def request_submitted():
    global request_win,req_author_name_entry,req_book_title_entry,req_contact_no_entry,req_customer_name_entry,root1,Query
    
   
    date_time=datetime.now()
    now1=date_time.strftime("%D  %H:%M:%S")
    print(now1)
    a=req_customer_name_entry.get()
    b=req_contact_no_entry.get()
    c=req_book_title_entry.get()
    d=req_author_name_entry.get()
    Query="INSERT INTO request_field (date_time,contact_name,contact_no,request_book_title,request_book_author) values(%s,%s,%s,%s,%s)"
    mycursor.execute(Query,(now1,a,b,c,d))
    k=mycursor.fetchall()
    print(k)
    for i in k:
        print(i)
    messagebox.showinfo('information',"thanks, we will update soon")

    root1.wm_deiconify()
    request_win.withdraw()

def request_checking():
    global request_win,req_author_name_entry,req_book_title_entry,req_contact_no_entry,req_customer_name_entry,root1
    curr_name=req_customer_name_entry.get()
    curr_no=req_contact_no_entry.get()

    alpha=(curr_no.isdigit())

    if(curr_name=="" or curr_name==" "):
        messagebox.showwarning(" ALERT!","Input the thing you are looking for :) ")
        req_customer_name_entry.delete(0,END)
        
    if(len(curr_name)<=6 or len(curr_name)>=25):
        messagebox.showinfo("Alert","Sorry,length of name should be lessthan 25 letters greaterthan 7 letters")
        req_customer_name_entry.delete(0,END)    

    elif (len(req_contact_no_entry.get())!=10):
        messagebox.showerror("Alert","Insufficient Numbers to store ")
        req_contact_no_entry.delete(0,END)
        
    elif (alpha==False):
        messagebox.showwarning("Alert","Unexpected input value ")
        req_contact_no_entry.delete(0,END)

    elif(len(req_book_title_entry.get())<5):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Address should be more than 5 characters")
        if(prompt_reply==True):
            req_book_title_entry.delete(0, END) 
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                request_win.destroy()
            else:
                req_book_title_entry.delete(0, END)
    elif(len(req_author_name_entry.get())<5):
        prompt_reply=messagebox.askretrycancel(" ALERT!","Click Retry to enter again or Cancel to Exit \n Hint: Address should be more than 5 characters")
        if(prompt_reply==True):
            (req_author_name_entry.delete(0, END) )
        else:
            yes_no=messagebox.askyesno("Request","Click 'YES' to quit or 'NO' to continue")
            if(yes_no==True):
                request_win.destroy()
            else:
                req_author_name_entry.delete(0, END)
    else:
        request_submitted()

def new_window():
    global root,rootaccess,root1,Search_entry,Frame_box
    root.withdraw()
    root1=Toplevel()
    root1.configure(bg="orange")
    root1.geometry('800x680')
    root1.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root1.title("BOOKSHOP AUTOMATION SYSTEM")
    
    search_label=Label(root1,text="Search:",anchor=E,relief=SUNKEN,padx=10)
    search_label.grid(row=1,column=0)
    Search_entry=Entry(root1,width=100,borderwidth=5)
    Search_entry.grid(row=1,column=1,columnspan=3)
    buttpn=Button(root1,text="back",command=lambda:backy(root1,root))
    buttpn.grid(row=12,column=3,sticky=W+S,pady=5)
    search_enter=Button(root1,text="Enter",command=frame_clear)
    search_enter.grid(row=12,column=2,sticky=W+S,pady=5,padx=5)
    request_field_but=Button(root1,text="Request",font=('Helvatical bold',10),command=request_field,bg="green")
    request_field_but.grid(row=1,column=4)
    cart_button=Button(root1,text="Add to cart",fg="green",command=cart_function)
    cart_button.grid(row=12,column=4)

    Frame_box=Frame(root1,highlightcolor="ivory",height=575,width=725,highlightbackground="ivory3",highlightthickness=3)
    Frame_box.grid(row=2,column=1,rowspan=9,columnspan=5,padx=5,pady=10)
    frame_label1=Label(Frame_box,text=" ISBN no ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label1.place(x=12,y=5)
    frame_label2=Label(Frame_box,text=" Name of the book/Title of the book ",bd=5,relief=SUNKEN,padx=2,justify='center',bg='ivory3')
    frame_label2.place(x=87,y=5)
    frame_label3=Label(Frame_box,text="Author of the book ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label3.place(x=312,y=5)
    frame_label4=Label(Frame_box,text=" Rack number ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label4.place(x=442,y=5)
    frame_label5=Label(Frame_box,text=" No of books ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label5.place(x=537,y=5)
    frame_label6=Label(Frame_box,text=" cost/book ",bd=5,relief=SUNKEN,padx=2,justify='left',bg='ivory3')
    frame_label6.place(x=632,y=5)



def details_entry():                                                                                                                                                                                                  
    global name_entry,contact_entry,address_entry,k,storing_data,mycursor,query,s,curr_add,curr_name,curr_no
    curr_name=name_entry.get()
    curr_add=address_entry.get()
    curr_no=contact_entry.get()
    #ok=int(curr_no)
    #alpha=((any(i)>=ascii(65)and any(i)<=ascii(90))or(any(i)>=ascii(97)and any(i)<=ascii(122))for i in contact_entry.get())
    alpha=(curr_no.isdigit())

    if(curr_name=="" or curr_name==" "):
        messagebox.showwarning(" ALERT!","Input the thing you are looking for :) ")
        name_entry.delete(0,END)
        
    if(len(curr_name)<=6 or len(curr_name)>=25):
        messagebox.showinfo("Alert","Sorry,length of name should be lessthan 25 letters greaterthan 7 letters")
        name_entry.delete(0,END)    

    elif (len(contact_entry.get())!=10):
        messagebox.showerror("Alert","Insufficient Numbers to store ")
        contact_entry.delete(0,END)
        
    elif (alpha==False):
        messagebox.showwarning("Alert","Unexpected input value ")
        contact_entry.delete(0,END)

    elif(len(curr_add)<=0 or len(curr_add)>=50):
        messagebox.showwarning('alert',"Unexpected error in address area, please enter again")
        address_entry.delete(0,END)

    else:
        query()
        new_window()

    
    
def customer_window():
    #rootaccess.destroy()
    rootaccess.withdraw()
    global root
    global Bookshop_img
    global name_entry,contact_entry,address_entry,back
    # main window
    root=Toplevel()
    
    # changing the colour of main window
    root.configure(bg="orange")

    # Geometry or dimensions of root Window
    root.geometry('800x680')
    # Displaying Icon
    root.iconbitmap('C:/Users/smile/Downloads/boo.ico')
    
    # Create Image Widget
    Bookshop_img=ImageTk.PhotoImage(Image.open("C:Users/smile/Downloads/7.jpg").resize((400,250)))
    Bookshop_img_label=Label(root,image=Bookshop_img,anchor=E, relief=SUNKEN,bd=10)
    Bookshop_img_label.grid(row=1,column=1,padx=10,pady=50) 
    # text label-Shop name
        # text label-Shop name
    text_label=Label(root,text="VS Book Store",font=('Helvatical bold',50),relief=SUNKEN,bg='ivory3')
    text_label.grid(row=0,column=0,columnspan=5,sticky=W+E,padx=20)

    fame=LabelFrame(root,text="quote",bg="lightgreen")
    fame.grid(row=1,column=0,padx=10)
    lee=Label(fame,text="Explore the world's \nknowledge today,\n discover tomorrow",padx=20,bg="lightgreen")
    lee.grid(row=0,column=0)

    fame1=LabelFrame(root,text="quote",bg="lightgreen")
    fame1.grid(row=1,column=2,padx=10)
    lee1=Label(fame1,text="Explore the world's \nknowledge today,\n discover tomorrow",padx=20,bg="lightgreen")
    lee1.grid(row=0,column=0)
    # Image label
    # title
    root.title("BOOKSHOP AUTOMATION SYSTEM")
    # Label
    #Status_bar_1=Label(root,text="Explore the world's knowledge today, discover tomorrow",anchor=CENTER,padx=50,font=(("Helvetica",20)),bg="lightgreen",fg="darkblue")
    #Status_bar_1.place(x=10,y=630)

    name_label=Label(root,text="Full Name:",font=('Helvatical bold',10),relief=SUNKEN,padx=25)
    name_label.grid(row=2,column=0,sticky=E,padx=20)
    contact_label=Label(root,text="Contact No:",font=('Helvatical bold',10),relief=SUNKEN,padx=21)
    contact_label.grid(row=3,column=0,sticky=E,padx=20)
    address_label=Label(root,text="Address:",font=('Helvatical bold',10),relief=SUNKEN,padx=30)
    address_label.grid(row=4,column=0,sticky=E,padx=20)

    name_entry=Entry(root,width=100,borderwidth=5)
    name_entry.grid(row=2,column=1,columnspan=2,pady=5)
    contact_entry=Entry(root,width=100,borderwidth=5)
    contact_entry.grid(row=3,column=1,columnspan=2,pady=5)
    address_entry=Entry(root,width=100,borderwidth=5)
    address_entry.grid(row=4,column=1,columnspan=2,pady=5)
    
    # open button in main window
    #Open_button=Button(root,text="OPEN",padx=5,pady=5,relief=SUNKEN,bg="green", anchor=CENTER, command=open_availability)
    #Open_button.grid(row=2,column=1)

    coustomer_detail_enter=Button(root,text="Enter",command=new_window,bg="limegreen",font=('Helvatical bold',10))
    coustomer_detail_enter.grid(row=5,column=1,padx=20,pady=5)
    
    back=Button(root,text="back",command=lambda:backy(root,rootaccess))
    back.grid(row=7,column=1)


def enter_button():
    global input_name
    global curr_name
    
    curr_name=input_name.get()
    if(curr_name=="" or curr_name==" "):
        messagebox.showwarning(" ALERT!","Input the thing you are looking for :) ")
    else:
        input_name.delete(0, END)

        #database_window()
    
    
def clear_button():
    global input_name
    input_name.delete(0,END)

    
def exit_button():
    #yes_no messagebox
    yes_no=messagebox.askyesno("Warning ","Do you really want to exit? ")
    global root2

    if(yes_no==1):
        
        root2.destroy()
        
    elif(yes_no==0):
        return

def customer():
    customer_window()

def salesman_window():
    global root3,root_s
    root3.withdraw()
    root_s=Toplevel()
    root_s.configure(bg="orange")
    root_s.geometry('800x680')
    root_s.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root_s.title("Salesman||BOOKSHOP AUTOMATION SYSTEM")

    back_button=Button(root_s,text="back",command=lambda:backy(root_s,rootaccess),pady=5)
    back_button.grid(row=5,column=2,padx=10,pady=5)


def details_check():
    global publisher_name_entry,publisher_contact_entry,publisher_address_entry,mycursor2,mycursor3
    global update_isbn_entry,update_title_entry,update_author_entry,update_rack_no_entry,update_no_of_books_entry,update_cost_entry

    name=publisher_name_entry.get()
    num=publisher_contact_entry.get()
    add=publisher_address_entry.get()

    isbn=update_isbn_entry.get()
    title=update_title_entry.get()
    author=update_author_entry.get()
    rack=update_rack_no_entry.get()
    no=int(update_no_of_books_entry.get())
    cost=update_cost_entry.get()

    mycursor2=storing_data.cursor()
    mycursor3=storing_data.cursor()

    query1="INSERT INTO publisher_information (publisher_name,contact_no,address,book_title,no_of_books) values(%s,%s,%s,%s,%s);"
    mycursor2.execute(query1,(name,num,add,title,no))
    cus1=mycursor2.fetchall()
    print(cus1)
    for i in cus1:
        print(i)

    query2="INSERT INTO inventory (ISBN,title,author,rack_no,no_of_books,cost) values(%s,%s,%s,%s,%s,%s);"
    mycursor3.execute(query2,(isbn,title,author,rack,no,cost))
    cus2=mycursor3.fetchall()
    print(cus2)
    for i in cus2:
        print(i)
    
    messagebox.showinfo("Granted","Successfully Updated")

def employee_work():
    global root_e,root_e_w,root3,publisher_name_entry,publisher_contact_entry,publisher_address_entry
    global update_isbn_entry,update_title_entry,update_author_entry,update_rack_no_entry,update_no_of_books_entry,update_cost_entry
    root_e.withdraw()
    root_e_w=Toplevel()
    root_e_w.configure(bg="orange")
    root_e_w.geometry('800x680')
    root_e_w.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root_e_w.title("Employee||BOOKSHOP AUTOMATION SYSTEM")

    

    publisher_name_label=Label(root_e_w,text="Publisher name",relief=SUNKEN)
    publisher_name_label.place(x=5,y=110)
    publisher_contact_no_label=Label(root_e_w,text="Contact no",relief=SUNKEN)
    publisher_contact_no_label.place(x=5,y=150)
    publisher_address_label=Label(root_e_w,text="Address",relief=SUNKEN)
    publisher_address_label.place(x=5,y=190)

    update_isbn_label=Label(root_e_w,text="ISBN of the book",relief=SUNKEN)
    update_isbn_label.place(x=5,y=230)
    update_title_label=Label(root_e_w,text="Title of the book",relief=SUNKEN)
    update_title_label.place(x=5,y=270)
    update_author_label=Label(root_e_w,text="Author name",relief=SUNKEN)
    update_author_label.place(x=5,y=310)
    update_rack_no_label=Label(root_e_w,text="Rack_no",relief=SUNKEN)
    update_rack_no_label.place(x=5,y=350)
    update_no_of_books_label=Label(root_e_w,text="No of books updated",relief=SUNKEN)
    update_no_of_books_label.place(x=5,y=390)
    update_cost_label=Label(root_e_w,text="Cost of each book",relief=SUNKEN)
    update_cost_label.place(x=5,y=430)


    publisher_name_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    publisher_name_entry.place(x=125,y=110)
    publisher_contact_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    publisher_contact_entry.place(x=125,y=150)
    publisher_address_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    publisher_address_entry.place(x=125,y=190)

    update_isbn_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    update_isbn_entry.place(x=125,y=230)
    update_title_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    update_title_entry.place(x=125,y=270)
    update_author_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    update_author_entry.place(x=125,y=310)
    update_rack_no_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    update_rack_no_entry.place(x=125,y=350)
    update_no_of_books_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    update_no_of_books_entry.place(x=125,y=390)
    update_cost_entry=Entry(root_e_w,width=80,bd=5,relief=SUNKEN)
    update_cost_entry.place(x=125,y=430)

    insert_button=Button(root_e_w,text="Submit",relief=SUNKEN,padx=15,pady=8,bd=5,bg="green",command=cross_check)
    insert_button.place(x=170,y=520)

    back_button=Button(root_e_w,text=" back ",command=lambda:backy(root_e_w,root_e),padx=15,pady=8,bd=5,relief=SUNKEN,bg="ivory3")
    back_button.place(x=570,y=520)

def employee():
    global root3,root_e
    root3.withdraw()
    root_e=Toplevel()
    root_e.configure(bg="orange")
    root_e.geometry('800x680')
    root_e.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root_e.title("Employee||BOOKSHOP AUTOMATION SYSTEM")

    update_label=Button(root_e,text="  Update Stock  ",font=(("Times New Roman",15)),relief=SUNKEN,padx=40,pady=5,borderwidth=2,bg="Violet",command=employee_work)
    update_label.place(x=230,y=90)

    back_button=Button(root_e,text="back",command=lambda:backy(root_e,rootaccess),pady=5,padx=15)
    back_button.place(x=300,y=520)

def cross_check():
    global publisher_name_entry,publisher_contact_entry,publisher_address_entry,mycursor2,mycursor3
    global update_isbn_entry,update_title_entry,update_author_entry,update_rack_no_entry,update_no_of_books_entry,update_cost_entry

    name=publisher_name_entry.get()
    num=publisher_contact_entry.get()
    is_dis=num.isdigit()
    add=publisher_address_entry.get()

    isbn=update_isbn_entry.get()
    title=update_title_entry.get()
    author=update_author_entry.get()
    rack=update_rack_no_entry.get()
    no=(update_no_of_books_entry.get())
    is_num=no.isdigit()
    print(no)
    cost=update_cost_entry.get()

    if len(name)<=6:
        messagebox.showwarning("Alert","Enter full name")
        publisher_name_entry.delete(0,END)
    elif len(num)!=10 and is_dis==False:
        messagebox.showerror("Alert","Enter correct contact number")
        publisher_contact_entry.delete(0,END)
    elif len(add)<=7:
        messagebox.showwarning("Alert",'Address should be 7 characters minimum')
        publisher_address_entry.delete(0,END)
    elif len(title)<=6:
        messagebox.showwarning("Alert","Enter full book name")
        update_title_entry.delete(0,END)
    elif len(isbn)<=4:
        messagebox.showwarning("Alert","Enter correct isbn")
        update_isbn_entry.delete(0,END)
    elif len(author)<=6:
        messagebox.showwarning("Alert","Enter full name of author")
        update_author_entry.delete(0,END)
    elif is_num==False:
        messagebox.showerror("Alert","No of books should be in integer")
        update_no_of_books_entry.delete(0,END)
    else:
        message_box()

    



def message_box():
    global publisher_name_entry,publisher_contact_entry,publisher_address_entry,mycursor2,mycursor3
    global update_isbn_entry,update_title_entry,update_author_entry,update_rack_no_entry,update_no_of_books_entry,update_cost_entry

    k=messagebox.askyesno('Cross Check',"Are you sure that the above information is True")
    if k==1:
        details_check()
    else:
        publisher_address_entry.delete(0,END)
        publisher_contact_entry.delete(0,END)
        publisher_name_entry.delete(0,END)

        update_author_entry.delete(0,END)
        update_cost_entry.delete(0,END)
        update_isbn_entry.delete(0,END)
        update_no_of_books_entry.delete(0,END)
        update_rack_no_entry.delete(0,END)
        update_title_entry.delete(0,END)

def manager_view():
    global root_m,root_m_
    root_m_v=Toplevel()

    root_m_v.configure(bg="orange")
    root_m_v.geometry('800x680')
    root_m_v.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root_m_v.title("Manager||BOOKSHOP AUTOMATION SYSTEM")
    
    request_field_frame=Frame(root_m_v,padx=10,pady=10,bg='Ivory3')
    request_field_frame.place(x=30,y=80,height=400,width=730)
    
    
    customer_name_label=Label(request_field_frame,text="customer name",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=25,anchor=CENTER,bg="violet")
    customer_name_label.place(x=20,y=5)
    title_label=Label(request_field_frame,text="Title ",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=60,bg="violet")
    title_label.place(x=370,y=5)
    author_label=Label(request_field_frame,text="Author",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=60,bg="violet")
    author_label.place(x=545,y=5)
    contact_label=Label(request_field_frame,text="Contact Number",font=("Helvetica",10),relief=SUNKEN,borderwidth=3,padx=15,bg="violet")
    contact_label.place(x=190,y=5)

    query="SELECT contact_name,contact_no,request_book_title,request_book_author FROM request_field;"
    mycursor.execute(query)
    request_list=mycursor.fetchall()
    size=0
    if(request_list):
        for item in request_list:
            customer_name_label1=Label(request_field_frame,text=item[0],font=("Helvetica",9,"bold"),anchor=CENTER,bg="ivory3")
            customer_name_label1.place(x=30,y=60+size)
            title_label1=Label(request_field_frame,text=f"{item[1]}",font=("Helvetica",9,"bold"),padx=2,bg="ivory3")
            title_label1.place(x=385,y=60+size)
            author_label1=Label(request_field_frame,text=item[2],font=("Helvetica",9,"bold"),padx=4,bg="ivory3")
            author_label1.place(x=555,y=60+size)
            contact_label=Label(request_field_frame,text=item[3],font=("Helvetica",9,"bold"),padx=15,bg="ivory3")
            contact_label.place(x=200,y=60+size)
        
            size+=55
    else:
        not_found_label1=Label(request_field_frame,text="NOT FOUND i.e., NO DATA AVAILABLE",font=("Helvetica",12,"bold"),anchor=CENTER,bg="ivory3")
        not_found_label1.place(x=250,y=100)
    Logout_button=Button(root_m_v,text=" Back ",relief=SUNKEN,bg="red",command=lambda: backy(root_m_v,rootaccess), anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)),borderwidth=5)
    Logout_button.place(x=350,y=620)

def manager():
    global root3,root_m
    root3.withdraw()
    root_m=Toplevel()
    root_m.configure(bg="orange")
    root_m.geometry('800x680')
    root_m.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root_m.title("Manager||BOOKSHOP AUTOMATION SYSTEM")

    request_field_button=Button(root_m,text="View Request Field",font=(("Times New Roman",15)),relief=SUNKEN,bg="green",padx=5,pady=5,borderwidth=5,command=manager_view)
    request_field_button.place(x=230,y=20)

    back_button=Button(root_m,text="back",command=lambda:backy(root_m,rootaccess),pady=5)
    back_button.place(x=300,y=520)

def owner():
    global root3,root_o
    root3.withdraw()
    root_o=Toplevel()
    root_o.configure(bg="orange")
    root_o.geometry('800x680')
    root_o.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root_o.title("Owner||BOOKSHOP AUTOMATION SYSTEM")

    back_button=Button(root_o,text="back",command=lambda:backy(root_o,rootaccess),pady=5)
    back_button.grid(row=5,column=2,padx=10,pady=5)


def member_entry():
    global mycursor1,id_entry,password_entry
    storing_data=connector.connect(host="localhost", database='bookshop_automation',user="root",passwd="Sravya@1528")
    mycursor1=storing_data.cursor()
    mycursor1.execute("select * from bookshop_automation.employ_details")
    list_members=mycursor1.fetchall()
    len_incre=0
    for i in list_members:
        len_incre=len_incre+1
    print(len_incre)
    increment=0
    
    for i in list_members:
        
        int_id=id_entry.get().isdigit()
       
        if int_id:
            if increment<=len_incre:
                if i[1]==int(id_entry.get()) and i[3]==password_entry.get():
                    if i[4]=='salesman':
                        salesman_window()
                    
                    elif i[4]=='employee':
                        employee()
                    elif i[4]=="manager":
                        manager()
                    elif i[4]=="owner":
                        owner()
                    break
                elif i[1]==int(id_entry.get()) and i[3]!=password_entry.get():
                    messagebox.showwarning("Warning","Entered wrong password")
                    password_entry.delete(0,END)
                    break
                elif increment==len_incre-1:
                    messagebox.showwarning("Warning","Entered wrong password or wrong id")
                    id_entry.delete(0,END)
                    password_entry.delete(0,END)
                    break
                else:
                   increment=increment+1
                   print(increment)

            else:
                messagebox.showwarning("Warning","Entered wrong password or wrong id")
                id_entry.delete(0,END)
                password_entry.delete(0,END)
                break
    
        else:
            messagebox.showwarning("Warning","Entered wrong password or wrong id")
            id_entry.delete(0,END)
            password_entry.delete(0,END)
            break

    
def VS_Member():
    global rootaccess
    global root3,id_entry,password_entry,image_vs,image_vs_label
    rootaccess.withdraw()
    root3=Toplevel()
    root3.configure(bg="orange")
    root3.geometry('800x680')
    root3.iconbitmap("C:/Users/smile/Downloads/boo.ico")
    root3.title("BOOKSHOP AUTOMATION SYSTEM")
    #C:Users/smile/Downloads/6.jpg

    image_vs=ImageTk.PhotoImage((Image.open("C:/Users/smile/Downloads/23.jpg")).resize((320,300)))
    image_vs_label=Label(root3,image=image_vs,anchor=CENTER, relief=SUNKEN,bd=10,bg="orange")
    image_vs_label.place(x=255,y=70)
    text_label_access=Label(root3,text="VS Member",font=('Helvatical bold',30),relief=SUNKEN,bg='ivory3',padx=190)
    text_label_access.place(x=115,y=10)

    id_entry=Entry(root3,width=45,borderwidth=5)
    id_entry.place(x=325,y=395)

    id_label=Label(root3,text="VS member ID",borderwidth=5,relief=SUNKEN)
    id_label.place(x=225,y=395)

    password_entry=Entry(root3,show="*",width=45,borderwidth=5)
    password_entry.place(x=325,y=425)

    password_label=Label(root3,text="    Password    ",borderwidth=5,relief=SUNKEN)
    password_label.place(x=225,y=425)

    member_entry_but=Button(root3,text="Enter",command=member_entry,pady=5,padx=15)
    member_entry_but.place(x=225,y=500)

    back_button=Button(root3,text="back",command=lambda:backy(root3,rootaccess),pady=5,padx=15)
    back_button.place(x=445,y=500)

    return
# two buttons
VS_button=Button(rootaccess,text="VS Member",relief=SUNKEN,bg="lightgreen",command=VS_Member, anchor=CENTER,padx=30,pady=10,font=(("Times New Roman",15)))
VS_button.place(x=230,y=480)
customer_button=Button(rootaccess,text="Customer",relief=SUNKEN,bg="lightgreen",command=customer,anchor=CENTER,padx=38,pady=10,font=(("Times New Roman",15)))
customer_button.place(x=405,y=480)

Status_bar=Label(rootaccess,text="WELCOME TO THE NEW VERSION OF BOOKSTORE",anchor=CENTER,padx=50,font=(("Helvetica",20)),bg="orange",fg="darkblue")
Status_bar.place(x=10,y=630)

'''
Manager_button=Button(rootaccess,text="Manager",relief=SUNKEN,bg="lightcyan",command=employee)
Manager_button.place(x=400,y=500)
Bookshop_owner_button=Button(rootaccess,text="Bookshop_owner",relief=SUNKEN,bg="lightcyan",command=customer)
Bookshop_owner_button.place(x=400,y=540)
Sales_Clerk_button=Button(rootaccess,text="Sales_Clerk",relief=SUNKEN,bg="lightcyan",command=employee,padx=50,pady=20)
Sales_Clerk_button.place(x=50,y=500)
'''
storing_data=connector.connect(host="localhost",database='bookshop_automation',user="root",passwd="Sravya@1528")
mycursor=storing_data.cursor()


rootaccess.mainloop()
storing_data.commit()


