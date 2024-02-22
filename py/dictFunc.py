def DictFunction(numbers):
    Dict = {}
    for x in range(len(numbers)-1,0,-1):
       if numbers[x] ** 2 % 2 != 0:
          Dict[numbers[x] * 2] = numbers[x] ** 2
    return Dict

print(DictFunction([2,7,4,5]))

