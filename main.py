from Board import Board
import time
from copy import deepcopy
import matplotlib.pyplot as plt

class Algorithm:
    def __init__(self, board):
        self._board = board
        self._board_size = self._board.size()
        self._result = []
        self._status = False
        self._total_move = self._board.moves()
        self._calculate()

    def _calculate(self):
        visited = deepcopy(self._board.board())
        path = []

        self._DFS(visited, 0, 0, path, '')

    def _DFS(self, visited, row, col, path, orientation):
        if row < 0 or row >= self._board_size or col < 0 or col >= self._board_size or visited[row][col] != 0:
            return False

        # Already success
        if self._status:
            return True

        # Pruning
        # When the path faces the wall and if either right/left or up/down is able to go
        # then the path is must wrong.
        if row == 0 or row == self._board_size - 1:
            if col + 1 < self._board_size and col - 1 >= 0:
                if visited[row][col + 1] == 0 and visited[row][col - 1] == 0:
                    return False

        if col == 0 or col == self._board_size - 1:
            if row + 1 < self._board_size and row - 1 >= 0:
                if visited[row + 1][col] == 0 and visited[row - 1][col] == 0:
                    return False

        # TODO: buggy prunning
        # Simliar prunning, but seems buggy.
        # When the path faces the visited cell, and if either right/left or up/down is able to go
        # then the path is must wrong.
        if orientation == 'l' and col - 1 >= 0 and visited[row][col - 1] == 1:
            if row + 1 < self._board_size and row - 1 >= 0 and visited[row + 1][col] == 0 and visited[row - 1][col] == 0:
                return False

        if orientation == 'u' and row - 1 >= 0 and visited[row - 1][col] == 1:
            if col + 1 < self._board_size and col - 1 >= 0 and visited[row][col + 1] == 0 and visited[row][col - 1] == 0:
                return False

        if orientation == 'r' and col + 1 < self._board_size and visited[row][col + 1] == 1:
            if row + 1 < self._board_size and row - 1 >= 0 and visited[row + 1][col] == 0 and visited[row - 1][col] == 0:
                return False

        if orientation == 'd' and row + 1 < self._board_size and visited[row + 1][col] == 1:
            if col + 1 < self._board_size and col - 1 >= 0 and visited[row][col + 1] == 0 and visited[row][col - 1] == 0:
                return False

        visited[row][col] = 1
        path.append(row * self._board_size + col)
        # Plot the grid
        # plt.imshow(visited)
        # plt.pause(0.0001)

        if len(path) == self._total_move:
            self._result = path
            self._status = True
            return self._status

        if self._DFS(visited, row + 1, col, path, 'd') or self._DFS(visited, row, col - 1, path, 'l') \
                or self._DFS(visited, row, col + 1, path, 'r') or self._DFS(visited, row - 1, col, path, 'u'):
                return True
        else:
            visited[row][col] = 0
            path.pop()

        return False

    def result(self):
        return self._result

def pretty_print(arr):
    for i in arr:
        print(i)

def main():
    # blocks = [[5,4]]
    blocks = [[10,1],[5,1],[4,5],[4,10]]
    board = Board(blocks, 12)
    print(Algorithm(board).result())
    # Enable plot in real time
    # plt.show()
main()
