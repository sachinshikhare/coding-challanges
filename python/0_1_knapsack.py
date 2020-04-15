def calculate_knapsack(max_wt, wts, values, n):
    if max_wt == 0 or n == 0:
        return 0
    if wts[-1] > max_wt:
        calculate_knapsack(max_wt, wts, values, n-1)
    return max(
        values[n-1] + calculate_knapsack(max_wt - wts[n-1], wts, values, n-1),
        calculate_knapsack(max_wt, wts, values, n-1)
    )


if __name__ == "__main__":
    max_wt = 150
    values = [3, 55, 3, 2, 5, 78, 65, 65, 43, 4, 6, 7, ]
    wts = [20, 3, 11, 34, 22, 55, 34, 66, 45, 23, 66, 22]

    # max_wt = 50
    # values = [60,100,120]
    # wts = [10,20,30]

    print(calculate_knapsack(max_wt, wts, values, len(wts)))
