# ❤️ Heart Disease Prediction using Machine Learning

##  Project Overview

This project is a **Machine Learning classification system** that predicts whether a person is at risk of heart disease based on their medical attributes.
The model is trained on the **UCI Heart Disease Dataset** and uses **Logistic Regression** for prediction.

---

##  Objective

To build a predictive model that can:

* Analyze patient medical data
* Identify patterns related to heart disease
* Predict whether a person has heart disease (1) or not (0)

---

## Dataset Information

* **Dataset Name:** Heart Disease UCI Dataset
* **Source:** Kaggle / UCI Repository
* **Total Samples:** 1025
* **Features:** 13 medical attributes
* **Target Variable:**

  * `0` → Healthy Heart
  * `1` → Heart Disease Present

###  Features Used:

* age
* sex
* cp (chest pain type)
* trestbps (resting blood pressure)
* chol (cholesterol)
* fbs (fasting blood sugar)
* restecg (resting ECG results)
* thalach (maximum heart rate achieved)
* exang (exercise induced angina)
* oldpeak (ST depression)
* slope
* ca (number of major vessels)
* thal (thalassemia)

---

##  Machine Learning Model

* Algorithm: **Logistic Regression**
* Type: Binary Classification
* Libraries Used:

  * pandas
  * numpy
  * scikit-learn
  * matplotlib
  * seaborn

---

##  Project Workflow

1. Data Collection
2. Data Cleaning (handling missing values)
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Train-Test Split
6. Model Training (Logistic Regression)
7. Model Evaluation
8. Prediction System

---

##  Model Evaluation

### ✔ Accuracy:

* Training Accuracy: ~85%
* Testing Accuracy: ~80%

### ✔ Evaluation Metrics:

* Accuracy Score
* Confusion Matrix
* ROC Curve (AUC Score)

---

##  Results & Insights

* Chest pain type is a strong indicator of heart disease
* Maximum heart rate (thalach) plays an important role
* Oldpeak is highly correlated with disease risk
* Model performs well on unseen data with good generalization

---

##  Web Application 

A **Streamlit web app** can be used for interactive predictions where users input medical data and get instant results.

---

##  How to Run This Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
```

---

### 2️⃣ Install Dependencies

```bash
pip install numpy pandas scikit-learn matplotlib seaborn streamlit
```

---

### 3️⃣ Run Jupyter Notebook

Open:

```
notebook.ipynb
```

Run all cells step by step.

---

### 4️⃣ (Optional) Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Heart-Disease-Prediction/
│── data.csv
│── notebook.ipynb
│── heart_model.pkl
│── app.py
│── README.md
```

---

##  Technologies Used

* Python 🐍
* Machine Learning 🤖
* Pandas & NumPy 📊
* Scikit-learn ⚙️
* Matplotlib & Seaborn 📈
* Streamlit (optional web app) 🌐

---

##  Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Improve accuracy using feature engineering
* Deploy web app on cloud (Streamlit / Render / HuggingFace)
* Add user authentication system

---
