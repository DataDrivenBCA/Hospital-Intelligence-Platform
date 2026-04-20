# Hospital Intelligence Platform

## Overview
End-to-end healthcare analytics platform built with Python, PostgreSQL, and Tableau. 
Includes data pipeline, KPI analysis, and ML-powered readmission risk predictor.

## Tech Stack
- Python (pandas, scikit-learn, sqlalchemy, streamlit)
- PostgreSQL (star schema data warehouse)
- Tableau Public (interactive dashboard)
- Jupyter Notebooks

## Project Structure
01_data_generation — data cleaning and feature engineering
02_database_loading — ETL pipeline to PostgreSQL
03_analytics — KPI analysis and visualization
04_readmission_prediction — Random Forest ML model
app.py — Streamlit web application

## Key Features
- Star schema database design with fact and dimension tables
- 5 hospital KPIs analyzed
- Random Forest readmission predictor (83.6% accuracy)
- Live Streamlit web app for non-technical users
- Tableau dashboard published online

## Dashboard
[View on Tableau Public](your tableau link here)

## Limitations & Future Work
- Model recall is low (3-4%) due to class imbalance
- SMOTE applied but needs real hospital data for meaningful improvement
- Future: XGBoost, real EMR data, HIPAA compliance
