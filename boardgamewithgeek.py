import re
from boardgamegeek import BGGClient
import boardgamegeek

bgg = BGGClient()
userName = input("Enter a BGG username! ")
numOfPlayers = input("How many people are playing? ")
while numOfPlayers.isnumeric() == False:
    numOfPlayers = input("How many people are playing? ")
numOfPlayers = int(numOfPlayers)
timeOfGame = input("How long do you want to play for? (In Minutes) ")
while timeOfGame.isnumeric() == False:
    timeOfGame = input("How long do you want to play for? (In Minutes) ")
timeOfGame = int(timeOfGame)
eligibleGames = []
user = bgg.collection(userName, own=True)
userCollection = user.items
collectionGames = []
for item in userCollection:
    item = str(item)
    item = re.findall(r'\d+', str(item))
    item = str(item).strip("[']")
    collectionGames.append(item)
listOfGames = bgg.game_list(game_id_list=collectionGames)
for game in listOfGames:
    name = game.name
    playerCount = game.player_suggestions
    listOfPlayerCounts = []
    for count in playerCount:
        addedCount = count.player_count
        if (count.best + count.recommended) > count.not_recommended:
            if "+" in addedCount:
                addedCount = re.findall(r'\d+', addedCount)
                addedCount = int(addedCount[0])
            listOfPlayerCounts.append(addedCount)
    minPlayTime = game.min_playing_time
    maxPlayTime = game.max_playing_time
    if not listOfPlayerCounts:
        continue
    minPlayers = int(listOfPlayerCounts[0])
    maxPlayers = int(listOfPlayerCounts[len(listOfPlayerCounts)-1])
    if numOfPlayers >= minPlayers and numOfPlayers <= maxPlayers and timeOfGame >= minPlayTime and timeOfGame <= maxPlayTime:
        eligibleGames.append(name)
if len(eligibleGames) == 0:
    print ("No games meet your criteria!")
for game in eligibleGames:
    print(game)