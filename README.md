# Web Reconnaissance Tool 🕵️‍♂️

A Python-based **OSINT (Open Source Intelligence)** tool designed to harvest links and extract email addresses from target websites. This project demonstrates the practical application of HTTP requests, HTML parsing, and Regular Expressions (Regex) in a cybersecurity context.

Built for **educational purposes** and ethical hacking / blue team operations.

## 🚀 Features

- **🛡️ WAF Evasion:** Uses custom HTTP Headers (User-Agent Spoofing) to bypass basic security filters and `403 Forbidden` errors.
- **📧 Email Hunter:** Scans the target website's source code using **Regex** to extract hidden email addresses.
- **🔗 Link Harvester:** Parses HTML DOM structure to collect and filter valid internal/external URLs.
- **📝 Automated Reporting:** Saves all findings into a timestamped file (`recon_report.txt`) for further analysis.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `requests` (HTTP Connection)
  - `beautifulsoup4` (HTML Parsing)
  - `re` (Regular Expressions)
  - `datetime` (Timestamping)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/grtemir/web-recon-tool.git](https://github.com/grtemir/web-recon-tool.git)
   cd web-recon-tool
