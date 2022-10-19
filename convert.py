def convert(s: str, numRows: int) -> str:
    res = ['' for _ in range(numRows) ]
    next = False
    i = 0
        
    for c in s:
        res[i] += c
        if i == numRows -1:
            next = True
        if i == 0:
            next = False
        if not next:
            i += 1
        else:
            i -= 1
    last = ''        
    for i in res: 
        last += i

    return last


if __name__ == '__main__':
    print(convert("testtest", 2))
