# 🔍 OSINT Username Checker

A powerful multithreaded Python tool to scan **100+ websites** for the existence of a given username. Results are displayed in the terminal and saved as a clickable HTML report for quick investigation.

---

## 📦 Features

- ✅ Scans 100+ social, dev, and community platforms
- ⚡ Blazing fast multithreaded requests (`ThreadPoolExecutor`)
- 🌐 Interactive HTML report with clickable links
- 📁 Customizable target sites via `osint_sites.json`
- 🛡️ User-agent headers to reduce detection and blocking

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- `git` (to clone repo)
- Internet connection

### 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/LaFG95/osint-username-checker.git
cd osint-username-checker
```
2. **Install dependencies**
```
python -m pip install -r requirements.txt
```
3. **Run the tool**
```
python osint.py

```
Enter a username when prompted. The tool will scan hundreds of services and generate an HTML report.

🗂 Example Output

After running, you’ll see:

![image](https://github.com/user-attachments/assets/1b3463f9-14b7-46de-8184-4e065e6571ed)

🔗 A file like osint_results_username.html will be created and automatically opened in your browser with all found links.



👨‍💻 Author

Made with ❤️ by LaFG95
Cybersecurity Student • OSINT Enthusiast

🛡️ Disclaimer
This tool is for educational and lawful investigative use only.
Do not use it for harassment, stalking, or any illegal activity.
You are responsible for how you use this software.

