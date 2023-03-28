import tkinter as tk
import math
import tkinter.simpledialog as simpledialog
import time


# Customize your options here
#options = ["밥 많이 먹기", "세인이랑 비밀!!", "게임하기", "공부하기", "세인이랑 놀기","운동하기","일하기","씻기","아케노 코스플레이"]

def get_user_options():
    user_options = simpledialog.askstring("Options", "Please enter the options separated by commas:")
    return [option.strip() for option in user_options.split(",")]
    # 옵션을 쉼표로 구분하여 입력하십시오
    # Lütfen seçenekleri virgülle ayırarak girin:

class DecisionWheel(tk.Canvas):
    def __init__(self, master, options, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.options = options
        self.angle = 2 * math.pi / len(options)
        self.rotation = 0
        self.is_spinning = False
        self.configure(bg="#262626",highlightbackground="#262626")
        self.draw_wheel()

    def draw_wheel(self):
        for i, option in enumerate(self.options):
            angle_start = i * self.angle + self.rotation
            angle_end = (i + 1) * self.angle + self.rotation

            x1 = 80
            y1 = 150
            x2 = 850
            y2 = 850

            self.create_arc(x1, y1, x2, y2, start=math.degrees(angle_start), extent=math.degrees(self.angle),
                            outline="black", fill=self.get_color(i), width=2)

        for i, option in enumerate(self.options):
            angle_start = i * self.angle + self.rotation
            angle_end = (i + 1) * self.angle + self.rotation

            x1 = 80
            y1 = 150
            x2 = 850
            y2 = 850

            text_angle = (angle_start + angle_end) / 2
            text_x = 0.5 * (x1 + x2) + (x2 - x1) * 0.35 * math.cos(text_angle - math.pi / 2)
            text_y = 0.5 * (y1 + y2) + (y2 - y1) * 0.35 * math.sin(text_angle - math.pi / 2)
            self.create_text(text_x, text_y, text=option, font=("Arial", 18,"bold"), fill="white")
            
        # seçim okunu oluştur
        x1 = 435
        x2 = x1 + 50
        x3 = 0.5*(x1+x2)

        y1 = 130
        y2 = y1
        y3 = y1 + 50
        self.create_polygon(x1, y1, x2, y2, x3, y3, fill="white")


    def spin(self, acceleration=0.01, deceleration=0.965, max_speed=4, duration=21):
        if self.is_spinning:
            return

        self.is_spinning = True
        speed = 0
        end_time = time.time() + duration
        accelerating = True

        while time.time() < end_time:
            if accelerating:
                speed += acceleration
                if speed >= max_speed:
                    speed = max_speed
                    accelerating = False
            else:
                speed *= deceleration

            if speed < 0.01:
                break

            self.rotation += speed
            self.rotation %= 2 * math.pi
            self.delete("all")
            self.draw_wheel()
            self.update()

        self.is_spinning = False


    def get_color(self, index):
        colors = ["red", "blue", "green", "orange", "purple", "cyan", "magenta"]
        return colors[index % len(colors)]

def main():
    root = tk.Tk()
    root.title("The Decision Wheel?")
    root.geometry("900x900")
    root.config(bg="#272727")


    options = get_user_options()


    wheel = DecisionWheel(root, options)
    wheel.pack(fill=tk.BOTH, expand=True)

    spin_button = tk.Button(root, text="Çevir!", command=wheel.spin)
    spin_button.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
