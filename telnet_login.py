import sys
import telnetlib
import time

password = "cisco123"
command = "show interface status"

##with open ("list.txt", "r") as devicelist:
##    hostlist = []
##    hostlist=devicelist.readlines()
##    print(hostlist)
hostlist= [ ("10.197.81.80","",""),]

for host in hostlist:

        cmd1 = "enable"
        tn = telnetlib.Telnet(host[0])

        time.sleep(2)
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        time.sleep(2)
        tn.write(cmd1.encode('ascii') + b"\n")
        time.sleep(2)
        tn.write(password.encode('ascii') + b"\n")
        time.sleep(2)
        tn.write(command.encode('ascii') + b"\n")
        time.sleep(2)
        tn.write(b"\n")
        time.sleep(2)
        tn.write(b"\n")
        time.sleep(2)
        tn.write(b"exit\n")
        lastpost = tn.read_all().decode('ascii')
        op=open ("output.txt", "w")
        op.write(lastpost)
        print("writing to file")
        op.close()
        print(lastpost)
        tn.close()
