import PIL.Image
import pathlib

current_path = pathlib.Path(__file__).parent.absolute()

ASCII_CHARS = ["@","#","S","%","?","*","+",";",":",",","."," "]


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

def main(new_width=100):
    
    
    try:
        image=PIL.Image.open("pic.jpg")
    except:
        print("Please rename the file to 'pic.jpg' and restart the script")
        quit()

    new_image_in_chars = convert_to_ascii(convert_to_grayscale(image_resize(image)))


    len_of_chars = len(new_image_in_chars)
    final_product = "\n".join(new_image_in_chars[i:(i+new_width)] for i in range(0,len_of_chars,new_width))
    
    print(final_product)

    with open("ascii-image.txt", "w") as doc:
        doc.write(final_product)
        print("Finished!")
        print("Finished!")

main()