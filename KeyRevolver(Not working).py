from queue import Queue

# Inits
bulletPrice = int(input())
gunBarrelSize = int(input())

bulletsStack = []
bulletsInput = int(input())
bulletsStack.append(bulletsInput)

locksQueue = Queue()
locksInput = int(input())
locks = locksQueue.put(locksInput)

valueOfIntelligence = int(input())

shootCounter = 0
bulletCount = 0

# LOGIC
while locksQueue.qsize() > 0 and len(bulletsStack) > 0:

    bullet = bulletsStack.pop()
    safeLock = locksQueue.get()

if bulletsStack.pop() <= locksQueue.get():
   # locksQueue.dequeue()
    print("Bang!")
else:
    print("Ping!")

shootCounter += 1

if shootCounter >= gunBarrelSize:
    shootCounter = 0
    if bulletsStack.count() != 0:
        print("Reload!")

bulletCount += 1

money = valueOfIntelligence - (bulletCount * bulletPrice)

if locksQueue.qsize() > bulletsStack.count:
    print(f"Couldn't get through. Locks left: {locksQueue.qsize}")
else:
    print(f"{bulletsStack.count()} bullets left. Earned ${money}")
