# The tower of hanoi consists of 3 towers and 64 discs arranged according to their sizes. This problem uses the concept of recursion and allows us to break the bigger problem into smaller ones.


def tower_of_hanoi(n, source, destination, intermediate):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
    else:
        tower_of_hanoi(n-1,source,intermediate,destination)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n-1,intermediate,destination,source)

tower_of_hanoi(64,"A","B","C")