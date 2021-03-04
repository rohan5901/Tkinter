from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer!")
root.iconbitmap('C:\Tkinter\levi.ico')

#creating images
my_img1 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:\Tkinter\images\img4.jpg"))
                                       
image_list = [my_img1, my_img2, my_img3, my_img4]   



status = Label(root, text="Image 1 of " + str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)
 
                                   
                                       
                                       
#storing the images in a variable i.e widget                                       
my_label = Label(image=my_img1)



def forward(img_no):
    global my_label
    global button_forward
    global button_back
    
    #creating the widgets again
    my_label.grid_forget()
    my_label = Label(image = image_list[img_no - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_no+1))
    button_back = Button(root, text="<<", command=lambda:back(img_no-1))
    
    status = Label(root, text="Image " + str(img_no)  + " of " + str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)


    #disabeling the forward button when it reaches the last image
    if img_no==4:
        button_forward = Button(root, text=">>", state=DISABLED)
        
        
    #displaying the created images
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    status.grid(row=2,column=0,columnspan=3, sticky=W+E) #W and E representing West And East.




def back(img_no):
    global my_label
    global button_forward
    global button_back
    
    
    #Creating widgets again
    my_label.grid_forget()
    my_label = Label(image = image_list[img_no - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_no+1))
    button_back = Button(root, text="<<", command=lambda:back(img_no-1))
    
    status = Label(root, text="Image " + str(img_no) + "  of " + str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)

    
    #disableing the back button in the start
    if img_no==1:
        button_back = Button(root, text="<<", state=DISABLED)
        
    #displaying the created widgets in the screen    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    status.grid(row=2,column=0,columnspan=3, sticky=W+E) #W and E representing West And East.

    


#creating widgets

button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root,text=">>", command=lambda: forward(2))



#putting widgets on the screen

my_label.grid(row=0, column=0, columnspan=3)


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2, pady=10)

status.grid(row=2,column=0,columnspan=3, sticky=W+E) #W and E representing West And East.



root.mainloop()