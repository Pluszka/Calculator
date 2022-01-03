import tkinter


def start():
    root = tkinter.Tk()
    root.geometry("450x450")
    root.config(bg='#333333')
    root.title('Calc'.center(80))  # nazwa okienka wyświetlana u góry
    return root


def screen():
    scr = [tkinter.Label(root, width=70,fg='#333333', bg='#F15156', text="test", anchor='w', borderwidth=15) for i in range(3)]
    for i in range(len(scr)):
        scr[i].grid(row=i, column=0, ipady=5, ipadx=1)
    return scr

def input():
    area=tkinter.Entry(root, bg='#D4F4DD', fg='#333333', borderwidth=0, highlightcolor='#333333', highlightbackground='#333333')
    area.grid(row=len(scr), column=0, ipady=15, ipadx=200)

    info = tkinter.Label(root, width=70, bg='#D4F4DD', fg='#333333', text="test", anchor='w', borderwidth=15)
    info.grid(row=len(scr)+1, column=0, ipady=5, ipadx=1)

    return area

if __name__ == '__main__':  # mówi py gdzie zaczynać (w main)
    root = start()
    scr = screen()
    dataarea = input()

    root.mainloop()
