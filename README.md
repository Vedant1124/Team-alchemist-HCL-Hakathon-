# 📊 Customer Churn Prediction – Telco Dataset

An end-to-end Machine Learning project that predicts whether a telecom customer will **churn** (leave the service).  
This repository includes:

- ✔ A trained **LightGBM** churn prediction model  
- ✔ Encoders for categorical features  
- ✔ A complete **Streamlit web application**  
- ✔ Clean code and easy setup  


---

## 📁 Project Structure

```
│── model1.pkl               # Trained LightGBM model  
│── encoders.pkl             # Saved label encoders  
│── streamlit_app.py         # Streamlit UI application  
│── requirements.txt         # Dependencies  
│── README.md                # Documentation  
```

---

## 📌 Problem Statement

Telecom companies face revenue loss when customers discontinue their services.  
The objective of this project is to build a model that predicts **whether a customer is likely to churn**, allowing the business to proactively retain them.

The dataset contains customer demographics, account details, and service usage features.

---

# 🚀 How to Run the Project

Follow these steps to run the Churn Prediction app on your local machine:

---

## **1️⃣ Clone the Repository**

```bash
git clone <your-github-repo-link>
cd <your-repo-folder>
```

---

## **2️⃣ Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
```

### Activate it:

#### Windows:
```bash
venv\Scripts\activate
```

#### macOS/Linux:
```bash
source venv/bin/activate
```

---

## **3️⃣ Install Requirements**

```bash
pip install -r requirements.txt
```

This installs:
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  
- LightGBM  

---

## **4️⃣ Run the Streamlit App**

```bash
streamlit run streamlit_app.py
```

Once launched, the app will open at:

```
http://localhost:8501
```

---

# 🖥️ Streamlit Application

The Streamlit UI allows you to:

- Select **categorical values** from dropdowns  
- Input numeric values (e.g., tenure, monthly charges)  
- Submit data and get instant churn prediction  
  


---

# 🧠 Model Information

- **Model Used:** LightGBM Classifier  
- **Preprocessing:** Label Encoding applied to all categorical columns  
- **Training Steps:**
  - Handling missing values  
  - Label Encoding  
  - Train-test split  
  - Model training  

The model outputs:
- `0` → Customer will **not** churn  
- `1` → Customer **will** churn  


---

# 📦 Dataset Features

The Telco churn dataset typically includes:

### **Customer Information**
- Gender  
- SeniorCitizen  
- Partner  
- Dependents  

### **Service Information**
- PhoneService  
- MultipleLines  
- InternetService  
- OnlineSecurity  
- OnlineBackup  
- DeviceProtection  
- TechSupport  
- StreamingTV  
- StreamingMovies  

### **Account Information**
- Contract  
- PaperlessBilling  
- PaymentMethod  
- Tenure  
- MonthlyCharges  
- TotalCharges  

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| UI | Streamlit |
| ML Model | LightGBM |
| Data Processing | Pandas, Scikit-learn |
| Deployment on Streamlit





