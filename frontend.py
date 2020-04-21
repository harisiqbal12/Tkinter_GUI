from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = List1.curselection()
    selected_tuple = List1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    
     
def view_command():
    List1.delete(0, END)
    for row in backend.view():
        List1.insert(END, row)
        

def search_command():
    List1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        List1.insert(END, row)
        

def add_entry():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    List1.delete(0, END)
    List1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    
def delete_command():
    backend.delete(selected_tuple[0])
    
def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())   
    
def clear_screen():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    

win = Tk()
win.wm_title("PornStars Pedia")

l1 = Label(win, text = "Actor Name")
l1.grid(row = 0, column = 0)

l2 = Label(win, text = "Age")
l2.grid(row = 0, column = 2)

l3 = Label(win, text = "Country")
l3.grid(row = 1, column = 0)

l4 = Label(win, text = "Porbhub")
l4.grid(row = 1, column = 2)


title_text = StringVar()
e1 = Entry(win, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(win, textvariable = author_text) 
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(win, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(win, textvariable = isbn_text)
e4.grid(row = 1, column = 3)


List1 = Listbox(win, height = 12, width = 40)
List1.grid(row = 3, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(win)
sb1.grid(row = 2, column = 2, rowspan = 6)
List1.configure(yscrollcommand = sb1.set)
sb1.configure(command = List1.yview)

sb2 = Scrollbar(win, orient = 'horizontal')
sb2.grid(row = 9, column = 2)
List1.configure(xscrollcommand = sb2.set)
sb2.configure(command =List1.xview)

List1.bind('<<ListboxSelect>>', get_selected_row)



b1 = Button(win, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(win, text = "Search Entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3, columnspan = 6)

b3 = Button(win, text = "Add Entry", width = 12, command = add_entry)
b3.grid(row = 4, column = 3)

b4 = Button(win, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(win, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b7 = Button(win, text = "Clear", width = 12, command = clear_screen)
b7.grid(row = 7, column = 3)

b6 = Button(win, text = "Close", width = 12, command = win.destroy)
b6.grid(row = 8, column = 3)


win.mainloop()