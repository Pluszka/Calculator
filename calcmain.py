import tkinter

char=['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(', ')', '1', '2', '3', '-', 'x^2', '\u221A', '0',',', '%', '+']
DarkC ='#333333'
LightC = '#9EBD6E'
def start():
    root = tkinter.Tk()
    root.geometry("525x420")
    root.config(bg=DarkC)
    root.title('Calc'.center(100))  # nazwa okienka wyświetlana u góry
    return root


def screen():
    scr = [tkinter.Label(root, width=70,fg=LightC, bg=DarkC, text="test", anchor='w', borderwidth=15) for i in range(3)]
    for i in range(len(scr)):
        scr[i].grid(row=i, columnspan=6, ipady=5, ipadx=1)
    return scr

def input():
    area=tkinter.Entry(root, bg=LightC, fg=DarkC, borderwidth=0, highlightcolor='#333333', highlightbackground='#333333')
    area.grid(row=len(scr), columnspan=6, ipady=10, ipadx=200)

    info = tkinter.Label(root, width=70, bg=DarkC, fg=LightC, text="test", anchor='w', borderwidth=15)
    info.grid(row=len(scr)+1, columnspan=6, ipady=5, ipadx=1)

    return area, info

def click(char):

    def f():
        if char=='\u21BA':
            lastchar=dataarea.get()[:-1]
            dataarea.delete(0, tkinter.END)
            dataarea.insert(0, lastchar)
        elif char=='C':
            dataarea.delete(0, tkinter.END)
        else:
            if char=='x^2':
                dataarea.insert(tkinter.END, '^2')
            else:
                dataarea.insert(tkinter.END, char)



    return f



def buttons():
    button= [tkinter.Button(root, borderwidth=0, text=x, width=5, bg=DarkC, fg=LightC) for x in char]

    r=len(scr)+2 #wiersze

    for i in range(len(button)):
        if i%6==0:
            r+=1
        margin = 15 if len(char[i]) == 1 else 14
        button[i].grid(row= r, column=i%6,ipady=5, ipadx=margin)
        button[i].config(command=click(button[i]['text']))

    equal=tkinter.Button(root, borderwidth=0, text='=', width=5, bg=LightC, fg=DarkC)
    equal.grid(row=len(scr)+6, columnspan=2, column=4,ipady=5, ipadx=40 )

    return button, equal

if __name__ == '__main__':  # mówi py gdzie zaczynać (w main)
    root = start()
    scr = screen()
    dataarea, info = input()
    numpad=buttons()

    root.mainloop()
