#!/usr/bin/python3
#
# show_version.py
#
# Execute a show version on a Cisco IOS device

from netmiko import ConnectHandler
import getpass
import time

def connect():

    # Cisco device credentials
    device1 = {
        'host': '10.0.0.1'
        'username': 'oguser',
        'password': 'myPassword
        'device_type': 'cisco_ios',
        'session_log': 'netmiko_log.txt'
    }   

    # set up ssh connection
    conn = ConnectHandler(**device1)

    return conn


def command():

    # connect ssh session
    conn = connect()

    # set up command
    output = conn.send_command('show version')

    # execute and print output
    print(output)

    # disconnect ssh session
    conn.disconnect()


if __name__ == "__main__":
    command()
