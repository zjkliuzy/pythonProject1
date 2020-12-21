from threading import Thread
from time import sleep

tickets = []
for i in range(1, 501):
    t = "T%d" % i
    tickets.append(t)


def sell(name):
    while tickets:
        t = tickets[0]
        del tickets[0]
        print(name + "------" + t)
        sleep(0.1)


jobs = []
for i in range(1, 11):
    name = "W%d" % i
    thd = Thread(target=sell, args=(name,))
    thd.start()
    jobs.append(thd)

[i.join() for i in jobs]
