# Client program.
import socket
import threading
from tkinter import *
import tkinter
top = tkinter.Tk()
top.title("Let's Chat")
top.geometry("600x800")
top.configure(bg = 'tan')
socketObject = socket.socket()
port = 2545
socketObject.connect(("192.168.22.6", port))
print(socketObject.recv(1024).decode())

# def getName():
# 	global senderName
# 	global receiverName
	# senderName = StringVar()
	# receiverName = StringVar()

def sendMessages():
	while True:
		senderName = fromEntry.get()
		receiverName = toEntry.get()
		chatBox.config(state = 'normal')
		message = textBox.get("0.0", "end")
		SocketObject.send(message.encode())
		display = senderName + " : " + message
		chatBox.insert(INSERT, display)
		chatBox.config(state = 'disable')
		textBox.delete("0.0", "end")

def receiveMessages():
	while True:
		global receiverName
		receivedMessage = socketObject.recv(1024).decode()
		display1 = receiverName + " : " + receivedMessage
		chatBox.insert(INSERT, display1)

fromLabel = Label(top, text = "From", width = 6)
fromLabel.place(x = 25, y = 15)
fromEntry = Entry(top, width = 50)
fromEntry.place(x = 80, y = 15)
toLabel = Label(top, text = "To", width = 6)
toLabel.place(x = 25, y = 50)
toEntry = Entry(top, width = 50)
toEntry.place(x = 80, y = 50)
socketObject.send(receiverName.encode())
if(socketObject.recv(1024).decode() == 'online'):
# if(1):
	status = "Online"
else:
	status = "Offline"
statusLabel = Label(top, text = status, width = 6, bg = "cyan")
statusLabel.place(x = 230, y = 85)
chatBoxLabel = Label(top, text = "ChatBox")
chatBoxLabel.place(x = 25, y = 85)
chatBox = Text(top, height = 15, width = 57)
chatBox.place(x = 25, y = 105)
chatBox.config(state = 'disable')
typeLabel = Label(top, text = "Type Here")
typeLabel.place(x = 25, y = 375)

textBox = Text(top, height = 2, width = 57)
textBox.place(x = 25, y = 395)
# textBox.delete("0.0", "end")
placeholder_text = 'type here'
textBox.insert("0.0", placeholder_text)
textBox.configure(state = 'disable', fg = "grey");
def clearEntry(event):
	textBox.configure(state = 'normal');
	textBox.delete("0.0", "end")
	textBox.unbind("<Button-1>", clickId)
clickId = textBox.bind("<Button-1>", lambda event: clearEntry(event))
# button = Button(top, text = "Name", command = getName) 
# top.bind('<Return>', lambda event = None: button.invoke())
sendButton = Button(top, height = 1, width = 4, text = "Send", bg = "green", fg = "white", relief = RAISED, command = sendMessages)
sendButton.place(x = 230, y = 450)
closeButton = Button(top, height = 1, width = 4, text = "Exit", bg = "red", fg = "white", relief = RAISED, command = top.destroy)
closeButton.place(x = 230, y = 550)

top.mainloop()
Thread2 = threading.Thread(target = receiveMessages)
Thread2.start()
# ClientName = input("Enter receiver name: ")
# print("Connected to " + ClientName + ".")

# def Send():
# 	while True:
# 		Message = input(" > ")
# 		SocketObject.send(Message.encode())

# def Receive():
# 	while True:
# 		ClientMessage = (SocketObject.recv(1024).decode())
# 		time.sleep(2)
# 		print(ClientName + " > " + ClientMessage)

# 	# SocketObject.send(input("Me > ").encode())
# 		# if ClientMessage:
# 		# 	if (ClientMessage == 'Bye'):
# 		# 		SocketObject.close()
# 		# break
# Thread1 = threading.Thread(target = sendMessages)
# Thread2 = threading.Thread(target = Send)
# Thread1.start()
# Thread2.start()



































# import socket
# import threading
# SocketObject = socket.socket()
# Port = 773
# SocketObject.connect(("192.168.22.4", Port))
# Name = input("Enter name: ")
# SocketObject.send(Name.encode())
# # Message = SocketObject.recv(1024).decode()
# ServerMessage = (SocketObject.recv(1024).decode())
# print(ServerMessage)

# def Send():
# 	while True:
# 		Message = input("Me > ")
# 		if (Message == 'Bye'):
# 			ClientMessageessage = 'Bye'
# 		SocketObject.send(Message.encode())


# def Receive():
# 	while True:
# 		print("********")
# 		ClientMessage = (SocketObject.recv(1024).decode())
# 		print(ClientMessage)
# 		if ClientMessage:
# 			print(ClientMessage)
# while True:
# 	Send()
# 	# Receive()
# 	Thread1 = threading.Thread(target = Receive)
# 	Thread1.start()
# SocketObject.close()



