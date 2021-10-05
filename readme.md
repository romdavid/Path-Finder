# Path Finder
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Path Finder is an algorithm visualizer for Depth First Search, Breadth First Search, Dijkstra, and A*
(Astar) algorithms.

## Setup
1. Make sure [`python3`](https://www.python.org/) and [`pygame`](https://github.com/pygame/pygame) are installed
2. Clone this repository
3. Run `PathFinder.py`

## Documentation
### Keyboard Shortcuts
* `Esc` is the same as the restart button
* `Space` will pause/play an algorithm's animation

### Start & End
* | Start | End |
  | ----- | --- |
  | <img src="images/red.png"/> | <img src="images/yellow.png"/> |
    - <strong>Note</strong>: After clicking `Change Start & End` select the block (start/end) you 
    want to change, then select where you want to move it. Click `Done` when finished.

### Walls
* Left click to place walls, drag mouse to place them faster. Right click to delete walls. 
    - <img src="images/teal.png"/>

### Weights
* Every block except walls has a weight value. You can increase a weight's value by left clicking on
a weight. Hold left click and drag to increase the value of multiple weights faster. Right click to
delete weights.  

* The weight values increase by a factor of 2.

    | Color | Value |
    | ----- | ----- |
    |<img src="images/1.png"/> | 1  |
    |<img src="images/2.png"/> | 2  |
    |<img src="images/4.png"/> | 4  |
    |<img src="images/8.png"/> | 8  |
    |<img src="images/16.png"/>| 16 |

### Algorithms
* The turquoise block means the node is discovered but not officially visited.
    - <img src="images/turquoise.png"/>

* The blue block means the node has been officially visited.
    - <img src="images/blue.png"/>