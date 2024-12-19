# NexScan

[![License](https://img.shields.io/badge/license-Custom%20License-blue.svg)](./LICENSE)

## Introduction

NexScan is a comprehensive penetration testing tool designed to automate security testing processes. Version 1.0.0 introduces a Command-Line Interface (CLI) to enable powerful features such as subdomain fuzzing, directory fuzzing, and various brute-force attacks (SSH, FTP, MySQL, SMB). This documentation provides all necessary details to understand, install, and operate the tool.

## Features

Subdomain Fuzzing: Identify subdomains of a target domain.

Directory Fuzzing: Discover directories and files on web servers.

Brute-force Modules:
- SSH
- FTP
- MySQL
- SMB

Verbose Mode: Display detailed logs during execution.

Stop on Success: Terminate brute-forcing upon successful credential discovery.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Internet Connectivity

### Installation Steps
1. Clone the repository:
```
git clone https://github.com/nexeosecurity/NexScan.git
```
2. Navigate to the project directory:
```
cd NexScan/
```
3. Install required Python dependencies:
```
pip install -r requirements.txt
```

## Usage Guide

### Basic Command Syntax
```
./NexScan.py <module> -T <target> [options]
```

### Modules and Options

1. Directory Fuzzing
    - Default
    ```
    ./NexScan.py directory -T https://nexeosecurity.tech
    ```
    - Verbose Fuzzing
    ```
    ./NexScan.py directory -T https://nexeosecurity.tech -v
    ```

2. Subdomain Fuzzing
    - Default
    ```
    ./NexScan.py subdomain -T https://nexeosecurity.tech
    ```
    - Verbose Fuzzing
    ```
    ./NexScan.py subdomain -T https://nexeosecurity.tech -v
    ```

3. SMB Enumeration
    - With username and password file
    ```
    ./NexScan.py smb -T 172.16.173.129 -u kali -P password_list.txt
    ```
    - With userfile and password
    ```
    ./NexScan.py smb -T 172.16.173.129 -U user_list.txt -p kali
    ```
    - With userfile and password file
    ```
    ./NexScan.py smb -T 172.16.173.129 -U user_list.txt -P password_list.txt
    ```

4. SSH Bruteforce
    - With username and password file
    ```
    ./NexScan.py ssh -T 172.16.173.129 -u kali -P password_list.txt
    ```
    - With userfile and password
    ```
    ./NexScan.py ssh -T 172.16.173.129 -U user_list.txt -p kali
    ```
    - With userfile and password file
    ```
    ./NexScan.py ssh -T 172.16.173.129 -U user_list.txt -P password_list.txt
    ```

5. FTP Bruteforce
    - Default
    ```
    ./NexScan.py ftp -T 172.16.173.129
    ```
    - Verbose option
    ```
    ./NexScan.py ftp -T 172.16.173.129 -v
    ```
    - Stop on Success option
    ```
    ./NexScan.py ftp -T 172.16.173.129 -s
    ```
    - Both options enabled
    ```
    ./NexScan.py ftp -T 172.16.173.129 -s -v
    ```

6. MySQL Bruteforce
    - With username and password file
    ```
    ./NexScan.py mysql -T 172.16.173.129 -u admin -P unix_passwords.txt -v
    ```

## License

This project is licensed under the terms of the [Custom License](./LICENSE).

For personal and non-commercial use only. For commercial use, please contact Nexeo Security at business@nexeosecurity.tech.

## Contributions

We welcome contributions! By contributing to this project, you agree that your contributions will be licensed under the same terms as the project.
