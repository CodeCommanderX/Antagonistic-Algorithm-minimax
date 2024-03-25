# Minimax Algorithm with Alpha-Beta Pruning

## Introduction

The Minimax algorithm, along with Alpha-Beta Pruning, is a technique used in adversarial search for decision-making in game trees. This README provides an overview of the Minimax algorithm and its extensions, Alpha-Beta pruning.

## Game Tree Components

1. **State Space**: Each state represents a game position.
2. **Start State, End State**: Initial and terminal states of the game.
3. **Successor Function**: Determines valid moves.
4. **Utility Function**: Evaluates end states.

## Adversarial Game Characteristics

- Players alternate moves according to rules.
- Players have complete knowledge of rules and game states.
- "Best" move leads to victory.

## Representing Game State

- **Game Tree**: Represents the state space of the game.
- **Root**: Initial state.
- **Max and Min Nodes**: Alternating levels of the tree represent players.
- **Leaves**: Terminal states.
- **Max Player's Strategy**: Path from root to leaf.

## Challenges

- Player moves depend heavily on opponent's moves.
- Generalizing is difficult due to large search spaces.
- Optimal solutions are hard to find; satisfactory ones are feasible.
- Typical algorithm: Minimax.

## Optimal Decision Making

- Max maximizes utility function.
- Min minimizes utility function.
- Max's strategy depends on Min's strategy.

## Minimax Value

- Utility value at end state corresponding to a path, assuming both players play optimally.

## Pseudocode

<img width="440" alt="image" src="https://github.com/CodeCommanderX/Antagonistic-Algorithm-minimax/assets/132070927/7595197d-7b23-4c02-b7cf-e0b2b2453c34">


## Conclusion

The Minimax algorithm, coupled with Alpha-Beta Pruning, is a powerful method for decision-making in adversarial environments. It allows for efficient exploration of game trees, enabling players to make optimal moves under uncertainty.

This README provides a structured overview of the Minimax algorithm and its application in adversarial search, focusing on decision-making in game trees. It outlines the components of game trees, characteristics of adversarial games, challenges, optimal decision-making strategies, Minimax value, and concludes with a discussion on the effectiveness of the algorithm.
