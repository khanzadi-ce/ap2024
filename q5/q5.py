# Author: P. Khanzadi and Bard, Google AI. (2024, April 30)
# Python: 3.9.7

# Library
import glob


# functions
def list_files(directory):

    # List all files in a directory and its subdirectories
    files = glob.glob(directory+'/**/*', recursive=True)
    
    # list of files
    image_files = []
    text_files  = []

    for filename in files:
        if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
            image_files.append(filename)
        if filename.endswith((".txt")):
            text_files.append(filename)
    return image_files, text_files

# Main
image_dir = "D:\\AdvancedProgramming\\github\\ap2024\\q5"
images, text = list_files(image_dir)

# Print Output 
print("Number of image files: " + str(len(images)))
print("Number of text files: " + str(len(text)))
