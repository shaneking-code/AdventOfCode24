import re

class Machine:
    def __init__(self, descriptor):
        self.Ax, self.Ay, self.Bx, self.By, self.Px, self.Py = descriptor 

    def cramers(self, part):

        x = 0
        y = 0

        self.Px += (part - 1) * 10000000000000
        self.Py += (part - 1) * 10000000000000

        xn = self.Px * self.By - self.Bx * self.Py
        yn = self.Ax * self.Py - self.Px * self.Ay
        d  = self.Ax * self.By - self.Bx * self.Ay

        if xn % d == 0:
            x = xn // d
        if yn % d == 0:
            y = yn // d
        
        if x <= 0 and y <= 0:
            return -x, -y
        elif x > 0 and y > 0:
            return x, y
        else:
            return 0, 0

machines = [*map(lambda machine : Machine([*map(int, re.findall(r'\d+', machine))]), open('in.txt').read().split('\n\n'))]
one = 0
two = 0

for machine in machines:

    x1, y1 = machine.cramers(1)
    x2, y2 = machine.cramers(2)

    one += (x1 * 3 + y1)
    two += (x2 * 3 + y2)

print(f"answer to part one is {one}")
print(f"answer to part two is {two}")