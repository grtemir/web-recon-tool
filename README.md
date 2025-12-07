


#Web Reconnaissance Tool 🕵️‍♂️

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
````

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install requests beautifulsoup4
    ```

## 💻 Usage

Run the tool directly from the terminal:

```bash
python recon_tool.py
```

1.  The script will ask for a **Target URL**.
2.  Enter the URL (e.g., `http://testphp.vulnweb.com/`).
3.  The tool will scan the page and print findings to the terminal.
4.  A detailed report will be saved as `recon_report.txt`.

## 📂 Output Example (recon\_report.txt)

```text
Target url: [http://testphp.vulnweb.com/](http://testphp.vulnweb.com/)
Scanning time: 2025-12-07 14:30:22.123456
------------------------------
[EMAILS FOUND] (2)
admin@vulnweb.com
support@testphp.com

------------------------------
[LINKS FOUND] (15)
[http://testphp.vulnweb.com/categories.php](http://testphp.vulnweb.com/categories.php)
[http://testphp.vulnweb.com/login.php](http://testphp.vulnweb.com/login.php)
...
```

## ⚠️ Disclaimer

This tool is created for **Educational Purposes Only**.
The usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

```
```
