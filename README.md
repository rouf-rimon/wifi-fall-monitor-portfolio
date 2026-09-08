# Privacy-First Wi-Fi CSI Fall & Inactivity Monitor (AAL)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-HMI-ff4b4b.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GDPR Compliant](https://img.shields.io/badge/Privacy-100%25%20Device--Free-success.svg)](https://gdpr-info.eu/)

An ambient assisted living (AAL) telemetry and monitoring pipeline designed for older adults or vulnerable individuals. The system analyzes router Wi-Fi Channel State Information (CSI) and subcarrier variance to detect human movement, sudden falls, and prolonged stillness in private zones (bathrooms/bedrooms) **without invasive cameras or wearables**.

---

## 🚀 Key Features

* **100% Privacy-First Architecture:** Eliminates cameras and wearable devices entirely, satisfying strict European data privacy standards (GDPR) for sensitive zones like bedrooms and bathrooms.
* **Sliding-Window Anomaly Detection:** Processes real-time subcarrier amplitude variance using NumPy to distinguish between standard motion and emergency states.
* **Dual-Watchdog Safety Timers:** 
  * *Floor Inactivity Watchdog:* Triggers an alert if zero movement (flatline variance) persists for **> 5 minutes** on the floor.
  * *Bed Stillness Watchdog:* Flags abnormal prolonged confinement in bed exceeding **> 1 hour** past expected morning hours.
* **Interactive Streamlit HMI:** A live simulation dashboard allowing operators/caregivers to test motion patterns, trigger simulated fall impacts, and monitor emergency webhook dispatch states.

---

## 📊 System Architecture
