from socket import *
import os
import sys
import datetime
from threading import Thread
from socketserver import ThreadingMixIn
threads = []
now = datetime.datetime.now()
datetime = now.strftime('%A,%d %B %Y %H:%M:%S ')
datetime += "GMT"
def delete(path,size,caddress,inputpath):
    cad,ip = caddress
    if os.path.exists(path):
        os.remove(path)
        response = "HTTP/1.1 200 OK\n"      
        response = "HTTP/1.1 201 CREATED\n"
        response += "Date: %s\n" % datetime
        response += "Server: RohitRushi/0.0.1 (ubuntu)\n"
        response += "Content-Length: %s\n" % size
        response += "Content-Type: text/html; charset= iso-8859\n"
        response += "Connection: closed\n\n"
        connection.send(response.encode())
     #   connection.close()
        if os.path.exists('accesstemp.log'):
            fpl = open('accesstemp.log','a+')
            fpl.write("%s\t"%datetime)
            fpl.write("%s\t"%cad)
            fpl.write("%s\t"%ip)
    #        fpl.write("%s\t"%ipaddr)
            fpl.write("%s\t"%inputpath)
            fpl.write("200\t")
            fpl.write("%d\n"%size)

def put(path,path1,caddress,inputpath):
    content = []
    cad,ip = caddress
    if os.path.exists(path):
        os.remove(path)
        fp1 = open(path1)
        content = fp1.readlines()
        fp2 = open(path,'w+')
        fp2.writelines(content)
        size = os.path.getsize(path1)
        response = "HTTP/1.1 200 OK\n"
        response += "Date: %s\n" % datetime
        response += "Server: RohitRushi/0.0.1 (ubuntu)\n"
        response += "Content-Length: %s\n" % size
        response += "Content-Type: text/html; charset= iso-8859\n"
        response += "Connection: closed\n\n"
        connection.send(response.encode())
    #    connection.close()
        if os.path.exists('accesstemp.log'):
            fpl = open('accesstemp.log','a+')
            fpl.write("%s\t"%datetime)
            fpl.write("%s\t"%cad)
            fpl.write("%s\t"%ip)
            fpl.write("%s\t"%inputpath)
            size = os.path.getsize(path)
            fpl.write("200\t")
            fpl.write("%d\n"%size)
        
    else:
        fp1 = open(path1)
        content = fp1.readlines()
        fp2 = open(path,'w+')
        fp2.writelines(content)
        size = os.path.getsize(path1)
        response = "HTTP/1.1 201 CREATED\n"
        response += "Date: %s\n" % datetime
        response += "Server: RohitRushi/0.0.1 (ubuntu)\n"
        response += "Content-Length: %s\n" % size
        response += "Content-Type: text/html; charset= iso-8859\n"
        response += "Connection: closed\n\n"
        connection.send(response.encode())
   #     connection.close()
        if os.path.exists('accesstemp.log'):
            fpl = open('accesstemp.log','a+')
            fpl.write("%s\t"%datetime)
            fpl.write("%s\t"%cad)
            fpl.write("%s\t"%ip)
            fpl.write("%s\t"%inputpath)
            size = os.path.getsize(path)
            fpl.write("200\t")
            fpl.write("%d\n"%size)
        
def head(path,caddress,inputpath):
    f = open(path)
    
    cad,ip = caddress
    size = os.path.getsize(path)
    response ="HTTP/1.1 200 OK\n"
    response += "Date: %s\n" % datetime
    response += "Server: RohitRushi/0.0.1 (ubuntu)\n"
    response += "Content-Length: %s\n" % size
    response += "Content-Type: text/html; charset= iso-8859\n"
    response += "Connection: closed\n\n"
    f1 = open(path)
    text1 = f1.read()
    connection.send(response.encode())
  #  connection.close()
    if os.path.exists('accesstemp.log'):
        fpl = open('accesstemp.log','a+')
        fpl.write("%s\t"%datetime)
        fpl.write("%s\t"%cad)
        fpl.write("%s\t"%ip)
        fpl.write("%s\t"%inputpath)
        size = os.path.getsize(path)
        fpl.write("200\t")
        fpl.write("%d\n"%size)

def get(path,caddress,inputpath):
    count = 0
    cad,ip = caddress
    if os.path.exists(path):
        f = open(path)
        size = os.path.getsize(path)
        response ="HTTP/1.1 200 OK\n"
        response += "Date: %s\n" % datetime
        response += "Server: RohitRushi/0.0.1 (ubuntu)\n"
        response += "Content-Length: %s\n" % size
        response += "Content-Type: text/html; charset= iso-8859\n"
        response += "Connection: closed\n\n"
        f1 = open(path)
        text1 = f1.read()
        output = response + text1
        connection.send(output.encode())
       # connection.close()
        if os.path.exists('accesstemp.log'):
            fpl = open('accesstemp.log','a+')
            fpl.write("%s\t"%datetime)
            fpl.write("%s\t"%cad)
            fpl.write("%s\t"%ip)
            fpl.write("%s\t"%inputpath)
            size = os.path.getsize(path)
            fpl.write("200\t")
            fpl.write("%d\n"%size)
            inputpathpost = connection.recv(1024).decode().split()
            li = list(inputpathpost[1].split("?"))
            li1 = list(li[1].split("&"))
            print(li1[0],end = ' ');print(li1[1])
       # connection.close()
    else:
        response ="HTTP/1.1 404 NOT FOUND\n"
        response += "Date: %s\n" % datetime
        response += "Server: RohitRushi/0.0.1 (ubuntu)\n"
        response += "Connection: closed\n\n"
        connection.send(response.encode())
        if os.path.exists('error.log'):
            fpl = open('accesstemp.log','a+')
            fpl.write("%s\t"%datetime)
            fpl.write("%s\t"%inputpath)
       #     size = os.path.getsize(path)
            fpl.write("404\t")
	
class cthread(Thread):
    def __init__(self,connection,caddress):
        Thread.__init__(self)
        self.connection = connection
        self.caddress = caddress

    def run(self):
        while(True):
            inputpath = list(connection.recv(1024).decode().split())
            print(inputpath)
            path1 = '/home/rushikesh'
            path = '/home/rushikesh/http'
            path += inputpath[1]
            path1 += inputpath[1]
            pathlog = '/home/rushikesh/http/'
            protocolver = inputpath[2]
      #      size = os.path.getsize(path)
            if(inputpath[0] == "GET"):
    	        get(path,caddress,inputpath)
            elif(inputpath[0] == "HEAD"):
                head(path,caddress,inputpath)
            elif(inputpath[0] == "PUT"):
                put(path,path1,caddress,inputpath)
            elif(inputpath[0] == "DELETE"):
                delete(path,size,caddress,inputpath)
            else:
                response ="HTTP/1.1 400 BAD REQUEST\n"
                response += "Date: %s\n" % datetime
                response += "Server: RohitRushi/0.0.1 (ubuntu)\n"
                response += "Connection: closed\n\n"
                connection.send(response.encode())
                connection.close()
                if os.path.exists('error.log'):
                    fpl = open('accesstemp.log','a+')
                    fpl.write("%s\t"%datetime)
                    fpl.write("%s\t"%inputpath)
                    size = os.path.getsize(path)
                    fpl.write("400\t")
                    fpl.write("%d\n"%size)

if __name__ == "__main__":
    s = socket(AF_INET,SOCK_STREAM)
    serverport = int(sys.argv[1])
    s.bind(('',serverport))
    print("Server is listening")
    while(True):
        s.listen(10)
        (connection,caddress) = s.accept()
        print("New connection received from:");print(caddress)
        newthread = cthread(connection,caddress)
        newthread.start()
        threads.append(newthread)

    for i in threads:
        i.join()
