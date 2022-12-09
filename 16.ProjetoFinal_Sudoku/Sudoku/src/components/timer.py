# 09/12/22
import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def reset(self):
        self.start = time.time()

    def get(self) -> float:
        return time.time() - self.start

    def timer(self):
        value = self.get()
        sec = int(value)
        min = int(sec/10)
        hour = int(min / 10)
        sec -= min * 10
        min -= hour*10

        return hour, min, sec

