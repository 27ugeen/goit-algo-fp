# goit-algo-fp

### Comparison of Monte Carlo Simulation Results with Analytical Calculations

#### Monte Carlo Simulation

The Monte Carlo simulation involves rolling two dice a large number of times and recording the sum of the numbers that appear on both dice. The program then calculates the probability of each possible sum based on the simulation results.

#### Analytical Calculations

Analytical calculations provide the theoretical probabilities of obtaining each sum when throwing two dice. These probabilities are calculated based on the total number of possible outcomes and the number of outcomes corresponding to each sum.

#### Results

| Sum | Probability (Monte Carlo) | Probability (Analytical) |
|-----|---------------------------|--------------------------|
| 2   | 2.78% (1.002/36)          | 2.78% (1/36)             |
| 3   | 5.56% (2.003/36)          | 5.56% (2/36)             |
| 4   | 8.35% (3.007/36)          | 8.33% (3/36)             |
| 5   | 11.09% (3.993/36)         | 11.11% (4/36)            |
| 6   | 13.92% (5.012/36)         | 13.89% (5/36)            |
| 7   | 16.62% (5.984/36)         | 16.67% (6/36)            |
| 8   | 13.82% (4.975/36)         | 13.89% (5/36)            |
| 9   | 11.15% (4.016/36)         | 11.11% (4/36)            |
| 10  | 8.33% (3.001/36)          | 8.33% (3/36)             |
| 11  | 5.58% (2.007/36)          | 5.56% (2/36)             |
| 12  | 2.78% (1.001/36)          | 2.78% (1/36)             |

### Conclusion

The results we obtained are quite close to the analytically calculated probabilities, but may differ slightly due to the randomness of the simulation itself. In our case, the deviations from the analytical values are small, which indicates that the Monte Carlo method is correct for this problem.

Typically, the accuracy of Monte Carlo results increases with the number of simulations. To reduce the deviation, you can try to increase the value of `num_trials`, which indicates the number of simulations performed.
