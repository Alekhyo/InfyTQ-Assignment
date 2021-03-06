#DSA-Assgn-4
# The Indian Cricket Board has decided to send its best players to ICC World Cup. They have chosen the best 11 players for the match.
# The players should be sent in for the batting based on their experience, i.e. the priority would be given to the player who has got the highest experience.
# At the last moment, the captain has decided that the player who has got the highest experience should bat at the 4th position.
# Use the Player class and players_list provided to implement the class Game as given in the class diagram.
# In the constructor of Game class, initialize players_list with list of players
# Display the name and experience of the players after sorting the players based on their experience(descending order)
# Display the name and experience of the players after moving the first player (0 index position) to the 4th (3 index position) position.

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
    def __init__(self,players_list):
        self.__players_list=players_list

    def sort_players_based_on_experience(self):
        try:
            self.__players_list.sort(key=lambda x:x.get_experience())
        except:
            return None

    def shift_player_to_new_position(self, old_index_position, new_index_position):
        try:
            self.__players_list[old_index_position],self.__players_list[new_index_position]=self.__players_list[new_index_position],self.__players_list[old_index_position]
        except:
            return None

    def display_player_details(self):
        for player in self.__players_list:
            print(player.get_name(),':',player.get_experience(),end='\n')




player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
#Create object of Game class, invoke the methods and test your program

p=Game(players_list)
p.display_player_details()
