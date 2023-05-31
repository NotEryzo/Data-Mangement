# Data Management

import json

def loginmenu():
    print("1. Signup")
    print("2. Login")
    return int(input("Enter a selection (1-2): "))
     
def login():
     choice = loginmenu

     if choice == 1:
        username = input("Enter your desired username: ")
        password = input("Enter your desired password: ")

        with open("users.json", "r") as f:
            data = json.load(f)
            if username in data:
                print("Username already exists.")
                return
        
        with open("users.json", "w") as f:
            data[username] = password
            json.dump(data, f)

def displayData():
    for i in songs:
        print("Title: ", i["title"])
        print("Artist: ", i["artist"])
        print("Genre: ", i["genre"])

def filterData():
    filter = input("Filter songs by artist: ").lower()
    found = False
    for i in songs:
        if filter == i["artist"].lower():
            found = True
            print(i["title"], i["artist"], i["genre"])
    if not found:
        print("Artist not found.")
    
def selectionSort(anArray):
    for i in range(len(anArray) - 1):
        minPoistion = i
        for n in range(i+1, len(anArray)):
            if anArray[n]["title"] < anArray[minPoistion]["title"]:
                minPoistion = n
        anArray[i], anArray[minPoistion] = anArray[minPoistion], anArray[i]

def addfav():
    pass 

def newUser(username, password):
	return {
		"username": username,
		"password": password,
		"faves": [ ]
	}

def newSong(title, artist, genre):
	return {
		"title": title,
		"artist": artist,
		"genre": genre
	}


songs = []
songs.append(newSong("God's Plan", "Drake", "Rap"))
songs.append(newSong("Mask Off", "Future", "Rap"))
songs.append(newSong("Ghost", "Justin Bieber", "RnB"))





