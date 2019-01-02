import random

debug = False


class Game1024:

    def __init__(self, t):
        self.board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.target = t
        self.random_new_digit()
        self.random_new_digit()

    def random_new_digit(self):
        while True:
            i = random.randrange(0,4)
            j = random.randrange(0,4)
            if self.board[i][j] == 0 :
                self.board[i][j] = 2 if random.random() < 0.9 else 4
                break

    def move(self, m):
        if m == 'w':
            self.moveUp()
        elif m == 's':
            self.moveDown()
        elif m == 'a':
            self.moveLeft()
        elif m == 'd':
            self.moveRight()
        else:
            print("Invalid move: only can use A (left), D (right), W (up), and S (down).")
        self.random_new_digit()
        self.print_board()
        

    def moveDown(self):
        j = 0
        while j < 4:
            i1 = 3
            i2 = i1 - 1
            while i1 > 0:
                if debug:
                    print("j: {}, i1: {}, i2: {}".format(j, i1, i2))
                    self.print_board()
                if self.board[i1][j] == 0:
                    if self.board[i2][j] != 0:
                        self.board[i1][j] = self.board[i2][j]
                        self.board[i2][j] = 0
                    i2 -= 1
                else:
                    if self.board[i2][j] == 0:
                        i2 -= 1
                    else:
                        if self.board[i2][j] == self.board[i1][j]:
                            self.board[i1][j] += self.board[i2][j]
                            self.board[i2][j] = 0
                        i1 -= 1
                        i2 = i1 - 1
                if i2 < 0:
                    i1 -= 1
                    i2 = i1 - 1
            j += 1

    def moveUp(self):
        j = 0
        while j < 4:
            i1 = 0
            i2 = i1 + 1
            while i1 < 3:
                if debug:
                    print("j: {}, i1: {}, i2: {}".format(j, i1, i2))
                    self.print_board()
                if self.board[i1][j] == 0:
                    if self.board[i2][j] != 0:
                        self.board[i1][j] = self.board[i2][j]
                        self.board[i2][j] = 0
                    i2 += 1
                else:
                    if self.board[i2][j] == 0:
                        i2 += 1
                    else:
                        if self.board[i2][j] == self.board[i1][j]:
                            self.board[i1][j] += self.board[i2][j]
                            self.board[i2][j] = 0
                        i1 += 1
                        i2 = i1 + 1
                if i2 > 3:
                    i1 += 1
                    i2 = i1 + 1
            j += 1

    def moveLeft(self):
        i = 0
        while i < 4:
            j1 = 0
            j2 = j1 + 1
            while j1 < 3:
                if debug:
                    print("i: {}, j1: {}, j2: {}".format(i, j1, j2))
                    self.print_board()
                if self.board[i][j1] == 0:
                    if self.board[i][j2] != 0:
                        self.board[i][j1] = self.board[i][j2]
                        self.board[i][j2] = 0
                    j2 += 1
                else:
                    if self.board[i][j2] == 0:
                        j2 += 1
                    else:
                        if self.board[i][j2] == self.board[i][j1]:
                            self.board[i][j1] += self.board[i][j2]
                            self.board[i][j2] = 0
                        j1 += 1
                        j2 = j1 + 1
                if j2 > 3:
                    j1 += 1
                    j2 = j1 + 1
            i += 1

    def moveRight(self):
        i = 0
        while i < 4:
            j1 = 3
            j2 = j1 - 1
            while j1 > 0:
                if debug:
                    print("i: {}, j1: {}, j2: {}".format(i, j1, j2))
                    self.print_board()
                if self.board[i][j1] == 0:
                    if self.board[i][j2] != 0:
                        self.board[i][j1] = self.board[i][j2]
                        self.board[i][j2] = 0
                    j2 -= 1 
                else:
                    if self.board[i][j2] == 0:
                        j2 -= 1
                    else:
                        if self.board[i][j2] == self.board[i][j1]:
                            self.board[i][j1] += self.board[i][j2]
                            self.board[i][j2] = 0
                        j1 -= 1
                        j2 = j1 - 1
                if j2 < 0:
                    j1 -= 1
                    j2 = j1 - 1
            i += 1

    def continue_check(self):
        zero_exist = False
        for line in self.board:
            for num in line:
                if num == self.target:
                    print("You Win, you have reached {}.".format(self.target))
                    return False
                if num == 0:
                    zero_exist = True
        if not zero_exist:
            print("You failed.")
            return False
        return True

    def print_board(self):
        for line in self.board:
            print(line)
        print("-------")


def main():
    
    index = input("Please input the index of target, it should be larger than 2:")
    if (not index.isdigit()) or (int(index) <= 2):
        index = 11
        print("target index is invalid, set to the default to be 11")
    target = 2 ** int(index)
    print("the target is 2^{} = {}".format(index, target))

    g = Game1024(target)
    g.print_board()
    while g.continue_check():
        m = input("Please use A (left), D (right), W (up), and S (down): ")
        g.move(m)


if __name__ == "__main__": 
    main()
