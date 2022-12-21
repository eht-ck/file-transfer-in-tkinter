from tkinter import *
import socket
from tkinter import ttk

from tkinter import filedialog, messagebox
import os

root=Tk()
root.title("File Transfer")
root.configure(bg="#f4fdfe")
root.geometry("502x520")
root.resizable(True,True)

def Send():
    window=Toplevel(root)
    window.title("SEND")
    window.configure(bg="#f4fdfe")
    window.geometry("450x560")
    window.resizable(True,True)


    def select_file():
        global filename
        filename=filedialog.askopenfile(initialdir=os.getcwd(), title='Select file', filetype=(('file_type','*.txt'),('all files','*.*')))
    
    def send_file():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("Waiting for any incoming connections.......")
        conn, addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitter successfully")

    image_icon_1=PhotoImage(file="images/send.png")
    window.iconphoto(False,image_icon_1)
    bg_1=PhotoImage(file="images/pg.png")
    Label(window,image=bg_1).place(x=-2,y=0)
    host=socket.gethostname()
    Label(window,text=f'ID: {host}',bg='white',fg='black').place(x=140,y=209)

    Button(window,text="+Select file", width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND", width=8,height=1,font='arial 14 bold',bg="#000",fg="#fff",command=send_file).place(x=300,y=150)
    window.mainloop()
def Receive():
    window=Toplevel(root)
    window.title("RECEIVE")
    window.configure(bg="#f4fdfe")
    window.geometry("450x560")
    window.resizable(True,True)

    def getFile():
        ID=SenderId.get()
        Fname=IncomingFile.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(Fname,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("FILE HAS BEEN RECEIVED SUCCESSFULLY")
        

    Label(window,text="RECEIVE", font=("arial,20"), bg="#f4fdfe").place(x=100,y=280)
    Label(window,text="Input sender ID: ", font=("arial,20"), bg="#f4fdfe").place(x=20,y=340)
    SenderId=Entry(window,width=25,fg="black",border=2,bg="white",font=("arial",15))
    SenderId.place(x=20,y=370)
    SenderId.focus()

    Label(window,text="Filename of the incoming fil: ", font=("arial,20"), bg="#f4fdfe").place(x=20,y=420)
    IncomingFile=Entry(window,width=25,fg="black",border=2,bg="white",font=("arial",15))
    IncomingFile.place(x=20,y=450)

    rr=Button(window,text="RECEIVE",command=getFile)
    rr.place(x=20,y=500)

    image_icon_1=PhotoImage(file="images/receive.png")
    window.iconphoto(False,image_icon_1)
    window.mainloop()

image_icon=PhotoImage(file="images/i.png")
root.iconphoto(False,image_icon)
Label(root,text="File Transfer",font=('Acumin Varibale Concept',20,'bold'), bg="#f4fdfe").place(x=120,y=30)

send_image=PhotoImage(file="images/send.png")
receive_image=PhotoImage(file="images/receive.png")
receive=ttk.Button(root,text="RECEIVE",command=Receive)
receive.pack()
send=ttk.Button(root,text="SEND",command=Send)
send.pack()
receive.place(x=50,y=100)
send.place(x=250,y=100)

bg=PhotoImage(file="images/trans.png")
Label(root,image=bg).place(x=-2,y=200)
root.mainloop()

