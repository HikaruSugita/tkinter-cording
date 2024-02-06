import tkinter as t
import time

window_width = 1000
window_height = 950

field_width = 950
field_height = 700

# co→ball: 跳ね返るボール
ball = {
    "x": field_width/2, "y": field_height/2,
    "dx": 8.5, "dy": 8.5,
    "r": 40
}

def create_ball(field, x, y, r, **kwargs):
    return field.create_oval(x-r, y-r, x+r,y+r, **kwargs)

def move_ball(x, y, dx, dy, r):
    #仮の変数に移動後の値を記録
    _x = x + dx
    _y = y + dy
    #左右の壁に当たったか？
    if _x <= 0+r or field_width-r < _x:
        dx *= -1
    if _y <= 0+r or field_height-r < _y:
        dy *= -1

    return _x, _y, dx, dy

def main():
    window = t.Tk()
    window.geometry("%dx%d" % (window_width, window_height))

    #windowのタイトル
    window.title("GUI")    

    guzai = t.Label(window, text="ball bounds movie")
    guzai.place(x=0, y=0)

    field = t.Canvas(window, width=field_width, height=field_height, bg="black")
    field.place(x=(window_width-field_width)/2, y=(window_height-field_height)/2)

    while True:
        #Create a ball
        #circle=ball_p
        ball_p = create_ball(field, ball["x"], ball["y"], ball["r"], fill="light cyan")
        ball["x"], ball["y"], ball["dx"], ball["dy"] = move_ball(ball["x"], ball["y"], ball["dx"], ball["dy"], ball["r"])


        time.sleep(0.01)
        window.update()
        #canvas_delete=field_delete
        field.delete(ball_p)
    
    window.mainloop()

if __name__ == "__main__":
    main()