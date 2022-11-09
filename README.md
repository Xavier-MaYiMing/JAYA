### JAYA Algorithm

##### Reference: Rao R. Jaya: A simple and new optimization algorithm for solving constrained and unconstrained optimization problems[J]. International Journal of Industrial Engineering Computations, 2016, 7(1): 19-34.

| Variables   | Meaning                                                 |
| ----------- | ------------------------------------------------------- |
| pop         | The number of candidates                                |
| iter        | The number of iterations                                |
| lb          | The lower bound (list)                                  |
| ub          | The upper bound (list)                                  |
| pos         | The position of all candidates (list)                   |
| score       | The score of all candidates (list)                      |
| dim         | Dimension                                               |
| gbest       | The position of the global best candidate               |
| gbest_pos   | The score of the global best candidate (list)           |
| best_score  | The best score of the iteration                         |
| best_pos    | The position of the best score of the iteration (list)  |
| worst_score | The worst score of the iteration                        |
| worst_pos   | The position of the worst score of the iteration (list) |
| new_pos     | The positions of newly updated candidates (list)        |
| new_score   | The scores of newly updated candidates (list)           |
| iter_best   | The global best score of each iteration (list)          |
| iter_con    | The last iteration number when the "gbest" is updated   |

#### Test problem: Pressure vessel design

![](C:\Users\dell\Desktop\研究生\个人算法主页\Grey Wolf Optimizer\Pressure vessel design.png)
$$
\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
\text{s.t.} -x_1+0.0193x_3\leq0,\\
-x_3+0.0095x_3\leq0,\\
-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
x_4-240\leq0,\\
0\leq x_1\leq99,\\
0\leq x_2 \leq99,\\
10\leq x_3 \leq 200,\\
10\leq x_4 \leq 200.
$$


#### Example

```python
if __name__ == '__main__':
    # Parameter settings
    pop = 50
    iter = 1000
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
```

##### Output:

![convergence curve](C:\Users\dell\Desktop\研究生\个人算法主页\JAYA\convergence curve.png)

The JAYA converges at its 587-th iteration, and the global best value is 8050.913534658795. 

```python
{
    'best score': 8050.913534658795, 
    'best solution': [1.3005502034963052, 0.6428626394484327, 67.3860209065443, 10.0], 
    'convergence iteration': 587
}
```

