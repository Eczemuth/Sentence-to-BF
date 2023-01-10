def findClosestMultiPlier(n):
    for i in range(int(n**(1/2)) + 1,1,-1):
        for j in range(int(n*(1/2)) + 1,1,-1):
            if i * j == n:
                return (i,j)
    return (n,1)

def sentenceToBrainFuck(s):
    res = ""
    for c in s:
        print(c,ord(c))
        first,second = findClosestMultiPlier(ord(c))
        res = res + "+" * first + "[->" + "+" * second + "<]>.>"
    return res

sentence = input()
bf = sentenceToBrainFuck(sentence)
print(bf)
