class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = [[]]

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        freq = self.freq[val]
        if freq >= len(self.stacks):
            self.stacks.append([])
        self.stacks[freq].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        self.freq[val] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return val
