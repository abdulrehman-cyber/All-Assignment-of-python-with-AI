import os

def create_file():
    filename=input("Enter the file name (with txt): ")
    try:
        with open(filename, "x") as f:
            print("file created successfully")
    except FileExistsError:
        print("file already exist ")


def write_file():
    filename=input("Enter The filename : ")
    data = input("Enter the data :\n")
    
    with open(filename, "w") as f:
        f.write()
    print("Data write successfully")

def read_file():
    filename=input("Enter The Filename : ")
    try:
        with open(filename,"r")as f:
            f.read()
    except FileNotFoundError:
        print("file not found")

def append_file():
    filename=input("Enter File name : ")
    data=input("Enter the data : ")
    with open(filename, "a") as f:
        f.write("\n", data)
    print("Data appended successfully!")

def view_file():
    files = os.listdir(".")
    print("="*45)
    print("{:<5} {:<30}".format("No", "File Name"))
    print("="*45)

    for i, file in enumerate(files, start=1):
        print("{:<5} {:<30}".format(i, file))

    print("="*45)

