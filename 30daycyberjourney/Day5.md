Cybersecurity 30 Days Challenge - Day 5
Achievement: Built WebReaper Reconnaissance Tool
On Day 5 of my Cybersecurity 30 Days Challenge, I developed WebReaper, a Python script that automates reconnaissance tasks for cybersecurity assessments. This tool streamlines the process of gathering information about a target domain, making it a valuable asset for ethical hacking and penetration testing.
What is WebReaper?
WebReaper is a command-line tool that performs the following tasks:

DNS Lookup: Uses dnsrecon to enumerate DNS records.
WHOIS Lookup: Queries domain registration details using the system whois command.
Subdomain & Email Harvesting: Leverages theHarvester to discover subdomains and associated email addresses.
Banner Grabbing: Uses curl to retrieve HTTP headers from the target domain.

Key Features

Automatically installs dependencies (dnsrecon, theHarvester, curl, whois) on Linux systems using apt or yum.
Organizes output in timestamped folders for easy access.
Includes robust error handling and user-friendly console messages.
Runs on any Linux system with Python 3.

Challenges & Learnings

Dependency Management: Learned to automate tool and Python package installation, ensuring portability across Linux distributions.
Error Handling: Improved my ability to capture and display errors from external tools, making the script more reliable.
Reconnaissance Workflow: Gained a deeper understanding of how reconnaissance fits into the cybersecurity lifecycle.
Python Scripting: Enhanced my skills in subprocess management, file handling, and command-line argument parsing.

How to Run WebReaper

Clone the repository: git clone https://github.com/CyberAriYehuda/CyberAriYehuda.git
Navigate to the webreaper folder: cd webreaper
Make the script executable: chmod +x webreaper.py
Run the script: ./webreaper.py -d example.com

Results are saved in webreaper_results/<domain>_<timestamp>/.
Next Steps

Add support for more reconnaissance tools (e.g., nmap, gobuster).
Implement parallel task execution to improve performance.
Create a summary report from the collected data.

Repository
The WebReaper tool and this write-up are available in my GitHub repository:

WebReaper Tool
Day 5 Write-up

Reflections
Building WebReaper was a rewarding experience that combined technical scripting with practical cybersecurity applications. I'm excited to continue this challenge and share more tools with the community!
#Cybersecurity #Python #Reconnaissance #30DaysChallenge
