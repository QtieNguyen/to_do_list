from tkinter import * 
from PIL import ImageTk, Image 

#First/Main Window
main = Tk() #Display root/first window and manages the components of the application
main.title("To-List List") #Title for the first window

#Second Window
def open_second():
    global resized_img1 #Without the global keyword, pictures won't show up. 
    global resized_img2 #Python think that picture files belong to garbage collection

    sec_win= Toplevel() #This is the second window
    sec_win.title('Second Window')

    #This whole block is to add a picture into the second window, and also resize the picture
    my_img1 = Image.open("C:/Users/quang/El Gato.jpg")
    img_resize1 = my_img1.resize((450,350), Image.ANTIALIAS)
    resized_img1 = ImageTk.PhotoImage(img_resize1)
    my_label1 = Label(sec_win, image=resized_img1)
    my_label1.pack()

    #Same thing with the above block
    my_img2 = Image.open("C:/Users/quang/Goofy Cat.jpg")
    img_resize2 = my_img2.resize((450,350), Image.ANTIALIAS)
    resized_img2 = ImageTk.PhotoImage(img_resize2)
    my_label2 = Label(sec_win, image=resized_img2)
    my_label2.pack()

#This function helps adding task into a list box
def addTask():
    enterTask = "Task: " + entry.get()
    task_list.insert(END, enterTask)
    entry.delete(0, END)

#This function delete a selected task in the list box
def removeTask(): 
    select_to_delete = task_list.curselection()
    if select_to_delete:
        task_list.delete(select_to_delete[0]) 
    
#Entry Box for user's inputs 
entry= Entry(main, width=30, border=4)
entry.pack()

#Interact with this button would add an input to the box list
enterButton = Button(main, text= "Add Task", command= addTask)
enterButton.pack()

#A Box List, where user's inputs will be stored in here
task_list = Listbox(main, width=35)
task_list.pack()

#Delete a task from a list by selecting one item, then press delete button
deleteButton = Button(main, text= "Delete Task", command = removeTask)
deleteButton.pack()

#Open a second Window by calling open_second function
open_second_window = Button(main, text='Open to see Motivation!', command=open_second)
open_second_window.pack()

#Launch GUI 
main.mainloop()