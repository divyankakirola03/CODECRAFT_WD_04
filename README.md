Task 4 – Basic Port Scanner

This task involves creating a simple **Port Scanner** using Python. The program scans a target IP address or domain for open ports in a specified range.

Description:
A **port scanner** is a tool that checks which ports on a target system are open or accessible. It can be used by system administrators for security testing and network diagnostics.

This script uses Python's built-in `socket` module to attempt connections on a range of ports and outputs which ones are open.

How to Use-

1. **Save the Script**  
   Save the code in a file called `port_scanner.py`

2. **Run the Script**  
   ```bash
   python port_scanner.py
   ```

3. **Provide Input**  
   - Target IP or domain (e.g., `127.0.0.1` or `scanme.nmap.org`)
   - Starting port number (e.g., `20`)
   - Ending port number (e.g., `80`)

4. **View Output**  
   The script will display a list of open ports in the given range.

Sample Output:

```bash
Enter target IP or hostname: 127.0.0.1
Enter starting port number: 20
Enter ending port number: 80

Scanning 127.0.0.1 from port 20 to 80...

Port 22: OPEN
Port 80: OPEN
```

Author-
**Divyanka Kirola**  
[LinkedIn Profile](https://www.linkedin.com/in/divyanka-kirola)
