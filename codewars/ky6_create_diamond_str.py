def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None

def diamond(n):
    # Make some diamonds!
    if n % 2 == 0 or n < 0:
        return
    diamond_str = []
    for i in range(1, n, 2):
        diamond_str.append(" " * int((n -i)/2) + "*" * i + "\n")
    for i in range(n, 0, -2):
        diamond_str.append(" " * int((n -i)/2) + "*" * i + "\n")
    return "".join(diamond_str)