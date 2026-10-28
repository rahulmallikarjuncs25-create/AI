
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
    print()


def hill_climbing():
    current = [1, 3, 0, 2]
    current_cost = cost(current)

    print("Initial Board:", current)
    print("Initial Cost:", current_cost)

    while current_cost != 0:
        best = current
        best_cost = current_cost

        for col in range(4):
            for row in range(4):
                if row != current[col]:
                    neighbor = current.copy()
                    neighbor[col] = row
                    neighbor_cost = cost(neighbor)

                    if neighbor_cost < best_cost:
                        best = neighbor
                        best_cost = neighbor_cost

        if best_cost >= current_cost:
            print("Local optimum reached.")
            return

        current = best
        current_cost = best_cost

        print("Current Board:", current)
        print("Current Cost:", current_cost)

    print("Solution Found!")
    print_board(current)

hill_climbing()

OUTPUT:
Initial Board: [1, 3, 0, 2]
Initial Cost: 0
Solution Found!
. . Q . 
Q . . . 
. . . Q 
. Q . . 

