
import random
import math


def cost(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def print_board(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def simulated_annealing():
    random.seed(42)

    n = 8
    current = [random.randrange(n) for _ in range(n)]
    initial_cost = cost(current)

    temperature = 10.0
    cooling_rate = 0.995
    minimum_temperature = 0.001
    steps = 0
    max_steps = 100000

    print("Initial Board:", current)
    print("Initial Cost:", initial_cost)

    while cost(current) != 0 and temperature > minimum_temperature and steps < max_steps:
        neighbor = current.copy()

        col = random.randrange(n)
        row = random.randrange(n)

        while row == neighbor[col]:
            row = random.randrange(n)

        neighbor[col] = row

        delta = cost(neighbor) - cost(current)

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current = neighbor

        temperature *= cooling_rate
        steps += 1

    print("Final Board:", current)
    print("Final Cost:", cost(current))
    print("Steps:", steps)

    if cost(current) == 0:
        print("Solution Found!")
        print_board(current)
    else:
        print("Solution Not Found!")


simulated_annealing()

OUTPUT:
Initial Board: [1, 0, 4, 3, 3, 2, 1, 1]
Initial Cost: 10
Final Board: [2, 5, 7, 0, 4, 6, 1, 3]
Final Cost: 0
Steps: 874
Solution Found!
. . . Q . . . . 
. . . . . . Q . 
Q . . . . . . . 
. . . . . . . Q 
. . . . Q . . . 
. Q . . . . . . 
. . . . . Q . . 
. . Q . . . . . 
