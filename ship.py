class BattleShip():
    def __init__(self, shipsize):
        self.shipleft = shipsize
        self.shipsize = shipsize
        self.location = []

    def hit(self, x, y):
        if self.remove_location(x, y):
            self.shipleft -= 1

    def get_shipsize(self):
        return self.shipsize

    def get_shipleft(self):
        return self.shipleft

    def add_location(self, x, y):
        self.location.append((x,y))

    def get_locations(self):
        return self.location

    def remove_location(self, x, y):
        for i in self.location:
            if i[0] == x and i[1] == y:
                self.location.remove(i)
                return True
        return False

    def destroyed(self):
        if self.shipleft == 0:
            return True

