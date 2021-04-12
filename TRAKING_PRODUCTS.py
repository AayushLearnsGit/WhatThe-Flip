import tkinter as tk
import tkinter.ttk as ttk
import Add_item
import get_conn


def showWelcome():
    root = tk.Tk()
    root.geometry('650x500')
    root.resizable(0,0)
    root.title('Status')

    def addProd():
        root.destroy()
        Add_item.call()

    def delProd():
        selected_item = tree.selection()[0]
        ID = tree.item(selected_item)['text']
        tree.delete(selected_item)

        qry = f'''DELETE FROM tracking WHERE ID = {ID}'''
        conn.execute(qry)
        conn.commit()


    tk.Label(root, text= "Welcome!", font= ('Consolas', 50, 'bold')).pack()
    tk.Label(root, text= "Currently Tracking", font= ('Consolas', 10, 'bold'), bg= '#ffd9ef').pack()
    tk.Button(root, text= "Track New", bg= "#24ff9c", font= ('Consolas', 10, 'bold'), command= addProd).pack()
    
    tree = ttk.Treeview(root, columns=('Name', 'Price', 'URL'))
    tree.heading('#0', text='ID')
    tree.heading('#1', text='Name')
    tree.heading('#2', text='Price')
    tree.heading('#3', text='URL')

    tree.column('#0', stretch=tk.YES)
    tree.column('#1', stretch=tk.YES)
    tree.column('#2', stretch=tk.YES)
    tree.column('#3', stretch=tk.YES)
    tree.pack()

    conn = get_conn.connect()
    results = conn.execute('''SELECT * FROM tracking''').fetchall()

    for row in results:
        tree.insert('', 'end', iid= None, text=row[0], values=(row[1], row[2], row[3]))

    tk.Button(root, text= "Delete Tracking", bg= "#c23e84", font= ('Consolas', 10, 'bold'), command= delProd).pack()    
    root.mainloop()

if __name__ == '__main__':
    showWelcome()