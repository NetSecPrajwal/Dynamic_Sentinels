# 🛡️ Dynamic Sentinel

**Dynamic Sentinel** is a Python-based malware detection tool designed to scan suspicious PDF files using a combination of **static** and **dynamic** analysis techniques. It provides insights into embedded objects, streams, suspicious keywords, and basic runtime behavior—all while keeping logs for forensic review.

---

## 📁 Features

- 🔍 **Static Analysis**  
  - Scans PDF headers, object counts, streams, and embedded elements  
  - Detects presence of JavaScript, embedded files, encryption, and suspicious actions

- ⚙️ **Dynamic Analysis** *(Basic)*  
  - Executes the file in a sandboxed environment with `strace` via `firejail`  
  - Captures system-level activity (like `open`, `execve`, etc.)  
  - Stores results in logs for manual inspection

- 📝 **Report Generation**  
  - Saves analysis report in `sandbox_logs/`  
  - Prints real-time results to console for quick review

---

## 📦 Project Structure

dynamic_sentinel_tool/
├── src/
│   ├── main.py
│   ├── static_scan.py
│   ├── dynamic_scan.py
│   ├── report.py
├── sandbox_logs/
├── requirements.txt
└── README.md

