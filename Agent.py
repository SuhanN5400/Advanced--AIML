import time

# Grid size
W, H = 5, 5

# Obstacles (just for display, agent ignores them)
obstacles = {(1, 1), (2, 4), (3, 4)}

# Tasks the agent must collect
tasks = {(0, 2), (2, 0), (3, 0)}

# Agent start position
agent = [0, 0]

# Show the grid
def show_grid():
    for y in range(H):
        for x in range(W):
            if [x, y] == agent:
                print("A", end=" ")
            elif (x, y) in tasks:
                print("T", end=" ")
            elif (x, y) in obstacles:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
    time.sleep(0.4)

print("Initial Grid:\n")
show_grid()

# SIMPLE REFLEX BEHAVIOR:
# Always move RIGHT first, then DOWN
while tasks:
    # If task is here, collect it
    if tuple(agent) in tasks:
        print(f"Task {tuple(agent)} completed!\n")
        tasks.remove(tuple(agent))

    # Movement rule (very simple)
    if tasks:
        if agent[0] < W - 1:
            agent[0] += 1   # move right
        else:
            agent[0] = 0    # go to next row
            if agent[1] < H - 1:
                agent[1] += 1

    show_grid()

print("✅ All tasks completed! Agent finished work!")
