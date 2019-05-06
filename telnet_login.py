import os,re,telnetlib
host = "10.xxx.xxx.xxx"
port = 23

telnet = telnetlib.Telnet()
telnet.open(host, port)
telnet.write('loginID\r\n')
telnet.write('Password\r\n')
out = telnet.read_until("DB>", 5)
telnet.write('show cable modem reg\r\n') #Mycommand
out = telnet.read_until("DB>", 5)
telnet.write('quit\r\n')
telnet.close()
