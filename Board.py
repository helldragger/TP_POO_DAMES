import Piece as p
import Capture as c
import Piece as p


class Board:
    def __init__(self, size):
        self._size = size

        board = []
        for row in range(size):
            board.append([])
            for col in range(size):
                case = ""
                if (col % 2 == 0 and row % 2 != 0) \
                    or (col % 2 != 0 and row % 2 == 0):

                    if row < size//2 - 1:
                        case = p.Piece("N", (row, col))
                    elif row > size//2:
                        case = p.Piece("B", (row, col))
                    else:
                        case = " "
                else:
                    case = "."
                board[row].append(case)

        self._board = board

    def to_lines(self):
        for row in self._board:
            print("[ ", end="")
            for case in row:
                if type(case) is p.Piece:
                    print(case._color, end=" ")
                else:
                    print(case, end=" ")
            print("]")
        return

    def move(self, move):
        if type(move) is c.Capture:
            self._board[move._captured[0]][move._captured[1]] = " "
        pion = self._board[move._start[0]][move._start[1]]
        pion._pos = move._end
        self._board[move._end[0]][move._end[1]] = pion
        self._board[move._start[0]][move._start[1]] = " "

