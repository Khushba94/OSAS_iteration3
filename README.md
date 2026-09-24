# OSAS Iteration 3 — Cognitive & Lifestyle Analytics Pipeline

## Overview
This repository contains a complete data processing and clustering pipeline for analysing cognitive performance and lifestyle behaviour patterns.
It includes:
- Data cleaning
- Feature engineering
- Dataset merging
- Scaling
- KMeans clustering
- Outputs for Tableau visualisation
The goal is to identify behavioural and cognitive clusters that support personalised wellbeing insights.

Project Structure
<pre>
OSAS_iteration3/
│
├── data/
│   ├── ncpt_formatted.csv
│   └── mental_health_lifestyle_survey_2024.csv
│
├── outputs/
│   ├── ncpt_clean.csv
│   ├── lifestyle_clean.csv
│   ├── ncpt_features.csv
│   ├── lifestyle_features.csv
│   ├── merged.csv
│   ├── scaled.csv
│   └── merged_scaled_clustered.csv
│
├── scripts/
│   ├── 01_load_data.py
│   ├── 02_clean_data.py
│   ├── 03_feature_engineering.py
│   ├── 04_merge.py
│   ├── 05_scaling.py
│   └── 06_kmeans.py
│
└── README.md
</pre>

## 1. Data Cleaning
### NCPT Cleaning
- Convert numeric-looking strings to numeric
- Fill missing values using median
- Winsorise outliers (3 SD rule)
Output: 
- ncpt_clean.csv

### Lifestyle Cleaning
- Handle missing sleep, stress, screen time
- Clip extreme screen time values
- Convert categorical fields (BMI, caffeine intake, exercise frequency)
Output: 
- lifestyle_clean.csv

## 2. Feature Engineering
### Cognitive Composite Score
Average of:
- Attention
- MemoryRecall
- ProcessingSpeed
- Reasoning
- WorkingMemory

### Wellbeing Index
MinMax scaled average of:
- Sleep hours
- Exercise frequency
- Stress level
- Social interaction frequency

### Risk Behaviour Score
Combination of:
- Daily screen time
- Caffeine intake
- BMI category

### Outputs:
- ncpt_features.csv
- lifestyle_features.csv

## 3. Dataset Merge
A synthetic ID is used to merge NCPT + lifestyle datasets row‑by‑row:

<pre>
ncpt["synthetic_id"] = range(len(ncpt))
lifestyle["synthetic_id"] = range(len(lifestyle))
</pre>

### Merged output:
- merged.csv

## 4. Scaling
StandardScaler applied to numeric features:
-Cognitive scores
- Composite score
- Wellbeing index
- Risk behaviour score
Output:
- scaled.csv

## 5. Clustering (KMeans)
- KMeans with n_clusters = 4
- Silhouette score printed for evaluation
- Cluster labels added to dataset
Output:
- merged_scaled_clustered.csv

## 6. Tableau Visualisation
Use the final dataset to build dashboards such as:
- Cluster scatterplots
- Cognitive vs lifestyle comparisons
- Risk profile heatmaps
- Behavioural segmentation views

### Requirements
<pre>
Python 3.10+
pandas
numpy
scikit-learn
</pre>

Install dependencies:
<pre>
pip install pandas numpy scikit-learn
</pre>

### How to Run the Pipeline
<pre>
python scripts/01_load_data.py
python scripts/02_clean_data.py
python scripts/03_feature_engineering.py
python scripts/04_merge.py
python scripts/05_scaling.py
python scripts/06_kmeans.py
</pre>