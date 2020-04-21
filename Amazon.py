from socket import *
import tkinter as tk
import tkinter.messagebox
import pickle
import pymysql
import json

# phpmyadmin database connection
db = pymysql.connect("127.0.0.1", "root", "", "amazon")


class Application(tk.Frame):
    def __init__(self, widget):
        tk.Frame.__init__(self, widget)
        self.createWidgets()

    # Display Order Function
    def selectOrder(self):
        self.window2 = tk.Tk()
        self.window2.title('Received Order')
        self.window2.geometry('900x900')
        self.window2.configure(background='white')

        # Select new order
        cursor = db.cursor()
        cursor.execute("SELECT * from `order`")
        results = cursor.fetchall()
        tk.Button(self.window2, text='send', command=self.sendOrder, width=30).pack(anchor="ne")
        # Order information sorting
        for order in results:
            tk.Label(self.window2, text="--  order id: " + str(order[0]) + "    --  product id: " + str(
                order[1]) + "   --  product name: " + str(order[2])
                                        + "    --  product detail: " + str(order[3]) + "    --  quantity: " + str(
                order[4]) + "\n" + "--  address: " + str(order[5])
                                        + "    --  client_name: " + str(order[6]) + "    --  phone number: " + str(
                order[7]) + "    --  weight in kg: " + str(order[8])
                                        + "\n" + "--  the order date: " + str(
                order[9]) + "    --  special requirement: " + str(order[10]), bg='white', font=('Arial', 10)).pack(
                anchor="nw")

    # Send order function
    def sendOrder(self):
        cursor = db.cursor()
        cursor.execute(
            "SELECT Json_object('order_id', order_id, 'product_id', product_id, 'product_name', product_name, "
            "'product_detail', product_detail, 'quantity', quantity, 'address', address, 'client_name', client_name, "
            "'phone_no', phone_no, 'weight_kg',weight_kg, 'date_time', date_time, 'special_req', special_req) from "
            "amazon.`order`;")
        jsStr = cursor.fetchall()
        # Transmit order in bytes
        sendMessage = bytes(json.dumps(jsStr) + "\n", encoding='utf8')
        clientSocket.send(sendMessage)

    # Colleague Display
    def colleague(self):
        window3 = tk.Tk()
        window3.title('Colleague')
        window3.geometry('800x350')
        window3.configure(background='white')
        tk.Label(window3, justify='left', text='Alex Au', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='alexau@gmail.com', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='Tel: 6292 1234', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='Brian Bon', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='brianbon@gmail.com', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='Tel: 6292 4321', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='Carl Clid', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='carlclid@gmail.com', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='Tel: 6292 6666', bg='white', font=('Arial', 14)).pack()
        tk.Label(window3, text='', bg='white', font=('Arial', 14)).pack()
        window3.mainloop()

    # Login checking
    def usr_login(self):
        self.usr_name = self.var_usr_name.get()
        self.usr_pwd = self.var_usr_pwd.get()
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                self.usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as usr_file:
                self.usrs_info = {'admin': 'admin'}
                pickle.dump(self.usrs_info, usr_file)
        if self.usr_name in self.usrs_info:
            if self.usr_pwd == self.usrs_info[self.usr_name]:

                self.window1 = tk.Tk()
                self.window1.title('Welcome Amazon ' + self.usr_name)
                self.window1.geometry('800x800')
                self.window1.configure(background='white')
                tk.Label(self.window1, text="Welcome to Amazon Backstage!", bg='white', font=('Arial', 30)).pack()

                menubar = tk.Menu(self.window1)
                filemenu = tk.Menu(menubar, tearoff=0)
                menubar.add_cascade(label='Work', menu=filemenu)
                filemenu.add_command(label='Data', command=self.selectOrder)
                filemenu.add_separator()
                filemenu.add_command(label='Logout', command=self.window1.quit)

                editmenu = tk.Menu(menubar, tearoff=0)
                menubar.add_cascade(label='Contact', menu=editmenu)
                editmenu.add_command(label='Colleague', command=self.colleague)

                self.window1.config(menu=menubar)
            else:
                tk.messagebox.showerror('ERROR', message='Error, your password is wrong, try again.')
        else:
            tk.messagebox.showerror(message='Error, invalid user')

    # Main Admin Login window
    def createWidgets(self):
        self.window = tk.Tk()
        self.window.title('Amazon Login')
        self.window.geometry('800x350')
        self.window.configure(background='white')

        tk.Label(self.window, text='User name: ', bg='orange').place(x=50, y=200)
        tk.Label(self.window, text='Password: ', bg='orange').place(x=50, y=240)

        self.var_usr_name = tk.StringVar()
        self.var_usr_name.set('admin')
        self.entry_usr_name = tk.Entry(self.window, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=160, y=200)
        self.var_usr_pwd = tk.StringVar()
        self.var_usr_pwd.set('admin')
        self.entry_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, show='*')
        self.entry_usr_pwd.place(x=160, y=240)
        btn_login = tk.Button(self.window, text='Login', command=self.usr_login, bg='orange')
        btn_login.place(x=170, y=280)

# python socket client connect server
servername = 'localhost'
serverport = 12000
try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
except:
    tk.messagebox.showinfo('unknown error', 'please check the address！')

clientSocket.connect((servername, serverport))
root = tk.Tk()
root.geometry('0x0')

app = Application(widget=root)
app.mainloop()
