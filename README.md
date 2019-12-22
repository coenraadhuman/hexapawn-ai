# Hexapawn-Machine_Learning
Extremely basic illustration of machine learning, something to do on my holiday inspired by [video](https://www.youtube.com/watch?v=sw7UAZNgGg8) a friend showed me from Vsauce2 (Youtube) on [hexapawn](https://en.wikipedia.org/wiki/Hexapawn).

# Codebase
I am quite unfamiliar with Python and any improvements are welcome, was forced to use it due to internet difficulties and using another person's Windows :sob: laptop.
- Python 3.8.1
- [Colorama 0.4.3](https://github.com/tartley/colorama)

# Game Rules
_Board:_
```
['x', 'x', 'x']
[' ', ' ', ' ']
['o', 'o', 'o']
```

_Movement that allowed:_ 
- Pawn can move one up if no pawn is in said position.
- Pawn can move one capture opponent's pawn in forward diagonal position.

_Three ways to win:_
- Get your pawn to oponent's starting side.
- The oponent is left with no valid moves.
- Capture all of the oponent's pawns.

# The Learning
- When player loses, all of their moves (states) are discouraged by reducing their points, thus diciplining the computer. 
- Otherwise encourage good moves (states) by increasing their points.