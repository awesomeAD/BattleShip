from game_logic import BattleShipGame
from game_logic import DoubleHit

import tkinter

_BOARD_BACKGROUND = "light blue"
_MENU_BACKGROUND = "light green"
_DEFAULT_FONT = ('Helvetica', 20)

class BattleMenu:
    def __init__(self):
        self._menu_window = tkinter.Tk()

        ## Menu Title

        start_label = tkinter.Label(master = self._menu_window,
                                     text = "Ready to Play BattleShip!",
                                     font = _DEFAULT_FONT)

        start_label.grid(row = 0, column = 0, columnspan = 2)

        ## Select size of grid Option

        grid_label = tkinter.Label(master = self._menu_window,
                                  text = "Grid Size: ",
                                  font = _DEFAULT_FONT)

        grid_label.grid(row = 1, column = 0)

        self._variable1 = tkinter.StringVar()
        self._variable1.set("10x10")

        grid_menu = tkinter.OptionMenu(self._menu_window, self._variable1,
                                      '10x10', '20x20', '30x30')

        grid_menu.grid(row = 1, column = 1,)

        ## Number of ships option

        num_ships_label = tkinter.Label(master = self._menu_window,
                                  text = "Number of Ships ",
                                  font = _DEFAULT_FONT)

        num_ships_label.grid(row = 2, column = 0)

        self._variable2 = tkinter.StringVar()
        self._variable2.set("5")

        num_ships_menu = tkinter.OptionMenu(self._menu_window, self._variable2,
                                      '3', '4', '5', '6', '7')

        num_ships_menu.grid(row = 2, column = 1)

        ## Selection Screen Button

        start_button = tkinter.Button(master = self._menu_window,
                                      text = 'Next Selection!', font = _DEFAULT_FONT,
                                      command = self._select_game)

        start_button.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

        self._menu_window.mainloop()


    def _select_game(self):

        self._ship_menu = tkinter.Toplevel()

        ## Second Window Menu Label

        options_label = tkinter.Label(master = self._ship_menu,
                                     text = "Choose Ship Options!",
                                     font = _DEFAULT_FONT)

        options_label.grid(row = 0, column = 0, columnspan = 3)

        ## Ship Options

        self._variable3 = []

        for i in range(int(self._variable2.get())):

            # Label for Ship Options

            ships_size_label = tkinter.Label(master = self._ship_menu,
                                      text = "Choose Ship Sizes for ship " + str(i+1) + ": ",
                                      font = _DEFAULT_FONT)

            ships_size_label.grid(row = 1 + i, column = 0)

            # Ship Sizes

            self._variable3.append(tkinter.StringVar())
            self._variable3[i].set('2')

            ships_size_menu = tkinter.OptionMenu(self._ship_menu, self._variable3[i], '2', '3','4','5')

            ships_size_menu.grid(row = 1 + i, column = 1)

        ## Start Game Button

        start_button = tkinter.Button(master = self._ship_menu,
                                      text = 'Start Game!', font = _DEFAULT_FONT,
                                      command = self._start_game)

        start_button.grid(row = int(self._variable2.get()) + 1, column = 0, columnspan = 2, padx = 10, pady = 10)


    def _start_game(self):

        var3 = []

        for i in self._variable3:
            var3.append(i.get())

        BattleBoard([self._variable1.get(), self._variable2.get(), var3])

class BattleBoard:
    def __init__(self, options):
        self._options = options

        if options[0] == '10x10':
            self._height, self._width = 10, 10
        elif options[0] == '20x20':
            self._height, self._width = 20, 20
        elif options[0] == '30x30':
            self._height, self._width = 30, 30

        self._root_window = tkinter.Toplevel()
        self._root_window.minsize(800, 400)
        self._root_window.maxsize(800, 400)

        self._info_frame = tkinter.Frame(master= self._root_window)
        self._info_frame.grid(row = 0, column = 0, columnspan = 4, sticky = tkinter.N)

        self._opponent_frame = tkinter.Frame(master = self._root_window)
        self._opponent_frame.grid(row = 1, column = 0, columnspan = 2, sticky = tkinter.W + tkinter.E)

        self._my_frame = tkinter.Frame(master = self._root_window)
        self._my_frame.grid(row = 1, column = 2, columnspan = 2, sticky = tkinter.W + tkinter.E)

        self._window1_frame = tkinter.Frame(master = self._opponent_frame)
        self._window1_frame.grid(row = 0, column = 0)
        self.window1 = tkinter.Canvas(master = self._opponent_frame, height = 300, width = 300, background = _BOARD_BACKGROUND)
        self.window1.grid(row = 0, column = 1)

        self._window2_frame = tkinter.Frame(master = self._my_frame)
        self._window2_frame.grid(row = 0, column = 0)
        self.window2 = tkinter.Canvas(master = self._my_frame, height = 300, width = 300, background = _BOARD_BACKGROUND)
        self.window2.grid(row = 0, column = 1)

        self._root_window.rowconfigure(0, weight = 2)
        self._root_window.rowconfigure(1, weight = 8)
        self._root_window.columnconfigure(0, weight = 2)
        self._root_window.columnconfigure(1, weight = 2)
        self._root_window.columnconfigure(2, weight = 2)
        self._root_window.columnconfigure(3, weight = 2)
        self._opponent_frame.columnconfigure(0, weight = 1)
        self._opponent_frame.columnconfigure(1, weight = 9)
        self._my_frame.columnconfigure(0, weight = 1)
        self._my_frame.columnconfigure(1, weight = 9)

        self.window1.bind("<Configure>", self.on_resize)
        self.window2.bind("<Configure>", self.on_resize)


    def on_resize(self, event: tkinter.Event):
        self.draw_lines()

    def draw_lines(self):
        self.window1.delete(tkinter.ALL)
        self.window2.delete(tkinter.ALL)

        width1 = self.window1.winfo_width()
        height1 = self.window1.winfo_height()

        width2 = self.window2.winfo_width()
        height2 = self.window2.winfo_height()

        x1 = width1 / (self._width)
        y1 = height1 / (self._height)

        x2 = width2 / (self._width)
        y2 = height2 / (self._height)

        for i in range(self._width):
            if i != self._width:
                self.window1.create_line(i*x1, 0, i*x1, height1, fill = 'black')
                self.window2.create_line(i*x2, 0, i*x2, height2, fill = 'black')
            else:
                self.window1.create_line(height1, 0, height1, height1, fill = 'black')
                self.window2.create_line(height2, 0, height2, height2, fill = 'black')

        for i in range(self._height):
            if i != self._height:
                self.window1.create_line(0, i*y1, width1, i*y1, fill = 'black')
                self.window2.create_line(0, i*y2, width2, i*y2, fill = 'black')
            else:
                self.window1.create_line(0, width1, width1, width1, fill = 'black')
                self.window2.create_line(0,width2, width2, width2, fill = 'black')




if __name__ == "__main__":
    k = BattleMenu()