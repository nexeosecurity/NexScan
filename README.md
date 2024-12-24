# NexScan

GitHub Link: https://github.com/nexeosecurity/NexScan
Version: v1.0.0

**NexScan** is a comprehensive penetration testing tool designed to automate security testing processes. Version 1.0.0 introduces a Command-Line Interface (CLI) to enable powerful features such as subdomain fuzzing, directory fuzzing, and various brute-force attacks (SSH, FTP, MySQL, SMB). This documentation provides all necessary details to understand, install, and operate the tool.

## Installation Methods

NexScan can be installed using any of the following methods:

- GitHub repository
- Docker container

Choose the installation method that best suits your environment and requirements. Detailed instructions for each method are provided in their respective sections below.

## Features

NexScan provides several powerful features through its command-line interface. Below are detailed instructions for using each major functionality. All commands follow a consistent structure and support various optional parameters for customization.

### Directory Fuzzing

Directory fuzzing is a powerful feature that allows users to scan web servers for hidden files and directories. This is essential for discovering sensitive resources that may not be directly accessible through the web interface.

Optional arguments for Directory Fuzzing:

- -T, --target: Specifies the target for the scan.
- -f, --file: Specifies the file contains keywords to fuzz
- -v, --verbose: Enable verbose output

### Subdomain Fuzzing

Subdomain fuzzing helps identify subdomains of a target domain, which can be critical in understanding the attack surface of a web application.

Optional arguments for Directory Fuzzing:

- -T, --target: Specifies the target for the scan.
- -f, --file: Specifies the file contains keywords to fuzz
- -v, --verbose: Enable verbose output

### SMB Enumeration

The SMB enumeration feature allows users to perform brute-force attacks against SMB (Server Message Block) services. This can help in identifying weak credentials and gaining unauthorized access to shared resources.

Optional arguments for SMB brute-force:

- -T, --target: Specifies the target for the scan.
- -p, --password: Specify single password
- -P, --passwordfile: Specify password list file
- -u, --user: Specify target username
- -U, --userfile: Specify file containing list of usernames
- -s, --stop: Stop on first successful login
- -v, --verbose: Enable verbose output
- -port: Specify target port (by default 445)

### SSH Brute-force

The SSH brute-force module attempts to gain unauthorized access to SSH servers by testing multiple username and password combinations. This is crucial for assessing the security of SSH services.

Optional arguments for SSH brute-force:

- -T, --target: Specifies the target for the scan.
- -p, --password: Specify single password
- -P, --passwordfile: Specify password list file
- -u, --user: Specify target username
- -U, --userfile: Specify file containing list of usernames
- -s, --stop: Stop on first successful login
- -v, --verbose: Enable verbose output
- -port: Specify target port (by default 22)

### FTP Brute-force

The FTP brute-force module attempts to gain unauthorized access to FTP servers by testing multiple username and password combinations.

Optional arguments for FTP brute-force:

- -T, --target: Specifies the target for the scan.
- -p, --password: Specify single password
- -P, --passwordfile: Specify password list file
- -u, --user: Specify target username
- -U, --userfile: Specify file containing list of usernames
- -s, --stop: Stop on first successful login
- -v, --verbose: Enable verbose output

### MySQL Brute-force

The MySQL brute-force module targets MySQL databases to test username and password combinations for unauthorized access.

Optional arguments for MySQL brute-force:

- -T, --target: Specifies the target for the scan.
- -p, --password: Specify single password
- -P, --passwordfile: Specify password list file
- -u, --user: Specify target username
- -U, --userfile: Specify file containing list of usernames
- -s, --stop: Stop on first successful login
- -v, --verbose: Enable verbose output

> [!NOTE]
> For more information visit our documentation page.
