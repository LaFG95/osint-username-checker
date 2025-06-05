[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/LaFG95/osint-username-checker?style=social)](https://github.com/LaFG95/osint-username-checker/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/LaFG95/osint-username-checker)](https://github.com/LaFG95/osint-username-checker/issues)
[![GitHub forks](https://img.shields.io/github/forks/LaFG95/osint-username-checker?style=social)](https://github.com/LaFG95/osint-username-checker/network)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/LaFG95/osint-username-checker/issues)
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

