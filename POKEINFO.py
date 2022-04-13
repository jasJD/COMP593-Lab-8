from tkinter import *
from tkinter import ttk


def main():
    
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap("Poke-Ball1.ico")
    root.geometry('400x400')




    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2)

    frm_user_input = ttk.LabelFrame(root, text='Info')
    frm_user_input.grid(row=1, column=0)

    frm_user_input = ttk.LabelFrame(root, text='Stats')
    frm_user_input.grid(row=0, column=1)

    lbl_name = ttk.Label(frm_user_input, text='Pokemon Name:')
    lbl_name.grid(column=0)

    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(column=1)




    


    root.mainloop()




main()
