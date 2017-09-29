import AtomicMove as am


class Capture(am.AtomicMove):
    def __init__(self, start, capture, end):
        super(Capture, self).__init__(start, end)
        self._captured = capture
