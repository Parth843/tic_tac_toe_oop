from models import Board, Player, Game

name1 = input("Enter player one name: ")
name2 = input("Enter player two name: ")

game = Game(name1, name2)

game.play_game()
        