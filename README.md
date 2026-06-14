# CMAD-vis
**Convolution Matrix Anomaly Detection (CMAD)**

An automated web-based research tool for detecting anomalous Antarctic sea ice melt using official NOAA NSIDC daily satellite imagery.

---

## 🌎 Overview

CMAD enables users to detect anomalous Antarctic melt events by simply entering two dates.

Instead of uploading images manually, the system:

- Automatically downloads official NOAA NSIDC v4.0 Antarctic sea ice imagery
- Crops the full Antarctic region
- Compares baseline (t-n) and target (t) dates
- Detects anomalous melt regions
- Generates a visual anomaly overlay

This ensures scientific consistency and removes user-upload variability.

---

## 🛰 Data Source

The tool automatically retrieves data from:

- **NOAA / NSIDC Sea Ice Index (Version 4.0)**
- Daily Antarctic sea ice concentration imagery

Data is fetched dynamically based on user-provided dates.

---

## 🔬 Motivation

Antarctic sea ice plays a critical role in:

- Global climate regulation  
- Ocean circulation  
- Ecosystem stability  

Recent variability in Antarctic sea ice extent has highlighted the need for:

- Rapid anomaly detection  
- Automated daily comparison  
- Spatio-temporal melt monitoring  

CMAD provides an automated framework for detecting abnormal melt behavior between two time points.

---

## ⚙️ Features

- 📅 Date-based input (YYYYMMDD)
- 🛰 Automatic NOAA NSIDC data download
- ✂ Automatic Antarctic region cropping
- 🧠 CMAD anomaly detection algorithm
- 📊 Visual anomaly overlay generation
- 📥 Downloadable processed result
- 🔒 Backend date validation
- 🌐 Web-based interface (Flask)

---

## 🧮 How It Works

1. User enters:
   - Baseline date (t-n)
   - Target date (t)

2. The system:
   - Validates date format and logical ordering
   - Downloads NOAA Antarctic daily images
   - Crops the Antarctic region
   - Applies CMAD anomaly detection
   - Highlights abnormal melt regions

3. Output:
   - Melt anomaly visualization
   - Downloadable anomaly image
  
## 🚀 Setup & Run

1. Clone the repository:
```bash
git clone https://github.com/iharp-institute/CMAD-Web-Application.git
cd CMAD-Web-Application
```

2. (Recommended) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python app.py
```

5. Open your browser at:
   http://localhost:5000
> **Note:** The app uses PyTorch with Apple MPS (Metal) backend by default (`device1 = "mps"` in `cmad_core.py`). If running on a non-Apple-Silicon machine, change this to `"cuda"` (NVIDIA GPU) or `"cpu"`.
