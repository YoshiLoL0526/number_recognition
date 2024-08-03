from tkinter import *
from main import NN
from PIL import ImageGrab
import numpy as np
import torch
import matplotlib.pyplot as plt


class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.clean_button = Button(self.root, text='Clean', command=self.clean)
        self.clean_button.grid(row=0, column=2)

        self.predict_button = Button(self.root, text='Predecir', command=self.predict)
        self.predict_button.grid(row=0, column=3)

        self.label = Label(self.root, text='None')
        self.label.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 100  # self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = 100  # self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def clean(self):
        self.c.create_rectangle(0, 0, 800, 800, fill='white')
        self.label['text'] = 'None'

    def predict(self):
        self.root.update()
        x = self.c.winfo_rootx()
        y = self.c.winfo_rooty()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()
        array = torch.tensor(
            1 - np.array(ImageGrab.grab((x, y, x1, y1)).resize((28, 28)).convert(mode='L', dither=1)) / 255,
            dtype=torch.float)
        prediction = net.model(array)

        self.label['text'] = str(torch.argmax(prediction).item())

        plt.imshow(array, cmap=plt.cm.gray_r, interpolation="nearest")
        plt.show()


if __name__ == '__main__':
    net = NN()
    net.load_weights('./weights')

    Paint()
