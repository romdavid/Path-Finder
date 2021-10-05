from collections import deque
from pygame.locals import*
from math import sqrt
from graph import*
import sys, heapq

class PriorityQ():
    def __init__(self):
        self.nodes = []
    
    def __str__(self):
        return "Priorityq: " + str(list(self.nodes))

    def put(self, cost, node):
        heapq.heappush(self.nodes, (cost, node))

    def get(self):
        return heapq.heappop(self.nodes)[1]

    def isEmpty(self):
        return len(self.nodes) == 0

def heuristic(node1, node2):
    # Pythagorean Threorem
    a = node1.X - node2.X
    b = node1.Y - node2.Y
    return sqrt(a*a + b*b)//BLOCKSIZE

def escapeCheck():
    for event in py.event.get():
        if event.type == QUIT:
            print("Quiting...")
            py.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                return reset(True)

def reset(animating: bool):
    while(True):
        mouse = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == QUIT:
                print("Quiting...") 
                py.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE and animating:
                    btnRestart(GREY)
                    txtRestart(dark('Restart'))
                    py.display.update(updateUI)
                    return False
                elif event.key == K_ESCAPE:
                    return True
            # Reset if pressed
            elif event.type == MOUSEBUTTONDOWN:
                if btnRestart(GREY).collidepoint(mouse):
                    return True
        if btnRestart(ORANGE).collidepoint(mouse):
            btnRestart(LIGHT)
        txtRestart(fntRestart)
        py.display.update(updateUI)

def drawPath(g:Graph, root: Point, target: Point, path: dict):
    if target in path:
        py.draw.rect(SCREEN, YELLOW, (target, (BLOCKSIZE-1, BLOCKSIZE-1)))
        currentNode = target + path[target]
        while (currentNode != root):
            py.draw.rect(SCREEN, GREEN, (currentNode, (BLOCKSIZE-1, BLOCKSIZE-1)))
            if currentNode in g.weights:
                py.draw.rect(SCREEN, g.weightColors[g.weights[currentNode]], (currentNode+Point(5,5), (BLOCKSIZE-11, BLOCKSIZE-11)))
            py.time.delay(50)
            py.display.update(updateScreen)
            currentNode += path[currentNode]

def BFS(g: Graph, root: Point, target: Point):
    greyOutButtons('BFS')
    newNodes = deque()
    newNodes.appendleft(root)
    path = {}
    path[root] = None
    py.draw.rect(SCREEN, RED, (root, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.draw.rect(SCREEN, YELLOW, (target, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.display.update(updateScreen)
    while (len(newNodes) > 0 and target not in path):
        if escapeCheck(): return
        node = newNodes.pop()
        if node != root:
            py.draw.rect(SCREEN, BLUE, (node, (BLOCKSIZE-1, BLOCKSIZE-1)))
            py.time.delay(20)
            py.display.update(updateScreen)
        for adj in g.find_Adj(node):
            if adj not in path:
                newNodes.appendleft(adj)
                path[adj] = node - adj
                py.draw.rect(SCREEN, TURQUOISE, (adj, (BLOCKSIZE-1, BLOCKSIZE-1)))
                py.time.delay(20)
                py.display.update(updateScreen)
    drawPath(g, root, target, path)
    reset(False)

def DFS(g: Graph, root: Point, target: Point):
    greyOutButtons('DFS')
    newNodes = []
    newNodes.append(root)
    path = {}
    path[root] = None
    py.draw.rect(SCREEN, RED, (root, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.draw.rect(SCREEN, YELLOW, (target, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.display.update(updateScreen)
    while (len(newNodes) > 0 and target not in path):
        if escapeCheck(): return
        node = newNodes.pop()
        if node != root:
            py.draw.rect(SCREEN, BLUE, (node, (BLOCKSIZE-1, BLOCKSIZE-1)))
            py.time.delay(20)
            py.display.update(updateScreen)
        for adj in g.find_Adj(node):
            if adj not in path:
                newNodes.append(adj)
                path[adj] = node - adj
                py.draw.rect(SCREEN, TURQUOISE, (adj, (BLOCKSIZE-1, BLOCKSIZE-1)))
                py.time.delay(20)
                py.display.update(updateScreen)
    drawPath(g, root, target, path)
    reset(False)

def dijkstra (g: Graph, root: Point, target: Point):
    greyOutButtons('Dijkstra')    
    newNodes = PriorityQ()
    newNodes.put(0, root)
    path = {}
    path[root] = None
    cost = {}
    cost[root] = 0
    py.draw.rect(SCREEN, RED, (root, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.draw.rect(SCREEN, YELLOW, (target, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.display.update(updateScreen)
    while not newNodes.isEmpty():
        if escapeCheck(): return
        node = newNodes.get()
        if node != root:
            py.draw.rect(SCREEN, BLUE, (node, (BLOCKSIZE-1, BLOCKSIZE-1)))
            if node in g.weights:
                py.draw.rect(SCREEN, g.weightColors[g.weights[node]], (node.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
            elif node == target:
                py.draw.rect(SCREEN, YELLOW, (node.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
            py.time.delay(20)
            py.display.update(updateScreen)
        if node == target:
            break
        for adj in g.find_Adj(node):
            adjCost = cost[node] + g.cost(adj)
            if adj not in cost or adjCost < cost[adj]:
                cost[adj] = adjCost
                newNodes.put(adjCost, adj)
                path[adj] = node - adj
                py.draw.rect(SCREEN, TURQUOISE, (adj, (BLOCKSIZE-1, BLOCKSIZE-1)))
                if adj in g.weights:
                    py.draw.rect(SCREEN, g.weightColors[g.weights[adj]], (adj.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
                elif adj == target:
                    py.draw.rect(SCREEN, YELLOW, (adj.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
                py.time.delay(20)
                py.display.update(updateScreen)
    drawPath(g, root, target, path)
    reset(False)

def aStar (g: Graph, root: Point, target: Point):
    greyOutButtons('AStar')
    newNodes = PriorityQ()
    newNodes.put(0, root)
    path = {}
    path[root] = None
    cost = {}
    cost[root] = 0
    py.draw.rect(SCREEN, RED, (root, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.draw.rect(SCREEN, YELLOW, (target, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.display.update(updateScreen)
    while not newNodes.isEmpty():
        if escapeCheck(): return
        node = newNodes.get()
        if node != root:
            py.draw.rect(SCREEN, BLUE, (node, (BLOCKSIZE-1, BLOCKSIZE-1)))
            if node in g.weights:
                py.draw.rect(SCREEN, g.weightColors[g.weights[node]], (node.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
            elif node == target:
                py.draw.rect(SCREEN, YELLOW, (node.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
            py.time.delay(20)
            py.display.update(updateScreen)
        if node == target:
            break
        for adj in g.find_Adj(node):
            adjCost = cost[node] + g.cost(adj)
            if adj not in cost or adjCost < cost[adj]:
                cost[adj] = adjCost
                newNodes.put(adjCost + heuristic(adj, target), adj)
                path[adj] = node - adj
                py.draw.rect(SCREEN, TURQUOISE, (adj, (BLOCKSIZE-1, BLOCKSIZE-1)))
                if adj in g.weights:
                    py.draw.rect(SCREEN, g.weightColors[g.weights[adj]], (adj.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
                elif adj == target:
                    py.draw.rect(SCREEN, YELLOW, (adj.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
                py.time.delay(20)
                py.display.update(updateScreen)
    drawPath(g, root, target, path)
    reset(False)