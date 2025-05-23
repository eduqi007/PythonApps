def calculation_process(state, value):
    value = float(value) if value else 0
    state.f_num = state.f_num*state.mult_or_sum_1*(value ** state.mult_or_div) + state.mult_or_sum_2*(state.f_num + state.sign_fix*value)

def handle_sum(state, value):
    calculation_process(state, value)
    state.mult_or_sum_1 = 0
    state.mult_or_sum_2 = 1
    state.sign_fix = 1

def handle_subtract(state, value):
    calculation_process(state, value)
    state.mult_or_sum_1 = 0
    state.mult_or_sum_2 = 1
    state.sign_fix = -1

def handle_mult(state, value):
    calculation_process(state, value)
    state.mult_or_sum_1 = 1
    state.mult_or_sum_2 = 0
    state.mult_or_div = 1

def handle_divide(state, value):
    calculation_process(state, value)
    state.mult_or_sum_1 = 1
    state.mult_or_sum_2 = 0
    state.mult_or_div = -1

def handle_equal(state, value):
    calculation_process(state, value)
    state.f_ans = state.f_num
    return state.f_num

def handle_ans(state):
    state.f_num = 0
    state.sign_fix = 1
    state.mult_or_sum_1 = 0
    state.mult_or_sum_2 = 1
    return state.f_ans

