import Piece as p

class Board:
    def __init__(self, size):
        self._size = size

        board = []
        for row in range(size):
            b_row = []
            char = ""
            for col in range(size//2):
                if row < size//2 - 1:
                    char = p.Piece("N", (row, col))
                elif row > size//2 :
                    char = p.Piece("B", (row, col))
                else:
                    char = " "
            board.append([char for _ in range(size//2)])

        self._board = board

    def to_lines(self):
        for row in range(self._size):
            print("[ ", end="")
            for case in self._board[row]:
                if row % 2 == 0:
                    print(".", end=" ")
                if case != " ":
                    print(case.get_color(),end=" ")
                else:
                    print(case, end=" ")
                if row % 2 != 0:
                    print(".", end=" ")
            print("]")
        return
