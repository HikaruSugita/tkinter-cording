import tkinter as t
import time

window_width = 1000
window_height = 950

canvas_width = 950
canvas_height = 800

# co→ball: 跳ね返るボール
ball = {
    "X": 350, "y": 250,
    "dx": 5, "dy": 5,
    "r": 5 
}

def create_circre(field, x, y, r, **kwargs):
    return field.create_oval(x-r, y-r, x+r,y+r, **kwargs)

def main():
    window = t.Tk()
    window.geometry("%dx%d" % (window_width, window_height))

    #windowのタイトル
    window.title("GUI")    

    guzai = t.Label(window, text="Hello World!")
    guzai.place(x=0, y=0)

    field = t.Canvas(window, width=canvas_width, height=canvas_height, bg="black")
    field.place(x=(window_width-canvas_width)/2, y=(window_height-canvas_height)/2)

    window.mainloop()

if __name__ == "__main__":
    main()