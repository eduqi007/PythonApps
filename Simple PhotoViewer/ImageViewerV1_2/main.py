import tkinter as tk
import core
from ui import ImageViewerUi

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerUi(root)
    root.mainloop()
    core