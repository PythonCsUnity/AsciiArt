import PIL.Image

# add more white spaces for quality
# more whitespace is recommended for varying colors of white that you want to remove
# Also mess around with the other characters
# change size for resolution

ASCII_CHARS = ["@", "&", "#", "$", "6", "%", "?", "1", "=", "*", "+", ":", ",", " ", " ", " "]
#ASCII_CHARS = ["@", "&", "#", "$", "6", "%", "?", "1", "=", "*", "+", ":", ",", " "]

#ASCII_CHARS = ["@", "&", "#", "$", "6", "%", "?", "1", "[", "]", "=", "*", " "]

#ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 750):
    width, height = image.size
    new_height = new_width * 17 * height / (40 * width)
    return image.resize((new_width, int(new_height)))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        try:
            ascii_str += ASCII_CHARS[round(pixel/(255//(len(ASCII_CHARS)))) - 1]
        except:
            try:
                ascii_str += ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS)))]
            except:
                try:
                    ascii_str += ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS))) + 1]
                except:
                    ascii_str += ASCII_CHARS[len(ASCII_CHARS) - 1]

    return ascii_str

def main():
    path = input("Enter the path to the image field you want to turn into ascii art: ")
    size = int(input("Enter wanted width of image: "))
    image = PIL.Image.open(path)

    #resize image
    image = resize(image, size)

    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    #save the string to a file
    path = input("Directory for ascii img (not the file name itself): ")
    with open(path + "/AsciiArt.txt", "w") as f:
        f.write(ascii_img)
main()