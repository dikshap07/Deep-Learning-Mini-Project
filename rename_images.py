import os
 
# Function to rename multiple files

def rename_images(folder,path):

    for count, filename in enumerate(os.listdir(folder)):
        for count, image_name in enumerate(os.listdir(path + folder + "/" +str(filename))):
            print(f"{count} , {image_name}")

            dst = f"{str(filename)}_{str(count)}.jpg"
            src =f"{folder}/{filename}/{image_name}"  # foldername/filename, if .py file is outside folder
            dst =f"{folder}/{filename}/{dst}"

            # rename() function will
            # rename all the files
            os.rename(src, dst)
            # print(f"{count} , {image_name}")

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    path = "/Users/dikshapaliwal/Deep-Learning-Mini-Project/"
    folder = "holding_weapon_or_not"
    rename_images(folder,path)


