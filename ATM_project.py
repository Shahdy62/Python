'''
/************************************/
/*  Author : Shahd Mahmoud          */
/*  Description : ATM system        */
/*  Date : 30/12/2021               */
/*  Version :3.8                    */
/************************************/
'''
import tkinter
import os
import json
clients = {
    '215321701332': {
        'name': 'Ahmed Abdelrazek Mohamed',
        'password': '1783',
        'balance': 3500166,
    },
    '203659302214': {
        'name': 'Salma Mohamed Foaad',
        'password': '1390',
        'balance': 520001,
    },
    '126355700193': {
        'name': 'Adel Khaled Abdelrahman',
        'password': '1214',
        'balance': 111000,
    },
    '201455998011': {
        'name': 'Saeed Amin Elsawy',
        'password': '2001',
        'balance': 1200,
    },
    '201122369851': {
        'name': 'Amir Salama Elgendy',
        'password': '8935',
        'balance': 178933,
    },
    '201356788002': {
        'name': 'Wael Mohamed khairy',
        'password': '3420',
        'balance': 55000,
    },
    '203366789564': {
        'name': 'Mina Sameh Bishoy',
        'password': '1179',
        'balance': 18000,
    },
    '201236787812': {
        'name': 'Omnia Ahmed Awad',
        'password': '1430',
        'balance': 180350,
    },
}
file=open('system_file.txt','r')
file_size=os.path.getsize('system_file.txt')
if file_size>0:
    y=file.read()
    clients=json.loads(y)
users = clients.keys()
count=0 
def check_cash ():
    global cash_entry
    cash_value=cash_entry.get()
    global ID_entry
    user_Id=ID_entry.get()
    print("cash value = ",cash_value)
    cash_value = int(cash_value)
    if cash_value<5000 and cash_value%100==0 and cash_value<clients[user_Id]['balance']:
        user_balance=clients[user_Id]['balance']
        new_balance=user_balance-cash_value
        clients[user_Id]['balance']=new_balance
        old_balance = {user_Id:user_balance}
        msg_window = tkinter.Toplevel()
        msg_window.geometry("300x100+100+100")
        msg_window.configure(background = "purple")
        lab = tkinter.Label(msg_window, text = "Successful procedure ")
        lab.pack()
        print("old balance = ",old_balance[user_Id])
        print("new balance = ",clients[user_Id]['balance'])
        msg_window.mainloop()
    else:
        msg_window = tkinter.Toplevel()
        msg_window.geometry("300x100+100+100")
        msg_window.configure(background = "purple")
        lab = tkinter.Label(msg_window, text = "Sorry, The amount of money is unavaliable ")
        lab.pack()
        msg_window.mainloop() 
def cash_withdraw ():
    global cash_entry
    # ID entry&label
    cash_entry = tkinter.Entry (user_window, text = 'cash withdraw',width =20)
    cash_entry.place(x=160,y=85)
    Enter_button = tkinter.Button(user_window, text='Enter', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = check_cash)
    Enter_button.place(x=300,y=85)
def Restart():
    user_window.destroy()
    file=open('system_file.txt','w')
    file.write(json.dumps(clients))
    file.close()
    os.startfile("ATM_project.py")
    
def Close():
    user_window.destroy()
    file=open('system_file.txt','w')
    file.write(json.dumps(clients))
    file.close()
def balance_Inquiry():
    global ID_entry
    user_Id=ID_entry.get()
    user_balance=clients[user_Id]['balance']
    user_name=clients[user_Id]['name']
    user_balance=str(user_balance)
    ok_button = tkinter.Button(user_window, text='OK', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = Restart)
    ok_button.place(x=150,y=120) 
    msg_window = tkinter.Toplevel()
    msg_window.geometry("400x200+100+100")
    msg_window.configure(background = "purple")
    lab = tkinter.Label(msg_window, text = "The user name is : "
                        +user_name+"\n"+"The user balance is : "+user_balance)
    lab.pack()
    msg_window.mainloop()
    
def check_password():
    global ID_entry
    user_Id=ID_entry.get()
    global change_entry1
    global change_entry2 
    password1=change_entry1.get()
    password2=change_entry2.get()
    length=len(password1)
    if password1==password2 and length==4:
        old_pass={user_Id:clients[user_Id]['password']}
        clients[user_Id]['password']=password1
        msg_window = tkinter.Toplevel()
        msg_window.geometry("400x100+100+100")
        msg_window.configure(background = "purple")
        lab = tkinter.Label(msg_window, text = "Successful procedure, Please log in again")
        lab.pack()
        print("old password = ",old_pass[user_Id])
        print("new password = ",clients[user_Id]['password'])
        msg_window.after(2000,lambda:msg_window.destroy())
        user_window.after(2000,lambda:Restart())
        msg_window.mainloop()
    else:
        msg_window = tkinter.Toplevel()
        msg_window.geometry("200x100+100+100")
        msg_window.configure(background = "purple")
        lab = tkinter.Label(msg_window, text = "Invalid Password")
        lab.pack()
        msg_window.mainloop() 
        
        
def change_password():
    global change_entry1
    global change_entry2
    
    #change1 label&entry
    L1 = tkinter.Label(user_window,text="New Password",
                   background = "grey")
    L1.place(x=160,y=160)
    
    change_entry1 = tkinter.Entry (user_window, text = 'change password',width =20)
    change_entry1.place(x=270,y=160)
    
    #change2 label&entry
    L2 = tkinter.Label(user_window,text="Confirm Password",
                   background = "grey")
    L2.place(x=160,y=200)
    
    change_entry2 = tkinter.Entry (user_window, text = 'confirm password',width =20)
    change_entry2.place(x=270,y=200)
   
    #confirm button
    confirm_button = tkinter.Button(user_window, text='Confirm', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = check_password)
    confirm_button.place(x=400,y=180)
    
def check_recharge ():
    global ID_entry
    user_Id=ID_entry.get()
    global recharge_entry
    user_recharge=recharge_entry.get()
    user_recharge=int(user_recharge)
    client_account=clients[user_Id]['balance']
    if user_recharge<client_account:
        new_balance=client_account-user_recharge
        clients[user_Id]['balance']=new_balance
        old_balance={user_Id:client_account}
        print("old balance = ",old_balance[user_Id])
        print("new balance = ",clients[user_Id]['balance'])
        msg_window = tkinter.Toplevel()
        msg_window.geometry("300x100+100+100")
        msg_window.configure(background = "purple")
        lab = tkinter.Label(msg_window, text = "Successfukl procedure")
        lab.pack()
        msg_window.mainloop()
    else:
        msg_window = tkinter.Toplevel()
        msg_window.geometry("300x100+100+100")
        msg_window.configure(background = "purple")
        lab = tkinter.Label(msg_window, text = "Sorry, can't perform this procedure")
        lab.pack()
        msg_window.mainloop()
    
def fawry():    
    global phone_entry
    global recharge_entry
    #phone number label&entry
    L1 = tkinter.Label(user_window,text="Phone Number",
                   background = "grey")
    L1.place(x=200,y=230)
    
    phone_entry = tkinter.Entry (user_window, text = 'phone number',width =20)
    phone_entry.place(x=200,y=250) 
    #Amount of money label&entry
    L2 = tkinter.Label(user_window,text="Amount of recharge",
                   background = "grey")
    L2.place(x=200,y=270)
    
    recharge_entry = tkinter.Entry (user_window, text = 'recharge amount',width =20)
    recharge_entry.place(x=200,y=290) 
    #recharge button
    recharge_button = tkinter.Button(user_window, text='Recharge', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = check_recharge)
    recharge_button.place(x=350,y=260)
    
def security_check():
    def Reset ():
             msg_window.destroy()
             pass_entry.delete(0, 'end')
    global count
    global ID_entry
    user_Id = ID_entry.get()
    global pass_entry
    user_password=pass_entry.get()
    print("Entered password = ",user_password)
    if count<3:
        if user_password == clients[user_Id]['password']:
            welcome_window = tkinter.Toplevel()
            welcome_window.geometry("300x100+100+100")
            welcome_window.configure(background = "purple")
            lab = tkinter.Label(welcome_window, text = "Welcme, "+clients[user_Id]['name'])
            lab.pack()
            with_button = tkinter.Button(user_window, text='Cash Withdraw', width=20, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = cash_withdraw)
            with_button.place(x=0,y=80)
            bal_button = tkinter.Button(user_window, text='Balance Inquiry', width=20, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = balance_Inquiry)
            bal_button.place(x=0,y=120) 
            change_button = tkinter.Button(user_window, text='Change Password', width=20, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = change_password)
            change_button.place(x=0,y=160)
            L1 = tkinter.Label(user_window,text="Fawry Service",
                   background = "grey")
            L1.place(x=0,y=210)
            orange_button = tkinter.Button(user_window, text='Orange Recharge',
                              width=20, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = fawry)
            orange_button.place(x=0,y=230)
            etisalat_button = tkinter.Button(user_window, text='Etisalat Recharge',
                              width=20, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = fawry)
            etisalat_button.place(x=0,y=260)
            vodafone_button = tkinter.Button(user_window, text='Vodafone Recharge',
                              width=20, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = fawry)
            vodafone_button.place(x=0,y=290)
            we_button = tkinter.Button(user_window, text='We Recharge',
                              width=20, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = fawry)
            we_button.place(x=0,y=320)
            welcome_window.mainloop()
        else :
            count +=1
            msg_window = tkinter.Toplevel()
            msg_window.geometry("300x100+100+100")
            msg_window.configure(background = "purple")
            lab = tkinter.Label(msg_window, text = "Sorry, Invalid Entry. Please try again")
            Reset_button = tkinter.Button(msg_window, text='Reset', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = Reset)
            Reset_button.place(x=100,y=50)
            lab.pack()
            msg_window.mainloop() 
            
    else :
       msg_window = tkinter.Toplevel()
       msg_window.geometry("300x100+100+100")
       msg_window.configure(background = "purple")
       lab = tkinter.Label(msg_window, text = "Sorry, You ran out of tring times")
       lab.pack()
       msg_window.after(2000,lambda:msg_window.destroy())
       user_window.after(2000,lambda:user_window.destroy())
       msg_window.mainloop()
       
       
       
        
        
        
def check_ID ():
    global ID_entry
    user_Id = ID_entry.get()
    global pass_entry
    
    
          
    def Reset ():
             msg_window.destroy()
             ID_entry.delete(0, 'end')
    
    print("Entered ID : ",user_Id)
    if user_Id in users:
        # Pass word entry&label
        L1 = tkinter.Label(user_window,text="Pass word",
                   background = "grey")
        L1.place(x=0,y=50)
        pass_entry = tkinter.Entry (user_window, text = 'User Name',width =20,show="*")
        pass_entry.place(x=100,y=50)
        
        #The login button
        login_button = tkinter.Button(user_window, text='Login', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = security_check)
        login_button.place(x=300,y=45)
        
        
        
        
    else:
        msg_window = tkinter.Toplevel()
        msg_window.geometry("300x200+100+100")
        msg_window.configure(background = "purple")
        lab = tkinter.Label(msg_window, text = "Sorry, This ID is incorrect, Please try again")
        lab.pack()
        Reset_button = tkinter.Button(msg_window, text='Reset', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = Reset)
        Reset_button.place(x=100,y=50)
        msg_window.mainloop()




#The main window
user_window = tkinter.Tk()
user_window.title("User Interface")
user_window.geometry("500x500+100+100")
user_window.configure(background = "light blue")

#Declaring entry variables
ID_entry=tkinter.StringVar()
pass_entry=tkinter.StringVar()
cash_entry=tkinter.IntVar()
change_entry1=tkinter.StringVar()
change_entry2=tkinter.StringVar()
phone_entry=tkinter.StringVar()
recharge_entry=tkinter.StringVar()

# ID entry&label
L1 = tkinter.Label(user_window,text="Account Number",
                   background = "grey")
L1.place(x=0,y=0)
ID_entry = tkinter.Entry (user_window, text = 'Enter ID',width =20)
ID_entry.place(x=100,y=1)

#ID button
Enter_button = tkinter.Button(user_window, text='Enter', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = check_ID)
Enter_button.place(x=300,y=0)
Close_button = tkinter.Button(user_window, text='Close', width=10, height = 1,
                              activebackground="dark green",
                              activeforeground="light green",
                              bg="light green",
                              command = Close)
Close_button.place(x=200,y=350)
user_window.mainloop()
    
