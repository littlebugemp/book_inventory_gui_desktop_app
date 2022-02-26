from tkinter import *
import backend

window = Tk()
window.resizable(width = 1, height = 1)
window.wm_title("Book Inventory")

def view_command():
    lst.delete(0,END)
    for row in backend.view():
        lst.insert(END,row)
    # print(backend.view)

def get_selected_row(event):
    try:
        global selected_tuple
        index=lst.curselection()[0]
    # print(f"Index {index}")
    # print(lst.get(index)[0])
        selected_tuple = lst.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        deleteBtn.configure(state='normal')
    except IndexError:
        pass
    # return(lst.get(index)[0])

def update_command():
    if lst.index("end") != 0:
        backend.update(selected_tuple[0],titleVal.get(),authorVal.get(),yearVal.get(),isbnVal.get())
        view_command()

def delete_command():
    if lst.index("end") != 0:
        backend.delete(selected_tuple[0])
        view_command()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

def add_command():
    backend.insert(titleVal.get(),authorVal.get(),yearVal.get(),isbnVal.get())
    view_command()

def search_command():
    lst.delete(0,END)
    for row in backend.search(titleVal.get(),authorVal.get(),yearVal.get(),isbnVal.get()):
        lst.insert(END,row)

#labels
l1 = Label(window,text="Title")
l2 = Label(window,text="Author")
l3 = Label(window,text="Year")
l4 = Label(window,text="ISBN")

#value parameters
titleVal    =   StringVar()
authorVal   =   StringVar()
yearVal     =   StringVar()
isbnVal     =   StringVar()   

#input texts
e1 = Entry(window,textvariable=titleVal)
e2 = Entry(window,textvariable=authorVal)
e3 = Entry(window,textvariable=yearVal)
e4 = Entry(window,textvariable=isbnVal)

#buttons
viewBtn     =   Button(window,text="View All",width=10,command=view_command)
searchBtn   =   Button(window,text="Search Entry",width=10,command=search_command)
addBtn      =   Button(window,text="Add Entry",width=10,command=add_command)
updateBtn   =   Button(window,text="Update",width=10,command=update_command)
deleteBtn   =   Button(window,text="Delete",width=10,command=delete_command,state= DISABLED)
closeBtn    =   Button(window,text="Close",width=10)



#listbox
lst =   Listbox(window,height=6,width=35)
lst.grid(row=2,column=0,rowspan=6,columnspan=2)

lst.bind('<<ListboxSelect>>',get_selected_row)

#scrollbar
sb  =   Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

lst.configure(yscrollcommand=sb.set)
sb.configure(command=lst.yview)

#binding labels to window
l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)

#binding texts to window
e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)

#binding buttons
viewBtn.grid(row=2,column=3)
searchBtn.grid(row=3,column=3)
addBtn.grid(row=4,column=3)
updateBtn.grid(row=5,column=3)
deleteBtn.grid(row=6,column=3)
closeBtn.grid(row=7,column=3)

if lst.index("end") == 0:
    deleteBtn.configure(state=DISABLED)

window.mainloop()