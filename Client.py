from jsonsocket import Client

cl = Client()
cl.connect('192.168.1.8',8000)
data = cl.recv()
print(data)