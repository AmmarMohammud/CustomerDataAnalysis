# CustomerDataAnalysis
Data cleaning, visualization, and analysis project
_______________________________________________________________________________________________
📊 Customer Data Analysis & Cleaning Project
This project focuses on End-to-End Data Cleaning and Exploratory Data Analysis (EDA) using Python. The primary goal was to transform a "messy" e-commerce dataset into a clean, structured format ready for professional analysis or machine learning models.

🚀 Key Features
Zero Excel Policy: Entirely built using Python libraries to handle data manipulation.

Advanced Data Cleaning: Implementation of logic to handle missing values, duplicates, and inconsistent categorical data (e.g., Gender normalization).

Outlier Detection: Used the Interquartile Range (IQR) method to identify and treat anomalies in user age.

Data Visualization: Created insightful charts using Matplotlib and Seaborn to understand customer demographics and sales trends.

🛠️ Tech Stack
Language: Python 3.x

Libraries:

Pandas: For data manipulation and cleaning.

NumPy: For numerical operations.

Seaborn & Matplotlib: For statistical data visualization.

📋 Data Cleaning Workflow
Handling Missing Values: Applied Median imputation for numerical columns (Age) and constant filling for categorical columns.

Type Casting: Ensured data integrity by converting columns to appropriate types (e.g., converting Age to int and PurchaseDate to datetime).

Standardization: Normalized string data (Gender) to ensure consistency across the dataset.

Feature Engineering: Derived new features like Age_Group and Month to enhance the analysis.

📈 Visualizations Included
Distribution of customers by Gender and Age.

Total Revenue trends by Month.

Correlation matrix between Age, Rating, and Purchase Amount.

📁 Project Structure
CustomerDataAnalysis.py: The main Python script containing the cleaning and analysis logic.

Clean_Data_2026.csv: The final processed and cleaned dataset.
