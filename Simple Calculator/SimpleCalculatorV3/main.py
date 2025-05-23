import tkinter as tk
from state import CalculatorState
import core
from ui import CalculatorUI

if __name__ == "__main__":
    root = tk.Tk()
    state = CalculatorState()
    app = CalculatorUI(root, state, core)
    root.mainloop()
