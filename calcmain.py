import tkinter
from math import sqrt

char=['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(', ')', '1', '2', '3', '-', 'x^2', '\u221A', '0',',', '%', '+']

MainC ='#333333'
SecondaryC = '#9EBD6E'

GrapeI='#BBCEA8'
GrapeII='#372549'

BabyI='#EBBAB9'
BabyII='#373F47'

MagicI='#564787'
MagicII='#DBCBD8'

OceanI="#2CA58D"
OceanII='#0A2342'

def start():
    root = tkinter.Tk()
    root.geometry("525x420")
    root.resizable(False, False)
    root.config(bg=MainC)
    root.title('Calc'.center(120))  # nazwa okienka wyświetlana u góry
    return root

def darkmode():
    global MainC
    global SecondaryC
    root.config(bg=MainC)
    [x.config(bg=MainC, fg=SecondaryC) for x in scr]
    dataarea.config(bg=SecondaryC, fg=MainC)
    info.config(bg=MainC, fg=SecondaryC)
    [x.config(bg=MainC, fg=SecondaryC) for x in button]
    equal.config(bg=SecondaryC, fg=MainC)

def grapemode():
    global GrapeI
    global GrapeII
    root.config(bg=GrapeI)
    [x.config(bg=GrapeI, fg=GrapeII) for x in scr]
    dataarea.config(bg=GrapeII, fg=GrapeI)
    info.config(bg=GrapeI, fg=GrapeII)
    [x.config(bg=GrapeI, fg=GrapeII) for x in button]
    equal.config(bg=GrapeII, fg=GrapeI)

def baby():
    global BabyI
    global BabyII
    root.config(bg=BabyI)
    [x.config(bg=BabyI, fg=BabyII) for x in scr]
    dataarea.config(bg=BabyII, fg=BabyI)
    info.config(bg=BabyI, fg=BabyII)
    [x.config(bg=BabyI, fg=BabyII) for x in button]
    equal.config(bg=BabyII, fg=BabyI)

def magic():
    global MagicI
    global MagicII
    root.config(bg=MagicI)
    [x.config(bg=MagicI, fg=MagicII) for x in scr]
    dataarea.config(bg=MagicII, fg=MagicI)
    info.config(bg=MagicI, fg=MagicII)
    [x.config(bg=MagicI, fg=MagicII) for x in button]
    equal.config(bg=MagicII, fg=MagicI)

def ocean():
    global OceanI
    global OceanII
    root.config(bg=OceanI)
    [x.config(bg=OceanI, fg=OceanII) for x in scr]
    dataarea.config(bg=OceanII, fg=OceanI)
    info.config(bg=OceanI, fg=OceanII)
    [x.config(bg=OceanI, fg=OceanII) for x in button]
    equal.config(bg=OceanII, fg=OceanI)

def menu():
    mainmenu=tkinter.Menu()
    root.config(menu=mainmenu)
    color= tkinter.Menu(mainmenu)
    mainmenu.add_cascade(label='Color Mode', menu=color)
    color.add_command(label='Dark', command=darkmode)
    color.add_command(label='Grape', command=grapemode)
    color.add_command(label='Baby Girl', command=baby)
    color.add_command(label='Magic', command=magic)
    color.add_command(label='Ocean', command=ocean)
    return mainmenu, color

def screen():
    scr = [tkinter.Label(root, width=70,fg=SecondaryC, bg=MainC, anchor='w', borderwidth=15) for i in range(3)]
    for i in range(len(scr)):
        scr[i].grid(row=i, columnspan=6, ipady=5, ipadx=1)
    return scr

def input():
    area=tkinter.Entry(root, bg=SecondaryC, fg=MainC, borderwidth=0, highlightcolor=MainC, highlightbackground=MainC)
    area.grid(row=len(scr), columnspan=6, ipady=10, ipadx=200)

    info = tkinter.Label(root, width=70, bg=MainC, fg=SecondaryC, anchor='w', borderwidth=15)
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

def calculate():

    def lastchar(line):
        i=1
        while line[-i]==')':
            i+=1
        return line[-i].isdigit()

    def toomuchop(line):
        for i in range(len(line)):
            if not line[i].isdigit() and not line[i+1].isdigit() and line[i+1]!='\u221A':
                return True
        return False

    def f():
        txt=dataarea.get()

        if not lastchar(txt) or toomuchop(txt):
            info['text']='Niepoprawnie zformuowane wyrażenie'
        else:
            info.config(text='')
            for i in range(1, len(scr)):
                if scr[i]['text']:
                    scr[i-1]['text']=scr[i]['text']
            if '^' in txt and '\u221A' in txt:
                place = txt.index('\u221A') + 1

                for num, char in enumerate(txt[place:]):
                    if not char.isdigit():
                        end = place + num
                        break
                    end = place + num + 1

                ntxt = txt.replace(txt[place:end], '')
                txtnew = ntxt.replace('\u221A', 'sqrt(int(txt[place:end]))')

                txtnew = txtnew.replace('^', '**')
                scr[-1]['text'] = txt + '=' + str(eval(txtnew))
            elif '^' in txt:
                txtnew=txt.replace('^','**')
                scr[-1]['text']=txt + '=' + str(eval(txtnew))
            elif '\u221A' in txt:
                place = txt.index('\u221A') + 1

                for num, char in enumerate(txt[place:]):
                    if not char.isdigit():
                        end = place + num + 1
                        break
                    end = place + num + 1

                ntxt = txt.replace(txt[place:end], '')
                txtnew= ntxt.replace('\u221A', 'sqrt(int(txt[place:end]))')
                scr[-1]['text'] = txt + '=' + str(eval(txtnew))
            else:
                scr[-1]['text'] = txt + '=' + str(eval(txt))

    return f

def buttons():
    button= [tkinter.Button(root, borderwidth=0, text=x, width=5, bg=MainC, fg=SecondaryC) for x in char]

    r=len(scr)+2 #wiersze

    for i in range(len(button)):
        if i%6==0:
            r+=1
        margin = 15 if len(char[i]) == 1 else 14
        button[i].grid(row= r, column=i%6,ipady=5, ipadx=margin)
        button[i].config(command=click(button[i]['text']))

    equal=tkinter.Button(root, borderwidth=0, text='=', width=5, bg=SecondaryC, fg=MainC)
    equal.grid(row=len(scr)+6, columnspan=2, column=4,ipady=5, ipadx=40 )
    equal.config(command=calculate())

    return button, equal

if __name__ == '__main__':  # mówi py gdzie zaczynać (w main)
    root = start()
    mainmenu = menu()
    scr = screen()
    dataarea, info = input()
    button, equal=buttons()

    root.mainloop()
