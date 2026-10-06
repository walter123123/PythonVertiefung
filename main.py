class tiktaktoe:

    def __init__(self):
        self.board = list(range(9))
        self.player1 = "X"
        self.player2 = "O"
        self.cur_player = 2
        self.game_runs = False

    def change_cur(self):
        self.cur_player = 2 if self.cur_player == 1 else 1

    def get_input(self):
        inp = input("chose a field: ")
        while (not inp.isdigit()) or (not (0 <= int(inp) < 9)) or self.board[int(inp)] != int(inp):
            inp = input("chose a correct field")
        return int(inp)

    def place_field(self):
        self.change_cur()
        print("Turn of player" + str(self.cur_player))
        inp = self.get_input()
        self.board[inp] = self.player1 if self.cur_player == 1 else self.player2


    def print_board(self):
        result = ""
        for i in range(9):
            result += str(self.board[i]) + (" | " if (i % 3 != 2) else "\n")
        print(result)

    def is_win(self):
        for i in range(3):
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i]:
                print("player" + str(self.cur_player) + " won")
                self.game_runs = False
            if self.board[0 + i * 3] == self.board[1 + i * 3] == self.board[2 + i *3]:
                print("player" + str(self.cur_player) + " won")
                self.game_runs = False
        if self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]:
            print("player" + str(self.cur_player) + " won")
            self.game_runs = False

    def is_draw(self):
        for field in self.board:
            if str(field).isdigit():
                return
        print("draw")
        self.game_runs = False

    def loop(self):
        self.game_runs = True
        while self.game_runs:
            self.print_board()
            self.place_field()
            self.is_win()
            self.is_draw()

cur = tiktaktoe()
cur.loop()


