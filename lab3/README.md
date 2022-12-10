# Lab 3: Policy Search

## Task

Write agents able to play [*Nim*](https://en.wikipedia.org/wiki/Nim), with an arbitrary number of rows and an upper bound $k$ on the number of objects that can be removed in a turn (a.k.a., *subtraction game*).

The player **taking the last object wins**.

* Task3.1: An agent using fixed rules based on *nim-sum* (i.e., an *expert system*)
* Task3.2: An agent using evolved rules
* Task3.3: An agent using minmax
* Task3.4: An agent using reinforcement learning

## Instructions

* Create the directory `lab3` inside the course repo 
* Put a `README.md` and your solution (all the files, code and auxiliary data if needed)

## Notes

* Working in group is not only allowed, but recommended (see: [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu_philosophy) and [Cooperative Learning](https://files.eric.ed.gov/fulltext/EJ1096789.pdf)). Collaborations must be explicitly declared in the `README.md`.
* [Yanking](https://www.emacswiki.org/emacs/KillingAndYanking) from the internet is allowed, but sources must be explicitly declared in the `README.md`.

**Deadline**

* Tasks 3.1 and 3.2 -->  4/12  
* Tasks 3.3 and 3.4 --> 11/12  

---

## __Note__  

__The documentation is inside every function. The readme gives just the high level idea of the strategy, while the functions contains an in depth documentation of what they do!__

---

## Task 3.1 - An agent using fixed rules based on nim-sum  

The agent uses an expert strategy based on nim-sum. If the agent is on a position with not zero nim-sum, then he will always win.  

Based on the explanation available here: https://en.wikipedia.org/wiki/Nim   


## Task 3.2 - An agent using evolved rules

The agent uses evolved hard-coded rules. Those rules are labeled with a number from 1 to 7. The order of the rules represents the genome of the agent.  

I used a hyerarcical island strategy to let evolve the initial population. Only the best individual surviving at each island where able to reproduce.  

The opponents where the following, ordered from the lowest island to the highest:
- Dumb opponent: always takes one obj from the first row available.  
- Dumb random opponent: there is 0.5 of probability to make a dumb action or a random action.  
- Random opponent: the opponent performs a random action.  
- Layered opponent: it always takes the whole row's objs choosing randomly the row.  
- Demigod opponent: there is a probability to play an expert move and a chance to play randomly
- God opponent: it is the expert agent developed at task3.1, the one that uses nim-sum.


## Task 3.3 - An agent using minmax   

The agent uses the MinMax strategy applyed on the game tree, a tree with all the possible states of nim.

I used the alpha-best pruning in order to reduce the time complexity of the function. The nodes of the tree stops expanding if there is at least a child already expanded that has the best result expected for the player at that layer.

> If the layer is played by the opponent and a child has -inf utility, than the opponent will stop expanding the current state because it knows that it will win with that move.
> The same if for the layer played by the agent: if there is at least a child with +inf utility, than stop expanding the subtree.


## Task 3.4 - An agent using reinforcement learning  

The solution is inspired by the maze example given by the professor.

THe states are encoded inside a game tree similar to the one of the previous task and the reward is set to:
- 100 if the agent wins
- -100 if the agent loses
- -1 if the state is not a win or lose state

