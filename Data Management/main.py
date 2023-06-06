# Data Management Project by Sami

import json

# Main login function
def mainLogin():
  userdata = loadUsers()

  while True:
    choice = loginMenu()

    if choice == 1:
      signup(userdata)
    elif choice == 2:
      user = login(userdata)
      if user: 
        mainMenu(user, userdata)
        break
    elif choice == 3:
      break
    else:
        print("Please enter either 1 or 2.")

# Login menu
def loginMenu():
  print("1. Signup")
  print("2. Login")
  print("3. Exit.")
  return int(input("Enter a selection (1-3): "))

# Loads data from json file
def loadUsers():
  with open("users.json", "r") as f:
    userdata = json.load(f)
  return userdata

# Dumps data into json file
def saveUsers(userdata):
  with open("users.json", "w") as f:
    json.dump(userdata, f)

# Signup function
def signup(userdata):
  username = input("Enter your desired username: ").lower()

  for user in userdata:
    if user["username"] == username:
      print("Username already exists.")
      return

  password = input("Enter your desired password: ").lower()
  userdata.append(newUser(username, password))
  saveUsers(userdata)
  print("Signup Successful!")

# Login function
def login(userdata):
  username = input("Enter your username: ").lower()
  password = input("Enter your password: ").lower()

  for user in userdata:
    if user["username"] == username and user["password"] == password:
      print("Login Successful!")
      return user

    print("Invalid username or password.")
    return 

def logout():
  print("Logout Successfully!")
  mainLogin()

# New user dictionary
def newUser(username, password):
  return {
    "username": username,
    "password": password,
    "faves": []
  }

# New song dictionary
def newSong(title, artist, genre):
  return {
    "title": title,
    "artist": artist,
    "genre": genre
  }

# Songs array
songs = []
songs.append(newSong("God's Plan", "Drake", "Rap"))
songs.append(newSong("Mask Off", "Future", "Rap"))
songs.append(newSong("Ghost", "Justin Bieber", "Pop"))
songs.append(newSong("Controlla", "Drake", "Rap"))
songs.append(newSong("Solo", "Future", "Rap"))
songs.append(newSong("Baby", "Justin Bieber", "Pop"))

# Main Menu function
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
      addFaves(user, userdata)
    elif choice == 5:
      removeFaves(user, userdata)
    elif choice == 6:
      displayFaves(user)
    elif choice == 7:
      logout()
      break
    elif choice == 8:
      break
    else:
      print("Please enter a selection between 1-7.")

# Selections for the Main Menu function
def selectionMenu():
  print("1. Display all Data.")
  print("2. Filter Data by Artist.")
  print("3. Sort Data by Title.")
  print("4. Add to favourite list.")
  print("5. Remove data from favourite list.")
  print("6. Display favourite list.")
  print("7. Logout")
  print("8. Exit.")
  return int(input("Enter a selection (1-8): "))

# Display all data
def displayData():
  for song in songs:
    print("Title: ", song["title"])
    print("Artist: ", song["artist"])
    print("Genre: ", song["genre"])

# Filter Data
def filterData():
  filter_str = input("Filter songs by artist: ").lower()
  found = False

  for song in songs:
    if filter_str == song["artist"].lower():
      found = True
      print(song["title"], song["artist"], song["genre"])

  if not found:
    print("Artist not found.")

# Selection sort function
def selectionSort(anArray):
  for i in range(len(anArray) - 1):
    minPoistion = i
    for n in range(i+1, len(anArray)):
      if anArray[n]["title"] < anArray[minPoistion]["title"]:
        minPoistion = n
        anArray[i], anArray[minPoistion] = anArray[minPoistion], anArray[i]

# Add songs to favourites
def addFaves(user, userdata):
  displayData()
  songnum = int(input("Enter the number of the song to add to favourites: "))

  # Choice of songs is between 1 - the length of the array, and we subtract 1 because the index starts from 0
  if 1 <= songnum <= len(songs):
    song = songs[songnum - 1]
    user["faves"].append(song)
    saveUsers(userdata)
    print(f"{song['title']} by {song['artist']} added to favourites.")
  else:
    print("Invalid song number.")

# Remove from favourites list
def removeFaves(user, userdata):
  displayFaves(user)
  songnum = int(input("Enter the number of the song to remove from favorites: "))

  # Choice of songs is between 1 - the length of the array, and we subtract 1 because the index starts from 0
  if 1 <= songnum <= len(user["faves"]):
    song = user["faves"][songnum - 1]
    user["faves"].remove(song)
    saveUsers(userdata)
    print(f"{song['title']} by {song['artist']} removed from favorites.")
  else:
    print("Invalid song number or the favorites list is empty.")

# Display favourites list
def displayFaves(user):
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
