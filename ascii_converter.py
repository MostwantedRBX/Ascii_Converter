import PIL.Image
import tkinter as tk

ASCII_CHARS = ["@","#","S","%","?","*","+",";",":",",","."," "]


b = "bg.jpg"
def image_resize(image,new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)


def convert_to_grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)


def convert_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def con_image(image=PIL.Image.open("pic.jpg"),new_width=100):
    
    # try:
    #     # image = PIL.Image.open("pic.jpg")
    # except:
    #     print("Please rename the file to 'pic.jpg' and restart the script")
    #     quit()
    
    new_image_in_chars = convert_to_ascii(convert_to_grayscale(image_resize(image)))
    
    len_of_chars = len(new_image_in_chars)
    final_product = "\n".join(new_image_in_chars[i:(i+new_width)] for i in range(0,len_of_chars,new_width))
    
    print(final_product)

    with open("ascii-image.txt", "w") as doc:
        doc.write(final_product)
        print("Finished!")




#### Window Stuffs ####

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.pic_path = "pic.jpg"
        

    def create_widgets(self):
        ## labels
        
        self.lab = tk.Label(self,text="Please enter the name of the picture, including extension:")
        self.lab.pack(side="top",pady=5)

        self.entry = tk.Entry(self,width=20)
        self.entry.pack(side="top",pady=5)

        self.convert = tk.Button(self,text="IMAGE_TO_ASCII",command=self.convert_click)
        self.convert.pack(side="top",pady=5)

        self.output = tk.Label(self)
        self.output.pack(side="top",pady=5)

        ##buttons
        self.quit = tk.Button(self,text="Close",command=self.master.destroy)
        self.quit.pack(side="bottom", pady=5)

    def get_entry(self):
        self.pic_path = self.entry.get()
        return self.pic_path

    def convert_click(self):
        try: 
            im = PIL.Image.open(self.get_entry())
            self.output["text"] = "Image Converted! Check for the .txt file!"
        except:
            self.output["text"] = "That is not a valid image, please try again."
            
        con_image(im)




####/Window Stuffs/####





#### Window 




root = tk.Tk()
root.geometry("320x170")
root.title("Image to Ascii Converter")
app = Application(master=root)



# background_image=tk.PhotoImage("bg.jpg")
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
app.mainloop()