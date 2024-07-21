from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Image Viewer')
root.iconbitmap('C:/Users/hp/Desktop/gui projects/images.ico')

my_image = ImageTk.PhotoImage(Image.open('C:/Users/hp/Desktop/gui projects/images.png'))
my_label = Label(image=my_image)
my_label.pack(pady=100)

exit_button = Button(root,text="EXIT",command=root.quit)
exit_button.config(font=("Times New Roman",20), fg="white", bg="black")
exit_button.pack()

root.mainloop()