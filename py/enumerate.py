
def odd_numbers(my_input):
    for x,y in enumerate(my_input):
        print(f"(index: {x}, value: {y})")
    return [y for x, y in enumerate(my_input) if x%2 != 0]


def palindrome(s):
    return s == s[::-1]    


print(palindrome("otto"))

xs = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(odd_numbers(xs))
