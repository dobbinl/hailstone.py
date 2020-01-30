
def hailstone(i):
    count = 0           """set a counter to track the number of times a loop is completed before reaching 1."""
    while i != 1:       """set a loop"""
        if (i % 2 == 0):
            i = i / 2
        else:
            i = i * 3 + 1
        count = count + 1
    return count

print(hailstone(7))
