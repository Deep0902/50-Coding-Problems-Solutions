#longest possible palindrome
def M1(str):
    occurance = [0] * 128
    for i in range (len(str)):
        occurance[ord(str[i])] = occurance[ord(str[i])] + 1

    length = 0
    for val in occurance:
        if val % 2 == 0:
            length+=val
        else: 
            length += val-1

    if length < len(str):
        length += 1
    
    return length

str = "racecar"
ans = M1(str)
print(ans)