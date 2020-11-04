# importing the module
from tkinter import Tk,Text,Button
from englisttohindi.englisttohindi import EngtoHindi
import tkinter
def convert(message):
    res = EngtoHindi(message)
    output_text.configure(state="normal")
    output_text.delete("1.0", tkinter.END)
    output_text.insert(tkinter.END, res.convert)
    output_text.configure(state="disabled")

def translate_text(event):
    message = typing_space.get("1.0", tkinter.END)
    convert(message)

display = Tk()

w,h = display.winfo_screenwidth(), display.winfo_screenheight()
display.geometry("%dx%d" % (w,h))
display.title("Translator")
display.iconbitmap('translator.ico')
typing_space = Text(display, bg="#aaaaaa", fg="black", font=("Helvetica", 20))
output_text = Text(display, bg="#aaaaaa", fg="black", font=("Helvetica", 20), state="disabled")
typing_space.place(x="50" , y="20" , height="500", width="600")
output_text.place(x="700" , y="20" , height="500", width="600")
translate = Button(display, bg="#ff0000", fg="white", font=("Helvetica", 20), text="Translate")
translate.place(x=str((w/2)-150), y="600", height="50", width="300")
translate.bind("<Button-1>", translate_text)

display.mainloop()