from jsonsocket import Server

server = Server('',8000)
server.accept()
data = {'msg':'bonjour'}
server.send(data)
data = server.recv()
print(data)
server.close()

