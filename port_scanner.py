import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to server.")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter starting port number: "))
    end_port = int(input("Enter ending port number: "))
    scan_ports(target, start_port, end_port)