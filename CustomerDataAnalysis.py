# CustomerDataAnalysis.py
# -*- coding: utf-8 -*-
"""
Customer Data Analysis Script
Clean, visualize, and analyze fake customer data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# Functions for cleaning data
# ---------------------------
def clean_data(df):
    """Clean the customer dataset"""
    # إزالة التكرارات
    df = df.drop_duplicates()

    # تنظيف العمود Gender
    df['Gender'] = df['Gender'].str.strip().str.lower()
    df['Gender'] = df['Gender'].replace({'m':'male', 'f':'female'})

    # التعامل مع missing values في Age
    mean_age = df.loc[df['Age'] >= 0, 'Age'].mean()
    df['Age'] = df['Age'].fillna(mean_age)
    df['Age'] = df['Age'].apply(lambda x: mean_age if x < 0 else x)

    # استبدال الأعمار الكبيرة جدًا بالقيمة المتوسطة
    df.loc[df['Age'] > 100, 'Age'] = df['Age'].median()

    # التعامل مع outliers باستخدام IQR
    Q1 = df['Age'].quantile(0.25)
    Q3 = df['Age'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df.loc[(df['Age'] < lower_bound) | (df['Age'] > upper_bound), 'Age'] = df['Age'].median()

    # التعامل مع missing values في ProductCategory
    df['ProductCategory'] = df['ProductCategory'].fillna('Unknown')

    # تحويل PurchaseDate لتاريخ
    df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'], errors='coerce')

    return df

# ---------------------------
# Functions for plotting data
# ---------------------------
def plot_gender_distribution(df):
    gender_counts = df['Gender'].value_counts()
    plt.figure(figsize=(3,3))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    plt.title('Distribution By Gender')
    plt.show()

def plot_age_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], bins=10, kde=True)
    plt.title('Distribution By Age')
    plt.show()

def plot_purchase_by_gender(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x='PurchaseAmount', y='Gender')
    plt.title('Purchase Amount By Gender')
    plt.show()

    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x="Gender", y="PurchaseAmount", estimator="mean")
    plt.title("Average Purchase Amount By Gender")
    plt.show()

def plot_correlation(df):
    corr = df[['Age','PurchaseAmount','Rating']].corr()
    plt.figure(figsize=(6,4))
    sns.heatmap(corr, annot=True, linewidths=2, cmap="coolwarm")
    plt.title('Correlation Matrix')
    plt.show()

def plot_age_group_revenue(df):
    bins = [0, 18, 35, 55, 100]
    labels = ['Teens', 'Young Adults', 'Adults', 'Seniors']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

    plt.figure(figsize=(8,5))
    sns.barplot(data=df, x='Age_Group', y='PurchaseAmount', estimator=sum)
    plt.title("Total Revenue by Age Group")
    plt.show()

def plot_age_vs_purchase(df):
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x='Age', y='PurchaseAmount', hue='Gender')
    plt.title('Purchase Amount By Age')
    plt.show()

def plot_monthly_sales(df):
    df['Month'] = df['PurchaseDate'].dt.month
    monthly_sales = df.groupby('Month')['PurchaseAmount'].sum()

    plt.figure(figsize=(10,3))
    monthly_sales.plot(kind='line', marker='o')
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.show()


# Main script

if __name__ == "__main__":
    # Load data
    df = pd.read_csv("fake_customer_data_with_errors.csv")

    # Clean data
    df = clean_data(df)

    # Data exploration
    print("Data shape:", df.shape)
    print("Columns info:\n", df.info())
    print("Number of duplicates:", df.duplicated().sum())
    print("Number of unique values:\n", df.nunique())
    print("Missing values:\n", df.isna().sum())
    print("Description:\n", df.describe())

    # Plots
    plot_gender_distribution(df)
    plot_age_distribution(df)
    plot_purchase_by_gender(df)
    plot_correlation(df)
    plot_age_group_revenue(df)
    plot_age_vs_purchase(df)
    plot_monthly_sales(df)

    # Save cleaned data
    df.to_csv("Clean_Data_2026.csv", index=False)
    print("Cleaned data saved to Clean_Data_2026.csv")