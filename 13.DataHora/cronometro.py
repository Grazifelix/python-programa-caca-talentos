# 09/12/22
import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def reset(self):
        self.start = time.time()

    def get(self) -> float:
        return time.time() - self.start

    def __str__(self):
        value = self.get()
        sec = int(value)
        min = int(sec/10)
        hour = int(min / 10)
        sec -= min * 10
        min -= hour*10

        return str(f"{hour}:{min}:{sec}")


t = Timer()

while True:
    if t.get() > 5.0:
        t.reset()
    print(t)