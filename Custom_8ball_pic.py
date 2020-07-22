from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from random import choice
import sqlite3


root = Tk()
root.title("Welcome to Customizable 8Ball!")
root.iconbitmap('c:/custom8ball/custom8ballimages/magicBallStart.ico')

welcome_label = Label(root, text="Welcome to Customizable 8Ball with Images!", font=("OpenSans-Regular.ttf", 22), height=3)
welcome_label.grid(row=0, column=0, columnspan=2)

connec = sqlite3.connect("custom_8Ball_images.db")
curso = connec.cursor()


# Only use code to create inital database table
curso.execute("""CREATE TABLE IF NOT EXISTS pictures (
        names TEXT,
        images BLOB
)""")

# Add Image

def show_add_image():
    global add_image_btn
    global name_image_entry
    global name_image_btn
    global hide_add_image_btn


    connec = sqlite3.connect("custom_8Ball_images.db")
    curso = connec.cursor()


    def hide_add_image_btn():
        global add_image_btn
        global name_image_entry
        global name_image_btn
        global hide_add_image_btn

        hide_add_image_btn.grid_forget()
        name_image_entry.grid_forget()
        name_image_btn.grid_forget()
        add_image_btn.grid(row=1, column=0, columnspan=2)


    add_image_btn.grid_forget()
    hide_add_image_btn = Button(root, text="Add Your Custom Image", height=3, width=85, relief=RAISED, font= ('OpenSans-Regular.ttf', 11, "bold"), command=hide_add_image_btn)
    hide_add_image_btn.grid(row=1, column=0, columnspan=2)
    name_image_entry = Entry(root, width=100)
    name_image_entry.insert(0, "Name Your Image")
    name_image_entry.grid(row=2, column=0, pady=2, ipady=11, sticky=W)


    def add_image():
        try:
            connec = sqlite3.connect("custom_8Ball_images.db")
            curso = connec.cursor()
            new_filename = filedialog.askopenfilename(initialdir='c:/custom8ball/custom8ballimages', title="Add an Image")
            with open(new_filename, 'rb') as file:
                image = file.read()
            name = str(name_image_entry.get())
            curso.execute("INSERT INTO pictures (names, images) VALUES (?, ?)",  (name, image))
            
            data = curso.execute("""
            SELECT * FROM pictures
            """)

            path = str("c:/custom8ball/custom8ballimages/")
            for x in data:
                rec_name = str(path + x[0] + ".jpg")
                rec_data = x[1]
                with open(rec_name, 'wb') as file:
                    file.write(rec_data)
                name_image_entry.delete(0, END)
                name_image_entry.insert(0, "Image Added")
        except:
            name_image_entry.delete(0, END)
            name_image_entry.insert(0, "Adding Image Failed")
    
    name_image_btn = Button(root, text="Choose Image", height=2, width=16, relief=RAISED, font=("OpenSans-Regular.ttf", 12, "bold"), command=add_image)
    name_image_btn.grid(row=2, column=1, pady=2, sticky=E)


    connec.commit()
    curso.close()
    connec.close()


add_image_btn = Button(root, text="Add Your Custom Image", height=3, width=85, relief=RAISED, font= ('OpenSans-Regular.ttf', 11, "bold"), command=show_add_image)
add_image_btn.grid(row=1, column=0, columnspan=2)

# Show Images





# Remove Images





# Play Game



#########################

connec.commit()
curso.close()
connec.close()

root.mainloop()