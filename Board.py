import Piece as p


class Board:
    def __init__(self, size):
        self._size = size

        board = []
        for row in range(size):
            board.append([])
            for col in range(size//2):
                case = ""
                if row < size//2 - 1:
                    case = p.Piece("N", (row, col))
                elif row > size//2:
                    case = p.Piece("B", (row, col))
                else:
                    case = " "
                board[row].append(case)

        self._board = board

    def to_lines(self):
        print(self._board)
        for row in range(self._size):
            print("[ ", end="")
            for case in self._board[row]:
                if row % 2 == 0:
                    print(".", end=" ")
                if case != " ":
                    print(case.get_color(), end=" ")
                else:
                    print(case, end=" ")
                if row % 2 != 0:
                    print(".", end=" ")
            print("]")
        return

    def move(self, move):
        pion = self._board[move._start[0]][move._start[1]]
        pion._pos = move._end
        self._board[move._end[0]][move._end[1]] = pion
        self._board[move._start[0]][move._start[1]] = " "

