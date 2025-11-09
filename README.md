# 🌞 Solar Challenge Week 0: Data Profiling & EDA

## 📌 Objective
This project focuses on profiling, cleaning, and exploring solar radiation datasets from African countries. The goal is to prepare high-quality data for regional comparison and ranking based on solar potential.

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/rahel-yab/solar-challenge-week0.git
```
## Create and activate a virtual environment

 ```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```
---
## 🚀 How to Run EDA

- Open notebooks/togo_eda.ipynb in VS Code or Jupyter
- Run cells to:
- Profile missing values
- Detect and clean outliers
- Visualize solar and weather trends
- Export cleaned data to data/togo_clean.csv

---
## 📊 Key Features

- Summary statistics and null analysis
- Z-score based outlier detection
- Time series plots of solar irradiance and temperature
- Correlation heatmaps and scatter plots
- Wind rose and distribution histograms
- Bubble charts for RH/BP vs. solar metrics

---

Note
- Ensure CSVs used by notebooks are present under raw_data/.
