https://wifi-fall-monitor-portfolio.streamlit.app

# Privacy-First Wi-Fi CSI Fall & Inactivity Monitor (AAL)

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

+---------------------------------------------------------+
| ESP32 Microcontroller / Wi-Fi Router Node               |
| Streams Raw Channel State Information (CSI) via UDP     |
+---------------------------+-----------------------------+
| Subcarrier Amplitudes
v
+---------------------------------------------------------+
| Python Ingestion & Preprocessing Backend                |
| NumPy / Pandas: Phase filtering & rolling variance      |
+---------------------------+-----------------------------+
|
+--------------+--------------+
|                             |
v                             v
+-------------------------+   +-------------------------+
| Fall Detection Engine   |   | Inactivity Watchdog     |
| - High variance spike   |   | - Floor Flatline > 5min |
| - Sharp signal drop     |   | - Bed Stillness > 1hr   |
+------------+------------+   +------------+------------+
|                             |
+--------------+--------------+
| Anomaly Triggered
v
+---------------------------------------------------------+
| FastAPI Webhook & Automated SOS Dispatch                |
| Sends instant alert to caregiver / emergency contact    |
+---------------------------------------------------------+

## 🛠️ Tech Stack

* **Language:** Python
* **Data Processing & Signal Analysis:** NumPy, Pandas, Collections
* **HMI & Dashboard:** Streamlit
* **Integration & Alerting:** FastAPI webhooks / Twilio-ready REST API hooks
