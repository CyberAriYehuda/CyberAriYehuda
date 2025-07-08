Lion's Pause: Day 4 - CLI Footprinting
Day 4: Back to Basics - Footprinting with CLI Tools
On day 4 of my 30-day cybersecurity learning streak, I hit a two-week posting delay due to an urgent project deadline. Now, I’m back, diving into footprinting using CLI tools: dnsenum, whois, and nikto. Below is a breakdown of footprinting and how these tools work in action.

What is Footprinting?
Footprinting is the initial phase of ethical hacking, where you gather data on a target (e.g., website, network) to map its structure and identify potential vulnerabilities. It can be passive (stealthy) or active (direct).
Goals:

Identify domains, subdomains, and IPs.
Gather contact and server details.
Find security weaknesses.


CLI Tools Used
1. dnsenum

Purpose: Enumerates DNS records to discover subdomains and associated IPs.
Usage: dnsenum example.com
Output: Lists subdomains (e.g., blog.example.com) and their IPs.
Use Case: Uncovered a client’s hidden subdomain, enabling proactive securing.

2. whois

Purpose: Retrieves domain registration information.
Usage: whois example.com
Output: Displays registrant details, contact email, and name servers.
Use Case: Identified outdated contact info, preventing potential domain hijacking.

3. nikto

Purpose: Scans web servers for vulnerabilities and misconfigurations.
Usage: nikto -h http://example.com
Output: Detects outdated software, exposed files, or weak configurations.
Use Case: Found a vulnerable Apache version, leading to a patching recommendation.


Back to Basics
dnsenum, whois, and nikto are simple yet powerful CLI tools. Footprinting requires patience to build a detailed target profile discreetly.
Key Takeaways:

Passive tools (whois, dnsenum) minimize detection risk.
Active scans (nikto) require explicit permission.
The basics lay the foundation for advanced reconnaissance.


Lion’s Return
After a project-driven pause, I’m back—like a lion—ready to conquer this 90-day challenge! Next up: combining dnsenum with additional recon tools to deepen my footprinting skills. Roar on! 🦁

Next Steps

Explore advanced recon tools to complement dnsenum.
Share more insights as I progress through the 30-day streak.

#Cybersecurity #EthicalHacking #Footprinting #CLI #30DayChallenge
