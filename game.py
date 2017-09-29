import Board as b
import AtomicMove as am


def run():
    is_white = True
    board = b.Board(10)
    while True:
        print("Game state")
        board.to_lines()
        print("Mouvements disponibles:")
        moves = []
        i = 0
        for row in board._board:
            for case in row:
                if case in [" ", "."]:
                    continue
                if (case._color == "B" and is_white) \
                    or (case._color == "N" and not is_white):
                    nxt_moves = case.atomic_moves(board)
                    for move in nxt_moves:
                        print(i, "from", case._pos ,"to", move.get_end())
                        i += 1
                        moves.append(move)
        print("Captures disponibles:")
        for row in board._board:
            for case in row:
                if case in [" ", "."]:
                    continue
                if (case._color == "B" and is_white) \
                    or (case._color == "N" and not is_white):
                    nxt_moves = case.captures(board)
                    for move in nxt_moves:
                        print(i, "from", case._pos, "to", move._end)
                        i += 1
                        moves.append(move)

        mv = int(input("Enter one of the correct propositions: "))
        while not (len(moves) - 1) >= mv >= 0:
            mv = int(input("Enter one of the correct propositions: "))

        board.move(moves[mv])
        is_white = not is_white



        