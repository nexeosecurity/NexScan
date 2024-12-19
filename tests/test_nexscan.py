import subprocess

# Helper function to run the NexScan CLI commands
def run_nexscan_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result

# Test Directory Fuzzing
def test_directory_fuzzing():
    command = ["python3", "NexScan.py", "directory", "-T", "https://nexeosecurity.tech"]
    result = run_nexscan_command(command)
    assert result.returncode == 0  # Ensure the command runs successfully
    assert "fuzzing completed" in result.stdout.lower()  # Check if expected output is in stdout

# Test Sub-domain Fuzzing
def test_subdomain_fuzzing():
    command = ["python3", "NexScan.py", "subdomain", "-T", "https://nexeosecurity.tech"]
    result = run_nexscan_command(command)
    assert result.returncode == 0  # Ensure the command runs successfully
    assert "subdomain fuzzing completed" in result.stdout.lower()  # Check if expected output is in stdout

# Test SMB Enumeration
def test_smb_enumeration():
    command = ["python3", "NexScan.py", "smb", "-T", "172.16.173.129", "-u", "kali", "-P", "unix_passwords.txt"]
    result = run_nexscan_command(command)
    assert result.returncode == 0  # Ensure the command runs successfully
    assert "smb enumeration completed" in result.stdout.lower()  # Check if expected output is in stdout

# Test SSH Bruteforce
def test_ssh_bruteforce():
    command = ["python3", "NexScan.py", "ssh", "-T", "172.16.173.129"]
    result = run_nexscan_command(command)
    assert result.returncode == 0  # Ensure the command runs successfully
    assert "ssh bruteforce completed" in result.stdout.lower()  # Check if expected output is in stdout

# Test FTP Bruteforce
def test_ftp_bruteforce():
    command = ["python3", "NexScan.py", "ftp", "-T", "172.16.173.129"]
    result = run_nexscan_command(command)
    assert result.returncode == 0  # Ensure the command runs successfully
    assert "ftp bruteforce completed" in result.stdout.lower()  # Check if expected output is in stdout

# Test MySQL Bruteforce
def test_mysql_bruteforce():
    command = ["python3", "NexScan.py", "mysql", "-T", "172.16.173.129", "-u", "admin", "-P", "unix_passwords.txt", "-v"]
    result = run_nexscan_command(command)
    assert result.returncode == 0  # Ensure the command runs successfully
    assert "mysql bruteforce completed" in result.stdout.lower()  # Check if expected output is in stdout
