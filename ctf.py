import subprocess
import sys
import time

args = sys.argv

ip_addr = input("IPv4 Address: ")

hydra_was_called_before = False

hydra_username = None

def run_as_new_instance(cmd):
    subprocess.run(['gnome-terminal', '--wait', '--', 'bash', '-c', cmd])

def nmap():
    command = "nmap -sC -sV " + ip_addr
    run_as_new_instance(command)

def hydra_ssh(username):
    command = "hydra -l " + username + "-P /usr/share/wordlists/rockyou.txt " + ip_addr + " ssh -V"
    run_as_new_instance(command)

def gobuster():
    wordlist = input("Wordlist Name (/usr/share/wordlists/): ")
    command = "gobuster dir -u http://"+ip_addr+"/ -w /usr/share/wordlists/"+wordlist
    run_as_new_instance(command)

def bf_ftp(username):
    command = "hydra -l " + username + "-P /usr/share/wordlists/rockyou.txt " + ip_addr + " ftp -V"
    run_as_new_instance(command)

def nikto():
    command = "nikto -h " + ip_addr
    run_as_new_instance(command)

def wpscan():
    command = "wpscan --url http://"+ip_addr+"/ --log"
    run_as_new_instance(command)

if __name__ == "__main__":
    for i in args:
        if i == "ctf.py":
            continue
        elif i == "--nmap":
            nmap()
        elif i == "--hydra_ssh":
            username = input("Hydra: Please input the username: ")
            hydra_was_called_before = True
            hydra_username = username
            hydra_ssh(username)
        elif i == "--gobuster":
            gobuster()
        elif i == "--bf_ftp":
            if not hydra_was_called_before: 
                username = input("bf_ftp: Please input the username: ")
                bf_ftp(username)
            else:
                bf_ftp(hydra_username)
        elif i == "--nikto":
            nikto()
        elif i == "--wpscan":
            wpscan()
        else:
            print("Unknown command: " + i)
        time.sleep(4)

print("Done!")
