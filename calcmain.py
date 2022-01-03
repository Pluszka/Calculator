import tkinter

char=['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(', ')', '1', '2', '3', '-', 'x^2', '\u221A', '0',',', '%', '+']

def start():
    root = tkinter.Tk()
    root.geometry("480x440")
    root.config(bg='#333333')
    root.title('Calc'.center(90))  # nazwa okienka wyświetlana u góry
    return root


def screen():
    scr = [tkinter.Label(root, width=70,fg='#333333', bg='#9EBD6E', text="test", anchor='w', borderwidth=15) for i in range(3)]
    for i in range(len(scr)):
        scr[i].grid(row=i, columnspan=6, ipady=5, ipadx=1)
    return scr

def input():
    area=tkinter.Entry(root, bg='#C9DAEA', fg='#333333', borderwidth=0, highlightcolor='#333333', highlightbackground='#333333')
    area.grid(row=len(scr), columnspan=6, ipady=10, ipadx=200)

    info = tkinter.Label(root, width=70, bg='#C9DAEA', fg='#333333', text="test", anchor='w', borderwidth=15)
    info.grid(row=len(scr)+1, columnspan=6, ipady=5, ipadx=1)

    return area

def buttons():
    button= [tkinter.Button(root, text=x) for x in char]

    r=len(scr)+2 #wiersze

    for i in range(len(button)):
        if i%6==0:
            r+=1
        margin = 5 if len(char[1]) == 1 else 1
        button[i].grid(row= r, column=i%6,ipady=5, ipadx=margin)
    return button

if __name__ == '__main__':  # mówi py gdzie zaczynać (w main)
    root = start()
    scr = screen()
    dataarea = input()
    numpad=buttons()

    root.mainloop()
