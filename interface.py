from tkinter import messagebox
from tkinter import *


if __name__ == "__main__":
    
    root = Tk()

    # Interface
    def interface():
        root.title("Button 창")

        simpleButton = Button(root, text="버튼", command="")
        simpleButton.pack()

    # Button event

    # Message
    def message(m_title, m_mss):
        messagebox.showinfo(title=m_title, message=m_mss)

    #

    interface()


    root.mainloop()