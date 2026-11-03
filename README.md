# 🔐 Failed Login Log Analyzer

A Python-based cybersecurity tool that analyzes login log files, identifies failed login attempts, tracks suspicious IP addresses, and generates a security report.

## 📌 About the Project

The **Failed Login Log Analyzer** is a beginner-friendly cybersecurity project developed using Python.

It reads log files, detects failed login attempts, extracts and validates IP addresses, and counts the number of failed attempts from each IP address.

If an IP address exceeds a predefined failure threshold, the program flags it as suspicious.

The tool also generates a `report.txt` file containing the analysis results.

## ✨ Features

- **Log File Analysis:** Reads login logs line by line.
- **Failed Login Detection:** Identifies failed login attempts while ignoring successful logins.
- **IP Address Extraction:** Extracts IP addresses from log entries.
- **IP Validation:** Validates IPv4 and IPv6 addresses using Python's built-in `ipaddress` module.
- **Attempt Tracking:** Uses Python dictionaries to count failed attempts per IP address.
- **Suspicious IP Detection:** Flags IP addresses that reach or exceed the configured threshold.
- **Error Handling:** Handles missing files and malformed log entries.
- **Command-Line Arguments:** Allows users to specify which log file to analyze.
- **Report Generation:** Automatically generates a `report.txt` file containing the analysis.

## 🛠️ Technologies Used

- **Python 3**
- File Handling
- Dictionaries
- Functions
- Exception Handling
- `sys` module
- `ipaddress` module
- Git and GitHub

## 📂 Project Structure

```text
failed_login_analyzer/
│
├── main.py
├── sample.log
├── test.log
├── report.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AryanMauryahere/failed_login_analyzer.git
```

### 2. Navigate to the project directory

```bash
cd failed_login_analyzer
```

### 3. Run the program

```bash
python main.py sample.log
```

No external Python packages are required. The project uses Python's built-in modules.

## 💻 Usage

Provide the log filename as a command-line argument:

```bash
python main.py sample.log
```

You can also analyze another log file:

```bash
python main.py test.log
```

If no filename is provided, the program displays usage instructions.

## 📝 Sample Log File

Example entries from `sample.log`:

```text
FAILED user=admin ip=192.168.1.10
SUCCESS user=aryan ip=192.168.1.12
FAILED user=root ip=192.168.1.10
FAILED user=test ip=192.168.1.10
FAILED user=guest ip=192.168.1.15
FAILED user=admin ip=192.168.1.15
FAILED user=root ip=192.168.1.20
```

## 📊 Sample Analysis

Example terminal output:

```text
Failed login summary:

192.168.1.10 : 3 failed attempts
192.168.1.15 : 2 failed attempts
192.168.1.20 : 1 failed attempts

Suspicious IPs:

192.168.1.10
```

The program also generates a `report.txt` file containing the analysis.

## 🎯 Learning Objectives

This project helped me understand and practice:

- Python file handling and reading log files.
- Working with dictionaries and strings.
- Extracting and validating IP addresses.
- Writing reusable Python functions.
- Handling exceptions and invalid input.
- Using command-line arguments.
- Applying basic cybersecurity log analysis techniques.
- Managing projects using Git and GitHub.

## 🚀 Future Improvements

- Add configurable failure thresholds.
- Include timestamps in generated reports.
- Generate CSV reports.
- Detect repeated failed attempts within a specific time window.
- Add graphical visualizations of login activity.
- Support more log formats.

## ⚠️ Disclaimer

This project is intended for educational purposes and basic defensive security log analysis.

Use it only with fictional logs or log files that you own or are authorized to analyze. A suspicious IP address is an indicator for further investigation, not proof of malicious activity.

## 👨‍💻 Author

**Aryan Maurya**

[GitHub](https://github.com/AryanMauryahere) · [LinkedIn](https://www.linkedin.com/in/aryan-maurya-96999734b/)
