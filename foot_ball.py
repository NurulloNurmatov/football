from json import *
class Team():
     def allTeamName(self,allName,numOfPlayers):
          self.allName = allName
          self.numOfPlayers = numOfPlayers
          self.allName.sort()
          return f"{self.allName}"
     def addTeam(self,newTeam):
          if len(self.allName)<8 and newTeam not in allName:
               self.allName.append(newTeam)
               self.numOfPlayers[newTeam] = 0
               return "✅"
          elif newTeam in allName:
               return "❗️"
          return "❌"

     def numberOfPlayers(self,numOfPlayers):
          self.numOfPlayers = numOfPlayers
          print(self.numOfPlayers)
     def addNewPlayer(self,numOfPlayers,commandName,number):
          checkCommand = True
          for key,value in self.numOfPlayers.items():
               if key == commandName:
                    if value+number<=11:
                         checkCommand = False
                         self.numOfPlayers[key] = value+number
                    elif value+number > 11:
                         return "❗️"
          if checkCommand:
               return "❌"

print("please answer the questions yes or no ❗️")
allName = ["Russia","Germany","Brazil","Portugal","Argentina","French"]
with open("allinfo.json","r") as file:
     data = file.read()
question = ""
numAndName ={
     "Russia":11,
     "Germany":8,
     "Brazil":9,
     "Portugal":10,
     "Argentina":10,
     "French":9
}
while 1:
     print("\nList of teams ")
     command1 = Team()
     print(command1.allTeamName(allName,numAndName))
     question = input("Do you want to add a new team ?\n")
     if question == "yes":
          checkTik = command1.addTeam(input("Name  the new team: "))
     else:
          question = input("Do you want to see the number of players in the team ?\n")
          break
     if checkTik == "✅":
          print("Your team has been added successfully ✅")
     elif checkTik=="❗️":
          print("There is a team with that name ❗️")
     else:
          print("Sorry you cannot add another team ❌")
          question = input("Do you want to see the number of players in the team ?\n")
          break

if question =="yes":
     while 1:
          command2 = Team()
          command2.numberOfPlayers(numAndName)
          question = input("Do you want to add your own player to the command ?\n")
          if question=="yes":
               chooseCommand = input("Shoose the command: ")
               if chooseCommand in numAndName:
                    player = int(input("How many players do you want to add: "))
                    checkTik = command2.addNewPlayer(numAndName,chooseCommand,player)
                    if checkTik =="❗️":
                         print("The number of players exceeded eleven ❗️")
                    elif checkTik =="❌":
                         print("There is no such team ❌")
          else:
               question = input("Do you want see all information ?\n")
               if question =="yes":
                    print(data)
               break