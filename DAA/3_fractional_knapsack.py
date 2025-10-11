def fractional_knapsack():
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    print("\nEnter weights and values for each item:")
    for i in range(n):
        w = float(input(f"Weight of item {i+1}: "))
        v = float(input(f"Value of item {i+1}: "))
        weights.append(w)
        values.append(v)

    capacity = float(input("\nEnter maximum capacity of the knapsack: "))
    res = 0.0

    # Pair: (weight, value), sorted by value/weight ratio in descending order
    for pair in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        if capacity <= 0:
            break
        if pair[0] > capacity:
            res += capacity * (pair[1] / pair[0])  # Take fraction of the item
            capacity = 0
        else:
            res += pair[1]  # Take full item
            capacity -= pair[0]

    print(f"\nMaximum total value in knapsack = {res:.2f}")

if __name__ == "__main__":
    fractional_knapsack()