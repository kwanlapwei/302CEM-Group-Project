from socket import *
import tkinter as tk
import tkinter.messagebox
import pickle
import json


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.createWidgets()

    # Display Order Function
    def orderDisplay(self):
        self.window2 = tk.Tk()
        self.window2.title('Preprocessed Order Information')
        self.window2.geometry('600x900')
        self.window2.configure(background='white')

        # bytes-data receive
        data = connectionSocket.recv(400000)
        data = data.decode("utf-8")
        # transform bytes-data into Json string
        jsStr = json.loads(data)
        orderAmount = len(jsStr)
        # Order information sorting
        for split in range(0, orderAmount):
            orderDict = eval(jsStr[split][0])
            print(orderDict)
            for key, value in eval(jsStr[split][0]).items():
                if key == 'order_id':
                    tk.Label(self.window2, text="order id: " + str(value), bg='white',
                             font=('Arial', 10)).place(
                        x=split * 200, y=10)
                if key == 'product_id':
                    tk.Label(self.window2, text="product id: " + str(value), bg='white',
                             font=('Arial', 10)).place(
                        x=split * 200, y=40)
                if key == 'product_name':
                    tk.Label(self.window2, text="product name: " + str(value), bg='white',
                             font=('Arial', 10)).place(
                        x=split * 200, y=70)
                if key == 'product_detail':
                    tk.Label(self.window2, text="product detail: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=100)
                if key == 'quantity':
                    tk.Label(self.window2, text="quantity: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=130)
                if key == 'address':
                    tk.Label(self.window2, text="address: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=160)
                if key == 'client_name':
                    tk.Label(self.window2, text="client name: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=190)
                if key == 'phone_no':
                    tk.Label(self.window2, text="phone number: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=220)
                if key == 'weight_kg':
                    tk.Label(self.window2, text="weight in kg: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=250)
                if key == 'date_time':
                    tk.Label(self.window2, text="order time: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=280)
                if key == 'special_req':
                    tk.Label(self.window2, text="special requirement: " + str(value), bg='white',
                             font=('Arial', 10)).place(x=split * 200, y=310)
    # Colleague Display
    def colleague(self):
        window3 = tk.Tk()
        window3.title('Amazon Login')
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
                self.window1.title('Welcome dhl ' + self.usr_name)
                self.window1.geometry('800x800')
                self.window1.configure(background='white')
                tk.Label(self.window1, text="Welcome to DHL Backstage!", bg='white', font=('Arial', 30)).pack()

                menubar = tk.Menu(self.window1)
                filemenu = tk.Menu(menubar, tearoff=0)
                menubar.add_cascade(label='Work', menu=filemenu)
                filemenu.add_command(label='Data', command=self.orderDisplay)
                filemenu.add_separator()
                filemenu.add_command(label='Logout', command=self.window1.quit)

                editmenu = tk.Menu(menubar, tearoff=0)
                menubar.add_cascade(label='Contact', menu=editmenu)
                editmenu.add_command(label='Colleague', command=self.colleague)

                self.window1.config(menu=menubar)
            else:
                tk.messagebox.showerror('ERROR', message='Error, your password is wrong, try again.')
        else:
            tk.messagebox.showerror(message='Error, invaild user')

    # Main Admin Login window
    def createWidgets(self):
        self.window = tk.Tk()
        self.window.title('DHL Login')
        self.window.geometry('800x350')
        self.window.configure(background='white')
        tk.Label(self.window, text='User name: ', bg='gold').place(x=50, y=200)
        tk.Label(self.window, text='Password: ', bg='gold').place(x=50, y=240)

        self.var_usr_name = tk.StringVar()
        self.var_usr_name.set('admin')
        self.entry_usr_name = tk.Entry(self.window, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=160, y=200)
        self.var_usr_pwd = tk.StringVar()
        self.var_usr_pwd.set('admin')
        self.entry_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, show='*')
        self.entry_usr_pwd.place(x=160, y=240)

        btn_login = tk.Button(self.window, text='Login', command=self.usr_login, bg='gold')
        btn_login.place(x=170, y=260)

# python socket open server
root = tk.Tk()
root.geometry('0x0')
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('Waiting for Connection....')
connectionSocket, addr = serverSocket.accept()
print('One Connection succeed')

app = Application(master=root)
app.mainloop()
