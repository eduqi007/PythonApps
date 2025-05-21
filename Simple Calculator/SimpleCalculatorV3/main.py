from tkinter import Tk
from state import CalculatorState
import core
from ui import CalculatorUI

def main():
    root = Tk()
    root.title("Simple Calculator - V3")
    setup_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
