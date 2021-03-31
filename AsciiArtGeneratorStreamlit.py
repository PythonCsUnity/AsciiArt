import PIL.Image
import streamlit as st
import keyboard

# streamlit run AsciiArtGeneratorStreamlit.py in terminal

# add more white spaces for quality
# more whitespace is recommended for varying colors of white that you want to remove
# Also mess around with the other characters
# change size for resolution

#ASCII_CHARS = ["@", "&", "#", "$", "6", "%", "?", "1", "=", "*", "+", ":", ",", " "]
#ASCII_CHARS = ["@", "&", "#", "$", "6", "%", "?", "1", "=", "*", "+", ":", ",", " "]

#ASCII_CHARS = ["@", "&", "#", "$", "6", "%", "?", "1", "[", "]", "=", "*", " "]

#ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 25, heighta = 1.0):
    width, height = image.size
    new_height = heighta * new_width * height / width
    return image.resize((new_width, int(new_height)))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image, ASCII_CHARS):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        try:
            ascii_str += ASCII_CHARS[pixel//(255//(len(ASCII_CHARS)))]
        except:
            try:
                ascii_str += ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS))) - 1]
            except:
                try:
                    ascii_str += ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS))) + 1]
                except:
                    ascii_str += ASCII_CHARS[len(ASCII_CHARS) - 1]

    return ascii_str

def main():
    st.set_page_config(layout="wide")
    st.title("ASCII Art From an Image")
    path = st.file_uploader(label="Choose an image to be turned to ASCII Art")
    ASCII_CHARS = []
    try:
        image = PIL.Image.open(path)

        st.write("Recommended characters: @&#$6%?1=*+:, (Add a space at the end if you wish to have whitespaces)")
        asciicharstr = st.text_input("Input the characters being used (No spaces between each character"\
                                     + " unless the character being used is a space)", "@&#$6%?1=*+:, ")
        for char in asciicharstr:
            ASCII_CHARS.append(char)
        w = st.slider("Width of ASCII image (The bigger the image, the higher resolution it is)", 0, 1500, 100, 10)
        ha = float(st.text_input("Height multiplier/adjuster (recommended is 0.35)", 7/20))
        #resize image
        image = resize(image, w, heighta=ha)

        #convert image to greyscale image
        greyscale_image = to_greyscale(image)

        # convert greyscale image to ascii characters
        ascii_str = pixel_to_ascii(greyscale_image, ASCII_CHARS=ASCII_CHARS)
        img_width = greyscale_image.width
        ascii_str_len = len(ascii_str)
        ascii_img = ""

        #Split the string based on width  of the image
        for i in range(0, ascii_str_len, img_width):
            ascii_img += ascii_str[i:i+img_width] + "\n"

        #save the string to a file
        with open("AsciiArt.txt", "w") as f:
            f.write(ascii_img)
        uploadPath = st.text_input("Type the file path you want to save to (include file name)"\
                                   + "(Ex:C:\\Users\\abc123\\Desktop\\Ascii Art\\AsciiImage.txt):")
        try:
            with open(uploadPath, "w") as f:
                f.write(ascii_img)
        except:
            st.write("Input a valid file path")
        col1, col2, col3 = st.beta_columns(3)
        size1 = col1.button(label="Original screen size")
        size2 = col2.button("Zoom in")
        size3 = col3.button("Zoom out")
        if size1:
            st.write("orig")
            st.write("This function is currently not working")
        if size2:
            st.write("in")
            st.write("This function is currently not working")
        if size3:
            st.write("out")
            st.write("This function is currently not working")
        st.subheader("ASCII IMAGE")
        st.text("(Zoom out to see full image if it is too large)\n" + ascii_img)
        st.subheader("Original image:")
        st.image(path, width=img_width * 4)
    except:
        st.write("Choose Valid Selections")
main()