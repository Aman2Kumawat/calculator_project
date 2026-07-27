# 📊 Telecom Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Losing existing customers can significantly impact business growth and revenue.

This project predicts whether a telecom customer is likely to churn using Machine Learning. A **Logistic Regression** model is trained on customer data to classify customers as either **Churn** or **Not Churn**.

---

## 🎯 Objectives

- Predict customer churn using Machine Learning.
- Perform data preprocessing and feature engineering.
- Train and evaluate a classification model.
- Save the trained model for future predictions.

---

## 📂 Dataset

The dataset contains customer information including:

- Customer Demographics
- Account Information
- Subscription Details
- Monthly Charges
- Total Charges
- Contract Type
- Payment Method
- Internet Services
- Customer Churn Status (Target Variable)

**Target Variable**

- 0 → Customer Will Not Churn
- 1 → Customer Will Churn

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📁 Project Structure

```
Telecom-Customer-Churn-Prediction/
│
├── telecom_customer_churn.xlsx
├── Telecom_Customer_Churn_Prediction.ipynb
├── customer_churn_model.pkl
├── scaler.pkl
├── README.md
└── Project_Report.pdf
```

---

## ⚙️ Workflow

1. Import Libraries
2. Load Dataset
3. Data Cleaning
4. Handle Missing Values
5. Encode Categorical Features
6. Feature Scaling
7. Train-Test Split
8. Train Logistic Regression Model
9. Evaluate Model
10. Predict Customer Churn
11. Save the Trained Model

---

## 📈 Model Used

**Logistic Regression**

This algorithm was selected because it is:

- Fast and efficient
- Easy to interpret
- Suitable for binary classification
- Performs well on structured datasets

---

## 📊 Evaluation Metrics

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

**Model Accuracy**

**Accuracy:** **79.35%**

---

## 🚀 How to Run the Project

### Clone the repository

```bash
git clone https://github.com/your-username/Telecom-Customer-Churn-Prediction.git
```

### Move into the project folder

```bash
cd Telecom-Customer-Churn-Prediction
```

### Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib openpyxl
```

### Run the notebook

```bash
jupyter notebook
```

Open:

```
Telecom_Customer_Churn_Prediction.ipynb
```

---

## 📌 Results

- Successfully cleaned and preprocessed the telecom dataset.
- Trained a Logistic Regression model for churn prediction.
- Achieved approximately **79.35% accuracy**.
- Saved the trained model for future use.

---

## 🔮 Future Improvements

- Random Forest Classifier
- XGBoost
- LightGBM
- CatBoost
- Hyperparameter Tuning
- Web Application using Flask/FastAPI
- Model Deployment
- Real-time Customer Churn Prediction

---

## 📚 Learning Outcomes

Through this project, I learned:

- Data Cleaning
- Data Preprocessing
- Feature Scaling
- Label Encoding
- Logistic Regression
- Model Evaluation
- Machine Learning Workflow
- Model Serialization using Joblib

---

## 👨‍💻 Author

**Aman Kumawat**

MCA (AI & ML)

Jain (Deemed-to-be University)

---

## ⭐ If you found this project useful, please consider giving it a Star.