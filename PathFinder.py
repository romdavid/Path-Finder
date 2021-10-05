from algo import BFS, DFS, dijkstra, aStar
from pygame.locals import*
from graph import*
import sys

def drawGrid():
    # Vertical Lines
    for x in range(BLOCKSIZE, sWIDTH, BLOCKSIZE):
        py.draw.line(SCREEN, TEAL, (x, uiHeight), (x, sHEIGHT-BLOCKSIZE), 1)
    # Horizontal Lines
    for y in range(uiHeight, sHEIGHT, BLOCKSIZE):
        py.draw.line(SCREEN, TEAL, (BLOCKSIZE, y), (sWIDTH-BLOCKSIZE, y), 1)
    py.display.update(updateScreen)

def startEnd(g: Graph, start: Point, end: Point):
    greyOutButtons('ChangeP')
    color = GREY
    point = start
    selected = False
    cont = True
    # Loop until done button is pressed
    while(cont):
        mouse = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == QUIT: 
                print("Quiting...")
                py.quit()
                sys.exit()
            # Go back when esc is pressed
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    cont = False
                    break
            elif event.type == py.MOUSEBUTTONDOWN:
                if py.mouse.get_pressed()[0] and mouse[1] > uiHeight and mouse[1] < sHEIGHT-BLOCKSIZE and mouse[0] > BLOCKSIZE and mouse[0] < sWIDTH-BLOCKSIZE:
                    pos = ((Point(mouse[0], mouse[1])//BLOCKSIZE)*BLOCKSIZE).inc()
                    if pos not in g.walls and pos not in g.weights:
                        # Update new start or end
                        if selected and pos != start and pos != end: 
                            py.draw.rect(SCREEN, BLACK, (point, (BLOCKSIZE-1, BLOCKSIZE-1)))
                            if point == start: start = pos
                            else: end = pos
                            point = pos
                            py.draw.rect(SCREEN, color, (point, (BLOCKSIZE-1, BLOCKSIZE-1)))
                            selected = False
                            py.display.update(updateScreen)
                            break
                        elif pos == start or pos == end:
                            if pos == start: 
                                point = start
                                color = RED
                                py.draw.rect(SCREEN, YELLOW, (end, (BLOCKSIZE-1, BLOCKSIZE-1)))
                            else: 
                                point = end; 
                                color = YELLOW
                                py.draw.rect(SCREEN, RED, (start, (BLOCKSIZE-1, BLOCKSIZE-1)))
                            py.draw.rect(SCREEN, ORANGE, (point, (BLOCKSIZE-1, BLOCKSIZE-1)))
                            py.draw.rect(SCREEN, color, (point.shrink(), (BLOCKSIZE-7, BLOCKSIZE-7)))
                            selected = True
                            py.display.update(updateScreen)
                            break
                elif btnDone(GREY).collidepoint(mouse):
                    cont = False
                    break
        if btnDone(ORANGE).collidepoint(mouse):
            btnDone(LIGHT)
        else: 
            btnDone(ORANGE)
        txtDone(fntDone)
        py.display.update(updateUI)

    # After loop remove selected point
    if selected:
        py.draw.rect(SCREEN, color, (point, (BLOCKSIZE-1, BLOCKSIZE-1)))
        py.display.update(updateScreen)
    btnDone(GREY)
    txtDone(dark('Done'))
    return (start, end)

def mainLoop(g: Graph):
    start = Point(340, 500).inc()
    py.draw.rect(SCREEN, RED, (start, (BLOCKSIZE-1, BLOCKSIZE-1)))
    end = Point(740, 500).inc()
    py.draw.rect(SCREEN, YELLOW, (end, (BLOCKSIZE-1, BLOCKSIZE-1)))
    py.display.update(updateScreen)
    while 1:
        mouse = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    if len(g.walls) > 0 or len(g.weights) > 0 or start != Point(341, 501) or end != Point(741, 501):
                        return main()

            elif event.type == MOUSEBUTTONDOWN:
                g.mouseButtonDown = True
                if btnChangeP(GREY).collidepoint(mouse):
                    newPoints = startEnd(g, start, end)
                    start, end = newPoints[0], newPoints[1]
                elif btnBFS(GREY).collidepoint(mouse):
                    BFS(g, start, end)
                    return main()
                elif btnDFS(GREY).collidepoint(mouse):
                    DFS(g, start, end)
                    return main()
                elif btnDijkstra(GREY).collidepoint(mouse):
                    dijkstra(g, start, end)
                    return main()
                elif btnAStar(GREY).collidepoint(mouse):
                    aStar(g, start, end)
                    return main()
                elif btnWalls(GREY).collidepoint(mouse):
                    g.wallMode = True
                elif btnWeights(GREY).collidepoint(mouse):
                    g.wallMode = False
                elif btnRestart(GREY).collidepoint(mouse):
                    if len(g.walls) > 0 or len(g.weights) > 0 or start != Point(341, 501) or end != Point(741, 501):
                        return main()

        # Display Buttons
        if btnBFS(ORANGE).collidepoint(mouse):
            btnBFS(LIGHT)
        if btnDFS(ORANGE).collidepoint(mouse):
            btnDFS(LIGHT)
        if btnAStar(ORANGE).collidepoint(mouse):
            btnAStar(LIGHT)
        if btnDijkstra(ORANGE).collidepoint(mouse):
            btnDijkstra(LIGHT)
        if btnChangeP(ORANGE).collidepoint(mouse):
            btnChangeP(LIGHT)
        if btnRestart(ORANGE).collidepoint(mouse):
            btnRestart(LIGHT)
        if g.wallMode == True:
            btnWalls(GREEN)
            btnWeights(GREY)
        else:
            btnWeights(GREEN)
            btnWalls(GREY)

        # Display Button Text
        txtBFS(fntBFS)
        txtDFS(fntDFS)
        txtAStar(fntAStar)
        txtDijkstra(fntDijkstra)
        txtChangeP(fntChangeP)
        txtRestart(fntRestart)
        txtWalls(fntWalls)
        txtWeights(fntWeights)
        py.display.update(updateUI)
        
        # Draw or erase selected walls/weights
        g.draw_Wall(start, end)
        g.mouseButtonDown = False

def main():
    SCREEN.fill(BLACK)
    btnDone(GREY)
    txtDone(dark('Done'))
    drawGrid()
    mainLoop(Graph())

    # Exit Game
    print("Quiting...")
    py.quit()
    sys.exit()

if __name__ == '__main__':
    main()