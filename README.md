# ☕ Coffee Sales Analytics & Prediction Dashboard

A complete Data Analytics and Machine Learning project to analyze, predict, and visualize coffee sales trends. This project combines **Power BI** dashboards with **Python-based ML models** to provide actionable insights for sales improvement and customer behavior understanding.

---

## 📊 Dashboards Preview

### 🔸 Coffee Sales Analytics Dashboard
> ![Coffee Sales Dashboard](<img width="1334" height="737" alt="Screenshot 2025-08-03 125937" src="https://github.com/user-attachments/assets/1bce860c-e91a-4c2b-a75d-a2b672824961" />
)

### 🔸 Sales Prediction Dashboard (ML Model)
> ![Sales Prediction Dashboard](<img width="1309" height="736" alt="Screenshot 2025-08-03 125837" src="https://github.com/user-attachments/assets/9d2910ba-f36c-45d7-aac1-a44adca37c87" />
)

---

## 🚀 Key Features

- 📈 Interactive Power BI reports:
  - Most Sold Coffee (Latte, Americano with Milk, etc.)
  - Daily and Hourly Sales Trends
  - Sales Distribution by Customer Frequency, Days, and Coffee Types
  - Revenue per Day and Payment Type Breakdown

- 🤖 Machine Learning Insights:
  - Built and compared multiple models
  - Exported best predictions for visualization in Power BI
  - Evaluated model performance using accuracy and absolute error

- 🧩 **Advanced Tooltip Implementation**:
  - Hovering over coffee types shows:
    - Average Order Value
    - Total Predicted Sales
    - Total Customers
  - Hovering over prediction error reveals:
    - Predicted vs Actual value
    - Whether the item is overvalued or undervalued
  - Improved user interactivity and faster insights with contextual popups

---

## 📁 Project Structure

SahilT0/
│
├── Python.py # Python script for model training and prediction
├── Report.pbix # Power BI dashboard file
├── Starbucks_Corporation_Logo_2011.png # Branding logo for dashboard
│
├── cleaned_coffee_sales.csv # Original cleaned dataset
├── cleaned_coffee_sales1.csv # Modified dataset for visualizations
├── cleaned_coffee_sales_one.csv # Processed dataset with encoded columns
├── sales_predictions_best_model.csv # Predicted sales output from ML model
├── index.csv # Supporting data
│
└── README.md

---

## 🧠 ML Model Highlights

- **Features**: Hour, Day, Customer Frequency, Coffee Type
- **Target**: Sales Value (money)
- **Models Used**: Linear Regression, Random Forest, Decision Tree
- **Best Model**: Chosen based on R² score and average absolute error
- **Error Analysis**:
  - Overvalued Coffees (predicted < actual) shown in **green**
  - Undervalued Coffees (predicted > actual) shown in **red**

---

## 🛠️ Tools & Technologies

- **Python**: pandas, scikit-learn, matplotlib, seaborn
- **Power BI**: for dashboard design, tooltip reporting, and storytelling
- **Git/GitHub**: version control and collaboration

---

## 📈 Sample Metrics

- **Model Accuracy**: 0.9852
- **Average Order Value**: ₹33.11
- **Most Sold Coffee**: Latte
- **Best Selling Day**: Tuesday
- **Top Error Hours**: Around 9 AM and 4 PM

---

## 🖱️ Tooltip Implementation

> Tooltips are added in **Power BI** for rich contextual interactions:

- ✅ **Coffee Name Tooltips**:
  - Average Order Value
  - Average Customers
  - Predicted vs Actual Sales

- ✅ **Error Breakdown Tooltips**:
  - Hover on errors to identify specific hours or coffee types
  - Classification as **Overvalued** (red) or **Undervalued** (green)

---

## 📷 Screenshots

> Replace below with actual uploaded screenshots on GitHub

### 🔹 Analytics Dashboard  
`![Coffee Sales Dashboard](<img width="1352" height="745" alt="Screenshot 2025-08-03 125708" src="https://github.com/user-attachments/assets/f55e103c-0340-4bf4-b670-7272c8e08e44" />
)`

### 🔹 ML Sales Prediction Dashboard  
`![ML Prediction Dashboard](<img width="1307" height="730" alt="Screenshot 2025-08-03 125910" src="https://github.com/user-attachments/assets/2d968707-c5fa-4339-823d-8b31c2651e7f" />)
`

---

## 🔧 Getting Started

### Steps to Reproduce:

1. Clone the repository:
   ```bash
   git clone https://github.com/SahilT0/coffee-sales-dashboard.git
   cd coffee-sales-dashboard

2. Run the ML pipeline:
   Open Python.py to preprocess and train the model.
   sales_predictions_best_model.csv will be generated.

3. Open Report.pbix in Power BI:
     Use the existing reports or connect updated CSVs if needed.

---

🙌 Acknowledgements
Prepared by Sahil Tuli | June 2025
Crafted with ❤️ using Power BI, Python, and Data Science.
