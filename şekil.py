import tkinter as tk
import random
import math
import time

# create a new Tkinter window
root = tk.Tk()
root.geometry("300x300")
root.config(bg="#262626")

# create a canvas to draw on
canvas = tk.Canvas(root, width=900, height=900,
                   bg="#262626", highlightbackground="#262626")
canvas.pack()

# define the colors to use for the pie slices
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
options = ["option1", "option2", "option3", "option4", "option5", "option6"]

# define the number of slices and the angle size of each slice
num_slices = len(options)
slice_angle = 360 / num_slices

# create the pie slices on the canvas
pie_slices = []
for i in range(num_slices):
    start_angle = i * slice_angle
    end_angle = (i + 1) * slice_angle
    slice_color = colors[i % len(colors)]
    pie_slice = canvas.create_arc(
        80, 150, 850, 850, start=start_angle, extent=slice_angle, fill=slice_color)
    pie_slices.append(pie_slice)

textler = []
# add text labels to the pie slices
for i, pie_slice in enumerate(pie_slices):
    # calculate the center coordinates of the pie slice
    bbox = canvas.bbox(pie_slice)
    x_center = (bbox[0] + bbox[2]) / 2
    y_center = (bbox[1] + bbox[3]) / 2
    # merkezi bulduk merkezden slice angel yönünde uzaklaşacak
    radian = math.radians(slice_angle)
    asılx = - math.sin((i-1)*radian)*130 + x_center
    asıly = - math.cos((i-1)*radian)*70 + y_center

    # choose the text label from the options list
    label = options[i]
    
    # create the text label on the canvas
    a =canvas.create_text(asılx, asıly, text=label,
                       font=("Arial", 20, "italic", "bold"), angle=(i-1)*slice_angle)
    textler.append(a)


# seçim okunu oluştur
x1 = 435
x2 = x1 + 50
x3 = 0.5*(x1+x2)

y1 = 130
y2 = y1
y3 = y1 + 50
canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="black")


def çevir():
    # dönecek açıyı belirle
    global angle
    angle -= 1
    for i in textler:
        canvas.delete(i)
    # her bir pie slice için renk değiştir
    for i, pie_slice in enumerate(pie_slices):
        

        # döndürme açısına göre yeni başlangıç ve bitiş açılarını hesapla
        start_angle = (i * slice_angle + angle) % 360
        end_angle = ((i + 1) * slice_angle + angle) % 360



        # pie slice'ı güncelle
        canvas.itemconfig(pie_slice, start=start_angle, extent=slice_angle)



    # bir sonraki dönüşü planla
    canvas.after(3, çevir)


# create a button to spin the wheel
spin_button = tk.Button(root, text="회전하다", bg="purple",
                        fg="white", font=("Arial", 15, "bold"), command=çevir)
spin_button.pack()


angle = 0
# start the Tkinter event loop
root.mainloop()
