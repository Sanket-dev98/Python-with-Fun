import os 

answer = input("Do you like Marvel (yes or No):")

if answer.lower() == "yes" :
    print(" Marvel is best")
else:
    import os
    file_path = "C:/Users/Sanket/Documents/Python"

    try:
        os.remove(file_path)
        print("file deleted successfully")

    except FileNotFoundError:
        print("File not found")
