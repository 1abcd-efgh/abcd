def solve_knapsack():
    n = int(input("Enter number of items: "))

    val = []
    wt = []

    print("\nEnter values and weights for each item:")
    for i in range(n):
        v = int(input(f"Value of item {i+1}: "))
        w = int(input(f"Weight of item {i+1}: "))
        val.append(v)
        wt.append(w)

    W = int(input("\nEnter maximum capacity of the knapsack: "))

    # Recursive knapsack function
    def knapsack(W, n):
        # Base case: no items left or capacity 0
        if n < 0 or W <= 0:
            return 0
        # Skip item if it is heavier than remaining capacity
        if wt[n] > W:
            return knapsack(W, n-1)
        else:
            # Max of including or not including current item
            return max(val[n] + knapsack(W - wt[n], n-1), knapsack(W, n-1))

    # Call recursive function with last item index
    print(f"\nMaximum total value in knapsack = {knapsack(W, n-1)}")


if __name__ == "__main__":
    solve_knapsack()