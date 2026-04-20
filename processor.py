import argparse
from instruction import Instruction
from register_file import RegisterFile
from alu import ALU
from control_unit import ControlUnit

rf = RegisterFile()
alu = ALU()
cu = ControlUnit()

def run(A, B, C, D):
    rf.load(A, B, C, D)

    print("===== INPUT VALUES =====")
    print(f"A = {A}, B = {B}, C = {C}, D = {D}")
    print()

    program = [
        Instruction("AND", "t4", "t0", "t1"),
        Instruction("AND", "t6", "t5", "t3", True),
        Instruction("OR", "t0", "t4", "t6")
    ]

    for i, instr in enumerate(program, 1):
        ctrl = cu.decode(instr)

        a = rf.read(instr.rs)
        b = rf.read(instr.rt)

        result = alu.execute(ctrl["op"], a, b, ctrl["invert"])

        if ctrl["write"]:
            rf.write(instr.rd, result)

        print(f"===== INSTRUCTION {i} =====")
        print(f"Operation: {instr.opcode}")
        print(f"Destination Register: {instr.rd}")
        print(f"Source Register 1: {instr.rs} = {a}")
        print(f"Source Register 2: {instr.rt} = {b}")
        print(f"Control Signals: {ctrl}")
        print(f"ALU Result: {result}")
        print("Register Values After Instruction:")
        for reg, val in rf.reg.items():
            print(f"  {reg} = {val}")
        print()

    print("===== INTERMEDIATE VALUES =====")
    print(f"t4 = A & B      = {rf.read('t4')}")
    print(f"t6 = (~C) & D   = {rf.read('t6')}")
    print(f"t0 = final Y    = {rf.read('t0')}")
    print()

    expected = (A & B) | ((1 - C) & D)

    print("===== FINAL OUTPUT =====")
    print(f"Y = {rf.read('t0')}")
    print(f"Expected Y = {expected}")
    print()

    print("===== VALIDATION =====")
    if rf.read("t0") == expected:
        print("PASS")
    else:
        print("FAIL")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--A", type=int, default=1)
    parser.add_argument("--B", type=int, default=0)
    parser.add_argument("--C", type=int, default=1)
    parser.add_argument("--D", type=int, default=1)
    args = parser.parse_args()

    for value_name, value in [("A", args.A), ("B", args.B), ("C", args.C), ("D", args.D)]:
        if value not in (0, 1):
            raise ValueError(f"{value_name} must be 0 or 1")

    run(args.A, args.B, args.C, args.D)

if __name__ == "__main__":
    main()
