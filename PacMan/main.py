import random

# Constants
EMPTY = ' 's
WALL = '#'
PACMAN = 'P'
DOT = '.'
GHOST = 'G'

# Game map
MAP = [
    "#######################",
    "#P...................G#",
    "#.###.###.###.###.###.#",
    "#.#.#.#.#.#.#.#.#.#.#.#",
    "#.###.###.###.###.###.#",
    "#.....................#",
    "#.###.#.#####.#.###.#.#",
    "#.....#...#...#.....#.#",
    "#######.#.#.#.#######.#",
    "      #.#...#.#       #",
    "      #.#####.#       #",
    "      #.......#       #",
    "      #############   #",
    "             #.......# #",
    "             #.#####.# #",
    "             #.......# #",
    "             ###########",
]

# Pac-Man's initial position
pacman_x, pacman_y = 1, 1

# Ghost's initial position
ghost_x, ghost_y = 22, 1

# Initialize score
score = 0

# Main game loop
while True:
    # Clear the screen
    print("\033c", end="")

    # Display the game map
    for row in MAP:
        print(row)

    # Display score
    print("Score:", score)

    # Get user input
    move = input("Enter a move (w/a/s/d): ").lower()

    # Update Pac-Man's position
    if move == 'w' and MAP[pacman_y - 1][pacman_x] != WALL:
        pacman_y -= 1
    elif move == 's' and MAP[pacman_y + 1][pacman_x] != WALL:
        pacman_y += 1
    elif move == 'a' and MAP[pacman_y][pacman_x - 1] != WALL:
        pacman_x -= 1
    elif move == 'd' and MAP[pacman_y][pacman_x + 1] != WALL:
        pacman_x += 1

    # Check for collisions with dots
    if MAP[pacman_y][pacman_x] == DOT:
        score += 10
        MAP[pacman_y] = MAP[pacman_y][:pacman_x] + EMPTY + MAP[pacman_y][pacman_x + 1:]

    # Check for collisions with ghosts
    if pacman_x == ghost_x and pacman_y == ghost_y:
        print("Game Over! Your score:", score)
        break

    # Move the ghost randomly
    ghost_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    random.shuffle(ghost_moves)
    for move_x, move_y in ghost_moves:
        if MAP[ghost_y + move_y][ghost_x + move_x] != WALL:
            ghost_x += move_x
            ghost_y += move_y
            break