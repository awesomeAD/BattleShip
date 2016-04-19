from field import BattleField

class DoubleHit(Exception):
    Exception("Already hit this target")

class BattleShipGame():
    def __init__(self, board_length, board_width, num_ships, ship_sizes,
                 p1_place, p2_place, p1_start, p2_start, first):
        self.P1 = BattleField(board_length, board_width, num_ships, ship_sizes, p1_place, p1_start)
        self.P2 = BattleField(board_length, board_width, num_ships, ship_sizes, p2_place, p2_start)
        self.P1.place_ships()
        self.P2.place_ships()

        self.turn = first
        self.length = board_length
        self.width = board_width

    def print_both_boards(self):
        print("Printing Player 1 Board")
        self.P1.print_field()
        print("\nPrinting Player 2 Board")
        self.P2.print_field()

    def attack(self, x, y):
        x = x-1
        y = y-1
        if self.turn == 2:
            val = self.P1.get_value(x, y)
            if val == 1:
                self.P1.change_value(x, y, -1)
                self.P1.ship_hit(x,y)
                return True
            elif val == 0:
                self.P1.change_value(x, y, -1)
                return False
            else:
                raise DoubleHit()
        else:
            val = self.P2.get_value(x, y)
            if val == 1:
                self.P2.change_value(x, y, -1)
                self.P2.ship_hit(x,y)
                return True
            elif val == 0:
                self.P2.change_value(x, y, -1)
                return False
            else:
                raise DoubleHit()

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def get_turn(self):
        return self.turn

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def game_over(self):
        if self.P1.all_ships_destroyed() or self.P2.all_ships_destroyed():
            return True
        return False

    def get_p1_field(self):
        return self.P1.get_field()

    def get_p2_field(self):
        return self.P2.get_field()

