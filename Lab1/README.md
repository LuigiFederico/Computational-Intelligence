
# __Lab1: Set Covering__

> Author: Luigi Federico  
>  
> Computational Intelligence 2022/23  
> Prof: G. Squillero

---

## __Task__

Given a number $N$ and some lists of integers $P = (L_0, L_1, L_2, ..., L_n)$, 
determine is possible $S = (L_{s_0}, L_{s_1}, L_{s_2}, ..., L_{s_n})$
such that each number between $0$ and $N-1$ appears in at least one list

$$\forall n \in [0, N-1] \ \exists i : n \in L_{s_i}$$

and that the total numbers of elements in all $L_{s_i}$ is minimum. 

---

## __Solution proposed__

To find a solution I did as follows:

1. I sorted the lists $L_0, L_1, L_2, ..., L_n$ using the cost function (explained below). This sorted lists are the frontier.
2. For a maximum of N iterations, the algorithm pops out the list with the lowest cost and adds it to the solution.
3.  It clears from the frontier every list that is a strict subset of the covered set, becouse it can't contribute to build a solution.
4. The frontier is now resorted using the cost function.
5. If there will be at least a not redundant list inside the frontier, it will be considered to build the solution in the next iteration. If the frontier is empty after the next loop and we didn't find the solution I declare it.

> __Why at most N iterations?__  
> The worst case in this approach occurs when we take at each step just one new digit into the covered set. If at some point we want to append a new list to the solution, we surely want to add the one that gives at least one new digit to the covered set. If we do more then N operations, it's garanteed that at least one of the lists is redundant, i.e. it contains only digits that was already added to the solution.

### __Cost function__

``` Python
def cost(l, goal, covered):
  extended_covered = set(l) | covered  
  return len(l) * W_FACTOR + len(goal - extended_covered) * INTW_FACTOR
```

The idea behind this function is to consider:
- the length of the current list *l*  
- the number of digits left to achive the solution if the list *l* was included in the *covered* set.  

I wanted to give more importance to the amount of contribution that the given list *l* brings to the solution (in terms of number of new digits offered to the *covered* set) rather then the weight of *l*, i.e. the length of the list.  
To do this, I scaled the weight and the number of new digits obtained adding *l* to the solution with __W_FACTOR__=2 (weight factor) and __INTW_FACTOR__=10 (internal weight factor), respectively.  

> Note that if we use as scale factor W_FACTOR = INTW_FACTOR, the algorithm will favorite short lists over longer ones, even if the first ones contribute with fewer new digits. I found it not ideal.


## __Results__

Running the algorithm with different values of N we obtain the following results.
> Of course they depend on the generated list set, but they should be similar to the peer rewiever results)

### __N = 5__
Solution found:
- Weight of the solution = 5  
- Execution time = 0.1s  
- Number of visited nodes = 3  

### __N = 10__
Solution found:
- Weight of the solution = 10
- Execution time = 0.1s  
- Number of visited nodes = 3  

### __N = 20__
Solution found:
- Weight of the solution = 28
- Execution time = 0.1s  
- Number of visited nodes = 4   

### __N = 100__ 
Solution found:
- Weight of the solution = 181
- Execution time = 0.1s  
- Number of visited nodes = 6

### __N = 500__ 
Solution found:
- Weight of the solution = 1419
- Execution time = 1.6s  
- Number of visited nodes = 11

### __N = 1000__ 
Solution found:
- Weight of the solution = 3110
- Execution time = 6.9s  
- Number of visited nodes = 13


