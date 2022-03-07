# Hamiltonian Path

Given a 12 x 12 matrix, visit all the cells once without passing through the blocks.
This is a solution of the questions from [internet game nft](https://internet.game/).

# Instructions
## Place Blocks
Modify block location in the main function
```
blocks = [[10,1],[5,1],[4,5],[4,10]]
```
Blocks are an 2d array. Each row stores the block location of
(row, column)
## Activate
```
python3 main.py
```
## Plot Image Real Time
1. install matplotlib
    ```
    pip3 install matplotlib
    ```
2. Uncomment the plot code
    ```python
    # Plot the grid
    # plt.imshow(visited)
    # plt.pause(0.0001)
    ...
    # Enable plot in real time
    # plt.show()
    ```

# Example

![Alt Text](https://github.com/kyu-kuanwei/Hamiltonian-Path/blob/main/example/sample1.gif)