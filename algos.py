import pygame
from maze import *
import random
import time

def DFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement DFS algorithm')
    open_set = [g.start.id] # stack
    closed_set = []
    father = [g.goal.id]*g.get_length()
    print(g.start.id)
    while True:
        # if there is no node in open_set to get (no path to the goal) -> wait 1.5 second then quit
        if len(open_set) == 0:
            print("# There is no path to the goal!")
            print("# Cost of result: 0")
            pygame.time.delay(1500)
            exit()
        # (else) get current node in open_set
        curID = open_set.pop() # pop from the end of list (stack)
        curNode = g.grid_cells[curID]
        # check current node is the goal (Loop condition)
        if g.is_goal(curNode):
            curNode.set_color(PURPLE, sc)
            break
        # set color for current node and find neighbors
        curNode.set_color(YELLOW, sc)
        nbs = g.get_neighbors(curNode)
        # open each neighbor and set RED for them
        for nb in nbs:
            if (nb.id not in closed_set) and (nb.id not in open_set):
                nb.set_color(RED, sc)
                open_set.append(nb.id)
                father[nb.id] = curID
        # then close current node and set BLUE for it
        closed_set.append(curNode.id)
        curNode.set_color(BLUE, sc) if curNode != g.start else curNode.set_color(ORANGE, sc)

    drawPath(father, g, sc)


def BFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement BFS algorithm')
    open_set = [g.start.id] # queue
    closed_set = []
    father = [g.goal.id]*g.get_length()

    while True:
        # if there is no node in open_set to get (no path to the goal) -> wait 1.5 second then quit
        if len(open_set) == 0:
            print("# There is no path to the goal!")
            print("# Cost of result: 0")
            pygame.time.delay(1500)
            exit()
        # (else) get current node in open_set
        curID = open_set.pop(0) # pop from the begin of list (queue)
        curNode = g.grid_cells[curID]
        # check current node is the goal (Loop condition)
        if g.is_goal(curNode):
            curNode.set_color(PURPLE, sc)
            break
        # set color for current node and find neighbors
        curNode.set_color(YELLOW, sc)
        nbs = g.get_neighbors(curNode)
        # open each neighbor and set RED for them
        for nb in nbs:
            if (nb.id not in closed_set) and (nb.id not in open_set):
                nb.set_color(RED, sc)
                open_set.append(nb.id)
                father[nb.id] = curID
        # then close current node and set BLUE for it
        curNode.set_color(BLUE, sc) if curNode != g.start else curNode.set_color(ORANGE, sc)
        closed_set.append(curNode.id)
    # Draw path 
    drawPath(father, g, sc)

        
def UCS(g: SearchSpace, sc: pygame.Surface):
    print('Implement UCS algorithm')
    # +1 respect if you can implement UCS with a priority queue

    open_set = [(0, g.start.id)] # g_cost, id
    closed_set = []
    father = [-1]*g.get_length()
    cost = [100_000]*g.get_length() # g_cost
    cost[g.start.id] = 0
    
    while True:
        # if there is no node in open_set to get (no path to the goal) -> wait 1.5 second then quit
        if len(open_set) == 0:
            print("# There is no path to the goal!")
            print("# Cost of result: 0")
            pygame.time.delay(1500)
            exit()
        # (else) get current node in open_set
        curID = open_set.pop(0) # pop the lowest g_cost
        curNode = g.grid_cells[curID[1]]
        # check current node is the goal (Loop condition)
        if g.is_goal(curNode):
            curNode.set_color(PURPLE, sc)
            break
        # set color for current node and find neighbors
        curNode.set_color(YELLOW, sc)
        nbs = g.get_neighbors(curNode)
        # open each neighbor and set RED for them
        for nb in nbs:
            # skip if neighbor id in closed_set
            if (nb.id in closed_set):
                continue
            # set g_cost for neighbor
            g_cost = cost[curID[1]] + getDistance(curNode, nb) 
            # if new path to neighbor is shorter than previous path 
            if g_cost < cost[nb.id]:
                cost[nb.id] = g_cost # update new g_cost path
                father[nb.id] = curID[1] # update father too
                # update g_cost in open_set too
                repl_update = (g_cost, nb.id)
                open_set = [repl_update if e[1] == repl_update[1] else e for e in open_set]
                # if neighbor is not opened, open it
                if (nb.id not in [k[1] for k in open_set]):
                    nb.set_color(RED, sc)
                    open_set.append((g_cost, nb.id))
            else:
                continue # neighbor is already in the open_set with the best g_cost
        # open_set sort by g_cost
        open_set = sorted(open_set, key=lambda x: (x[0]))                           
        # then close current node and set BLUE for it
        closed_set.append(curNode.id)
        curNode.set_color(BLUE, sc) if curNode != g.start else curNode.set_color(ORANGE, sc)   
    # Draw path 
    drawPath(father, g, sc)


def AStar(g: SearchSpace, sc: pygame.Surface):
    print('Implement AStar algorithm')
    # +1 respect if you can implement AStar with a priority queue

    open_set = [(0, 0, g.start.id)] # (f_cost, h_cost, id) sort by f_cost then h_cost
    closed_set = []
    father = [g.goal.id]*g.get_length()
    cost = [100_000]*g.get_length() # g_cost
    cost[g.start.id] = 0

    while True:
        # if there is no node in open_set to get (no path to the goal) -> wait 1.5 second then quit
        if len(open_set) == 0:
            print("# There is no path to the goal!")
            print("# Cost of result: 0")
            pygame.time.delay(1500)
            exit()
        # (else) get current node in open_set
        curID = open_set.pop(0) # pop the lowest f_cost (, then h_cost) 
        curNode = g.grid_cells[curID[2]]
        # check current node is the goal (Loop condition)
        if g.is_goal(curNode):
            curNode.set_color(PURPLE, sc)
            break
        # set color for current node and find neighbors
        curNode.set_color(YELLOW, sc)
        nbs = g.get_neighbors(curNode)
        # open each neighbor and set RED for them
        for nb in nbs:
            # skip if neighbor id in closed_set
            if (nb.id in closed_set):
                continue
            # set f_cost, h_cost, g_cost for neighbor
            g_cost = cost[curID[2]] + getDistance(curNode, nb) 
            h_cost = getDistance(g.goal, nb)
            f_cost = g_cost + h_cost
            # if new path to neighbor is shorter than previous path (all first define cost is 100_000)
            if g_cost < cost[nb.id]:
                cost[nb.id] = g_cost # update new g_cost path
                father[nb.id] = curID[2] # update father too
                # update f_cost and h_cost in open_set too 
                repl_update = (f_cost, h_cost, nb.id)
                open_set = [repl_update if e[2] == repl_update[2] else e for e in open_set]
                # if neighbor is not opened, open it
                if (nb.id not in [k[2] for k in open_set]):
                    nb.set_color(RED, sc)
                    open_set.append((f_cost, h_cost, nb.id))
            else:
                continue # neighbor is already in the open_set with the best g_cost
        # open_set sort by f_cost then h_cost 
        open_set = sorted(open_set, key=lambda x: (x[0], x[1]))                         
        # then close current node and set BLUE for it
        closed_set.append(curNode.id)
        curNode.set_color(BLUE, sc) if curNode != g.start else curNode.set_color(ORANGE, sc)       
    # Draw path 
    drawPath(father, g, sc)


def Greedy(g: SearchSpace, sc: pygame.Surface):
    print('Implement Greedy algorithm')

    open_set = [(0, g.start.id)] # (h_cost, id) 
    closed_set = []
    father = [-1]*g.get_length()
    cost = [-1]*g.get_length() # h_cost
    # set h_cost for all node
    for i in range(g.get_length()):
        cost[i] = getDistance(g.goal, g.grid_cells[i])
    
    while True:
        # if there is no node in open_set to get (no path to the goal) -> wait 1.5 second then quit
        if len(open_set) == 0:
            print("# There is no path to the goal!")
            print("# Cost of result: 0")
            pygame.time.delay(1500)
            exit()
        # (else) get current node in open_set
        curID = open_set.pop(0) # pop the lowest h_cost
        curNode = g.grid_cells[curID[1]]
        # check current node is the goal (Loop condition)
        if g.is_goal(curNode):
            curNode.set_color(PURPLE, sc)
            break
        # set color for current node and find neighbors
        curNode.set_color(YELLOW, sc)
        nbs = g.get_neighbors(curNode)
        # open each neighbor and set RED for them
        for nb in nbs:
            # skip if neightbor id in closed_set
            if (nb.id in closed_set):
                continue
            # set father of nb
            father[nb.id] = curID[1]
            if (nb.id not in [k[1] for k in open_set]):
                nb.set_color(RED, sc)
                open_set.append((cost[nb.id], nb.id))
        # open_set sort by h_cost 
        open_set = sorted(open_set, key=lambda x: (x[0]))
        # then close current node and set BLUE for it
        closed_set.append(curNode.id)
        curNode.set_color(BLUE, sc) if curNode != g.start else curNode.set_color(ORANGE, sc)   

    # Draw path 
    
    drawPath(father, g, sc)
    

## Helper
# Get distance between two node: heuristic
def getDistance(A, B):
    disX = abs(B.rect.x - A.rect.x)
    disY = abs(B.rect.y - A.rect.y)
    return (disX**2 + disY**2)**0.5

#Draw path according to father list (draw from the goal to the start node)
def drawPath(listFather, g: SearchSpace, sc: pygame.Surface):
    res = []
    cost = 0
    pathNode = g.goal.id
    while True:
        if (pathNode == g.start.id): # loop condition
            break
        #value to align center of the rectangle 26 x 26
        center = A / 2 # that is 13
        #start node
        x_start = g.grid_cells[pathNode].rect.x + center
        y_start = g.grid_cells[pathNode].rect.y + center
        #father of start node
        pathNode = listFather[pathNode]
        #father node (end node)
        x_end = g.grid_cells[pathNode].rect.x + center
        y_end = g.grid_cells[pathNode].rect.y + center

        res.append((x_start, y_start, x_end, y_end))
    
    # draw
    for i in reversed(res):
        if (i[0] == i[2] or i[1] == i[3]):
            cost += 10
        else:
            cost += 14

        pygame.draw.line(sc, WHITE, (i[2], i[3]), (i[0], i[1]), 2)
        pygame.time.delay(10)
        pygame.display.update()

    print(f"# Cost of result: {cost}")


def BFSWithStations(g: SearchSpace, sc: pygame.Surface):
    # Initialize the open set with the start node
    open_set = [g.start.id]
    # Initialize the closed set as empty
    closed_set = []
    # Initialize the father list
    father = [-1]*g.get_length()
    
    collect = 0 # Number of stations collected
    
    while True:    
        if len(open_set) == 0:
            print("\tThere is no path to the goal!")
            pygame.time.delay(1500)
            exit()
        
        # Get the current node from the open set
        curID = open_set.pop(0)
        curNode = g.grid_cells[curID]
        
        # Check if the current node is a station
        if g.is_station(curNode) and not curNode.reached:
            curNode.reached = True
            drawPathForStations(g, sc, father, g.start.id, curNode.id)
            closed_set = []
            father = [-1]*g.get_length()
            father[curNode.id] = curID
            g.start = curNode
            open_set = [curNode.id]
            collect = collect + 1
            continue

        # Check if the current node is the goal
        if g.is_goal(curNode):
            curNode.set_color(PURPLE, sc)
            if (collect < 2):
                continue
            else: # collect == 2
                drawPathForStations(g, sc, father, g.start.id, curNode.id)
                break
        
        # Get the neighbors of the current node
        nbs = g.get_neighbors(curNode)

        # Open each neighbor
        for nb in nbs:
            if (nb.id not in closed_set) and (nb.id not in open_set):
                open_set.append(nb.id)
                father[nb.id] = curID

        # Set color for the current node if it is the station node (reached)
        if g.is_station(curNode):
            curNode.set_color(GREEN, sc)
        closed_set.append(curID)


def drawPathForStations(g: SearchSpace, sc: pygame.Surface, father: list, start_id: int, end_id: int):
    path = []
    cost = 0
    temp = end_id
    while temp != start_id:
        path.append(temp)
        temp = father[temp]
    path.append(start_id)  # add start to the path
    path.reverse()

    for pathNode in path:
        center = g.grid_cells[pathNode].rect.width // 2
        x_start = g.grid_cells[pathNode].rect.x + center
        y_start = g.grid_cells[pathNode].rect.y + center
        if father[pathNode] != -1:
            x_end = g.grid_cells[father[pathNode]].rect.x + center
            y_end = g.grid_cells[father[pathNode]].rect.y + center
            if x_start == x_end or y_start == y_end:
                cost += 10
            else:
                cost += 14
            # draw
            pygame.draw.line(sc, BLACK, (x_start, y_start), (x_end, y_end), 3)
            pygame.display.update()
            pygame.time.delay(30)
    print(f"# Cost of result: {cost}")


def drawPathMoving(listFather, g: SearchSpace, sc: pygame.Surface):
    res = []
    cost = 0
    pathNode = g.goal.id
    while True:
        if (pathNode == g.start.id): # loop condition
            break
        #value to align center of the rectangle 26 x 26
        center = A / 2 # that is 13
        #start node
        x_start = g.grid_cells[pathNode].rect.x + center
        y_start = g.grid_cells[pathNode].rect.y + center
        #father of start node
        pathNode = listFather[pathNode]
        #father node (end node)
        x_end = g.grid_cells[pathNode].rect.x + center
        y_end = g.grid_cells[pathNode].rect.y + center

        res.append((x_start, y_start, x_end, y_end))
    
    # draw
    for i in reversed(res):
        if (i[0] == i[2] or i[1] == i[3]):
            cost += 10
        else:
            cost += 14

        pygame.draw.line(sc, BLUE, (i[2], i[3]), (i[0], i[1]), 2)
        pygame.time.delay(10)
        pygame.display.update()

    print(f"# Cost of result: {cost}")

def AStarMoving(g: SearchSpace, sc: pygame.Surface):
    print('Implement AStar algorithm')
    # +1 respect if you can implement AStar with a priority queue

    open_set = [(0, 0, g.start.id)] # (f_cost, h_cost, id) sort by f_cost then h_cost
    closed_set = []
    father = [g.goal.id]*g.get_length()
    cost = [100_000]*g.get_length() # g_cost
    cost[g.start.id] = 0

    while True:
        # if there is no node in open_set to get (no path to the goal) -> wait 1.5 second then quit
        if len(open_set) == 0:
            print("# There is no path to the goal!")
            print("# Cost of result: 0")
            pygame.time.delay(15)
            return
        # (else) get current node in open_set
        curID = open_set.pop(0) # pop the lowest f_cost (, then h_cost) 
        curNode = g.grid_cells[curID[2]]
        # check current node is the goal (Loop condition)
        if g.is_goal(curNode):
            curNode.set_color(PURPLE, sc)
            break
        # set color for current node and find neighbors
        # curNode.set_color(BLUE, sc)
        nbs = g.get_neighbors(curNode)
        # open each neighbor and set RED for them
        for nb in nbs:
            # skip if neighbor id in closed_set
            if (nb.id in closed_set):
                continue
            # set f_cost, h_cost, g_cost for neighbor
            g_cost = cost[curID[2]] + getDistance(curNode, nb) 
            h_cost = getDistance(g.goal, nb)
            f_cost = g_cost + h_cost
            # if new path to neighbor is shorter than previous path (all first define cost is 100_000)
            if g_cost < cost[nb.id]:
                cost[nb.id] = g_cost # update new g_cost path
                father[nb.id] = curID[2] # update father too
                # update f_cost and h_cost in open_set too 
                repl_update = (f_cost, h_cost, nb.id)
                open_set = [repl_update if e[2] == repl_update[2] else e for e in open_set]
                # if neighbor is not opened, open it
                if (nb.id not in [k[2] for k in open_set]):
                    open_set.append((f_cost, h_cost, nb.id))
            else:
                continue # neighbor is already in the open_set with the best g_cost
        # open_set sort by f_cost then h_cost 
        open_set = sorted(open_set, key=lambda x: (x[0], x[1]))                         
        # then close current node and set BLUE for it
        closed_set.append(curNode.id)
    
    # Draw path 
    drawPathMoving(father, g, sc)


def Moving (myMatrix : Matrix, sc:pygame.surface) : 
    diss = [1,2,3,4]
    for i in range(20) : 
        dis = random.choice(diss)
        if(i%2 ==0) :
            myMatrix.movingPolygon(dis) 
        else :
            myMatrix.movingPolygon(dis*-1)
        g = SearchSpace(myMatrix)
        g.draw(sc)
        pygame.display.update()
        AStarMoving(g, sc)
        time.sleep(0.5)
        sc.fill(pygame.color.Color(GREY))