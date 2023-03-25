import tkinter as tk
import math

root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

x1, y1 = 200, 100
x2, y2 = 300, 300
x3, y3 = 100, 300

triangle = canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='blue')

center_x = (x1 + x2 + x3) / 3
center_y = (y1 + y2 + y3) / 3
angle = 0


def rotate_triangle():
    global angle
    angle += 1
    radians = math.radians(angle)
    x1_new = center_x + (x1 - center_x) * math.cos(radians) - (y1 - center_y) * math.sin(radians)
    y1_new = center_y + (y1 - center_y) * math.cos(radians) + (x1 - center_x) * math.sin(radians)
    x2_new = center_x + (x2 - center_x) * math.cos(radians) - (y2 - center_y) * math.sin(radians)
    y2_new = center_y + (y2 - center_y) * math.cos(radians) + (x2 - center_x) * math.sin(radians)
    x3_new = center_x + (x3 - center_x) * math.cos(radians) - (y3 - center_y) * math.sin(radians)
    y3_new = center_y + (y3 - center_y) * math.cos(radians) + (x3 - center_x) * math.sin(radians)
    canvas.coords(triangle, x1_new, y1_new, x2_new, y2_new, x3_new, y3_new)
    canvas.after(int(1000/(angle+10)), rotate_triangle)


rotate_triangle()

root.mainloop()

