# AnyDesk-7.0.15---Unquoted-Service-Path-PoC
This script serves as a proof of concept (PoC) for the CVE-2024-XXXX vulnerability in AnyDesk version 7.0.15. The vulnerability involves an unquoted service path, allowing an authorized but non-privileged local user to potentially execute arbitrary code with elevated privileges on the system.

# Functionality

## The script provides the following functionality:

- Check AnyDesk Service Configuration: Allows you to query the service configuration of the AnyDesk service, including its binary path.

- View System Information: Displays system information using the systeminfo command.

- Run Custom Command: If the AnyDesk service path is correctly identified as unquoted and an AnyDesk connection is in progress, you can input a custom command to be executed with elevated privileges.

- Error Handling: Includes error handling to gracefully handle any unexpected issues during execution.

## Usage
Setup Environment

- Python Installation: Ensure you have Python installed on your system. If not, download and install Python from the official website.

- Clone Repository: Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/AnyDesk-Unquoted-Service-Path-PoC.git](https://github.com/blackmagic2023/AnyDesk-7.0.15---Unquoted-Service-Path-PoC.git
```

- Navigate to Directory: Change directory to the cloned repository:

```bash
cd AnyDesk-7.0.15---Unquoted-Service-Path-PoC
```

- Install Requirements: Install the required Python libraries by running:
```python
pip install -r requirements.txt
```

## Running the Script

- Ensure AnyDesk is Installed and Running: Before running the script, make sure AnyDesk is installed and running on your system.

- Establish an AnyDesk Connection: Additionally, an AnyDesk connection must be in progress for the script to work. This ensures that the service path vulnerability is exploitable.

- Run the Python script anydesk_poc.py using the following command:

```bash
    python anydesk_poc.py
```
   
Follow the instructions provided by the script to perform various actions.
- Check AnyDesk service configuration.
- View system information.
- Run a custom command (if service path is correct and an AnyDesk connection is in progress).
- Exit the program.

## Disclaimer

This PoC script is provided for educational and informational purposes only. Use it responsibly and only on systems you have permission to test. The author takes no responsibility for any misuse or damage caused by the use of this script.
Author

BlackMagic
Vulnerability Information

AnyDesk 7.0.15 has been found to have an unquoted service path vulnerability, potentially allowing an attacker to execute arbitrary code with elevated privileges on the system. This vulnerability has been assigned CVE-2024-XXXX. AnyDesk users are advised to update to the latest version to mitigate this issue.
