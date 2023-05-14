from Lab7_1_kolejka import Queue
import random as rd


def hot_potato(num):
    register = Queue()
    players = ["John", "Lusi", "Gor", "Mrok", "Arnold", "Nora"]
    for player in players:
        register.enqueue(player)

    while register.size() > 1:
        for i in range(num):
            register.enqueue(register.dequeue())

        numbers = rd.randint(0, 35)
        if numbers == 5:
            register.dequeue()


    return register.dequeue()

print(hot_potato(8))