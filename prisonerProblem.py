import random

runCount = 50
results = []
total = 0
success = 0


def run():
    #Initiation of boxes
    boxNumber = []
    prisonerID = []
    boxAssignment = []

    safeCount = 0

    boxes = 100

    for i in range(1, boxes + 1):
        boxNumber.append(i)
        prisonerID.append(i)

    for i in range(1, boxes + 1):
        n = random.randint(1, boxes)

        isUnique = False

        while isUnique == False:
            if boxAssignment.count(n) == 0:
                boxAssignment.append(n)
                isUnique = True
            else:
                n = random.randint(1, boxes)

    #Prisoners openning boxes
    for i in prisonerID:
        boxesOpened = 0
        memory = []
        memory.clear()

        open = 0

        while boxesOpened < (boxes/2):

            isUnique = False

            while isUnique == False:
                if memory.count(open) == 0:
                    memory.append(open)
                    isUnique = True
                else:
                    open = random.randint(1, boxes)

            if prisonerID[i - 1] == open:
                safeCount = safeCount + 1
                break
            else:
                boxesOpened = boxesOpened + 1
    return safeCount

for i in range(int(runCount)):
    a = run()
    results.append(a)
    total = total + a

    if a == 100:
        success = success + 1

average = total/len(results)
rate = success/len(results)

print(results)
print(average)
print(rate)
