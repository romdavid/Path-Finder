from public import*

class Point(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(Point, (x, y))

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # Enables the use of '+' to add two points
    def __add__(self, other):
        return Point(self.X + other.X, self.Y + other.Y)
    __radd__ = __add__ 

    def __sub__(self, other):
        return Point(self.X - other.X, self.Y - other.Y)

    def __floordiv__(self, other):
        return Point(self.X // other, self.Y // other)

    def __mul__(self, other):
        return Point(self.X * other, self.Y * other)

    def inc(self):
        return Point(self.X + 1, self.Y + 1)

    def shrink(self):
        return Point(self.X + 3, self.Y + 3)

class Graph ():
    def __init__(self):
        self.walls = set()
        self.weights = {}
        self.adjacent = [Point(BLOCKSIZE,0), Point(0,BLOCKSIZE), Point(-BLOCKSIZE,0), Point(0,-BLOCKSIZE)]
        self.wallMode = True
        self.weightColors = {2:(255,200,210), 4:(250,130,180), 8:(145,70,145), 16:(100,0,200)}
        self.mouseButtonDown = False
        self.prevColor = 0

    def check_Bounds(self, node):
        return (BLOCKSIZE <= node.X < sWIDTH-BLOCKSIZE) and (uiHeight <= node.Y < sHEIGHT-BLOCKSIZE)
    
    def check_Walls(self, node):
        return node not in self.walls

    def find_Adj(self, node):
        neighbors = [node + adj for adj in self.adjacent]
        if (node.X+node.Y)//BLOCKSIZE % 2:
            neighbors.reverse()
        neighbors = filter(self.check_Bounds, neighbors)
        neighbors = filter(self.check_Walls,  neighbors)
        return neighbors

    def draw_Wall(self, start, end):
        pos = py.mouse.get_pos()
        pos = ((Point(pos[0], pos[1])//BLOCKSIZE)*BLOCKSIZE).inc()
        # If MOUSE1 is held down draw a wall or weight
        if py.mouse.get_pressed()[0]:
            if pos not in self.walls and pos[1] > uiHeight and pos[1] < sHEIGHT-BLOCKSIZE and pos[0] > BLOCKSIZE and pos[0] < sWIDTH-BLOCKSIZE and pos != start and pos != end:
                if self.wallMode == True and pos not in self.weights:
                    self.walls.add(pos)
                    py.draw.rect(SCREEN, TEAL, (pos, (BLOCKSIZE-1, BLOCKSIZE-1)))
                    py.display.update(updateScreen)
                elif self.wallMode == False:
                    color = 2
                    if pos in self.weights:
                        color = self.weights[pos]
                        if self.weights[pos] > 8 or (self.mouseButtonDown == False and color != self.prevColor):
                            return
                        self.prevColor = color
                        color *= 2
                    else:
                        self.prevColor = 0
                    self.weights[pos] = color
                    py.draw.rect(SCREEN, self.weightColors[color], (pos, (BLOCKSIZE-1, BLOCKSIZE-1)))
                    py.display.update(updateScreen)
        # If MOUSE2 delete walls
        elif py.mouse.get_pressed()[2]:
            if pos in self.walls:
                py.draw.rect(SCREEN, BLACK, (pos, (BLOCKSIZE-1, BLOCKSIZE-1)))
                self.walls.remove(pos)
                py.display.update(updateScreen)
            elif pos in self.weights:
                py.draw.rect(SCREEN, BLACK, (pos, (BLOCKSIZE-1, BLOCKSIZE-1)))
                self.weights.pop(pos)
                py.display.update(updateScreen)

    def cost(self, adjNode):
        return self.weights.get(adjNode, 1)