import json

def mainLogin():
  while True:
    choice = loginMenu()
    if choice == 1:
      signup()
      break
    elif choice == 2:
      login()
      break
    elif choice == 3:
      break
    else:
      print("Please enter either 1 or 2.")

def loginMenu():
    print("1. Signup")
    print("2. Login")
    print("3. Exit.")
    return int(input("Enter a selection (1-2): "))

def loadUsers():
    with open("users.json", "r") as f:
        userdata = json.load(f)
    return userdata

def saveUsers(userdata):
    with open("users.json", "w") as f:
        json.dump(userdata, f)

def signup():
    username = input("Enter your desired username: ").lower()
    password = input("Enter your desired password: ").lower()
    userdata = loadUsers()

    for user in userdata:
        if user["username"] == username:
            print("Username already exists.")
            mainLogin()
            return

    userdata.append(newUser(username, password))
    saveUsers(userdata)
    print("Signup Successful!")
    mainLogin()


def login():
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ").lower()
    userdata = loadUsers()
    for user in userdata:
        if user["username"] == username and user["password"] == password:
            print("Login Successful!")
            mainMenu(user, userdata)
            return
    print("Invalid username or password.")
    mainLogin()

def newUser(username, password):
    return {
        "username": username,
        "password": password,
        "faves": []
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

def mainMenu(user, userdata):
   print("\nHello " + user["username"])
   while True:
      choice = selectionMenu()
      if choice == 1:
        displayData()
      elif choice == 2:
        filterData()
      elif choice == 3:
        selectionSort(songs)
        displayData()
      elif choice == 4:
        addfaves(user, userdata)
      elif choice == 5:
        removefaves(user, userdata)
      elif choice == 6:
        displayfaves(user)
      elif choice == 7:
        break
      else:
        print("Please enter a selection between 1-7.")

def selectionMenu():
   print("1. Display all Data.")
   print("2. Filter Data by Artist.")
   print("3. Sort Data by Title.")
   print("4. Add to favourite list.")
   print("5. Remove data from favourite list.")
   print("6. Display favourite list.")
   print("7. Exit.")
   return int(input("Enter a selection (1-6): "))

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

def addfaves(user, userdata):
  displayData()
  songnum = int(input("Enter the number of the song to add to favourites: "))
  if songnum >= 1 and songnum <= len(songs):
    song = songs[songnum - 1]
    user["faves"].append(song)
    saveUsers(userdata)
    print(f"{song['title']} by {song['artist']} added to favourites.")
  else:
    print("Invalid song number.")

def removefaves(user, userdata):
    title = input("Enter the title of the song to remove from favorites: ")
    found = False

    for song in user["faves"]:
        if song["title"].lower() == title.lower():
            user["faves"].remove(song)
            saveUsers(userdata)
            print(f"{song['title']} by {song['artist']} removed from favorites.")
            found = True
            break

    if not found:
        print("Song not found in favorites or the faves list is empty.")

def displayfaves(user):
  if user["faves"]:
    print("Your favourite songs:")
    for song in user["faves"]:
      print("Title:", song["title"])
      print("Artist:", song["artist"])
      print("Genre:", song["genre"])
  else:
    print("Your favourite list is empty.")
  
userdata = loadUsers()
mainLogin()
