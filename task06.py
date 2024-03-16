def greedy_algorithm(items, budget):
    # Sort items by the ratio of calories to cost in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    print(sorted_items)
    
    selected_items = {}
    total_calories = 0
    total_cost = 0
    
    # Greedily select items while staying within the budget
    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            selected_items[item] = properties
            total_calories += properties['calories']
            total_cost += properties['cost']
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    # Initialize a 2D array to store the maximum total calorie content achievable for each budget and number of items
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i, (item_name, item_data) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            # Check if the current item can be included within the budget
            if item_data['cost'] <= j:
                # Calculate the maximum calorie content achievable by either including or excluding the current item
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_data['cost']] + item_data['calories'])
            else:
                # If the current item cannot be included, copy the value from the previous row
                dp[i][j] = dp[i - 1][j]

    # Trace back to find the selected items
    selected_items = {}
    i, j = n, budget
    while i > 0 and j > 0:
        item_name, item_data = list(items.items())[i - 1]
        if dp[i][j] != dp[i - 1][j]:
            selected_items[item_name] = item_data
            j -= item_data['cost']
        i -= 1

    return selected_items, dp[n][budget]

# Data about food items
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Budget for selecting food items
budget = 100

# Run greedy algorithm
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm - Selected Items:", selected_items_greedy)
print("Total Calories:", total_calories_greedy)

# Run dynamic programming algorithm
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nDynamic Programming Algorithm - Selected Items:", selected_items_dp)
print("Total Calories:", total_calories_dp)
