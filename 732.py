class MyCalendarThree:

    def __init__(self):
        self.timeline = []

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline.append((startTime, 1))
        self.timeline.append((endTime, -1))
        self.timeline.sort()

        maxBooking = 0
        ongoingBooking = 0

        for _, delta in self.timeline:
            ongoingBooking += delta
            maxBooking = max(maxBooking, ongoingBooking)

        return maxBooking
