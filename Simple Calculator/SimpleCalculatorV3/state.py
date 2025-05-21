class CalculatorState:
    def __init__(self):
        self.f_num = 0   
        self.f_ans = 0
        self.sign_fix = 1
        self.mult_or_sum_1 = 0
        self.mult_or_sum_2 = 1
        self.mult_or_div = 1

    def reset(self):
        self.__init__()


