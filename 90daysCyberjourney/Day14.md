# 🧠 Day 14 – OS Command Injection (OWASP A01:2021 – Broken Access Control)

Today’s journey into the 90-Day Cybersecurity Challenge focused on **OS Command Injection** — one of the most dangerous and real-world impactful vulnerabilities.

## ✅ Labs Completed:
1. **Lab: OS command injection, simple case** ![simple injection](images/os.png)
2. **Lab: OS command injection with time delays**![Blind Delay](images/os2.png)

## 🔍 What I Did:
- Exploited a user input field to inject shell commands
- Used payloads like `& ping -c 10 127.0.0.1` to introduce time delays and confirm blind injection
- Understood how user input is passed unsanitized into backend system calls

## 🛠️ Impact:
- Remote Code Execution (RCE)  
- Full system compromise possible  
- Abuse of logic via unsanitized input

## 🛡️ Fixes:
- Never pass user input directly to system-level functions  
- Use whitelisting and secure APIs (e.g., subprocess with argument arrays)  
- Apply proper input validation and encoding

> “Put on the whole armor of God, that you may be able to stand against the schemes of the devil.” – Ephesians 6:11

#Cybersecurity #OWASP #CommandInjection #Vulnerability #RedTeam #BuildInPublic #90DayChallenge
