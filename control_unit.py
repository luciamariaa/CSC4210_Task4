class ControlUnit:
    def decode(self, instr):
        return {
            "op": instr.opcode,
            "invert": instr.invert_rs,
            "write": 1
        }
