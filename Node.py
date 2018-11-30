class Node(object):
    def __init__(self, char="-1", LHS=None, RHS=None):
        self.code = str()
        self.LHS = LHS
        self.RHS = RHS
        if LHS is None and RHS is None:
            self.cnt = 0
            self.char = char
        else:
            self.cnt = LHS.cnt + RHS.cnt
            self.char = LHS.char + RHS.char

    def code_set(self, code):
        self.code = code
        if not (self.LHS is None and self.RHS is None):
            self.LHS.code_set(code + '0')
            self.RHS.code_set(code + '1')

    def is_leaf(self):
        return self.RHS is None

    def increase(self):
        self.cnt += 1

    def __lt__(self, other):
        return self.cnt < other.cnt

    def __cmp__(self, other):
        return self.cnt < other.cnt
