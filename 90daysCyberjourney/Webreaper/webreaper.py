#!/usr/bin/env python3
import subprocess
import argparse
import os
from datetime import datetime
import sys
import platform

# Detect package manager
def get_package_manager():
    if os.path.exists("/usr/bin/apt"):
        return "apt"
    elif os.path.exists("/usr/bin/yum"):
        return "yum"
    return None

# Install dependencies automatically
def install_dependencies():
    package_manager = get_package_manager()
    if not package_manager:
        print("[!] No supported package manager found (apt or yum). Please install dependencies manually.")
        sys.exit(1)

    tools = {
        "dnsrecon": "dnsrecon",
        "theHarvester": "theharvester",
        "curl": "curl",
        "whois": "whois"
    }
    python_packages = ["theHarvester"]

    print("[*] Checking and installing dependencies...")
    
    # Install system tools
    for tool, pkg in tools.items():
        result = subprocess.run(["which", tool], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[*] Installing {pkg}...")
            try:
                if package_manager == "apt":
                    subprocess.run(["sudo", "apt", "update"], check=True, capture_output=True)
                    subprocess.run(["sudo", "apt", "install", "-y", pkg], check=True, capture_output=True)
                elif package_manager == "yum":
                    subprocess.run(["sudo", "yum", "install", "-y", pkg], check=True, capture_output=True)
                print(f"[+] {pkg} installed.")
            except subprocess.CalledProcessError as e:
                print(f"[!] Failed to install {pkg}: {e}")
                sys.exit(1)

    # Install Python packages
    for pkg in python_packages:
        try:
            __import__(pkg)
        except ImportError:
            print(f"[*] Installing Python package {pkg}...")
            try:
                subprocess.run(["pip3", "install", pkg], check=True, capture_output=True)
                print(f"[+] {pkg} installed.")
            except subprocess.CalledProcessError as e:
                print(f"[!] Failed to install Python package {pkg}: {e}")
                sys.exit(1)

# Create folder for output
def create_output_folder(domain):
    folder = f"webreaper_results/{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(folder, exist_ok=True)
    return folder

# DNS Lookup using dnsrecon
def run_dnsrecon(domain, output_folder):
    print("[*] Running dnsrecon...")
    try:
        output_file = os.path.join(output_folder, "dnsrecon.txt")
        result = subprocess.run(
            ["dnsrecon", "-d", domain, "-a", "-n", "8.8.8.8"],
            stdout=open(output_file, "w"),
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stderr:
            print(f"[!] dnsrecon warnings/errors: {result.stderr}")
        print("[+] DNSRecon completed.")
    except Exception as e:
        print(f"[!] Error in dnsrecon: {e}")

# WHOIS Lookup using system whois command
def run_whois(domain, output_folder):
    print("[*] Running WHOIS lookup...")
    try:
        output_file = os.path.join(output_folder, "whois.txt")
        result = subprocess.run(
            ["whois", domain],
            stdout=open(output_file, "w"),
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stderr:
            print(f"[!] whois warnings/errors: {result.stderr}")
        print("[+] WHOIS info saved.")
    except Exception as e:
        print(f"[!] Error in whois lookup: {e}")

# Email & Subdomain Harvesting using theHarvester
def run_theHarvester(domain, output_folder):
    print("[*] Running theHarvester...")
    try:
        output_file = os.path.join(output_folder, "theharvester.txt")
        result = subprocess.run(
            ["theHarvester", "-d", domain, "-b", "all", "-f", output_file],
            stdout=open(output_file, "a"),
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stderr:
            print(f"[!] theHarvester warnings/errors: {result.stderr}")
        print("[+] theHarvester completed.")
    except Exception as e:
        print(f"[!] Error in theHarvester: {e}")

# Banner grabbing
def banner_grabbing(domain, output_folder):
    print("[*] Performing basic banner grabbing (port 80)...")
    try:
        output_file = os.path.join(output_folder, "banner.txt")
        result = subprocess.run(
            ["curl", "-I", f"http://{domain}", "--connect-timeout", "5"],
            stdout=open(output_file, "w"),
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stderr:
            print(f"[!] curl warnings/errors: {result.stderr}")
        print("[+] Banner grabbing completed.")
    except Exception as e:
        print(f"[!] Error in banner grabbing: {e}")

# Main
if __name__ == "__main__":
    # Install dependencies
    install_dependencies()

    # Parse arguments
    parser = argparse.ArgumentParser(description="WebReaper - Recon Automation Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain name (e.g., example.com)")
    args = parser.parse_args()

    target_domain = args.domain.strip()
    if not target_domain:
        print("[!] Error: Domain cannot be empty.")
        sys.exit(1)

    output_folder = create_output_folder(target_domain)

    print(f"\n🚀 WebReaper started for {target_domain} at {datetime.now()}\n")

    # Run all tasks
    run_dnsrecon(target_domain, output_folder)
    run_whois(target_domain, output_folder)
    run_theHarvester(target_domain, output_folder)
    banner_grabbing(target_domain, output_folder)

    print(f"\n✅ All recon tasks completed for {target_domain}. Results saved in '{output_folder}'.\n")
