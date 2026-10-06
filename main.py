class tiktaktoe:

    def __init__(self):
        self.board = list(range(9))
        self.player1 = "X"
        self.player2 = "O"
        self.cur_player = 2

    def change_cur(self):
        self.cur_player = 2 if self.cur_player == 1 else 1

    def get_input(self):
        inp = input("chose a field: ")
        while (not inp.isdigit()) or (not (0 <= int(inp) < 9)) or self.board[int(inp)] != int(inp):
            inp = input("chose a correct field")
        return int(inp)

    def place_field(self, inp):
        self.board[inp] = self.player1 if self.cur_player == 1 else self.player2


    def print_board(self):
        result = ""
        for i in range(9):
            result += str(self.board[i]) + (" | " if (i % 3 != 2) else "\n")
        print(result)

    def is_win(self):
        for i in range(3):
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i]:
                return True
            if self.board[0 + i * 3] == self.board[1 + i * 3] == self.board[2 + i *3]:
                return True
        if self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]:
            return True
        return False

    def is_draw(self):
        free_fields = 0
        for field in self.board:
            if str(field).isdigit():
                free_fields += 1
        if free_fields == 0:
            return True
        return False

    def loop(self):
        game_runs = True
        while game_runs:
            self.print_board()
            self.change_cur()
            print("Turn of player" + str(self.cur_player))
            self.place_field(self.get_input())
            if self.is_win():
                print("Player" + str(self.cur_player) + " won")
                game_runs = False
            if self.is_draw():
                print("draw")
                game_runs = False

cur = tiktaktoe()
cur.loop()


