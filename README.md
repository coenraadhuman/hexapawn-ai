# Hexapawn-Machine_Learning
Extremely basic illustration of machine learning, something to do on my holiday inspired by [video](https://www.youtube.com/watch?v=sw7UAZNgGg8) a friend showed me from Vsauce2 (Youtube) on [hexapawn](https://en.wikipedia.org/wiki/Hexapawn).

## Codebase
I am quite unfamiliar with Python and any improvements are welcome, was forced to use it due to internet difficulties and using another person's Windows :sob: laptop.
- Python 3.8.1
- [Colorama 0.4.3](https://github.com/tartley/colorama)

## Game Rules
_Board:_

![Wikipedia board illustration](https://upload.wikimedia.org/wikipedia/commons/a/a1/Hexapawn.png)

_Board in game:_

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

## The Learning
- When player loses, all of their moves (states) are discouraged by reducing their points, thus diciplining the computer. 
- Otherwise encourage good moves (states) by increasing their points.

_Points:_
- New state: 50
- Increase amount: 5
- Decreases amount: -5 or amount is made 0 when a negative result is reached.

## Decision Making
Each player generates a random value and checks in which decision range the value falls under, afterwards this state is returned. This is based on Monte Carlo simulations.

## Conclusion
It was a fun experiment and I learned a bit about Python 3 syntax and side note Colorama is a very cool project, do have a look! In terms of the game and the basic machine learning, I found it quite interesting that after a simulation with a hundred games the 'players' would still encounter 'unknown' states and that during this simulation that none of the decisions could be phased out (reach a zero value). Another interesting find was after a thousand games the general losing player would be inable to make decisions because all of their decisions lead in a bad outcome, to resolve this I had to let the player in this situation just randomly choose a decision rather than no decision.
