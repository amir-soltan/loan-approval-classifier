# Loan Approval Prediction Model

This repository features a Machine Learning model built to predict whether a loan application will be `Approved` or `Rejected` based on applicant data. 

## Dataset
The model utilizes the `loan_approval_dataset.csv` file, which includes details such as education level, employment status, and loan history.

## Features & Preprocessing
- Encoded categorical variables (`self_employed`, `education`, `loan_status`) into binary format.
- Dropped unique identifiers (`loan_id`) that don't contribute to predictive power.
- Evaluated models using an 70/30 train-test split.

## Models Trained
- **Random Forest Classifier**

## How to Run
1. Clone the repository:
```bash
   git clone [https://github.com/amir-soltan/loan-approval-classifier.git](https://github.com/amir-soltan/loan-approval-classifier.git)