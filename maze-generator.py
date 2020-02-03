import random
from collections import deque

class CreateMaze:

    maze = []
    visited = []
    position_searched = []
    rows = 0
    columns = 0
    still_searching = True

    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns

    def creation(self):
        # begin by initializing a 2D array with its borders
        # initialized to 1 and its interior initialized to 0

        temp = ['-' for l in range(self.columns*2+1)]
        falseRow = [False for j in range(self.columns*2+1)]

        self.maze.append(temp)
        self.visited.append(falseRow)
        self.position_searched.append(falseRow)
        for i in range(1, self.rows+1):
            temp = ['-' for l in range(self.columns * 2 + 1)]
            self.maze.append([])
            self.visited.append([])
            self.position_searched.append([])
            self.maze[2 * i-1].append("|")
            self.maze[2*i-1].append("*")
            self.maze[2*i-1].append("|")
            self.visited[2*i-1].append(False)
            self.visited[2*i-1].append(False)
            self.visited[2 * i-1].append(False)
            self.visited[2 * i-1].append(False)
            self.position_searched[2 * i - 1].append(False)
            self.position_searched[2 * i - 1].append(False)
            self.position_searched[2 * i - 1].append(False)
            self.position_searched[2 * i - 1].append(False)


            for j in range(1, self.columns-1):
                self.visited[2*i-1].append(False)
                self.position_searched[2*i-1].append(False)
                if i == 1 or i == self.rows:
                    self.maze[2*i-1].append("*")

                else:
                    self.maze[2*i-1].append("*")

                self.visited[2*i-1].append(False)
                self.position_searched[2 * i - 1].append(False)

                self.maze[2*i-1].append('|')

            self.maze[2*i-1].append("*")
            self.maze[2 * i-1].append("|")
            self.visited[2 * i - 1].append(False)
            self.position_searched[2 * i - 1].append(False)
            self.visited.append(falseRow)
            self.position_searched.append(falseRow)
            self.maze.append(temp)

        # for i in range(len(self.maze[0])):
        #
        #     print(self.maze[i])


        # allow for entrance and exit into the self.maze by changing
        # 2 locations on the border to 0
        # NOTE:
        #   it cannot be the corners because our self.maze has only
        #   valid paths of right, left, up, or down, not
        #   diagonal
        self.maze[1][0] = " "
        self.maze[1][1] = " "
        self.maze[2*self.rows - 1][2*self.columns - 1] = " "
        self.maze[2 * self.rows - 1][2 * self.columns] = " "
        self.visited[1][1] = True


        # randomize one valid path from the start to the end
        # NOTE:
        #   we can go right (x+1), left (x-1), down (y+1), or up (y-1)

        # use a stack that can be used to eliminate a cycle should it
        # appear in the path

        stack_positions_visited = deque()
        stack_positions_visited.append([1, 1, 'right'])
        position = [1, 1]

        # this will dictate the random path
        directions = ["right", "left", "down", "up"]
        opposite_position = {"right": "left", "down": "up", "up": "down", "left": "right"}
        lastMovementMap = {"right": " ", "left": " ", "down": " ", "up": " "}
        randomDirection = random.choice([0, 2])
        lastMovement = directions[randomDirection]


        while position != [2*self.rows-1, 2*self.columns-1]:
            # print(stack_positions_visited)
            cycled = False
            if directions[randomDirection] == "right":
                position[1] += 2

            elif directions[randomDirection] == "left":
                position[1] -= 2

            elif directions[randomDirection] == "down":
                position[0] += 2

            else:
                position[0] -= 2

            while True:

                if position[0] == 1:

                    if position[1] == 1:
                        # we are at top left, so we either just went up or left
                        # (or we came from our entry point, so we just went right).
                        # since we do not want to revisit, we go right if we last
                        # went up, or we go down if we last went left
                        if lastMovement == "up":
                            randomDirection = 0
                        else:
                            randomDirection = 2

                    elif position[1] == 2*self.columns - 1:
                        # we are at top right, so we either just went up or right.
                        # since we do not want to revisit, we go left if we last
                        # went up, or we go down if we last went right
                        if lastMovement == "up":
                            randomDirection = 1
                        else:
                            randomDirection = 2

                    else: # position[0] == 1:
                        # we are at the top level but not on corners, so we can't go up
                        randomDirection = random.randint(0, 2)

                elif position[0] == 2*self.rows-1:
                    if position[1] == 1:
                        # we are at bottom left, so we either just went down or left.
                        # since we do not want to revisit, we go right if we last
                        # went down, or we go up if we last went left
                        if lastMovement == "down":
                            randomDirection = 0
                        else:
                            randomDirection = 3

                    elif position[1] == 2*self.columns - 1:
                        # we are at bottom right, so we can just exit right
                        randomDirection = 0

                    else:
                        # we are at the bottom level, so we can't go down
                        randomDirection = random.choice([0, 1, 3])

                elif position[1] == 1:
                    # we are on the left level, so we can't go left
                    randomDirection = random.choice([0, 2, 3])

                elif position[1] == 2*self.columns-1:
                    # we are on the right level, so we can't go right
                    randomDirection = random.choice([1, 2, 3])

                else:
                    randomDirection = random.randint(0, 3)

                if directions[randomDirection] != opposite_position.get(lastMovement):
                    break



            # check if we have cycled
            # print(position, end='')
            # print('is now true')


            if self.visited[position[0]][position[1]]:
                cycled = True
                # print("have we booasdasdaj here??")
                # if we have been here before, let's remove the cycle that got us here
                # print(stack_positions_visited[-1])
                # print(position)
                while not(stack_positions_visited[-1][0] == position[0] and stack_positions_visited[-1][1] == position[1]):
                    # print("have we entered here??")
                    temp_position = stack_positions_visited.pop()
                    self.maze[temp_position[0]+1][temp_position[1]] = '-'
                    self.maze[temp_position[0]-1][temp_position[1]] = '-'
                    self.maze[temp_position[0]][temp_position[1]-1] = '|'
                    self.maze[temp_position[0]][temp_position[1]+1] = '|'
                    self.visited[temp_position[0]][temp_position[1]] = False
                    self.maze[temp_position[0]][temp_position[1]] = '*'

                    # self.maze_with_lines()
                    # print()
                stack_positions_visited.pop()[2]

            # print("BEFORE UPDATE")
            # self.maze_with_lines()
            if not cycled:
                self.update_path(lastMovement, position)
            lastMovement = directions[randomDirection]

            stack_positions_visited.append([position[0], position[1], lastMovement])

            self.maze[position[0]][position[1]] = ' '
            self.visited[position[0]][position[1]] = True
            
        self.maze_with_lines()
        self.fill_remaining_maze(stack_positions_visited)

    def fill_remaining_maze(self, path_backward):
        # path_backward will be a stack of the valid path
        # if we pop it and move back word, we will fill the remaining parts of
        # the maze with invalid paths
        self.forming_path(path_backward)


        # while this point has points around it unvisited, fill in paths

    def forming_path(self, paths_to_fill):

        # I could scramble it, reverse it, or keep it
        paths_to_fill.reverse()

        directions = ["right", "left", "down", "up"]

        while len(paths_to_fill) != 0:
            # i want to pop all positions off the maze path and add all points around it that are not on the path
            # print(paths_to_fill)
            false_paths = deque()
            position = paths_to_fill.pop()
            if position[0] == 1:

                if position[1] == 1:
                    # we are at top left,
                    if not self.visited[position[0]][position[1]+2]:
                        false_paths.append([position[0], position[1]+2, "right"])
                    if not self.visited[position[0]+2][position[1]]:
                        false_paths.append([position[0]+2, position[1], "down"])

                elif position[1] == 2 * self.columns - 1:
                    # we are at top right, so we can go left or down
                    if not self.visited[position[0]][position[1]-2]:
                        false_paths.append([position[0], position[1]-2, "left"])
                    if not self.visited[position[0]+2][position[1]]:
                        false_paths.append([position[0]+2, position[1], "down"])

                else:  # position[0] == 1:
                    # we are at the top level but not on corners, so we just can't go up
                    if not self.visited[position[0]][position[1]-2]:
                        false_paths.append([position[0], position[1]-2, "left"])
                    if not self.visited[position[0]+2][position[1]]:
                        false_paths.append([position[0]+2, position[1], "down"])
                    if not self.visited[position[0]][position[1]+2]:
                        false_paths.append([position[0], position[1]+2, "right"])

            elif position[0] == 2 * self.rows - 1:
                if position[1] == 1:
                    # we are at bottom left
                    if not self.visited[position[0]][position[1]+2]:
                        false_paths.append([position[0], position[1]-2, "right"])
                    if not self.visited[position[0]-2][position[1]]:
                        false_paths.append([position[0]-2, position[1], "up"])

                elif position[1] == 2 * self.columns - 1:
                    # we are at bottom right, so we just can't go right or down
                    if not self.visited[position[0]][position[1]-2]:
                        false_paths.append([position[0], position[1]-2, "left"])
                    if not self.visited[position[0]-2][position[1]]:
                        false_paths.append([position[0]-2, position[1], "up"])

                else:
                    # we are at the bottom level, so we can't go down
                    if not self.visited[position[0]][position[1]-2]:
                        false_paths.append([position[0], position[1]-2, "left"])
                    if not self.visited[position[0]-2][position[1]]:
                        false_paths.append([position[0]-2, position[1], "up"])
                    if not self.visited[position[0]][position[1]+2]:
                        false_paths.append([position[0], position[1]+2, "right"])

            elif position[1] == 1:
                # we are on the left level, so we can't go left
                if not self.visited[position[0]][position[1] + 2]:
                    false_paths.append([position[0], position[1] + 2, "right"])
                if not self.visited[position[0] - 2][position[1]]:
                    false_paths.append([position[0] + 2, position[1], "up"])
                if not self.visited[position[0] + 2][position[1]]:
                    false_paths.append([position[0], position[1] + 2, "down"])

            elif position[1] == 2 * self.columns - 1:
                # we are on the right level, so we can't go right
                if not self.visited[position[0]][position[1] - 2]:
                    false_paths.append([position[0], position[1] - 2, "left"])
                if not self.visited[position[0] - 2][position[1]]:
                    false_paths.append([position[0] - 2, position[1], "up"])
                if not self.visited[position[0] + 2][position[1]]:
                    false_paths.append([position[0] + 2, position[1], "down"])

            else:
                if not self.visited[position[0]][position[1] - 2]:
                    false_paths.append([position[0], position[1] - 2, "left"])
                if not self.visited[position[0] - 2][position[1]]:
                    false_paths.append([position[0] - 2, position[1], "up"])
                if not self.visited[position[0] + 2][position[1]]:
                    false_paths.append([position[0] + 2, position[1], "down"])
                if not self.visited[position[0]][position[1] + 2]:
                    false_paths.append([position[0], position[1] + 2, "right"])

            # now that we have a stack of positions around a point
            # we can start forming a false path...
            # print(false_paths)
            while len(false_paths) != 0:

                position = false_paths.pop()
                # print(position)
                if not (position[0] > 0 and position[0] < 2*self.rows+1 and position[1] > 0 and position[1] < 2*self.columns+1):
                    continue
                if self.visited[position[0]][position[1]]:
                    continue

                self.maze[position[0]][position[1]] = " "
                self.visited[position[0]][position[1]] = True

                false_paths.append([position[0] + 2, position[1], "down"])
                false_paths.append([position[0] - 2, position[1], "up"])
                false_paths.append([position[0], position[1] + 2, "right"])
                false_paths.append([position[0], position[1] - 2, "left"])

                if position[2] == "up":
                    self.maze[position[0] + 1][position[1]] = " "
                elif position[2] == "down":
                    self.maze[position[0] - 1][position[1]] = " "
                elif position[2] == "right":
                    self.maze[position[0]][position[1] - 1] = " "
                elif position[2] == "left":
                    self.maze[position[0]][position[1] + 1] = " "

                if position[0] == 1:

                    if position[1] == 1:
                        # we are at top left, so we either just went up or left
                        # (or we came from our entry point, so we just went right).
                        # since we do not want to revisit, we go right if we last
                        # went up, or we go down if we last went left
                        randomDirection = random.choice([0, 2])
                        # paths_to_fill.append([position[0]+2, position[1]])
                        # paths_to_fill.append([position[0], position[1] + 2])

                    elif position[1] == 2 * self.columns - 1:
                        # we are at top right, so we can go left or down
                        randomDirection = random.choice([1, 2])

                    else:  # position[0] == 1:
                        # we are at the top level but not on corners, so we just can't go up
                        randomDirection = random.randint(0, 2)

                elif position[0] == 2 * self.rows - 1:
                    if position[1] == 1:
                        # we are at bottom left, so we either just went down or left.
                        # since we do not want to revisit, we go right if we last
                        # went down, or we go up if we last went left
                        randomDirection = random.choice([0, 3])

                    elif position[1] == 2 * self.columns - 1:
                        # we are at bottom right, so we just can't go right or down
                        randomDirection = random.choice([1, 3])

                    else:
                        # we are at the bottom level, so we can't go down
                        randomDirection = random.choice([0, 1, 3])

                elif position[1] == 1:
                    # we are on the left level, so we can't go left
                    randomDirection = random.choice([0, 2, 3])

                elif position[1] == 2 * self.columns - 1:
                    # we are on the right level, so we can't go right
                    randomDirection = random.choice([1, 2, 3])

                else:
                    randomDirection = random.randint(0, 3)



                if directions[randomDirection] == "right":
                    position[1] += 2

                elif directions[randomDirection] == "left":
                    position[1] -= 2

                elif directions[randomDirection] == "down":
                    position[0] += 2

                else:
                    position[0] -= 2

                position[2] = directions[randomDirection]
                false_paths.append(position)

    def update_path(self, lastMovement, position):

        if lastMovement == 'up':
            self.maze[position[0] + 1][position[1]] = ' '
        elif lastMovement == 'down':
            self.maze[position[0] - 1][position[1]] = ' '
        elif lastMovement == 'right':
            self.maze[position[0]][position[1] - 1] = ' '
        else: # lastMovement == 'left':
            self.maze[position[0]][position[1] + 1] = ' '
            
    def maze_with_lines(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                print(f'{str(self.maze[i][j]):2s}', end='')
            print()

    def solve_dfs(self, position):
        # will recursively search through the maze until the valid path solves
        # or we reach a dead end
        self.position_searched[position[0]][position[1]] = True
        if position[0] == len(self.maze)-2 and position[1] == len(self.maze[0])-2:
            self.maze[position[0]][position[1]] = 'V'
            self.still_searching = False
            return True

        legal_directions = []
        # first, let's add the valid connections to a list
        if (self.maze[position[0]+1][position[1]] != '-'):
            legal_directions.append([position[0]+2,position[1]])
        if (self.maze[position[0]-1][position[1]] != '-'):
            legal_directions.append([position[0]-2,position[1]])
        if (self.maze[position[0]][position[1]+1] != '|'):
            legal_directions.append([position[0],position[1]+2])
        if (self.maze[position[0]][position[1]-1] != '|'):
            legal_directions.append([position[0],position[1]-2])

        valid = False

        for pos in legal_directions:
            if self.legal(pos):
                truth = self.solve_dfs(pos)
                if truth:
                    valid = True

        if valid:
            self.maze[position[0]][position[1]] = 'D'
        else:
            self.maze[position[0]][position[1]] = ' '

        return valid

    def solve_bfs(self):

        queue = deque()
        visited = []

        for i in range(len(self.visited)):
            visited.append([])
            for j in range(len(self.visited[0])):
                visited[i].append(False)

        queue.append([(1, 1)])
        while len(queue) != 0:
            position = queue.popleft()
            visited[position[-1][0]][position[-1][1]] = True
            last_vertex = position[-1]
            #self.maze[last_vertex[0]][last_vertex[1]] = 'B'
            
            if last_vertex == (self.rows*2 - 1, self.columns*2 - 1):
                self.bfs_correct_path(position)
                return last_vertex
            
            if (self.maze[last_vertex[0] + 1][last_vertex[1]] != '-'):
                if self.bfs_legal([last_vertex[0] + 2, last_vertex[1]], visited):
                    new_path = position.copy()
                    new_path.append((last_vertex[0] + 2, last_vertex[1]))
                    queue.append(new_path)
            if (self.maze[last_vertex[0] - 1][last_vertex[1]] != '-'):
                if self.bfs_legal([last_vertex[0] - 2, last_vertex[1]], visited):
                    new_path = position.copy()
                    new_path.append((last_vertex[0] - 2, last_vertex[1]))
                    queue.append(new_path)
            if (self.maze[last_vertex[0]][last_vertex[1] + 1] != '|'):
                if self.bfs_legal([last_vertex[0], last_vertex[1] + 2], visited):
                    new_path = position.copy()
                    new_path.append((last_vertex[0], last_vertex[1] + 2))
                    queue.append(new_path)
            if (self.maze[last_vertex[0]][last_vertex[1] - 1] != '|'):
                if self.bfs_legal([last_vertex[0], last_vertex[1] - 2], visited):
                    new_path = position.copy()
                    new_path.append((last_vertex[0], last_vertex[1] - 2))
                    queue.append(new_path)
    def bfs_correct_path(self, path):
        for points in path:
            self.maze[points[0]][points[1]] = 'B'
    
    def legal(self, position):
        if (position[0] > 0 and position[0] < len(self.maze) and position[1] > 0 and position[1] < len(self.maze[0])):
            if not self.position_searched[position[0]][position[1]]:
                return True
        return False

    def bfs_legal(self, position, visited):
        if (position[0] > 0 and position[0] < len(self.maze) and position[1] > 0 and position[1] < len(self.maze[0])):
            if not visited[position[0]][position[1]]:
                return True
        return False

maze1 = CreateMaze(10, 12)
maze1.creation()
print('\n\n')
maze1.maze_with_lines()
maze1.solve_dfs([1, 1])
maze1.maze_with_lines()
maze1.solve_bfs()
maze1.maze_with_lines()


