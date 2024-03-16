import random
from tabulate import tabulate

def monte_carlo_dice_simulation(num_trials):
    """
    Simulate rolling two dice a large number of times and calculate the probabilities of each possible sum.

    Args:
    - num_trials (int): The number of times to simulate the dice rolls.

    Returns:
    - dict: A dictionary where keys represent the sum of the dice, and values represent the probability of each sum.
    """
    results = {}
    # Perform the dice simulation for the specified number of trials
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        # Update the results dictionary with the count of each sum
        if total in results:
            results[total] += 1
        else:
            results[total] = 1
    
    # Calculate the probabilities for each possible sum
    probabilities = {i: results[i] / num_trials * 100 for i in range(2, 13)}
    return probabilities

def display_probabilities(probabilities):
    """
    Display the probabilities of each possible sum of two dice rolls.

    Args:
    - probabilities (dict): A dictionary containing the probability of each sum.
    """
    table = []
    # Populate the table with rows containing the sum and its corresponding probability
    for i in range(2, 13):
        table.append([i, f"{probabilities[i]:.2f}% ({(probabilities[i] / 100 * 36):.3f}/36)"])
    
    # Display the table using the tabulate library
    headers = ["Sum", "Probability"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

# Set the number of trials for the Monte Carlo simulation
num_trials = 1000000

# Perform the Monte Carlo simulation
probabilities = monte_carlo_dice_simulation(num_trials)

# Display the probabilities obtained from the simulation
display_probabilities(probabilities)

