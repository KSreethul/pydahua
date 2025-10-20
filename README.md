# pydahua
[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-LGPL--3.0-green)](https://www.gnu.org/licenses/lgpl-3.0.html)  
**DahuaAPI Python Library for Biometric and Access Control Devices**

`pydahua` is a Python library designed to simplify interaction with Dahua biometric devices and access control systems. It provides a set of high-level methods for managing users, fetching attendance logs, configuring device settings, and handling network or system parameters via HTTP API.

---

## Features

- Retrieve system information (serial number, hardware version, device type).
- Manage users:
  - Add, delete, and fetch user information.
  - Enroll new access control cards.
- Fetch attendance logs and offline records.
- Configure device settings:
  - Network, language, general system configuration.
  - Snapshot, record, and record mode configuration.
- Set system time and language.
- Reboot or shut down devices.
- Fully compatible with Python 3.10+.
- Lightweight and dependency minimal (`requests` only).

---

## Installation

Install via pip:

```bash
pip install pydahua
````

---

## Usage

```python
from pydahua import DahuaAPI
from datetime import datetime

# Initialize the Dahua API client
dahua = DahuaAPI(ip="http://192.168.1.100", username="admin", password="password")

# Get system information
system_info = dahua.get_system_info()
print(system_info)

# Fetch all users
users = dahua.get_user_info_all()
print(users)

# Enroll a new access control card
response = dahua.enroll_new_user(
    card_name="John Doe",
    card_no="123456",
    user_id="JD1001",
    password="Pass@123"
)
print(response)

# Fetch attendance records for a specific card
logs = dahua.get_control_card_rec(
    card_no="123456",
    start_time=datetime(2025, 1, 1, 0, 0, 0),
    end_time=datetime(2025, 1, 18, 23, 59, 59)
)
print(logs)

# Set system time
dahua.set_system_time(date="2025-10-18", time="23:00:00")
```

---

## Supported Devices

This library works with Dahua biometric and access control devices that support HTTP API endpoints. Confirm your device supports `magicBox.cgi`, `configManager.cgi`, `userManager.cgi`, and `recordFinder.cgi` endpoints.

---

## Documentation

* **System info**: `get_system_info()`, `get_serial_number()`, `get_hardware_version()`, `get_device_type()`
* **User management**: `add_user()`, `delete_user()`, `get_user_info()`, `get_user_info_all()`
* **Access cards**: `enroll_new_user()`, `get_control_card_rec()`
* **Logs**: `fetch_attendance_logs()`, `get_logs()`
* **Configuration**: `get_general_config()`, `set_general_config()`, `get_basic_config()`, `set_basic_config()`, `get_record_config()`, `set_record_config()`
* **Time & language**: `get_system_time()`, `set_system_time()`, `get_language_config()`, `set_language_config()`
* **Device operations**: `reboot_device()`, `shutdown_device()`

---

## Dependencies

* `requests>=2.0`

---

## License

This project is licensed under the **LGPL 3.0** License.

---

## Author

**Sreethul Krishna**
Email: [sreethulkrishna24@gmail.com](mailto:sreethulkrishna24@gmail.com)

## Project Links

* [GitHub Repository](https://github.com/KSreethul/pydahua)
* [Bug Tracker](https://github.com/KSreethul/pydahua/issues)