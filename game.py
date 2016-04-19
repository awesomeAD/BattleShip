from game_logic import BattleShipGame
from game_logic import DoubleHit


length = 10
width = 10
num_ships = 2
ship_sizes = [2, 3]
p1_place = ["long", "long"]
p2_place = ["long", "side"]
p1_start = [(4,4), (3,2)]
p2_start = [(2,2), (8,3)]
first = 1

game = BattleShipGame(length, width, num_ships, ship_sizes, p1_place, p2_place, p1_start, p2_start, first)
while not game.game_over():

    print("Player " + str(game.get_turn()) + "'s turn!")

    x = int(input("attack pos x: "))
    y = int(input("attack pos y: "))

    while x > game.get_length() or y > game.get_width():
        print("You went out of bounds, please select a proper position")
        x = int(input("attack pos x: "))
        y = int(input("attack pos y: "))

        # raise Exception("Out of Bounds")

    try:
        if game.attack(x, y):
            print("Player " +str(game.get_turn()) +" Hit other Player at "+ str(x) + ", " +str(y))
        else:
            print("Player " +str(game.get_turn()) +" Missed other Player at "+ str(x) + ", " +str(y))
        game.print_both_boards()
        game.change_turn()
    except DoubleHit:
        print("Try Again Hit Target Already")

game.change_turn()
print("\n\nWinner is Player: " + str(game.get_turn()))