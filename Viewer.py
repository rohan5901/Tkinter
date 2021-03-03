from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer!")
root.iconbitmap('C:\Tkinter\levi.ico')


my_img1 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img4.jpg"))
                                       
image_list = [my_img1, my_img2, my_img3, my_img4]    
                                   
                                       
                                       
                                       
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(img_no):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image = image_list[img_no - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_no+1))
    button_back = Button(root, text="<<", command=lambda:back(img_no-1))
    
    if img_no==4:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)



def back(img_no):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image = image_list[img_no - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_no+1))
    button_back = Button(root, text="<<", command=lambda:back(img_no-1))
    
    
    if img_no==1:
        button_back = Button(root, text="<<", state=DISABLED)
        
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)


button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root,text=">>", command=lambda: forward(2))

my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()