from dataclasses import dataclass

@dataclass
class Instruction:
    opcode: str
    rd: str
    rs: str
    rt: str
    invert_rs: bool = False
