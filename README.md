# NexScan

GitHub Link: https://github.com/nexeosecurity/NexScan
Version: v1.0.0

# Introduction

**NexScan** is a comprehensive penetration testing tool designed to automate security testing processes. Version 1.0.0 introduces a Command-Line Interface (CLI) to enable powerful features such as subdomain fuzzing, directory fuzzing, and various brute-force attacks (SSH, FTP, MySQL, SMB). This documentation provides all necessary details to understand, install, and operate the tool.

## Overview

Welcome to NexScan Docs! This is the place where you can find official information about how to install and use NexScan. Feel free to navigate through our documentation and if you still couldn’t find the solution to your problem you can mail our support team at [contact@nexeosecurity.tech](mailto:contact@nexeosecurity.tech).

To get started using NexScan, check out the Getting Started section.

## Licensing

This project is licensed under the terms of the [Custom License](./LICENSE). The tool is for personal and non-commercial use only. For commercial use, please contact **Nexeo Security** at [business@nexeosecurity.tech](mailto:business@nexeosecurity.tech).

# Getting Started

This section will guide you through the initial setup and basic usage of NexScan. Before proceeding with installation, ensure you meet all prerequisites and have the necessary permissions for your intended use case.

## System Requirements

- Python 3.8 or higher
- Operating System: Linux, macOS, or Windows
- Internet connection for installation and updates

## Installation Methods

NexScan can be installed using any of the following methods:

- GitHub repository
- Docker container

Choose the installation method that best suits your environment and requirements. Detailed instructions for each method are provided in their respective sections below.

# Installation and Setup

This section provides detailed instructions for installing NexScan using different methods to accommodate various user needs and deployment scenarios. Each installation method has been thoroughly tested to ensure reliability and ease of use.

## Github

The GitHub repository for NexScan contains the complete source code and is the recommended method for developers who want to contribute or customize the tool. This section covers how to clone, set up, and use NexScan directly from the GitHub repository.

### Prerequisites

Before installing NexScan from GitHub, ensure you have the following prerequisites:

- Git installed on your system
- Python 3.8+ with pip package manager
- Required system permissions to install Python packages
- Basic knowledge of command-line operations
- Recommended: Virtual environment management tool (venv or conda)

Note: Some features may require root/administrator privileges depending on your operating system and intended use case.

### Procedure

Follow these steps to install NexScan from the GitHub repository:

**For Windows**

```bash
# Clone the repository
git clone https://github.com/nexeosecurity/NexScan.git

# Navigate to the project directory
cd NexScan

# Create and activate virtual environment (recommended)
python -m venv nexscan
nexscan\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

**For MacOS/Unix**

```bash
# Clone the repository
git clone https://github.com/nexeosecurity/NexScan.git

# Navigate to the project directory
cd NexScan

# Create and activate virtual environment (recommended)
python3 -m venv nexscan
source nexscan/bin/activate

# Install required dependencies
pip3 install -r requirements.txt
```

After successful installation, you can run NexScan using the command line interface. The tool will be available as a command-line utility as of now, and you can access all features through the CLI.

To ensure proper functionality, make sure all dependencies are correctly installed and your Python environment is properly configured. If you encounter any issues during installation, check the troubleshooting section or contact our support team.

## Docker Image

### Prerequisites

Before installing NexScan using Docker, ensure you have the following prerequisites:

- Docker Engine installed and running on your system
- Internet connection for pulling Docker images
- Basic understanding of Docker commands and container management

Note: Docker installation varies by operating system. Please refer to the official Docker documentation for system-specific installation instructions.

### Procedure

Follow these steps to install NexScan using Docker:

```bash
# Pull the NexScan Docker image
docker pull harshmurjani/nexscan:latest

# Verify the image
docker images | grep nexscan

# Create a container and run NexScan
docker run -it --rm harshmurjani/nexscan:latest
```

After running these commands, you'll have access to all NexScan features within the Docker container. The container provides an isolated environment with all required dependencies pre-installed.

To persist output data, you can mount a local directory to the container:

```bash
docker run -it -v $(pwd)/output:/app/nexscan --name nexscan nexeosecurity/nexscan:latest
```

This will create an 'nexscan' directory in your current location that's mapped to the container's output folder.

# Usage

## **Windows**

NexScan provides several powerful features through its command-line interface. Below are detailed instructions for using each major functionality. All commands follow a consistent structure and support various optional parameters for customization.

### Directory Fuzzing

Directory fuzzing is a feature that allows scanning web directories to discover hidden files and folders.

**Default**

```bash
python ./NexScan.py directory -T https://nexeosecurity.tech
```

The above command will start directory fuzzing on the target URL using default wordlists and settings.

**Verbose Fuzzing**

To enable verbose output during directory fuzzing:

```bash
python ./NexScan.py directory -T https://nexeosecurity.tech -v
```

This will display detailed information about the scanning process, including:

- Request/response details
- Status codes for each discovered path
- Timing information
- Error messages and warnings

### SubDomain Fuzzing

Subdomain fuzzing helps discover subdomains of a target domain.

**Default**

For basic subdomain fuzzing operations, use the default command as shown below. This will start the fuzzing process using the built-in wordlist and default settings to discover potential subdomains.

```bash
python ./NexScan.py subdomain -T https://nexeosecurity.tech

```

**Verbose Fuzzing**

For verbose subdomain fuzzing, use the -v flag to enable detailed output. This will show additional information such as response times, DNS resolution details, and any errors encountered during the scanning process. The verbose output is particularly useful for debugging or when you need to analyze the scanning behavior in detail.

```bash
python ./NexScan.py subdomain -T https://nexeosecurity.tech -v
```

### SMB Enumeration

The SMB enumeration module allows scanning and enumerating SMB shares. Here are the different ways to use this module:

**With username and password file**

This command allows you to perform SMB enumeration using a specific username and a list of passwords from a file. The tool will systematically attempt to authenticate using each password in the specified list, making it useful for security testing of SMB services.

```bash
python ./NexScan.py smb -T 127.0.0.1 -u kali -P password_list.txt
```

**With userfile and password**

This command allows you to perform SMB enumeration by providing a list of usernames in a file and a single password. This method is useful when testing multiple potential usernames against a known or common password.

```bash
python ./NexScan.py smb -T 127.0.0.1 -U user_list.txt -p kali
```

**With userfile and password file**

This command enables you to perform SMB enumeration using both a list of usernames and a list of passwords from separate files. This method provides the most comprehensive testing capability as it attempts all possible combinations of usernames and passwords. The tool will systematically work through both lists to attempt authentication for each username-password pair.

```bash
python ./NexScan.py smb -T 127.0.0.1 -U user_list.txt -P password_list.txt
```

Optional arguments for SMB enumeration:

- -u, --user: Specify target username
- -U, --userfile: Specify file containing list of usernames
- -p, --password: Specify single password
- -P, --passwordfile: Specify password list file
- -T, --target: option specifies the target for the scan

### SSH Brute-force

The SSH brute-force module attempts to gain unauthorized access to SSH servers by testing multiple username and password combinations. Use this command:

Here are the different ways to use the SSH brute-force module:

**With username and password file**

This command attempts SSH authentication using a specified username and a list of passwords from a file. The tool will systematically try each password in the list until a successful authentication is found or the list is exhausted. This method is particularly useful when testing against a known username.

```bash
python ./NexScan.py ssh -T 127.0.0.1 -u kali -P password_list.txt
```

**With userfile and password**

This command allows you to test multiple usernames from a file against a single specified password. This approach is useful when you have a list of potential usernames and want to check them against a known or commonly used password. The usernames are read sequentially from the specified file, and each is tested with the provided password.

```bash
python ./NexScan.py ssh -T 127.0.0.1 -U user_list.txt -p kali
```

**With userfile and password file**

This command performs the most comprehensive SSH brute-force attempt by using both a list of usernames and a list of passwords from separate files. The tool will systematically test each username-password combination, making it an effective method for thorough security testing. However, use this option carefully as it may generate significant network traffic and could trigger security alerts.

```bash
python ./NexScan.py ssh -T 127.0.0.1 -U user_list.txt -P password_list.txt
```

### FTP Brute-force

The FTP brute-force module attempts to gain unauthorized access to FTP servers by testing multiple username and password combinations.

Here are the different ways to use the FTP brute-force module:

**Default command**

The default command initiates a basic FTP brute-force attempt against the specified target IP address. This command uses built-in wordlists and default settings to perform the authentication attempts. While this is the simplest form of the command, it provides a good starting point for initial reconnaissance.

```bash
python ./NexScan.py ftp -T 127.0.0.1
```

**With verbose output**

Adding verbose output provides detailed information about each FTP authentication attempt, including connection details, timing information, and full response messages. This level of detail is particularly useful for debugging connection issues or understanding the server's behavior during testing.

```bash
python ./NexScan.py ftp -T 127.0.0.1 -v
```

**With stop on success option**

The stop on success option halts the brute-force process as soon as valid credentials are found. This is useful when you only need to verify if the target is vulnerable to unauthorized access and want to minimize network traffic.

```bash
python ./NexScan.py ftp -T 127.0.0.1 -s
```

**With both verbose and stop on success options**

```bash
python ./NexScan.py ftp -T 127.0.0.1 -s -v
```

Optional arguments for FTP brute-force:

- -p, --password: Specify single password
- -P, --passwordlist: Specify password list file
- -s, --stop: Stop on first successful login
- -v, --verbose: Enable verbose output
- -o, --output: Save results to specified output file
- -T, --target: option specifies the target for the scan.

### MySQL Brute-force

The MySQL brute-force module attempts to gain unauthorized access to MySQL servers by testing multiple username and password combinations. Use this command:

```bash
python NexScan.py mysqlbrute -t 127.0.0.1 -u username -w lists/password_list.txt
```

Optional arguments for MySQL brute-force:

- -u, --user: Specify target username
- -U, --userlist: Specify file containing list of usernames
- -w, --wordlist: Custom password wordlist (default: lists/password_list.txt)
- -t, --threads: Number of concurrent threads (default: 5)
- -o, --output: Save results to specified output file

## **macOS/linux/unix**

For macOS/Linux/unix systems, the commands are similar but with slight modifications in syntax:

### Directory Fuzzing

Directory fuzzing is a feature that allows scanning web directories to discover hidden files and folders.

Default

```bash
./NexScan.py directory -T https://nexeosecurity.tech
```

The above command will start directory fuzzing on the target URL using default wordlists and settings.

**Verbose Fuzzing**

To enable verbose output during directory fuzzing:

```bash
./NexScan.py directory -T https://nexeosecurity.tech -v
```

This will display detailed information about the scanning process, including:

- Request/response details
- Status codes for each discovered path
- Timing information
- Error messages and warnings

### Subdomain Fuzzing

Subdomain fuzzing helps discover subdomains of a target domain. Use this command:

**Default**

```bash
./NexScan.py subdomain -T https://nexeosecurity.tech
```

**Verbose Fuzzing**

```bash
./NexScan.py subdomain -T https://nexeosecurity.tech -v
```

### SMB Enumeration

**With username and password file**

This command attempts SSH authentication using a specified username and a list of passwords from a file. The tool will systematically try each password in the list until a successful authentication is found or the list is exhausted. This method is particularly useful when testing against a known username.

```bash
./NexScan.py smb -T 127.0.0.1 -u kali -P password_list.txt
```

**With userfile and password**

This command allows you to test multiple usernames from a file against a single specified password. This approach is useful when you have a list of potential usernames and want to check them against a known or commonly used password. The usernames are read sequentially from the specified file, and each is tested with the provided password.

```bash
./NexScan.py smb -T 127.0.0.1 -U user_list.txt -p kali
```

**With userfile and password file**

This command performs the most comprehensive SSH brute-force attempt by using both a list of usernames and a list of passwords from separate files. The tool will systematically test each username-password combination, making it an effective method for thorough security testing. However, use this option carefully as it may generate significant network traffic and could trigger security alerts.

```bash
./NexScan.py smb -T 127.0.0.1 -U user_list.txt -P password_list.txt
```

Optional arguments for SMB enumeration:

- -u, --user: Specify target username
- -U, --userlist: Specify file containing list of usernames
- -p, --password: Specify single password
- -P, --passwordlist: Specify password list file
- -o, --output: Save results to specified output file

### SSH Brute-force

The SSH brute-force module attempts to gain unauthorized access to SSH servers by testing multiple username and password combinations. Use this command:

Here are the different ways to use the SSH brute-force module:

**With username and password file**

This command attempts SSH authentication using a specified username and a list of passwords from a file. The tool will systematically try each password in the list until a successful authentication is found or the list is exhausted. This method is particularly useful when testing against a known username.

```bash
./NexScan.py ssh -T 127.0.0.1 -u kali -P password_list.txt
```

**With userfile and password**

This command allows you to test multiple usernames from a file against a single specified password. This approach is useful when you have a list of potential usernames and want to check them against a known or commonly used password. The usernames are read sequentially from the specified file, and each is tested with the provided password.

```bash
./NexScan.py ssh -T 127.0.0.1 -U user_list.txt -p kali
```

**With userfile and password file**

This command performs the most comprehensive SSH brute-force attempt by using both a list of usernames and a list of passwords from separate files. The tool will systematically test each username-password combination, making it an effective method for thorough security testing. However, use this option carefully as it may generate significant network traffic and could trigger security alerts.

```bash
./NexScan.py ssh -T 127.0.0.1 -U user_list.txt -P password_list.txt
```

### FTP Brute-force

The FTP brute-force module attempts to gain unauthorized access to FTP servers by testing multiple username and password combinations.

Here are the different ways to use the FTP brute-force module:

**Default command**

The default command initiates a basic FTP brute-force attempt against the specified target IP address. This command uses built-in wordlists and default settings to perform the authentication attempts. While this is the simplest form of the command, it provides a good starting point for initial reconnaissance.

```bash
./NexScan.py ftp -T 127.0.0.1
```

**With verbose output**

Adding verbose output provides detailed information about each FTP authentication attempt, including connection details, timing information, and full response messages. This level of detail is particularly useful for debugging connection issues or understanding the server's behavior during testing.

```bash
./NexScan.py ftp -T 127.0.0.1 -v
```

**With stop on success option**

The stop on success option halts the brute-force process as soon as valid credentials are found. This is useful when you only need to verify if the target is vulnerable to unauthorized access and want to minimize network traffic.

```bash
./NexScan.py ftp -T 127.0.0.1 -s
```

Optional arguments for FTP brute-force:

- -T, --target: option specifies the target for the scan.
- -v, --verbose: Enable verbose output
- -o, --output: Save results to specified output file

### MySQL Brute-force

```bash
./NexScan.py mysqlbrute -t 127.0.0.1 -u username -w lists/password_list.txt
```

Optional arguments for MySQL brute-force:

- -u, --user: Specify target username
- -U, --userlist: Specify file containing list of usernames
- -w, --wordlist: Custom password wordlist (default: lists/password_list.txt)
- -p, --port: Specify custom MySQL port (default: 3306)
- -o, --output: Save results to specified output file

Note: Make sure to set appropriate execute permissions using:

```bash
chmod +x NexScan.py
```

# Developer Section

## Project Directory Structure

- modules/
    - NexDir.py
    - NexFTP.py
    - NexMySql.py
    - NexSMB.py
    - NexSSH.py
    - NexSubD.py
- lists/
    - directory_list.txt
    - password_list.txt
    - subdomain_list.txt
    - user_list.txt
- NexScan.py

## Scope of Improvement

- GUI Implementation
- AI Integration to identify vulnerabilities based on scans
- Implementation of Project workspace

# Contributor Section

If you’d like to support NexScan development personally, consider making a small donation (Buy me a coffee). Your contributions will help keep the project active and enable new features.

# Sponsor Section

For high-capital individuals or corporate organizations, sponsorship opportunities are available. Sponsors receive benefits such as early access to features, logo placements, and direct collaboration opportunities.

For sponsorship inquiries, please contact us at [business@nexeosecurity.tech](mailto:business@nexeosecurity.tech).

# Disclaimer

NexScan is intended for ethical use. Unauthorized use of this tool against systems without explicit permission is strictly prohibited and may violate legal regulations.
