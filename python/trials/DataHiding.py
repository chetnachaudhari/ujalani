#!/usr/bin/python

class HideDetails:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = HideDetails()
counter.count()
counter.count()

## Hack to access
print(counter._HideDetails__secretCount)