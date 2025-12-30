# Banking Infrastructure Compliance Auditor

![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python)
![Standards](https://img.shields.io/badge/Standards-TIA--942-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge)

## 📌 Business Case
Financial institutions like **Santander** and **Banxico** require rigid adherence to infrastructure standards (TIA-942) to ensure 99.999% uptime. This tool automates the audit process for cabling infrastructure, validating that installed assets (Cat 6A/7A) meet the bandwidth requirements for high-frequency trading and core banking systems.

## ⚙️ How It Works
1.  **Input:** Ingests a CSV export of installed cable runs and test results (Fluke networks format).
2.  **Validate:** Checks against defined thresholds for **Next (Near-End Crosstalk)**, **Insertion Loss**, and **Length**.
3.  **Report:** Generates a compliance certification PDF for the PMO.

## 🚀 Usage

```bash
# Run the compliance check
python auditor.py --site="Banxico_DataCenter_Main"
```

## 💻 Code Logic
*Standard Validation:*

```python
def validate_standard(cable_type, length, margin):
    # Tier 4 Data Center Requirements
    standards = {
        'Cat6A': {'max_len': 90, 'min_margin': 3.0},
        'Cat7A': {'max_len': 100, 'min_margin': 5.0} # Required for Core Banking
    }
    
    spec = standards.get(cable_type)
    if length > spec['max_len']:
        return "FAIL: Length exceeds ISO/IEC 11801 limits"
    if margin < spec['min_margin']:
        return "FAIL: Signal margin below TIA-942 thresholds"
    
    return "PASS: Compliant"
```

## 💡 Why I Built This
During the **Santander HQ modernization**, manual verification of 5,000+ cable nodes was causing project delays. I wrote this script to auto-validate Fluke test results, reducing the acceptance phase from 2 weeks to 2 days.