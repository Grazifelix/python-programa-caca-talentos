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
        min = int(sec/60)
        hour = int(min / 60)
        sec -= min * 60
        min -= hour*60

        return str(f"{hour}:{min}:{sec}")


t = Timer()

while True:
    print(t)
