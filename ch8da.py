def get_instruction(opcode):

    s = opcode[0]
    x = opcode[1]
    y = opcode[2]
    n = opcode[3]
    kk = opcode[2:4]
    addr = opcode[1:4]

    if s == '0':
        if addr == "0E0":
            return "CLS \t\t\t Clear the display"
        elif addr == "0EE":
            return "RET \t\t\t Return from subroutine"
        else:
            return f""
    elif s == '1':
        return f"JP {addr} \t\t Jump to address {addr}"
    elif s == '2':
        return f"CALL {addr} \t\t Call subroutine at {addr}"
    elif s == '3':
        return f"SE V{x}, {kk} \t\t If V{x} == {kk}, skip next instruction"
    elif s == '4':
        return f"SNE V{x}, {kk} \t If V{x} != {kk}, skip next instruction"
    elif s == '5':
        if n == '0':
            return f"SE V{x}, V{y} \t\t If V{x} == V{y}, skip next instruction"
        else:
            return ""
    elif s == '6':
        return f"LD V{x}, {kk} \t\t Set V{x} = {kk}"
    elif s == '7':
        return f"ADD V{x}, {kk} \t Set V{x} = V{x} + {kk}"
    elif s == '8':
        if n == '0':
            return f"LD V{x}, V{y} \t\t Set V{x} = V{y}"
        elif n == '1':
            return f"OR V{x}, V{y} \t\t Set V{x} = V{x} OR V{y}"
        elif n == '2':
            return f"AND V{x}, V{y} \t Set V{x} = V{x} AND V{y}"
        elif n == '3':
            return f"XOR V{x}, V{y} \t Set V{x} = V{x} XOR V{y}"
        elif n == '4':
            return f"ADD V{x}, V{y} \t Set V{x} = V{x} + V{y}, set VF = carry"
        elif n == '5':
            return f"SUB V{x}, V{y} \t Set V{x} = V{x} - V{y}, set VF = NOT borrow"
        elif n == '6':
            return f"SHR V{x} {{, V{y}}} \t Set V{x} = V{x} (old: V{y}) SHR 1, set VF = shifted bit"
        elif n == '7':
            return f"SUBN V{x}, V{y} \t Set V{x} = V{y} - V{x}, set VF = NOT borrow"
        elif n == 'E':
            return f"SHL V{x} {{, V{y}}} \t Set V{x} = V{x} (old: V{y}) SHL 1, set VF = shifted bit"
        else:
            return ""
    elif s == '9':
        if n == '0':
            return f"SNE V{x}, V{y} \t If V{x} != V{y}, skip next instruction"
        else:
            return ""
    elif s == 'A':
        return f"LD I {addr} \t\t Set I = {addr}"
    elif s == 'B':
        return f"JP V0 {addr} \t\t Jump to address {addr} + V0 (new: {addr} + V{x})"
    elif s == 'C':
        return f"RND V{x}, {kk} \t Set V{x} = random byte AND {kk}"
    elif s == 'D':
        return f"DRW V{x}, V{y}, {n} \t Display {n}-byte sprite at memory location I at (V{x}, V{y}), set VF = collision"
    elif s == 'E':
        if kk == "9E":
            return f"SKP V{x} \t\t If key V{x} is pressed, skip next instruction"
        elif kk == "A1":
            return f"SKNP V{x} \t\t If key V{x} is not pressed, skip next instruction"
        else:
            return ""
    elif s == 'F':
        if kk == "07":
            return f"LD V{x}, DT \t\t Set V{x} = delay timer value"
        elif kk == "0A":
            return f"LD V{x}, K \t\t Wait for key press, store key value in V{x}"
        elif kk == "15":
            return f"LD DT, V{x} \t\t Set delay timer = V{x}"
        elif kk == "18":
            return f"LD ST, V{x} \t\t Set sound timer = V{x}"
        elif kk == "1E":
            return f"ADD I, V{x} \t Set I = I + V{x}"
        elif kk == "29":
            return f"LD F, V{x} \t\t Set I = location of digit V{x} sprite"
        elif kk == "33":
            return f"LD B, V{x} \t\t Store BCD of V{x} in memory locations I, I+1, and I+2"
        elif kk == "55":
            return f"LD [I], V{x} \t Store registers V0 through V{x} in memory at location I"
        elif kk == "65":
            return f"LD V{x}, [I] \t Store memory at location I in registers V0 through V{x}"
        else:
            return ""

path = open("filepath.txt", "r").read()

raw = open(path, "rb").read()
bytes = [f"{byte:02x}" for byte in raw]

with open("output.txt", "w") as output:
    for i in range(0, len(bytes) - (len(bytes) % 2), 2):
        opcode = (bytes[i] + bytes[i + 1]).upper()
        output.write(opcode + " \t " + get_instruction(opcode) + '\n')