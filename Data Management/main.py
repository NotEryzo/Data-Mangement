# Data Management

import json

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





