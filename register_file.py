class RegisterFile:
    def __init__(self):
        self.reg = {
            "t0": 0, "t1": 0, "t2": 0, "t3": 0,
            "t4": 0, "t5": 0, "t6": 0
        }

    def read(self, r):
        return self.reg[r]

    def write(self, r, v):
        self.reg[r] = v

    def load(self, A, B, C, D):
        self.reg["t0"] = A
        self.reg["t1"] = B
        self.reg["t2"] = C
        self.reg["t3"] = D
        self.reg["t5"] = C
