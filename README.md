# 🩺 Blood Pressure Prediction Using Machine Learning

This project aims to predict **blood pressure abnormality levels** using **Linear Regression** based on various health, lifestyle, and medical factors. Early detection of abnormal blood pressure helps prevent cardiovascular risks, making this model useful for healthcare analysis and preliminary screening.

---

## 📘 **Project Overview**

Blood pressure levels are influenced by several factors such as age, BMI, hemoglobin level, stress, kidney function, smoking habits, and salt intake.  
This project uses **Machine Learning** to identify patterns in these parameters and predict blood pressure abnormality scores.

A **Streamlit web app** has also been built to allow users to interactively enter health details and receive predictions in real time.

---

## 🎯 **Key Features**

- Data preprocessing and feature engineering  
- One-hot encoding for categorical attributes  
- Linear Regression model for predicting BP abnormality  
- Evaluation using R² Score, MSE, and RMSE  
- Streamlit-based web interface for real-time predictions  
- Saved model (`bp_model.pkl`) and feature set (`bp_features.pkl`) for deployment  

---

## 🧠 **Machine Learning Workflow**

1. **Data Loading & Cleaning**  
   - Handled missing values  
   - Encoded categorical features  
   - Removed invalid and inconsistent data  

2. **Exploratory Data Analysis (EDA)**  
   - Heatmap  
   - Distribution plots  
   - Scatter and bar charts  

3. **Model Development**  
   - Linear Regression model  
   - Train-test split  
   - Performance evaluation  

4. **Deployment**  
   - Streamlit web app (`app.py`)  
   - Model loaded using pickle  

---

## 🔢 **Tech Stack**

- **Programming Language:** Python  
- **Libraries:**  
  - Pandas, NumPy  
  - Scikit-Learn  
  - Matplotlib, Seaborn  
  - Streamlit  
  - Pickle  

---

## 🚀 **How to Run the Project**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/blood-pressure-prediction.git
cd blood-pressure-prediction

2. Install Required Libraries
pip install -r requirements.txt

3.Run the Streamlit App
streamlit run app.py

📂 Project Structure
├── bp_model.pkl
├── bp_features.pkl
├── app.py
├── notebook.ipynb
├── README.md
└── dataset.csv

📊 Results

The Linear Regression model was evaluated on test data

Scatter plots and bar charts show good alignment between actual and predicted values

The model effectively estimates blood pressure abnormality scores based on input features

🚧 Future Enhancements

Use advanced models such as Random Forest, XGBoost

Add more health parameters for improved accuracy

Deployment using Streamlit Cloud or Render

Create mobile-friendly UI

📝 Conclusion

The project demonstrates that machine learning can effectively analyze health parameters to predict blood pressure abnormalities. The system can support early diagnosis, preventive healthcare, and risk assessment.
