# Machine Learning Midterm Assignment: Classification & K-Means Clustering

**Author:** Aslıhan Tanyeli
**University:** İstanbul Topkapı Üniversitesi - Bilgisayar Mühendisliği
**Course:** Machine Learning (Autumn 2026)

---

## Project Overview

This repository contains a complete, rigorous machine learning benchmark comparing **Decision Tree**, **K-Nearest Neighbors (KNN)**, and **Gaussian Naive Bayes** classifiers alongside **K-Means Clustering** on two standard benchmark datasets:
1. **Breast Cancer Wisconsin** (Binary Classification)
2. **Wine Classification** (Multi-class Classification)

---

## Repository Structure

```
MachineProject/
├── breast_cancer.ipynb       # Executable notebook for Breast Cancer analysis (Sections 1-10)
├── wine.ipynb                # Executable notebook for Wine analysis (Sections 1-10)
├── report.docx               # Formatted Word report (Arial 12pt, Sections 1-11)
├── classifier_runs.csv       # 132 classifier fit records
├── classifier_summary.csv    # 44 aggregated configuration summaries (mean & std)
├── classifier_test.csv       # Final test evaluation metrics for seed 42 best models
├── kmeans_runs.csv           # 12 K-Means fit records (inertia, ARI, silhouette)
├── kmeans_summary.csv        # 4 K-Means representation summaries
├── kmeans_test.csv           # Final test K-Means evaluation metrics (seed 42)
├── README.md                 # Project documentation & instructions
├── requirements.txt          # Python package dependency requirements
└── AI_DISCLOSURE.md          # Transparency statement on tool usage
```

---

## Installation & Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Notebooks:**
   Open Jupyter Notebook or VS Code and execute `breast_cancer.ipynb` and `wine.ipynb`.
