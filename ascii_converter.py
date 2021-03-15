## import packages, if they don't have em it'll tell them to get them.
import time
try:
    import PIL.Image
except:
    print("Pillow is not installed! Install it using the following command: 'pip3 install pillow'")
    quit()

try:
    import tkinter as tk
    from tkinter import filedialog
except:
    print("tkinter is not installed! Install it using the following command: 'pip3 install tkinter'")
    

# Chars to use with making the image, from most intense to least intense
ASCII_CHARS = ["@","#","S","%","?","*","+",";",":",",","."," "]

# Resize the image to make it easier to work with
def image_resize(image,new_width=50):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

# Grayscale the image
def convert_to_grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# Converts the pixels to the characters on the table above. Returns the string of pixel to characters.
def convert_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def con_image(image,new_width=50):
    
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
        self.pic_path = ""
        
    ## Create elements on the window
    def create_widgets(self):
        
        
        self.lab = tk.Label(self,text="Please enter the name of the picture, including extension:")
        self.lab.pack(side="top",pady=5)

        self.filelab = tk.Label(self,text = "Current Selected File: ")
        self.filelab.pack(side="top",pady=5)

        self.selImage = tk.Button(self,width=97,text="Select File",command=self.defineTarget)
        self.selImage.pack(side="top",pady=5)

        self.convert = tk.Button(self,width=97,text="IMAGE_TO_ASCII",command=self.convert_click)
        self.convert.pack(side="top",pady=5)

        self.output = tk.Label(self)
        self.output.pack(side="top",pady=5)

        self.quit = tk.Button(self,width=97,text="Close",command=self.master.destroy)
        self.quit.pack(side="bottom", pady=5)

    # Fetch text in textbox
    def get_entry(self):
        return self.pic_path

    def convert_click(self):
        try: 
            im = PIL.Image.open(self.get_entry())
            self.output["text"] = "Image Converted! Check for the .txt file!"
        except:
            self.output["text"] = "That is not a valid image, please try again."
            
        con_image(im)

    def defineTarget(self):
        self.pic_path = filedialog.askopenfilename(initialdir="", title="select file")
        self.filelab["text"] = "Currently Selected File: " + self.pic_path

####/Window Stuffs/####





#### Opens the Window
root = tk.Tk()
root.geometry("700x200")
root.title("Image to Ascii Converter")
app = Application(master=root)
app.mainloop()
