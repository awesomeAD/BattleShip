from ship import BattleShip

class BattleField():
    def __init__(self, board_length, board_width, ships, shipsizes, ship_placement, start_ship):
        self._length = board_length
        self._width = board_width
        self.ships = []
        self._ship_placement = ship_placement
        self.place_index = start_ship
        self.field = [[0]*board_width for i in range(board_length)]

        for i in range(ships):
            self.ships.append(BattleShip(shipsizes[i]))

    def place_ships(self):
        for i in range(len(self.ships)):
            ship = self.ships[i]
            ship_size = ship.get_shipsize()
            x,y = self.place_index[i]
            self.field[x-1][y-1] = 1
            self.ships[i].add_location(x-1, y-1)

            if self._ship_placement[i] == "long":
                for j in range(ship_size-1):
                    if x+j >= self._length or y-1 >= self._width:
                        raise Exception("Length out of Range")
                    self.field[x+j][y-1] = 1
                    self.ships[i].add_location(x+j, y-1)
            elif self._ship_placement[i] == "side":
                for j in range(ship_size-1):
                    if y+j >= self._width or x-1 >= self._length:
                        raise Exception("Width out of Range")
                    self.field[x-1][y+j] = 1
                    self.ships[i].add_location(x-1, y+j)
            else:
                Exception("Ship Angle Error")

    def change_value(self, x, y, val):
        self.field[x][y] = val

    def get_value(self, x, y):
        return self.field[x][y]

    def get_field(self):
        return self.field

    def print_field(self):
        for i in self.field:
            print(i)

    def ship_hit(self, x, y):
        for i in self.ships:
            i.hit(x, y)

    def all_ships_destroyed(self):
        for i in self.ships:
            if not i.destroyed():
                return False
        return True

    def reset_field(self):
        self.field = [[0]*self._width for i in range(self._length)]
        self.place_ships()

if __name__ == "__main__":
    x = BattleField(10,10, 2, [2,3], ["long", "side"], [(3,3),(2,8)])
    x.place_ships()
    x.print_field()
