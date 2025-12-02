with open("17.in") as f:
    lines = [line.strip() for line in f.readlines()]

A = int(lines[0][12:])
B = int(lines[1][12:])
C = int(lines[2][12:])

program = [int(x) for x in lines[4][9:].split(",")]
ip = 0
output = []

def combo_value(operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C

while ip < len(program):
    opcode, operand = program[ip:ip+2]
    if opcode == 0: # adv, COMBO
        A = A // 2**combo_value(operand)
    elif opcode == 1: # bxl, LITERAL
        B = B ^ operand
    elif opcode == 2: # bst, COMBO
        B = combo_value(operand) % 8
    elif opcode == 3: # jnz, LITERAL
        if A != 0:
            ip = operand - 2
    elif opcode == 4: # bxc, LITERAL
        B = B ^ C
    elif opcode == 5: # out, COMBO
        output.append(combo_value(operand) % 8)
    elif opcode == 6: # bdv, COMBO
        B = A // 2**combo_value(operand)
    elif opcode == 7: # cdv, COMBO
        C = A // 2**combo_value(operand)
    ip += 2

print(",".join(str(x) for x in output))


def find_target(prev_A, ndx):
    for tmp in range(8):
        A = prev_A * 8 + tmp
        B = A % 8
        C = (A >> (B ^ 7)) % 8
        if B ^ C == program[ndx]:
            if ndx == 0:
                return A
            recur = find_target(prev_A*8 + tmp, ndx-1)
            if recur is not None:
                return recur
    return None

print(find_target(0, len(program)-1))

"""
A = 7
B = int(lines[1][12:])
C = int(lines[2][12:])
output = []

while A != 0:
    B = A % 8
    C = (A >> (B ^ 7)) % 8
    output.append((B ^ C) % 8)
    print(A,B,C)
    A = A >> 3

print(",".join(str(x) for x in output))
"""
