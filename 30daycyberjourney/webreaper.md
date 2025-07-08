WebReaper - Reconnaissance Automation Tool
WebReaper is a Python-based tool that automates reconnaissance tasks for cybersecurity assessments. It performs DNS lookups, WHOIS queries, subdomain/email harvesting, and banner grabbing on a target domain.
Features

DNS Lookup: Enumerates DNS records using dnsrecon.
WHOIS Lookup: Retrieves domain registration details using the system whois command.
Subdomain & Email Harvesting: Discovers subdomains and emails with theHarvester.
Banner Grabbing: Fetches HTTP headers using curl.
Automatically installs dependencies on Linux (supports apt and yum).
Saves results in timestamped folders for easy analysis.
Robust error handling and user-friendly output.

Requirements

Linux system with Python 3.
Administrative privileges (sudo) for installing dependencies.
Internet connection for tool installation and scans.

Installation

Clone the repository:git clone https://github.com/CyberAriYehuda/CyberAriYehuda.git


Navigate to the webreaper folder:cd webreaper


Make the script executable:chmod +x webreaper.py



Usage
Run the script with a target domain:
./webreaper.py -d example.com

Results are saved in webreaper_results/<domain>_<timestamp>/ with files:

dnsrecon.txt
whois.txt
theharvester.txt
banner.txt

Example
./webreaper.py -d google.com

Output:
🚀 WebReaper started for google.com at 2025-05-02 12:34:56

[*] Running dnsrecon...
[+] DNSRecon completed.
[*] Running WHOIS lookup...
[+] WHOIS info saved.
[*] Running theHarvester...
[+] theHarvester completed.
[*] Performing basic banner grabbing (port 80)...
[+] Banner grabbing completed.

✅ All recon tasks completed for google.com. Results saved in 'webreaper_results/google.com_20250502_123456'.

Notes

Legal: Only scan domains you have permission to analyze to avoid legal issues.
Dependencies: The script automatically installs dnsrecon, theHarvester, curl, and whois using apt or yum. Ensure you have sudo privileges.
Supported Systems: Works on Linux distributions with apt (Debian/Ubuntu) or yum (CentOS/RHEL). Contact the maintainer for other package managers.

Contributing
Feel free to fork this repository, submit pull requests, or open issues to suggest improvements!
License
This project is licensed under the MIT License.
Author
Joel Chinta - Created as part of the Cybersecurity 90 Days Challenge (Day 5).
#Cybersecurity #Python #Reconnaissance
