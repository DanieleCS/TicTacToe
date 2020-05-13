# write your code here
class TicTacToe():
    ACTIVE ='A'
    END = 'E'
    def __init__(self):
        # self.status_old = "_________"
        self.cells = [list('___') for i in range(3)]
        self.status = TicTacToe.ACTIVE
        self.next_player = 'X'
        self.status_description = None

    def load_status(self, status):
        self.cells = [list(status[i * 3:(i + 1) * 3]) for i in range(3)]
        self.check_game()

    def start(self):
        self.print_board()
        while self.status == TicTacToe.ACTIVE:
            self.next_move()
            self.print_board()
        self.show_game_status()

    def start_from_cells(self, init_cells, first_player='X'):
        self.next_player = first_player
        self.load_status(init_cells)
        self.start()

    def check_game(self):
        count_x = sum([row.count('X') for row in self.cells])
        count_o = sum([row.count('O') for row in self.cells])
        count_empty = sum([row.count('_') for row in self.cells])
        wins = {"X": 0, "O": 0}

        for row in self.cells:
            if row[0] == row[1] == row[2] and row[0] != '_':
                wins[row[0]] += 1
        for i in range(3):
            col = [row[i] for row in self.cells]
            if col[0] == col[1] == col[2] and col[0] != '_':
                wins[col[0]] += 1
        if self.cells[1][1] != '_' and ((self.cells[0][0] == self.cells[1][1] == self.cells[2][2])
                                        or (self.cells[2][0] == self.cells[1][1] == self.cells[0][2])):
            wins[self.cells[1][1]] += 1

        if (abs(count_x - count_o) > 1
                or wins['X'] + wins['O'] > 1):
            self.status = TicTacToe.END
            self.status_description = 'Impossible'
        elif wins['X'] == 1:
            self.status = TicTacToe.END
            self.status_description = 'X wins'
        elif wins['O'] == 1:
            self.status = TicTacToe.END
            self.status_description = 'O wins'
        elif count_empty > 0:
            self.status = TicTacToe.ACTIVE
            self.status_description = 'Game not finished'
        else:
            self.status = TicTacToe.END
            self.status_description = 'Draw'

    def print_board(self):
        print("-" * 9)
        print("| " + " ".join(self.cells[0]) + " |")
        print("| " + " ".join(self.cells[1]) + " |")
        print("| " + " ".join(self.cells[2]) + " |")
        print("-" * 9)

    def show_game_status(self):
        print(self.status_description)

    def next_move(self):
        while True:
            in_str = input("Enter the coordinates: > ")
            coors = [int(s) for s in in_str.split() if s.isnumeric()]
            if len(coors) < 2:
                print("You should enter numbers!")
                continue
            if not (1 <= coors[0] <= 3) or not (1 <= coors[1] <= 3):
                print("Coordinates should be from 1 to 3!")
                continue
            if self.cells[3-coors[1]][coors[0]-1] != '_':
                print("This cell is occupied! Choose another one!")
                continue
            break
        self.cells[3-coors[1]][coors[0]-1] = self.next_player
        self.check_game()
        self.switch_player()

    def switch_player(self):
        self.next_player = 'X' if self.next_player == 'O' else 'O'



my_game = TicTacToe()
# my_cells = input('Enter cells: > ')
# my_game.start_from_cells(my_cells)
my_game.start()
