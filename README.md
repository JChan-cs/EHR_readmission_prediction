# EHR_readmission_prediction

## Objective
 Develop a prediction model to predict
 30-day all-cause hospital readmission using only the provided Electronic Health Record (EHR)
 data (ehr_preprocessed_seq_by_day_cat_embedding.pkl).

 ## Dataset Description
  (1) Electronic Health Record Data (Tabular): Sourced from MIMIC-IV v1.0, this includes
  demographics, comorbidities (ICD-10 codes), lab results, and medications.
  
  (2) Chest Radiographs (Imaging): Sourced from MIMIC-CXR-JPG v2.0.
  
  (3) Clinical Notes (Text): De-identified free-text notes from MIMIC-IV-Note.
 
 Overview: Our dataset consists of 13,763 hospital admissions from 11,041 unique patients,
 with 2,379 admissions resulting in a 30-day readmission.
 
Data Files :\
  • train.csv, valid.csv, test.csv: Datasets with IDs, labels, etc.\
  • ehr_preprocessed_seq_by_day_cat_embedding.pkl: Preprocessed sequential EHR data.\
  • image_features.zip: Pre-extracted image features from a MoCo-CXR model.\
  • notes.csv: Free-text discharge summaries.
  
 Evaluation Metric: AUROC to evaluate model performance.

 ## Related to
 HKU STAT3612 Group Project\
 [https://www.kaggle.com/competitions/2025-fall-stat-3612-group-project]
