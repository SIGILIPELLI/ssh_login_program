import getpass
import telnetlib
import time
#user = input("Enter your telnet username: ")
#password = getpass.getpass()

f = open("test.txt")
for line in f:
      print ("Getting running config from devices " + line)
      HOST = line.strip()
      print(HOST)
      tn = telnetlib.Telnet(HOST)
       # tn.read_until(b"Username:")
       # tn.write(user.encode("ascii")+ b"\n")
       # if password:
       #     tn.read_until(b"Password:")
       #     tn.write(password.encode("ascii")+b"\n")

      tn.read_until(b"#")
      tn.write(b"conf t"+b"\n")
      time.sleep(1)
      tn.write(b"hostname test"+b"\n")
      time.sleep(1)
      tn.write(b"exit"+b"\n")
      time.sleep(1)
      tn.write(b"terminal length 0"+b"\n")
      time.sleep(3)
      tn.write(b"show run"+b"\n")
      time.sleep(3)
      tn.write(b"exit"+b"\n")
      readoutput = tn.read_all().decode('ascii')
      saveoutput = open("device.txt" + HOST, "w")
      saveoutput.write(readoutput)
      saveoutput.close
