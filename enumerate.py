
def fun(my_input):
    return [x for x, y in enumerate(my_input) if y%2 != 0]

xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fun(xs))
