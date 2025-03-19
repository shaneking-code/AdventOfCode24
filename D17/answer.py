from typing import List
from re import findall
from itertools import product

class Computer:
    def __init__(self, A: int, B: int, C: int) -> None:

        # init regs
        self.A = A
        self.B = B
        self.C = C

        # operation, combo? mapping
        self.ops = {
            0 : (self.adv, True),
            1 : (self.bxl, False),
            2 : (self.bst, True),
            3 : (self.jnz, False),
            4 : (self.bxc, False),
            5 : (self.out, True),
            6 : (self.bdv, True),
            7 : (self.cdv, True)
        }
    def opvals(self, operand: int) -> int:
        if operand in [0, 1, 2, 3]:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        if operand > 6:
            raise ValueError(f"Reserved operand: {operand}")
    def run(self, program: List[int]) -> str:
        ip = 0
        bound = len(program) - 1
        out = []

        while ip < bound:

            opcode, operand = program[ip], program[ip + 1]
            op, cmb = self.ops[opcode]
            opval= self.opvals(operand) if cmb else operand
            #print(f"state before op : A = {self.A}, B = {self.B}, C = {self.C}, ip = {ip}, out = {out}")
            print(f"op = {op.__name__}, operand = {opval}")
            if cmb:
                if operand == 4:
                    print("Using register A, value = ", self.A)
                if operand == 5:
                    print("Using register B, value = ", self.B)
                if operand == 6:
                    print("Using register C, value = ", self.C)
                
            res = op(opval)
            #print(f" state after op : A = {self.A}, B = {self.B}, C = {self.C}, ip = {ip}, out = {out}")
            if res and len(res) == 2:
                op, ret = res
                if op == 'jnz' and ret != -1:
                    ip = ret
                    continue
                elif op == 'out':
                    out.append(ret)
                    print()

            ip += 2
        
        return out
    def adv(self, cmb):
        self.A >>= cmb
    def bxl(self, lit):
        self.B ^= lit
    def bst(self, cmb):
        self.B = cmb & 7
    def jnz(self, lit):
        ret = -1 if self.A == 0 else lit
        return 'jnz', ret
    def bxc(self, lit):
        self.B ^= self.C
    def out(self, cmb):
        return 'out', cmb & 7
    def bdv(self, cmb):
        self.B = self.A >> cmb
    def cdv(self, cmb):
        self.C = self.A >> cmb

input   = open('in.txt').read()
pattern = r'\d+'
matches = findall(pattern, input)
A, B, C, *program = list(map(int, matches))

cpu = Computer(A, B, C)
out = cpu.run(program)

print(out)


