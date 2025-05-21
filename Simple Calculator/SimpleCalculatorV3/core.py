def process_operation(state, value):
    value=float(value) if value else 0
    state.f_num = (
        state.f_num*state.mult_or_sum_1*(value**state.mult_or_div) + state.mult_or_sum2*(state.f_num + state.sign_fix*value)
    )

    def handle_add(state, value):
        process_operation(state, value)
        state.sign_fix = 1
        state.mult_or_sum_1 = 0
        state.mult_or_sum_2=1
        state.mult_or_div=1

    def handle_subtract(state, value):
        process_operation(state, value)
        state.sign_fix = -1
        state.mult_or_sum_1=0
        state.mult_or_sum_2=1
        state.mult_or_div=1
    
    def handle_multiply(state, value):
        process_operation(state, value)
    