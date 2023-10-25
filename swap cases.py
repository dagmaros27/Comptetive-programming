def swap_case(s):
    arr = []
    for i in range(len(s)):
        if s[i].islower():
            arr.append(s[i].upper())
        else:
            arr.append(s[i].lower())
    string = ''.join(arr)
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)