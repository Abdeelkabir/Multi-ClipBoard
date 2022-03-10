import sys
import clipboard
import json

#define the json path to stor our data
JSON_PATH = "clipboard.json"


#fonction to save our data into the json file
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

#fonction to load the data from the json file
def load_data(filepath):
   try:
       with open(filepath, "r") as f:
        data = json.load(f)
        return data
    
   #if the file dont exist, returne an empty dictionary
   except:
       return {}


#sys.argv is the list of words in the command we pased in, for example: for the command "python CBoard.py save"    sys.argv = ["CBoard.py", "save"]
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(JSON_PATH)
    if command == "save" or command == "s":
        key = input("Enter a key")
        data[key] = clipboard.paste()
        save_data(JSON_PATH, data)
        print("clipboard saved successfully")


    elif command == "load" or command == "l":
        key = input("Enter a key")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to the clipboard successfully")
        else:
            print("key does not exist")

    elif command == "list" or command == "ls":
        print(data)

    else: print("unknown command")


else: print("pleas past one command")
