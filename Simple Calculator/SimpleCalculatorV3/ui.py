import tkinter as tk

class CalculatorUI:
    def __init__(self, root, state, logic):
        self.state = state
        self.logic = logic

        root.title("CalculatorAPP - V3.0")
        root.configure(bg="white")

        self.past_display = tk.Entry(root, borderwidth=0, width=20, font=("Arial", 12), fg="gray")
        self.past_display.grid(row=0, column=0, columnspan=3, ipady=5, ipadx=5)

        self.button_ans = tk.Button(root, text="Ans", padx=15, pady=5, borderwidth=0, command=self.call_ans)
        self.button_ans.grid(column=3, row=0)

        self.display = tk.Entry(root, borderwidth=0, width=25, font=("Arial", 11), fg="black")
        self.display.grid(row=1, column=0, columnspan=3, ipady=5, ipadx=5)

        self.result_display = tk.Entry(root, borderwidth=0, width=8, font=("Arial", 16), fg="green")
        self.result_display.grid(row=1, column=3, columnspan=1, ipady=5, ipadx=0)

        self._create_buttons(root)
    
    def _create_buttons(self, root):
        button = lambda txt, r, c, cmd: tk.Button(root, text=txt, padx=40, pady=20, borderwidth=0, command=cmd).grid(row=r, column=c)

        for i in range(1,10):
            print(i)
            button(str(i), 4 - (i - 1) // 3, (i - 1) % 3, lambda n = i: self.insert_number(n))
        button_0 = tk.Button(text="0",padx=40, pady=20, borderwidth = 0, command=lambda: self.insert_number(0)).grid(row=5, column=0, columnspan=1)

        tk.Button(root, text="+", padx=38, pady=20, borderwidth=0, command=self.sum).grid(row=2, column=3)
        tk.Button(root, text="-", padx=40, pady=20, borderwidth=0, command=self.subtract).grid(row=3, column=3)
        tk.Button(root, text="X", padx=39, pady=20, borderwidth=0, command=self.multiply).grid(row=4, column=3)
        tk.Button(root, text="/", padx=40, pady=20, borderwidth=0, command=self.divide).grid(row=5, column=3)

        tk.Button(root, text="=", padx=39, pady=20, borderwidth=0, command=self.equal).grid(row=5, column=2)
        tk.Button(root, text="Clear", padx=30, pady=20, borderwidth=0, command=self.clear).grid(row=5, column=0, columnspan=3)
    
    def insert_number(self, number):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, f"{current}{number}")
    
    def clear(self):
        self.state.reset()
        self.display.delete(0, tk.END)
        self.past_display.delete(0, tk.END)
        self.result_display.delete(0, tk.END)
    
    def call_ans(self):
        self.state.f_num = 0
        self.display.delete(0, tk.END)
        self.past_display.delete(0, tk.END)
        self.display.insert(0, str(self.logic.handle_ans(self.state)))
    
    def _common_op(self, handler):
        self.result_display.delete(0, tk.END)
        val = self.display.get()
        handler(self.state, val)
        self.past_display.delete(0, tk.END)
        self.past_display.insert(0, str(self.state.f_num))
        self.display.delete(0, tk.END)

    def sum(self):
        self._common_op(self.logic.handle_sum)
    
    def subtract(self):
        self._common_op(self.logic.handle_subtract)
    
    def multiply(self):
        self._common_op(self.logic.handle_mult)
    
    def divide(self):
        self._common_op(self.logic.handle_divide)
    
    def equal(self):
        self.result_display.delete(0, tk.END)
        val = self.display.get()
        result = self.logic.handle_equal(self.state, val)
        self.result_display.insert(0, str(result))
        self.past_display.delete(0, tk.END)
        self.display.delete(0, tk.END)
