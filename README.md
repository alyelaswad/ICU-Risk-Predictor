# ICU Risk Predictor

A machine learning framework for ICU patient risk assessment and mortality prediction using physiological time-series data.

## Overview
This project implements a comprehensive machine learning pipeline for predicting mortality risk in Intensive Care Unit (ICU) patients. By analyzing time-series physiological data, the system provides early risk assessment to help clinicians identify high-risk patients and potentially improve outcomes through early intervention.

## Features
- **Data Processing Pipeline**: Transforms raw patient time-series data into structured features suitable for machine learning  
- **Advanced Imputation**: Handles missing values using iterative imputation techniques  
- **Class Imbalance Handling**: Implements ADASYN, SMOTE, and SMOTETomek to address the imbalance between mortality outcomes  
- **Multiple Classifier Support**: Evaluates various machine learning algorithms including:
  - Random Forest
  - XGBoost
  - Logistic Regression
  - Support Vector Machines
  - K-Nearest Neighbors
  - Decision Trees
- **Comprehensive Evaluation**: Provides confusion matrices, ROC curves, and key performance metrics (accuracy, precision, recall, F1, AUC)

## Dataset
The system works with the PhysioNet Challenge dataset, which includes:
- Time-series physiological measurements (vital signs, lab values)
- Patient demographics
- ICU stay information
- Mortality outcomes

The data is organized into:
- Training set (set-a)
- Testing set (set-b)

## Installation
```bash
# Clone the repository
git clone https://github.com/alyelaswad/ICU-Risk-Predictor.git
cd ICU-Risk-Predictor

```

## Results
Our evaluation shows that Random Forest and XGBoost classifiers achieve the best performance for mortality prediction, with AUC scores above 0.80. The models demonstrate good discriminative ability between survival and mortality outcomes.

## Future Work
- Continous predictions (non-classification problems) to access the risk of each patient
- Assembling this work into a single notebook
- Adding gui to input patient data and expect a medical recommendation based on how the patient is doing (hopeful)

## Acknowledgments
- PhysioNet for providing the clinical datasets
- Scikit-learn for the ML models
