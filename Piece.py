import AtomicMove as am
import Capture as cpt

class Piece:
    def __init__(self, color, pos):
        """
        short desc

        long desc

        :param self: this class instance

        :return: nothing
        """
        self._pos = pos
        self._color = color

    def get_color(self):
        return self._color

    def get_pos(self):
        return self._pos

    def atomic_moves(self, board):
        go_up = self._color == "B"
        modif = 1 - 2 * int(go_up)
        moves = []

        x = self._pos[0]
        y = self._pos[1]
        if 0 <= x+modif < len(board._board):
            if 0 <= y+modif < len(board._board):
                if board._board[x+modif][y+modif] == " ":
                    moves.append(am.AtomicMove(self._pos, (x+modif, y+modif)))
            if 0 <= y-modif < len(board._board):
                if board._board[x+modif][y-modif] == " ":
                    moves.append(am.AtomicMove(self._pos, (x+modif, y-modif)))
        return moves

    def captures(self, board):
        colors = ["B", "N"]
        go_up = self._color == "B"
        modif = 1 - 2 * int(go_up)
        moves = []
        x = self._pos[0]
        y = self._pos[1]
        if 0 <= x + modif * 2 < len(board._board):
            if 0 <= y + 2 < len(board._board):
                if board._board[x + modif * 2][y + 2] == " " \
                    and type(board._board[x + modif][y + 1]) is Piece:
                    if board._board[x + modif][y + 1]._color == colors[int(go_up)]:
                        moves.append(cpt.Capture(self._pos,
                                                 [x + modif, y + 1],
                                                 [x + modif * 2, y + 2]))
            if 0 <= y - 2 < len(board._board):
                if board._board[x + modif * 2][y - 2] == " " \
                    and type(board._board[x + modif][y - 1]) is Piece:
                    if board._board[x + modif][y - 1]._color == colors[int(go_up)]:
                        moves.append(cpt.Capture(self._pos,
                                                 [x + modif, y - 1],
                                                 [x + modif * 2, y - 2]))
        return moves


class Man(Piece):

    def atomic_moves(self, board):
        go_up = self._color == "B"
        modif = 1 - 2 * int(go_up)
        moves = []

        x = self._pos[0]
        y = self._pos[1]
        if 0 <= x + modif < len(board._board):
            if 0 <= y + modif < len(board._board):
                if board._board[x + modif][y + modif] == " ":
                    moves.append(am.AtomicMove(self._pos, (x + modif, y + modif)))
            if 0 <= y - modif < len(board._board):
                if board._board[x + modif][y - modif] == " ":
                    moves.append(am.AtomicMove(self._pos, (x + modif, y - modif)))
        return moves

class Queen(Piece):
    def atomic_moves(self, board):
        moves = []
        row = self._pos[0]
        column = self._pos[1]

        for rad in range(1, board._size):
            if (column + rad < board._size and row + rad < board._size):
                if type(board._board[row + rad][column + rad]) is Piece:
                    break
                else:
                    moves.append(am.AtomicMove(self._pos, (row + rad, column + rad)))
        for rad in range(1, board._size):
            if (column + rad < board._size and row - rad >= 0):
                if type(board._board[row - rad][column + rad]) is Piece:
                    break
                else:
                    moves.append(am.AtomicMove(self._pos, (row + rad, column + rad)))
        for rad in range(1, board._size):
            if (column - rad >= 0 and row - rad >= 0):
                if type(board._board[row - rad][column - rad]) is Piece:
                    break
                else:
                    moves.append(am.AtomicMove(self._pos, (row + rad, column + rad)))
        for rad in range(1, board._size):
            if (column - rad >= 0 and row + rad < board._size):
                if type(board._board[row + rad][column - rad]) is Piece:
                    break
                else:
                    moves.append(am.AtomicMove(self._pos, (row + rad, column + rad)))
        return moves

