import time


with open("log.txt", "a+") as file:
    file.seek(0)
    lines = file.readlines()
    num = 1
    if lines:
        lastline = lines[len(lines) - 1]
        num = int(lastline.split(".")[0]) + 1

    while True:
        stime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        str_to_write = str(num) + ". " + stime + "\n"
        file.write(str_to_write)
        print(str_to_write)
        file.flush()
        num += 1
        time.sleep(2)
