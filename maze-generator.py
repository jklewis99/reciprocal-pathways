import random
from collections import deque
import heapq
from union_find import union_find
random.seed(5)

class CreateMaze:

    maze = []
    visited = []
    position_searched = []
    random_edge_weights = dict()
    rows = 0
    columns = 0
    still_searching = True

    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns
        self.randomly_generate_weights(self.random_edge_weights)

    def build_walls(self):
        # begin by initializing a 2D array with its borders
        # initialized to 1 and its interior initialized to 0

        temp = ['-' for l in range(self.columns * 2 + 1)]
        falseRow = [False for j in range(self.columns * 2 + 1)]

        self.maze.append(temp)
        self.visited.append(falseRow)
        self.position_searched.append(falseRow)
        for i in range(1, self.rows + 1):
            temp = ['-' for l in range(self.columns * 2 + 1)]
            self.maze.append([])
            self.position_searched.append([])
            self.maze[2 * i - 1].append("|")
            self.maze[2 * i - 1].append(" ")
            self.maze[2 * i - 1].append("|")

            for j in range(1, self.columns - 1):
                if i == 1 or i == self.rows:
                    self.maze[2 * i - 1].append(" ")

                else:
                    self.maze[2 * i - 1].append(" ")

                self.maze[2 * i - 1].append('|')

            self.maze[2 * i - 1].append(" ")
            self.maze[2 * i - 1].append("|")
            self.visited.append(falseRow)
            self.position_searched.append(falseRow)
            self.maze.append(temp)

        # allow for entrance and exit into the self.maze by changing
        # 2 locations on the border to 0
        # NOTE:
        #   it cannot be the corners because our self.maze has only
        #   valid paths of right, left, up, or down, not
        #   diagonal
        self.maze[1][0] = " "
        self.maze[1][1] = " "
        self.maze[2 * self.rows - 1][2 * self.columns - 1] = " "
        self.maze[2 * self.rows - 1][2 * self.columns] = " "
        

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

                    # self.print_maze()
                    # print()
                stack_positions_visited.pop()[2]

            # print("BEFORE UPDATE")
            # self.print_maze()
            if not cycled:
                self.update_path(lastMovement, position)
            lastMovement = directions[randomDirection]

            stack_positions_visited.append([position[0], position[1], lastMovement])

            self.maze[position[0]][position[1]] = ' '
            self.visited[position[0]][position[1]] = True
            # print("AFTER UPDATE")
            # self.print_maze()
            # print()
            # for i in range(len(self.visited[0])):
            #     print(self.visited[i])
            # print(stack_positions_visited)
            # print()
        self.print_maze()
        self.fill_remaining_maze(stack_positions_visited)

    def randomly_generate_weights(self, random_edge_weights):
        '''
        I want to randomly generate the weights between each vertex so I can make a minimum spanning tree
        connecting all vertices

        First I need to randomly assign the weights between the tangent vertices
        I will use a 2D list for this
        '''


        for row in range(1, self.rows*2, 2):
            for col in range(1, self.columns * 2, 2):
                random_edge_weights.update({(row, col): dict()})

        ''' 
        random_edge_weights would look like this
        {
        
            (A, B) : {
                        (A+1, B) : weight1, 
                        (A-1, B) : weight2,
                        ...
                     },
            (A+1, B) : {
                           (A, B) : weight1, 
                        ...
                       },
            ...
             
        }
        '''
        # for all in random_edge_weights:
        #     print(all)
        for key in random_edge_weights:
            list_connections = []
            if key[0] == 1:

                if key[1] == 1:
                    # we are at top left
                    list_connections.append((key[0] + 2, key[1]))
                    list_connections.append((key[0], key[1] + 2))

                elif key[1] == 2*self.columns - 1:
                    # we are at top right
                    list_connections.append((key[0] + 2, key[1]))
                    list_connections.append((key[0], key[1] - 2))

                else: # position(0] == 1:
                    # we are at the top level but not on corners
                    list_connections.append((key[0] + 2, key[1]))
                    list_connections.append((key[0], key[1] + 2))
                    list_connections.append((key[0], key[1] - 2))



            elif key[0] == 2*self.rows-1:
                if key[1] == 1:
                    # we are at bottom left
                    list_connections.append((key[0] - 2, key[1]))
                    list_connections.append((key[0], key[1] + 2))


                elif key[1] == 2*self.columns - 1:
                    # we are at bottom right,
                    list_connections.append((key[0] - 2, key[1]))
                    list_connections.append((key[0], key[1] - 2))

                else:
                    # we are at the bottom level, so we can't go down
                    list_connections.append((key[0] - 2, key[1]))
                    list_connections.append((key[0], key[1] + 2))
                    list_connections.append((key[0], key[1] - 2))


            elif key[1] == 1:
                # we are on the far left column, so we can't go left
                list_connections.append((key[0] - 2, key[1]))
                list_connections.append((key[0], key[1] + 2))
                list_connections.append((key[0] + 2, key[1]))


            elif key[1] == 2*self.columns-1:
                # we are on the far right column, so we can't go right
                list_connections.append((key[0] - 2, key[1]))
                list_connections.append((key[0], key[1] - 2))
                list_connections.append((key[0] + 2, key[1]))


            else:
                # we can go up, down, left, and right
                list_connections.append((key[0] - 2, key[1]))
                list_connections.append((key[0], key[1] - 2))
                list_connections.append((key[0] + 2, key[1]))
                list_connections.append((key[0], key[1] + 2))

            # now we want to append these connections to our current vertex and assign random weights
            # to each connection
            if random_edge_weights.get((key[0], key[1])) is None:
                random_edge_weights.update({(key[0], key[1]): dict()})
            # print(list_connections)
            for vertex in list_connections:

                if random_edge_weights.get((key[0], key[1])).get(vertex) is None:
                    random_weight = random.random()
                    random_edge_weights.get((key[0], key[1])).update({vertex: random_weight})
                    random_edge_weights.get(vertex).update({(key[0], key[1]): random_weight})

    def update_path(self, lastMovement, position):

        if lastMovement == 'up':
            self.maze[position[0] + 1][position[1]] = ' '
        elif lastMovement == 'down':
            self.maze[position[0] - 1][position[1]] = ' '
        elif lastMovement == 'right':
            self.maze[position[0]][position[1] - 1] = ' '
        else: # lastMovement == 'left':
            self.maze[position[0]][position[1] + 1] = ' '

    def prims_maze(self):

        '''
        prim's algorithm will pick a vertex with which the connections will begin
        from that point, it will add the vertex with the smallest weight between the two vertices

        because we want to reduce the random biases, we will randomly generate the starting vertex
        '''

        # each of our valid vertices has odd x and y values, so we will add one after the position is
        # randomly generated
        min_heap = []

        starting_point = (random.randint(0, self.rows-1) * 2 + 1, random.randint(0, self.columns-1) * 2 + 1)
        visited = set([starting_point])
        # we need a min heap to keep track of which vertices will be added
        # the objects in the min heap will be in the order of weight, from_vertex, to_vertex
        for connection in self.random_edge_weights.get(starting_point):
            heapq.heappush(min_heap, (self.random_edge_weights.get(starting_point)[connection], starting_point,
                                      connection))
        

        while len(visited) < self.rows*self.columns:
            next_connection = heapq.heappop(min_heap)
            if next_connection[2] not in visited:
                visited.add(next_connection[2])
                # need to remove the bar that is between the connections
                self.remove_wall(next_connection[1], next_connection[2])
                for connection in self.random_edge_weights.get(next_connection[2]):
                    if connection not in visited:
                        heapq.heappush(min_heap, (self.random_edge_weights.get(next_connection[2])[connection],
                                                   next_connection[2], connection))


    def kruskalls_maze(self):
        min_heap = []

        pair_added_to_heap = set([])
        # we need a min heap to keep track of which vertices will be added
        # the objects in the min heap will be in the order of weight, from_vertex, to_vertex
        for point in self.random_edge_weights:
            for connection in self.random_edge_weights.get(point):
                if (point, connection) not in pair_added_to_heap and (connection, point) not in pair_added_to_heap:
                    heapq.heappush(min_heap, (self.random_edge_weights.get(point)[connection], point, connection))
                    pair_added_to_heap.add((point, connection))
        

        uf = union_find(self.rows * self.columns)
        # added_to_tree = set([])
        
        while (uf.get_num_components() > 1):
            next_connection = heapq.heappop(min_heap)
            #since we kept a 1D array for the parents of our union_find object, we have to send
            # over the calculated index, which is just 
            # (the number of columns) * (the vertex's row // 2) + (the vertex's column // 2)

            if not uf.are_in_same_component(self.columns * (next_connection[1][0] // 2) + (next_connection[1][1] // 2), 
                                            self.columns * (next_connection[2][0] // 2) + (next_connection[2][1] // 2)):
                
                self.remove_wall(next_connection[1], next_connection[2])
                uf.union(self.columns * (next_connection[1][0] // 2) + next_connection[1][1] // 2, 
                         self.columns * (next_connection[2][0] // 2) + next_connection[2][1] // 2)
        

    def remove_wall(self, from_vertex, to_vertex):
        '''
        this method will simply remove the "wall" between the two points
        if the x of the to_vertex is greater than the x value of from_vertex
            then we will move the "wall" below the from_vertex
        if the x of the to_vertex is less than the x value of from_vertex
            then we will move the "wall" above the from_vertex
        if the y of the to_vertex is greater than the y value of from_vertex
            then we will move the "wall" to the right of the from_vertex
        if the y of the to_vertex is less than the y value of from_vertex
            then we will move the "wall" to the left of the from_vertex

        :param from_vertex: one vertex ono the connection
        :param to_vertex: the other vertex on the connection
        '''

        if to_vertex[0] > from_vertex[0]:
            self.maze[from_vertex[0] + 1][from_vertex[1]] = ' '
        elif to_vertex[0] < from_vertex[0]:
            self.maze[from_vertex[0] - 1][from_vertex[1]] = ' '
        elif to_vertex[1] > from_vertex[1]:
            self.maze[from_vertex[0]][from_vertex[1] + 1] = ' '
        else:
            self.maze[from_vertex[0]][from_vertex[1] - 1] = ' '

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

    def print_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                print(f'{str(self.maze[i][j]):2s}', end='')
            print()

    def solve_dfs(self, position):
        # will recursively search through the maze until the valid path solves
        # or we reach a dead end
        self.position_searched[position[0]][position[1]] = True
        if position[0] == len(self.maze)-2 and position[1] == len(self.maze[0])-2:
            self.maze[position[0]][position[1]] = 'D'
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

    def solve_dfs1(self):
        self.position_searched = self.visited_init()
        start = (1, 1)
        self.solve_dfs(start)

    def solve_bfs(self):

        queue = deque()
        visited = self.visited_init()


        queue.append([(1, 1)])
        while len(queue) != 0:
            # print()
            # for i in range(len(visited)):
            #     print(visited[i])
            # print()
            position = queue.popleft()
            visited[position[-1][0]][position[-1][1]] = True
            last_vertex = position[-1]
            # self.maze[last_vertex[0]][last_vertex[1]] = 'B'

            if last_vertex == (self.rows * 2 - 1, self.columns * 2 - 1):
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
        # print(len(self.maze))
        if (position[0] > 0 and position[0] < len(self.maze) and position[1] > 0 and position[1] < len(self.maze[0])):
            # print(position)
            if not visited[position[0]][position[1]]:
                return True
        return False

    def visited_init(self):
        visited = []
        for i in range(2 * self.rows + 1):
            visited.append([])
            for j in range(2 * self.columns + 1):
                visited[i].append(False)
        return visited

# Debug Statements
# maze1 = CreateMaze(13, 15)
# maze1.build_walls()
# maze1.print_maze()
# maze1.prims_maze()
# maze1.kruskalls_maze()
# maze1.print_maze()
# maze1.solve_dfs1()
# maze1.print_maze()
# maze1.solve_bfs()
# maze1.print_maze()

def main():
    print("How big would you like the maze to be?")
    rows = int(input("Number of Rows: "))
    columns = int(input("Number of Columns: "))
    print("How would you like this maze to be generated?")
    print("Type 1 for prim's. Type 2 for Kruskall's. Type 3 for badgorithm. ")
    generate = int(input("Your choice: "))
    print("And how would you like to solve this maze? (Type 1 for BFS and 2 for DFS)")
    solve = input("Your choice: ")
    maze = CreateMaze(rows, columns)
    maze.build_walls()
    if (generate == 1):
        maze.prims_maze()
    elif generate == 2:
        maze.kruskalls_maze()
    else:
        maze.creation()
    maze.print_maze()

    if solve == 1:
        maze.solve_bfs()
    else:
        maze.solve_dfs1()
    maze.print_maze()

main()