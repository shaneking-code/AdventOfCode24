
class MemUnit:
    def __init__(self, start, size):
        self.start = start
        self.size  = size
    def val(self):
        return (2 * self.start + self.size - 1) * self.size // 2
      
curr = 0
disk = []

for i, size in enumerate(map(int, open('in.txt').read())):
    disk += [MemUnit(curr, size)]
    curr += size

for full in disk[::-2]:
    for free in disk[1::2]:
        if free.start <= full.start and free.size >= full.size:
            full.start  = free.start
            free.start += full.size
            free.size  -= full.size

print(sum(i * unit.val() for i, unit in enumerate(disk[::2])))