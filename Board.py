# A board with 10 x 10 size
# 0 means unvisited, -1 means block, 1 means visited
class Board:
    def __init__(self, blocks, size):
        self._board = []
        self._size = size
        self._blocks = blocks
        self._init_board()
        self._place_block(blocks)

    def _init_board(self):
        self._board = [[0 for _ in range(self._size)] for _ in range(self._size)]

    def _place_block(self, blocks):
        for i in blocks:
            self._board[i[0]][i[1]] = -1

    def size(self):
        return self._size

    def moves(self):
        return self._size * self._size - len(self._blocks)

    def board(self):
        return self._board

    def print_board(self):
        for i in range(self._size):
            print(self._board[i])