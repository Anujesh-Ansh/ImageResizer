import cv2
import os

try:
    scale_percent = int(input("Enter the Percent of the original size: ")) # percent of original size
    reName = input("Enter the name of the resized image: ")
    reFormat = input("Enter the format of the resized image: ")
    image = cv2.imread('photo.jpeg')

    # Percentage by which the image is resized

    # Calculate the 50 percent of original dimensions
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    # dsize - is the size of the output image (Desired Size)
    dsize = (width, height)


    # resize image
    output = cv2.resize(image, dsize)
    cv2.imwrite(f"/Users/anujeshansh/Git/Python/Projects/imageResizer/{reName}.{reFormat}", output)
    print("Done !!")
    os.system("say Done")
except:
    print('Error occurred')