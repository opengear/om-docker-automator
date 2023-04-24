#!/usr/bin/python3
#
# cisco_cmd_pmshell.py
# Opengear Solutions Engineering, 6 July 2022
#  
# Send a command to a Cisco IOS device through OM pmshell
# Validated on IOS XE version 16.12.04 and IOS version 15.2(7)E4

from netmiko import ConnectHandler, redispatch
import creds
import time

def connect():

    device1 = {
        'host': creds.omHost,
        'username': creds.omUser,
        'password': creds.omPassword,
        'device_type': 'terminal_server'
    }   

    conn = ConnectHandler(**device1)

    return conn


def command():

    conn = connect()

    conn.send_command_timing(creds.pmshell)
    conn.write_channel('\r\n\r\n\r\n')
    time.sleep(5)
    conn.write_channel('\r\n\r\n')

    redispatch(conn, device_type='cisco_ios')
    conn.find_prompt()

    conn.enable()  
    output = conn.send_command(creds.command)
    print(output)

    conn.write_channel('\r\n')
    time.sleep(1)

    conn.disconnect()


if __name__ == "__main__":
    command()