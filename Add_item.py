import tkinter as tk
from tkinter import messagebox
from Tracker import checkfor_this
import get_conn
import Welcome


def call():
    root = tk.Tk()
    root.geometry('550x350')
    root.resizable(0,0)
    root.title('Track New')

    def trackProd():
        global prod, url
        conn = get_conn.connect()
        q = f'''INSERT INTO tracking VALUES(NULL, '{prod.title}', {prod.last_price}, '{url}')'''
        conn.execute(q)
        conn.commit()
        messagebox.showinfo("Done!", "The item has been added into tracking successfully!")
        root.destroy()
        Welcome.showWelcome()

    def check():
        global prod, url
        url = txt.get()
        prod = checkfor_this(url)
        tk.Label(root, text= "Current Price", font= ('Consolas', 30, 'bold')).pack()
        tk.Label(root, text= "___").pack()
        tk.Label(root, text= "₹ " + str(prod.last_price), font= ('Consolas', 60, 'bold')).pack()

        trackbt.destroy()
        tk.Button(root, text= "Track!", bg= "#24ff9c", font= ('Consolas', 20, 'bold'), command= trackProd).pack()

    tk.Label(root, text= "Add URL", font= ('Consolas', 30, 'bold')).pack()
    txt = tk.Entry(root, width= 100, font= ('Consolas', 20))
    txt.pack()

    trackbt = tk.Button(root, text= "Check", bg= "#24ff9c", font= ('Consolas', 10, 'bold'), command= check)
    trackbt.pack()
    root.mainloop()

if __name__ == '__main__':
    print("Use call() to make it run here, and use some URL to run this module.")
