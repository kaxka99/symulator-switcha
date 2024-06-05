import subprocess
import os
import signal


class NetworkManager:
    def __init__(self):
        self.switch_process = None
        self.pc_processes = []

    def deploy_switch(self):
        # Uruchamia przełącznik sieciowy poprzez uruchomienie skryptu Sw.py w cmd

        if self.switch_process is None:
            self.switch_process = subprocess.Popen(
                ['python', 'Sw.py', '-s', '10000', '-p', '10001,10002,10003,10004,10005,10006,10007,10008'],
                creationflags=subprocess.CREATE_NEW_CONSOLE)
            print("Switch deployed on port 10000 with connected ports 10001 to 10008")
        else:
            print("Switch is already deployed.")

    def deploy_pc(self, pc_port, switch_port):
        # Uruchamia PC poprzez uruchomienie skryptu Pc.py w cmd z określonymi portami jako argumentami

        pc_process = subprocess.Popen(
            ['python', 'Pc.py', '-s', str(pc_port), '-d', str(switch_port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
        self.pc_processes.append(pc_process)
        print(f"PC deployed on port {pc_port}, connected to switch port {switch_port}")

    def shutdown_system(self):
        # Wyłączenie przełącznika i komputerów

        if self.switch_process:
            os.kill(self.switch_process.pid, signal.SIGTERM)
            self.switch_process = None
            print("Switch shut down.")
        for pc_process in self.pc_processes:
            os.kill(pc_process.pid, signal.SIGTERM)
        self.pc_processes = []
        print("All PCs shut down.")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Deploy Switch")
            print("2. Deploy PC")
            print("3. Shutdown System")
            print("q. Quit")
            choice = input("Select an option: ")

            if choice == '1':
                self.deploy_switch()
            elif choice == '2':
                try:
                    pc_port = int(input("Enter PC port (e.g., 10001): "))
                    switch_port = 10000  # stały port na, którym uruchamiany jest przełącznik
                    self.deploy_pc(pc_port, switch_port)
                except ValueError:
                    print("Invalid port number. Please enter a valid integer.")
            elif choice == '3':
                self.shutdown_system()
            elif choice == 'q':
                self.shutdown_system()
                print("Exiting...")
                break
            else:
                print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    manager = NetworkManager()
    manager.run()
