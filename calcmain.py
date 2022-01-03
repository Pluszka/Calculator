import tkinter
def start():
    root=tkinter.Tk()
    root.geometry("450x450")
    root.title('Calc') #nazwa okienka wyświetlana u góry
    return root

if __name__=='__main__': #mówi py gdzie zaczynać (w main)
    root = start()

    root.mainloop()