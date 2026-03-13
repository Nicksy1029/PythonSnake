import tkinter as tk

WIDTH = 400
HEIGHT = 400

root = tk.Tk()
root.title('Змейка | Счет: 0')
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width = WIDTH,
    height = HEIGHT,
    bg = 'black',
    highlightthickness = 0
)
canvas.pack()

root.mainloop()
