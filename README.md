# 🚀 pydahua – Python Library for Dahua Biometric & Access Control Devices

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-LGPL--3.0-green)](https://www.gnu.org/licenses/lgpl-3.0.html)
![PyPI Downloads](https://img.shields.io/pypi/dm/pydahua)
![GitHub stars](https://img.shields.io/github/stars/KSreethul/pydahua)

Stop struggling with Dahua HTTP APIs and messy responses.

**pydahua** is a clean, production-ready Python library that helps you interact with Dahua biometric and access control devices effortlessly.

✔ No manual API construction
✔ Clean Python methods
✔ Structured responses (no raw parsing headaches)
✔ Built for real-world systems

Perfect for **HRMS, attendance systems, access control, and automation tools**.

---

## ⚡ Quick Start (2 Minutes)

```python
from pydahua import DahuaAPI

dahua = DahuaAPI(
    ip="http://192.168.1.100",
    username="admin",
    password="password"
)

# Fetch system info
print(dahua.get_system_info())

# Fetch attendance logs
print(dahua.fetch_attendance_logs())
```

That’s it. You're connected.

---

## 📦 Installation

Install from PyPI:

```bash
pip install pydahua
```

---

## ❓ Why pydahua?

Working directly with Dahua APIs is frustrating:

* Responses come in raw key-value format
* Authentication requires HTTP Digest handling
* Logs are hard to structure
* API endpoints are not intuitive

**pydahua solves this by:**

* 🔐 Handling HTTP Digest authentication internally
* 🔄 Converting raw responses into structured dictionaries
* 📊 Converting logs into clean Python lists
* ⚙️ Providing simple, readable methods
* ✅ Validating inputs before sending requests

So you can focus on your application—not reverse-engineering APIs.

---

## ✨ Features

* 📊 Attendance Logs (fetch + structured parsing)
* 👤 User Management (add / delete / fetch users)
* 🪪 Access Card Enrollment & tracking
* ⚙️ Device Configuration (network, system, language)
* 🕒 Time & Localization control
* 🔁 Device Operations (reboot, shutdown)
* 📄 Structured API responses (no raw parsing)
* 🔐 HTTP Digest authentication support

---

## 🛠 Real-World Usage

This library is used in real systems to:

* Sync biometric attendance with backend systems
* Manage access control users and cards
* Process large volumes of attendance logs
* Automate device configuration

Tested with real Dahua biometric devices.

---

## 🔌 Common Use Cases

* HRMS / Employee Management Systems
* Attendance Tracking Systems
* Access Control Systems
* Security & Surveillance Integrations

---

## 📄 Example Usage

### Get system information

```python
system_info = dahua.get_system_info()
print(system_info)
```

---

### Add a new user

```python
dahua.add_user(
    username="john",
    password="1234",
    group="admin",
    sharable=True,
    reserved=False
)
```

---

### Enroll access card

```python
dahua.enroll_new_user(
    card_name="John Doe",
    card_no="123456",
    user_id="JD1001",
    password="Pass@123"
)
```

---

### Fetch attendance logs

```python
from datetime import datetime

logs = dahua.get_control_card_rec(
    card_no="123456",
    start_time=datetime(2025, 1, 1, 0, 0, 0),
    end_time=datetime(2025, 1, 18, 23, 59, 59)
)

print(logs)
```

---

### Set system time

```python
dahua.set_system_time(
    date="2025-10-18",
    time="23:00:00"
)
```

---

## 📄 Example Log Output

```json
{
  "records": [
    {
      "card_no": "123456",
      "card_name": "John Doe",
      "attendance_state": "CheckIn",
      "door": "1",
      "create_time": "2025-01-18T09:12:33"
    }
  ],
  "found": 1,
  "status_code": 200
}
```

---

## 🔌 Supported Devices

Works with Dahua devices that support:

* `magicBox.cgi`
* `configManager.cgi`
* `userManager.cgi`
* `recordFinder.cgi`

👉 Check your device API documentation to confirm compatibility.

---

## 📚 API Coverage

### System Info

* `get_system_info()`
* `get_serial_number()`
* `get_hardware_version()`
* `get_device_type()`

### User Management

* `add_user()`
* `delete_user()`
* `get_user_info()`
* `get_user_info_all()`

### Access Control

* `enroll_new_user()`
* `get_control_card_rec()`

### Logs

* `fetch_attendance_logs()`
* `get_logs()`

### Configuration

* `get_general_config()`
* `set_general_config()`
* `get_basic_config()`
* `set_basic_config()`
* `get_record_config()`
* `set_record_config()`

### Time & Language

* `get_system_time()`
* `set_system_time()`
* `get_language_config()`
* `set_language_config()`

### Device Operations

* `reboot_device()`
* `shutdown_device()`

---

## 🚧 Roadmap

* [ ] Async support
* [ ] More endpoint wrappers
* [ ] Better error handling
* [ ] Webhook/event-based integrations

---

## 🤝 Contributing

Contributions are welcome!

You can help with:

* Adding new API endpoints
* Improving documentation
* Writing usage examples

### Steps:

1. Fork the repo
2. Create a branch: `git checkout -b feature-name`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **LGPL-3.0 License**
👉 [https://www.gnu.org/licenses/lgpl-3.0.html](https://www.gnu.org/licenses/lgpl-3.0.html)

---

## 🔗 Links

* GitHub: [https://github.com/KSreethul/pydahua](https://github.com/KSreethul/pydahua)
* Issues: [https://github.com/KSreethul/pydahua/issues](https://github.com/KSreethul/pydahua/issues)

---

## ⭐ Support

If this project helped you:

* ⭐ Star the repo
* 🐛 Report issues
* 🔁 Share with others

---

## 🎯 Final Note

This library was built to simplify real-world Dahua device integrations.

If you're working with biometric or access control systems,
**pydahua will save you hours of effort.**
