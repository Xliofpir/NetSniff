from scapy.all import sniff
from colorama import init, Fore

class Main:
    def __init__(self):
        pass

    def ask(self):
        self.input_for_interface = input("Select interface [wlan0 / eth0]: ")
        self.input_for_packet_name = input("Type packet type (leave empty for all packets): ")
        self.input_for_count_per_packet = int(input("How many packets do you want to display: "))
        
        return self.input_for_interface, self.input_for_packet_name, self.input_for_count_per_packet

    def display(self, packet):
        packet_info = f"[{packet.proto}] {packet.src} --> {packet.dst}"
        print(Fore.GREEN + packet_info + Fore.RESET)

    def start_process(self):
        if self.input_for_packet_name == "":
            sniff(iface=self.input_for_interface, prn=self.display, count=self.input_for_count_per_packet)
        else:
            sniff(filter=self.input_for_packet_name, prn=self.display, count=self.input_for_count_per_packet)

if __name__ == "__main__":
    init(autoreset=True)
    app = Main()
    app.ask()
    app.start_process()
