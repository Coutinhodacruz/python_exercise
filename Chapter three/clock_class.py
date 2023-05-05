class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self._hour = hour
        self._minute = minute
        self._second = second

    def get_hour(self) -> int:
        return self._hour

    def set_hour(self, hour: int):
        if hour <= 23:
            self._hour = hour
        else:
            self._hour = 0
            self._minute = 0
            self._second = 0

    def get_minute(self) -> int:
        return self._minute

    def set_minute(self, minute: int):
        if minute <= 59:
            self._minute = minute
        else:
            self._hour = 0
            self._minute = 0
            self._second = 0

    def get_second(self) -> int:
        return self._second

    def set_second(self, second: int):
        if second <= 59:
            self._second = second
        else:
            self._hour = 0
            self._minute = 0
            self._second = 0

    def displayTime(self):
        print(f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}")


class ClockTest:
    def run(self):
        clock = Clock(23, 59, 58)
        clock.displayTime()
        clock.set_second(60)
        clock.displayTime()
        clock.set_hour(24)
        clock.displayTime()


ClockTest().run()
