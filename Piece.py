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