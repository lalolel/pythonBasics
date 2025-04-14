# Step 1: Create a list called toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Step 2: Create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Step 3: Count the occurrences of $2 slices in prices
num_two_dollar_slices = prices.count(2)
print("Number of $2 slices:", num_two_dollar_slices)

# Step 4: Find the length of the toppings list
num_pizzas = len(toppings)

# Step 5: Print how many kinds of pizza are sold
print(f"We sell {num_pizzas} different kinds of pizza!")

# Step 6: Create the pizza_and_prices list
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# Step 7: Print pizza_and_prices
print("Pizza and Prices:", pizza_and_prices)

# Step 8: Sort pizza_and_prices in ascending order
pizza_and_prices.sort()
print("Sorted Pizza and Prices:", pizza_and_prices)

# Step 9: Store the cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# Step 10: Store the priciest pizza
priciest_pizza = pizza_and_prices[-1]

# Step 11: Remove the priciest pizza (anchovies)
pizza_and_prices.pop()
print("Updated Pizza and Prices after removing priciest:", pizza_and_prices)

# Step 12: Add the new "peppers" topping
peppers_pizza = [2.5, "peppers"]
pizza_and_prices.append(peppers_pizza)

# Ensure the list remains sorted
pizza_and_prices.sort()
print("Pizza and Prices after adding peppers:", pizza_and_prices)

# Step 13: Get the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print("Three Cheapest Pizzas:", three_cheapest)
