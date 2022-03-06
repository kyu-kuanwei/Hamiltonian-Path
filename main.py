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

        self._DFS(visited, 0, 0, path)
        plt.show()

    def _DFS(self, visited, row, col, path):
        if row < 0 or row >= self._board_size or col < 0 or col >= self._board_size or visited[row][col] != 0:
            return False

        # a,b,c,d = True, True, True, True

        # Already success
        if self._status:
            return True

        # Split cell into two part
        if row == 0 or row == self._board_size - 1:
            if col + 1 < self._board_size and col - 1 >= 0:
                if visited[row][col + 1] == 0 and visited[row][col - 1] == 0:
                    return False

        if col == 0 or col == self._board_size - 1:
            if row + 1 < self._board_size and row - 1 >= 0:
                if visited[row + 1][col] == 0 and visited[row - 1][col] == 0:
                    return False

        # if col - 1 >= 0 and visited[row][col - 1] == 1:
        #     if row + 1 < self._board_size and row - 1 >= 0 and visited[row + 1][col] == 0 and visited[row - 1][col] == 0:
        #         return False

        # if row - 1 >= 0 and visited[row - 1][col] == 1:
        #     if col + 1 < self._board_size and col - 1 >= 0 and visited[row][col + 1] == 0 and visited[row][col - 1] == 0:
        #         return False

        # if col + 1 < self._board_size and visited[row][col + 1] == 1:
        #     if row + 1 < self._board_size and row - 1 >= 0 and visited[row + 1][col] == 0 and visited[row - 1][col] == 0:
        #         return False

        # if row + 1 < self._board_size and visited[row + 1][col] == 1:
        #     if col + 1 < self._board_size and col - 1 >= 0 and visited[row][col + 1] == 0 and visited[row][col - 1] == 0:
        #         return False

        visited[row][col] = 1
        path.append(row * 10 + col)
        # Plot the grid
        # plt.imshow(visited)
        # plt.pause(0.0001)

        if len(path) == self._total_move:
            self._result = path
            self._status = True
            return self._status

        if self._DFS(visited, row + 1, col, path) or self._DFS(visited, row, col - 1, path) \
                or self._DFS(visited, row, col + 1, path) or self._DFS(visited, row - 1, col, path):
                return True
        else:
            visited[row][col] = 0
            path.pop()

        return False

    def result(self):
        return self._result

def main():
    blocks = [[10,1],[1,3],[3,6],[2,10]]
    # blocks = [[7,1],[0,2],[8,5],[7,8]]
    # blocks = [[5,4]]
    board = Board(blocks, 12)
    # board = Board(blocks, 10)
    print(Algorithm(board).result())
main()
