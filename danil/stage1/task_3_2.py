def out_of_range(values, low, high):

    return [
        i for i, num in enumerate(values) if abs(num) > abs(low) or abs(num) > abs(high)
    ]


def rate(values, dt):
    return [(values[i + 1] - values[i]) / dt for i in range(len(values) - 1)]


def moving_average(values, n):
    return [sum(values[i : i + n]) / n for i in range(len(values) - n + 1)]


if __name__ == "__main__":
    print(out_of_range([0, 2, 10, 15, 5], 5, -5))
