import pygame as py
py.init()
py.font.init()
py.display.set_caption("Path Finder")

## Global Variables ##
BLOCKSIZE = 20

# Block Colors
WHITE = (255,255,255)
BLUE = (75,190,250)
TEAL = (0,130,130)
GREY = (70,70,70)
BLACK = (40,40,40)
TURQUOISE = (50,190,190)
RED = (200,0,0)
GREEN = (0,150,0)
YELLOW = (250,250,0)
ORANGE = (220,120,0)
LIGHT = (170,170,170)

# Screen size
sWIDTH, sHEIGHT = 1100, 900
SCREEN = py.display.set_mode((sWIDTH, sHEIGHT))

# UI Screen
uiHeight = 140
updateUI = py.Rect(0, 0, sWIDTH, uiHeight)
# Graph Screen
updateScreen = py.Rect(0, uiHeight, sWIDTH, sHEIGHT)

# Fonts
font = py.font.SysFont('corbel', 30, bold=True, italic=False)
fntBFS = font.render('Breadth First Search', True, WHITE)
fntDFS = font.render('Depth First Search', True, WHITE)
fntAStar = font.render('A*', True, WHITE)
fntDijkstra = font.render('Dijkstra', True, WHITE)
fntChangeP = font.render('Change Start & End', True, WHITE)
fntRestart = font.render('Restart', True, WHITE)
fntDone = font.render('Done', True, WHITE)
fntWalls = font.render('Walls', True, WHITE)
fntWeights = font.render('Weights', True, WHITE)

# Greyed out font
def dark(name: str): return font.render(name, True, LIGHT)

# Buttons
def btnBFS(color): return py.draw.rect(SCREEN, color, [60, 12, 300, 50])
def btnDFS(color): return py.draw.rect(SCREEN, color, [60, 77, 300, 50])
def btnAStar(color): return py.draw.rect(SCREEN, color, [400, 12, 140, 50])
def btnDijkstra(color): return py.draw.rect(SCREEN, color, [400, 77, 140, 50])
def btnChangeP(color): return py.draw.rect(SCREEN, color, [580, 12, 300, 50])
def btnRestart(color): return py.draw.rect(SCREEN, color, [920, 12, 130, 50])
def btnDone(color): return py.draw.rect(SCREEN, color, [920, 77, 130, 50])
def btnWalls(color): return py.draw.rect(SCREEN, color, [580, 77, 130, 50])
def btnWeights(color): return py.draw.rect(SCREEN, color, [750, 77, 130, 50])

# Button Text
def txtBFS(font): SCREEN.blit(font, (80, 22))
def txtDFS(font): SCREEN.blit(font, (90, 87))
def txtAStar(font): SCREEN.blit(font, (455, 22))
def txtDijkstra(font): SCREEN.blit(font, (420, 87))
def txtChangeP(font): SCREEN.blit(font, (605, 22))
def txtRestart(font): SCREEN.blit(font, (940, 22))
def txtDone(font): SCREEN.blit(font, (950, 87))
def txtWalls(font): SCREEN.blit(font, (610, 87))
def txtWeights(font): SCREEN.blit(font, (760, 87))

def greyOutButtons(exception: str):
    if exception == 'BFS': txtBFS(fntBFS)
    else: btnBFS(GREY); txtBFS(dark('Breadth First Search'))

    if exception == 'DFS': txtDFS(fntDFS)
    else: btnDFS(GREY); txtDFS(dark('Depth First Search'))

    if exception == 'AStar': txtAStar(fntAStar)
    else: btnAStar(GREY); txtAStar(dark('A*'))

    if exception == 'Dijkstra': txtDijkstra(fntDijkstra)
    else: btnDijkstra(GREY); txtDijkstra(dark('Dijkstra'))
    
    if exception == 'ChangeP': txtChangeP(fntChangeP)
    else: btnChangeP(GREY); txtChangeP(dark('Change Start & End'))

    btnWalls(GREY)
    btnWeights(GREY)
    btnRestart(GREY)
    txtWalls(dark('Walls'))
    txtWeights(dark('Weights'))
    txtRestart(dark('Restart'))
    py.display.update(updateUI)