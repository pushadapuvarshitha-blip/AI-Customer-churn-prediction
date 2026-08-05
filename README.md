Customer Churn Prediction Using Machine Learning
📌 Project Overview

Customer Churn Prediction is a Machine Learning project that predicts whether a customer is likely to leave (churn) or continue using a company's services. Customer retention is one of the biggest challenges faced by businesses such as telecom companies, banks, insurance companies, and subscription-based services. Losing existing customers can significantly reduce a company's revenue and increase customer acquisition costs.

This project uses Machine Learning algorithms to analyze customer information such as contract type, internet service, monthly charges, payment method, tenure, and other service-related features. Based on these details, the model predicts whether the customer is likely to churn. The project also provides business recommendations to help companies retain valuable customers.

🎯 Project Objectives
Predict whether a customer will churn.
Help businesses identify customers at high risk of leaving.
Improve customer retention strategies.
Reduce financial losses caused by customer churn.
Demonstrate the practical application of Machine Learning in business decision-making.
🚀 Features
Customer churn prediction using Machine Learning.
Professional Flask-based web application.
User-friendly interface for entering customer information.
Predicts customer churn in real time.
Displays High Risk or Low Risk prediction.
Shows churn probability.
Provides business recommendations based on prediction.
Attractive and responsive user interface.
🛠 Technologies Used
Programming Language
Python
Libraries
Pandas
NumPy
Scikit-learn
Joblib
Machine Learning Algorithms
Logistic Regression
Decision Tree Classifier
Random Forest Classifier
Web Technologies
Flask
HTML5
CSS3
JavaScript
Development Tools
Visual Studio Code
Jupyter Notebook
Git
GitHub
📂 Dataset Information

The project uses the Telco Customer Churn Dataset.

Dataset contains customer information such as:
Gender
Senior Citizen
Partner
Dependents
Tenure
Phone Service
Multiple Lines
Internet Service
Online Security
Online Backup
Device Protection
Tech Support
Streaming TV
Streaming Movies
Contract Type
Paperless Billing
Payment Method
Monthly Charges
Total Charges
Customer Churn

The target variable is:

Churn

Yes → Customer left the company.
No → Customer stayed with the company.
📊 Data Preprocessing

The following preprocessing techniques were applied:

Removed unnecessary columns.
Handled missing values.
Converted categorical values into numerical format.
One-Hot Encoding.
Converted TotalCharges into numeric format.
Train-Test Split.
Feature Engineering.
🤖 Machine Learning Models

The following Machine Learning models were trained and evaluated:

1. Logistic Regression

Logistic Regression is a supervised classification algorithm used to predict binary outcomes. It provided the best balance between accuracy and recall for this dataset.

Accuracy: 78.75%

2. Decision Tree Classifier

Decision Tree builds a tree-like structure to classify customer records.

Accuracy: 72.49%

3. Random Forest Classifier

Random Forest combines multiple Decision Trees to improve prediction performance.

Accuracy: 78.54%

🏆 Final Selected Model

After comparing all models, Logistic Regression was selected as the final model because it achieved the highest accuracy and better overall performance for customer churn prediction.

📈 Model Evaluation

The models were evaluated using:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Classification Report

These evaluation metrics help measure the effectiveness of the Machine Learning model.

🌐 Web Application

The project includes a Flask web application where users can:

Enter customer details.
Click the Predict Customer button.
View prediction results instantly.
See churn probability.
Receive business recommendations.
📁 Project Structure
CustomerChurnProject/
│
├── app.py
├── customer_churn_pipeline.pkl
├── churn.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── images/
│
└── README.md
▶️ How to Run the Project
Step 1

Clone the repository.

git clone <repository_link>
Step 2

Open the project folder.

cd CustomerChurnProject
Step 3

Install dependencies.

pip install -r requirements.txt
Step 4

Run the Flask application.

py app.py
Step 5

Open the browser.

http://127.0.0.1:5000
💼 Business Applications

Customer Churn Prediction can be used in:

Telecommunications
Banking
Insurance
E-Commerce
OTT Streaming Platforms
Healthcare
Online Education
Subscription-Based Businesses
🌟 Benefits
Reduces customer loss.
Improves customer satisfaction.
Supports data-driven business decisions.
Increases company revenue.
Helps identify high-risk customers.
Saves marketing costs.
Improves customer retention strategies.
🔮 Future Enhancements
Deploy the project on Render or PythonAnywhere.
Add user authentication.
Store prediction history in a database.
Create an interactive analytics dashboard.
Integrate email alerts for high-risk customers.
Improve prediction accuracy using advanced algorithms such as XGBoost or LightGBM.
Visualize customer insights with charts and graphs.
Add multilingual support.
📚 Learning Outcomes

Through this project, the following concepts were learned:

Data Cleaning
Data Preprocessing
Feature Engineering
One-Hot Encoding
Classification Algorithms
Model Evaluation
Model Saving using Joblib
Flask Web Development
HTML & CSS Integration
Machine Learning Deployment
👨‍💻 Author

Name: Pushadapu Varshitha

Course: B.Tech – Artificial Intelligence & Machine Learning (AI & ML)

Project: Customer Churn Prediction Using Machine Learning

Developed Using: Python, Scikit-learn, Flask, HTML, CSS, JavaScript

📜 License

This project is developed for educational purposes and to demonstrate the practical application of Machine Learning and Artificial Intelligence in predicting customer churn. It can be extended and customized for research, academic learning, or business use.
