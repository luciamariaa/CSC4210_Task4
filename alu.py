class ALU:
    def execute(self, op, a, b, invert_a=False):
        if invert_a:
            a = 1 - a

        if op == "AND":
            return a & b
        elif op == "OR":
            return a | b
