import tkinter as t
import time

window_width = 1400
window_height = 1000

def main():
    window = t.Tk()
    window.geometry("%dx%d" % (window_width, window_height))

    #windowのタイトル
    window.title("GUI")    

    guzai = t.Label(window, text="Hello World!")
    guzai.place(x=0, y=0)
    
    window.mainloop()

if __name__ == "__main__":
    main()