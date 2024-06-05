import socket
import sys
import argparse
import threading
from time import ctime


class Switch:
    def __init__(self, listen_port, connected_ports):
        self.listen_port = listen_port
        self.connected_ports = list(map(int, connected_ports.split(',')))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', self.listen_port))
        self.mac_table = []

    def print_mac_table(self):
        # Wyświetlanie nauczonych portów - 'adresów mac'
        print("\nCurrent MAC Table:")
        for mac in self.mac_table:
            print(f"Port: {mac}")
        print()

    def listen(self):
        # Nasłuchuje przychodzące pakiety i przełącza je dalej za pomocą uni lub
        # broadcastu w zależności czy ma zapamietany dany 'adres mac' w tabeli

        while True:
            try:
                data, addr = self.sock.recvfrom(8192)
                info = data.decode().split(',')
                dst_port = int(info[0])
                src_port = int(info[1])
                message = info[2]

                if message:
                    print(f"\nReceived Message:\nMsg: {info}\nDest port: {dst_port}")

                    if dst_port in self.connected_ports:
                        print('Given destination port is valid')
                    else:
                        print('Given destination port is not valid, exiting the program. Please try again with a valid port number')
                        sys.exit(2)

                    if dst_port in self.mac_table:
                        dst_addr1 = ('localhost', dst_port)
                        self.sock.sendto(f"{dst_port},{src_port},{message}".encode(), dst_addr1)
                        print('\nUnicasting\nMessage Received\nDst port:', dst_port, '\nMessage:', message, '\nTime:', ctime(), '\n' + '-'*47)
                        if src_port not in self.mac_table:
                            self.mac_table.append(src_port)
                            self.print_mac_table()
                    else:
                        print('\nPacket broadcasting')
                        if src_port not in self.mac_table:
                            self.mac_table.append(src_port)
                            self.print_mac_table()
                        for port in self.connected_ports:
                            if src_port != port:
                                dst_addr = ('localhost', port)
                                self.sock.sendto(f"{dst_port},{src_port},{message}".encode(), dst_addr)

            except Exception as e:
                pass
                # błąd będzie występował gdy wiadomość broadcast
                # dotrze do nieużywanych portów,
                # nie obsługuje błędu czy nie wyświetlam ze względu na
                # utrzymanie okna konsoli przełącznika  w czystości :)

    def run(self):
        # Uruchamia nasłuchiwanie na portach

        if len(self.connected_ports) > 8:
            print('Switch has only 8 ports to connect PCs')
            sys.exit(2)
        threading.Thread(target=self.listen, daemon=True).start()
        while True:
            pass


if __name__ == '__main__':

    # Argumenty do uruchomienia Switcha
    # -s NUMER_PORTU - port na którym ma zostać uruchomiony przełącznik
    # -p NUMER_PORTU ... - numery portów, które mają zostać uruchomione na przełączniku

    parser = argparse.ArgumentParser(description='Processing Command line inputs of self-learning and forwarding of bridge/switch')
    parser.add_argument('-s', type=int, default=10000, help='Is sthe UDP port on which a switch will listen to receive msg from connected devices')
    parser.add_argument('-p', type=str, default='10001,10002,10003,10004,10005,10006,10007,10008', help='Ports which implies that devices are connected i.e. those devices having these ethernet addresses')
    args = parser.parse_args()

    if args.s and args.p:
        switch = Switch(args.s, args.p)
        switch.run()

    input("Press Enter to close the switch...")
