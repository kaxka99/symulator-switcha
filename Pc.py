#!/usr/bin/env python

import socket
import argparse
import threading


class PC:
    def __init__(self, src_port, switch_port):
        self.src_port = src_port
        self.switch_port = switch_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', self.src_port))
        self.sys_ipaddr = '127.0.0.1'

    def listen(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(8192)
                info = data.decode().split(',')
                dst_port = int(info[0])
                if self.src_port == dst_port:
                    src_port = int(info[1])
                    message = info[2]
                    if message:
                        print(f"\nReceived Message:\nDst port: {dst_port}\nSrc port: {src_port}\nMessage: {message}\n{'-'*47}\n")
                else:
                    print('\nReceived broadcast packet, but I am not the designated PC to receive this packet\n')
            except ConnectionResetError as e:
                print(f"Connection reset error: {e}")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    def send_message(self, dst_port, message):
        packet = f"{dst_port},{self.src_port},{message}".encode()
        self.sock.sendto(packet, ('localhost', self.switch_port))

    def run(self):
        threading.Thread(target=self.listen, daemon=True).start()
        while True:
            msg = input('Enter destination port and message (format: dst_port,msg_data): ')
            try:
                dst_port, msg_data = msg.split(',')
                dst_port = int(dst_port)
                self.send_message(dst_port, msg_data)
            except ValueError:
                print("Invalid input format. Please use the format: dst_port,msg_data")


if __name__ == '__main__':
    # Argumenty do uruchomienia PC
    # -s NUMER_PORTU - port na przełączniku do którego podpinamy komputer
    # -d NUMER_PORTU ... - numer portu przełącznika

    parser = argparse.ArgumentParser(description='Processing Command line inputs for pc program')
    parser.add_argument('-s', type=int, default=10001, help='Port program will listen for incoming msgs on this UDP port')
    parser.add_argument('-d', type=int, default=10000, help='Switch udp port this PC is connected.')
    args = parser.parse_args()

    if args.s and args.d:
        pc = PC(args.s, args.d)
        pc.run()

    input("Press Enter to close the PC...")
