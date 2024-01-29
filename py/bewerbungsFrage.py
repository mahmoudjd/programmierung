
def read_textfile(filename):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    return lines


def process_data(lines):
    tuples = [] 
    for line in lines:
        (nr,word) = line.split()
        tuples.append((int(nr),word))

    return tuples


def make_pyr(tuples):
    nums = [x[0] for x in tuples]
    current_num = 1

    for i in range(1, 4):
        spaces = " " * (3 - i)
        row = spaces
        for _ in range(i):
            row += str(nums[current_num - 1]) + " "
            current_num += 1
        print(spaces + row.strip())


infos = read_textfile("./input.txt")

tuples= process_data(infos)

stuples = sorted(tuples, key=lambda t: t[0])

print(infos)

print(stuples)

make_pyr(stuples)

for num, word in stuples:
    if num % 2 != 0:
        print(word)
