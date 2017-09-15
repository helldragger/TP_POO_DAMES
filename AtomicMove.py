class AtomicMove:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def get_end(self):
        return self._end
