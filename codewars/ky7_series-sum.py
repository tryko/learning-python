# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


def series_sum(n):
    sum = 0.0
    for i in range(0, n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum
