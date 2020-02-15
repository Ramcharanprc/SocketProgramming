import socket, threading, sqlite3, time

# connection = sqlite3.connect('DataStore.db')
users = {'Ram': '192.168.22.7', 'Syfali': '192.168.22.6', 'Sindhu': '192.168.22.11', 'Shruti': '192.168.22.4', 'Tanu': '192.168.22.13', 'Priya': '192.168.22.10'}
connected_clients = {}
socket_object = socket.socket()
print('socket created successfully')
socket_object.bind(('', 2545))
socket_object.listen(5)
def sendMessage(client_1, from_address, to_address,):
	while True:
		message = client_1.recv(1024).decode()
		sendConnection = sqlite3.connect('DataStore.db')
		messagesInDatabase = sendConnection.execute("select message from chat where sender_address = '" + to_address + "' and receiver_address = '" + from_address +"';")
		previousMessages = ''
		for row in messagesInDatabase:
			for previousMessage in row: 
				previousMessages = previousMessages + previousMessage
		previousMessages = previousMessages + message
		sendConnection.execute("update chat set message = '"+ previousMessages + "' where sender_address = '" + from_address + "' and receiver_address = '" + to_address +"';")
		sendConnection.commit()
		sendConnection.close()
		# client_2.send(message_1.encode('utf-8'))

		# message_2 = client_2.recv(1024).decode('utf-8')
		# client_1.send(message_2.encode('utf-8'))
def receiveMessage(fromIp, toIp, clientObj,):
	while True:
		time.sleep(5)
		receiveConnection = sqlite3.connect('DataStore.db')
		messagesInDatabase = receiveConnection.execute("select message from chat where sender_address = '" + toIp + "' and receiver_address = '" + fromIp+ "';")
		messages = ''
		for row in messagesInDatabase:
			for message in row:
				messages = messages + message
		clientObj.send(messages.encode())
		receiveConnection.execute("update chat set message = '' where sender_address = '" + fromIp + "' and receiver_address = '" + toIp + "';")
		receiveConnection.commit()
		receiveConnection.close()



def connect_to_chatroom(client_1, client_1_address):
	client_name = client_1.recv(1024).decode()
	print(client_name)
	client_2_address = users[client_name]
	if client_2_address in connected_clients:
		print('done')
		client_2 = connected_clients[users[client_name]]
		client_1.send((client_name + ' is online.').encode())
		connection = sqlite3.connect('DataStore.db')
		connection.execute("insert into Chat values('" + client_1_address + "', '"+ client_2_address + "', 'Welcome' );")
		connection.commit()
		connection.close()
		# while True:
		# 	message_1 = client_1.recv(1024).decode()
		# 	client_2.send(message_1.encode('utf-8'))
		# 	message_2 = client_2.recv(1024).decode('utf-8')
		# 	client_1.send(message_2.encode('utf-8'))
		sender = threading.Thread(target = sendMessage, args =(client_1, client_1_address,  client_2_address, ))
		receiver = threading.Thread(target = receiveMessage, args =(client_1_address, client_2_address, client_1, ))
		sender.start()
		receiver.start()
	# client_2 = connected_clients[users[client_name]]
				# client_2.send(message.encode('utf-8'))
	else:
		client_1.send((client_name + ' is offline').encode())
		# client_2.close()

print('Listening')
while True:
	
	client1, client1_address = socket_object.accept()
	connected_clients[client1_address[0]] = client1
	client1.send('Welcome to Syf Server \nThank You for connecting.'.encode('utf-8'))
	print(connected_clients)
	connect = threading.Thread(target = connect_to_chatroom, args = (client1, client1_address[0], ))
	connect.start()
	
