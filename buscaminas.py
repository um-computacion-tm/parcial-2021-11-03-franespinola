import random


class Buscaminas():
    def __init__(self, rows=None, cols=None, bombs=None):
        self.bombs = bombs
        self.board = []
        self.rows = rows
        self.cols = cols
        for i in range(0, rows):
            v = [" "]*cols
            self.board.append(v)
        mi = 1
        while mi <= bombs:
            fil = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            if " " in self.board[fil][col]:
                self.board[fil][col] = "B"
                mi += 1

    def play(self):
        pass

    def show_board(self):
        pass

    def question(self):
        pass

    def win(self):
        count = 1
        for x in range(len(self.board)):
            if "F" in self.board[x]:
                count += 1
                print(count)
        if count != 9:
            return True
        return False

    def lose(self):
        for i in range(len(self.board)):
            if i in self.board[i] == "B":
                return False
            return True
