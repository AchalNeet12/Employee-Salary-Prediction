# Employee Salary Prediction Using Polynomial Regression

## 📝 Project Overview:
This project is a Salary Predictor that uses Polynomial Regression to predict employee salaries based on their years of experience. The project leverages a dataset of employee salaries and their corresponding years of experience to train a polynomial regression model. The model then predicts the salary for a given input of years of experience. The objective of this project is to demonstrate how polynomial regression can be used to model non-linear relationships between variables and predict continuous outcomes like salary.

## 📌 Polynomial Regression:
Polynomial Regression is an extension of linear regression, where the relationship between the independent variable X and the dependent variable y is modeled as a polynomial of degree 
n. It is useful when the data shows a non-linear relationship.
For instance, in the case of the salary prediction, polynomial regression captures the non-linear growth of salary with respect to years of experience. A linear regression model may not fit this non-linearity as effectively as polynomial regression.
- **Formula:**
        y=β0 + β1x + β2x^2 + β3x^3 +⋯+ βnx^n
Where:
- x is the independent variable (years of experience),
- y is the dependent variable (salary),
- 𝛽0,𝛽1,…,𝛽𝑛 are the regression coefficients,
- n is the degree of the polynomial (in this case, 5).

## 📂 Data Preprocessing:
In this project, data preprocessing is minimal because the dataset is already well-structured. Here are the key preprocessing steps:

1. **Loading the Dataset:**
The dataset is loaded using pandas (pd.read_csv).
2. **Feature Selection:**
The features (independent variable) X are the years of experience, and the target variable y is the salary.
3. **Polynomial Feature Transformation:**
Polynomial features are created from the X variable to capture the non-linear relationship between experience and salary. This is achieved using PolynomialFeatures(degree=5).
4.**Model Training:**
Polynomial regression is implemented by applying Linear Regression on the transformed polynomial features.
5.**Prediction:**
After training, predictions are made using the trained model, based on the user-provided experience.

## 🛠️ Libraries Used:
- **Streamlit:**
Streamlit is used for building the web interface and providing real-time predictions. It also handles the interaction between the user and the model.
- **pandas:**
Used for loading and managing the dataset.
- **numpy:**
Provides numerical operations and array handling capabilities.
- **sklearn.linear_model.LinearRegression:**
Used to implement polynomial regression by fitting a linear model on the polynomial features of the dataset.
- **sklearn.preprocessing.PolynomialFeatures:**
Used to create polynomial features from the experience variable, enabling the polynomial regression model to capture non-linear trends.
- **base64:**
Used to encode the background image and apply it to the Streamlit app.

## 📑 Features of the Application
- **User Input for Experience:**
The user can input the number of years of experience via a slider or input box in the sidebar.
- **Salary Prediction:**
Based on the input experience, the app uses a polynomial regression model to predict the estimated salary.
- **Background Image:**
The app includes a custom background image, making the interface visually appealing.
- **Instant Feedback:**
The result is shown instantly when the user provides an input, offering a smooth and responsive user experience.
- **Predefined Dataset:**
The app uses a predefined dataset of salaries and experience to train the polynomial regression model.

## 📊 Result
The result of this project is a fully functioning web application where users can input their years of experience, and the app will predict their salary based on the polynomial regression model. The application provides an estimated salary output and gives users a clear understanding of how their experience translates to salary according to the model trained on the given dataset.

## 📈 Conclusion
This project demonstrates how Polynomial Regression can be used for predicting continuous values (like salary) based on an independent variable (like experience). By transforming the original linear relationship into a polynomial, we can capture more complex relationships in the data.

Polynomial Regression is useful when the relationship between the independent and dependent variables is non-linear.
The Streamlit app provides an intuitive interface for users to interact with the model and receive instant predictions.
The application is built with a predefined dataset, making it easy to demonstrate polynomial regression's effectiveness for real-world applications like salary prediction.

