def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def tower_of_hanoi(n, source, target, auxiliary, moves=None):
    if moves is None:
        moves = []
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, target, moves)
        moves.append((n, source, target))
        tower_of_hanoi(n - 1, auxiliary, target, source, moves)
    return moves

# Example usage
if __name__ == "__main__":
    n = 5
    print(f"Fibonacci series up to {n}:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print("\n")

    disks = 3
    print(f"Tower of Hanoi moves for {disks} disks:")
    moves = tower_of_hanoi(disks, 'A', 'C', 'B')
    for move in moves:
        print(f"Move disk {move[0]} from {move[1]} to {move[2]}")
