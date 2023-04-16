

class Solver:
    def __init__(self, name=''):
        self.name = name

    def solve(self, *args):
        raise NotImplementedError()
    
    def test_solve(self):
        raise NotImplementedError()
    