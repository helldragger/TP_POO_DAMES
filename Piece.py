import AtomicMove as am


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
        if  0 <= self._pos[0]+modif < len(board._board):
            if board._board[self._pos[0]+modif][self._pos[1]] == " " :
                moves.append(am.AtomicMove(self._pos, (self._pos[0]+modif, self._pos[1])))
        if  0 <= self._pos[0]+modif < len(board._board) \
                and 0 <= self._pos[1]+modif < len(board._board)//2:
            if board._board[self._pos[0]+modif][self._pos[1] + modif] == " ":
                moves.append(am.AtomicMove(self._pos, (self._pos[0]+modif, self._pos[1] + modif)))
        return moves
