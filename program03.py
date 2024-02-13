print("\nRequirement 1")
print("\nThis is Program03 - Pablo Barrientos")

print("\nRequirement 2")
print("\nThis program records goals for soccer players and points for basketball players.")

# list for players and goals
soccerPlayersList = []
soccerPlayerGoalsList = []

# list for players and points
basketballPlayersList = []
basketballPointsList = []

# ask user for three players
print("\nRequirement 3")
print("\nThis program records goals for three players")
for i in range(3):
    soccerPlayers = str(input("\nPlease enter the name of soccer player {}: ".format(i+1)))
    soccerPlayersList.append(soccerPlayers)

# ask user for goals for each player
print("\nRequirement 4")
for player in soccerPlayersList:
    soccerGoals = int(input("\nPlease enter the amount of goals scored by {}: ".format(player)))
    soccerPlayerGoalsList.append((player, soccerGoals))

# bubble sort by goals: greatest to least
print("\nRequirement 5")
print("\nUsing bubblesort logic to determine the most goals")
for i in range(len(soccerPlayerGoalsList) - 1):
    for j in range(0, len(soccerPlayerGoalsList) - i - 1):
        # swap if the item is less than the next item
        if soccerPlayerGoalsList[j][1] < soccerPlayerGoalsList[j + 1][1]:
            soccerPlayerGoalsList[j], soccerPlayerGoalsList[j + 1] = soccerPlayerGoalsList[j + 1], soccerPlayerGoalsList[j]

# ouput sorted list
print("\nRequirement 6")
print("\nSoccer Players in sorted order:")
for player in soccerPlayerGoalsList:
    print("{} - {}".format(player[0], player[1]))
    
print("\nRequirement 7")
for i in range(3):
    basketballPlayers = str(input("\nPlease enter the name of basketball player {}: ".format(i+1)))
    basketballPlayersList.append(basketballPlayers)

print("\nRequirement 8")
for player in basketballPlayersList:
    points = int(input("\nPlease enter the amount of carrer points scored by {}: ".format(player)))
    basketballPointsList.append((player, points))

print("\nRequirement 9")
print("\nUsing bubblesort logic to determine the most career points")
for i in range(len(basketballPointsList) - 1):
    for j in range(0, len(basketballPointsList) - i - 1):
        # swap if the item is less than the next item
        if basketballPointsList[j][1] < basketballPointsList[j + 1][1]:
            basketballPointsList[j], basketballPointsList[j + 1] = basketballPointsList[j + 1], basketballPointsList[j]

print("\nRequirement 10")
print("\nBasketball Players in sorted order:")
for player in basketballPointsList:
    print("{} - {}".format(player[0], player[1]))

print("\nRequirement 11")
print("\nMy experience with Program 03 was overall good. The bubblesort logic was the best way to approach"
      " the decision making portion.")