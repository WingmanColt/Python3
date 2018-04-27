def kangaroo(x1, v1, x2, v2):
    someLocationPossible = ""
    if x1 < x2 and v1 < v2:
        sameLocationPossible = "NO"

    elif x2 < x1 and v2 < v1:
        sameLocationPossible = "NO"

    elif x2 < x1:
        Jumps = float((x1 - x2) // (v2 - v1))
        if Jumps % 1 == 0:
            sameLocationPossible = "YES"
        else:
            sameLocationPossible = "NO"

    else:
        Jumps = float((x2 - x1) // (v1 - v2))
        if Jumps % 1 == 0:
            sameLocationPossible = "YES"
        else:
            sameLocationPossible = "NO"

    return sameLocationPossible

# MAIN DECLARATIONS
tokens_x1 = str(input())
tokens_x1.split(' ')

x1 = int(tokens_x1[0])
v1 = int(tokens_x1[1])
x2 = int(tokens_x1[2])
v2 = int(tokens_x1[3])

result = kangaroo(x1, v1, x2, v2)
print(result)
