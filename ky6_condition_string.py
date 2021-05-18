def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes(names):
    l = len(names)
    if l == 0: return 'no one likes this'
    if l == 1: return '{} likes this'.format(names[0])
    if l == 2: return '{} and {} like this'.format(names[0], names[1])
    if l == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)
