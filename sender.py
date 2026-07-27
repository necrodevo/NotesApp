import requests
choice = -1

def inputHandler():
    try:
        num = int(input("Enter any number"))
    except ValueError:
        print("Please enter an integer")
        num = inputHandler()
    return num
    
def get_note():
    num = inputHandler()
    GETURL = f"http://127.0.0.1:8000/note/{num}"
    try:
        RESPONSE = requests.get(url=GETURL,timeout=10)
        RESPONSE.raise_for_status()
        data = RESPONSE.json()
    except requests.exceptions.Timeout:
        print("Server Timed Out!")
        return
    except requests.exceptions.HTTPError:
        print("Server couldn't find the data")
        return
    note = data.get("note")
    author = data.get("author")
    print(f"Author Name:{author}")
    print(f"Note:{note}")

def post_note():
    author = input("Enter your name:")
    note = input("Enter your Notes:")

    POSTURL = f"http://127.0.0.1:8000/note" 
    try:
        RESPONSE = requests.post(url=POSTURL,timeout=10,params={"author":{author},"note":{note}})
        RESPONSE.raise_for_status()
        data = RESPONSE.json()
    except requests.exceptions.RequestException:
        print("Failed to Get Access To Sever")
        return
    print("Data posted successfully!")
    
def menu():
    print("1.Get a note")
    print("2.Post a note")
    print("3 to exit")

while choice !=5:
    menu()
    try:
        choice = int(input("Enter 1-3"))
    except ValueError as e:
        print("Please Enter A number")
        continue
    match(choice):
        case 1: get_note()
        case 2: post_note()
        case 3: break
print("Exiting the program")

    
