n = int(input())
sk = int(input())

totalLoss = 0
selcol = 1

namesweb = []

for i in range(n):
    selcol *= sk

for i in range(n):
    cread = input().tolist()
    name = cread[0]
    Visits1 = cread[1]
    Visits2 = cread[2]

    namesweb.__add__(name)
    totalLoss += Visits1 * Visits2

print('\n', namesweb)
print("Total Loss: {0:F20}", totalLoss)
print("Security Token: {0}", selcol)
