#!/usr/bin/env python
# coding: utf-8

# In[41]:



import socket
import sys
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
correctValues=["4"]
buttons=["1","2","3","4"]
# Connect the socket to the port where the server is listening
server_address = ('46.101.134.129', 31337)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
data = sock.recv(1024)
#print ('Received', repr(data))
#send first one

message = correctValues[0].encode()  #print('sending {!r}'.format(message))
sock.sendall(message)
data = sock.recv(1024)
receivedData=repr(data)
print(receivedData)
# Send data

counter=0
index=0;
def randomValues():
    global counter
    global index
    if counter>1002:
        return
    if(index==4):
        index=0
    index=index+1  
    val = str(index)
    message = val.encode()  #print('sending {!r}'.format(message))
    sock.sendall(message)
    data = sock.recv(1024)
    substring ="Your answer is correct"
    receivedData=repr(data)
    if substring in receivedData:
        print("Found!",receivedData)
        correctValues.append(val)
        counter=counter+1;
    else:
        print("Not found*****************REPEAT!")
        for x in correctValues:
            m = x.encode()  #print('sending {!r}'.format(message))
            sock.sendall(m)
            d = sock.recv(1024)
            rd=repr(d)
            #print("repeat ->!")
        randomValues()
                
    randomValues()



    
#doooooooooooooooooooooooooone    
randomValues()
print ('Array values', correctValues)

sock.close()


# In[57]:


print("hey")
print ('Array values', correctValues)
print ('Array len', len(correctValues))


# In[58]:


correctValues.pop()
correctValues.pop()
correctValues.pop()
correctValues.pop()
correctValues.pop()
correctValues.pop()
print ('length values', len(correctValues))
a_list = correctValues
print ('length values', len(a_list))
textfile = open("a_file.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()


# In[60]:


a_list.pop();
print ('after the pop', len(a_list))
a_list.append("1")
print ('length values', len(a_list))
# Create a TCP/IP socket
socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting to {} port {}'.format(*server_address))
socks.connect(server_address)
data = socks.recv(1024)
receivedData=repr(data)
print(receivedData)


for val in a_list:
    
    message = val.encode()  
    socks.sendall(message)

    try:
        data = socks.recv(1024)
    except socket.timeout:
        raise socket.timeout("Error! Socket did not get info, when expected")
    if not data:
        s = "Empty"
    else:
        s = data.decode('utf-8')
    print(val,"\n === Read from socket === \n%s\n" % s)
        
        
    #receivedData=repr(data)
    #print(receivedData)


# In[ ]:




