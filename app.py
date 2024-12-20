import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import base64

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Salary Predictor", layout="wide", page_icon="💼")

# Function to set background image and text color
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}"); 
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: white; /* Set all text color to white */
    }}
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
        color: white; /* Ensure headers are also white */
    }}
    .stApp .stMarkdown p {{
        color: white; /* Set all paragraph text to white */
    }}
    .stButton button {{
        background-color: #0078D7; /* Optional: Adjust button color */
        color: white;
        border-radius: 5px;
        border: none;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call the function to set the background (provide the correct image path)
set_background("img4.jpg")

# Load the dataset
dataset = pd.read_csv(r"E:\3.spyder\Regression\non-linear regression\Polynomial regression\emp_sal.csv")
X = dataset.iloc[:, 1:2].values  # Experience (years)
y = dataset.iloc[:, 2].values    # Salary

# Polynomial Regression Model
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

# Sidebar
st.sidebar.title("💼 Salary Predictor")
st.sidebar.write("Use this app to predict an employee's salary based on years of experience.")
experience_years = st.sidebar.number_input(
    "Enter Years of Experience:", 
    min_value=0.0, 
    step=0.1, 
    value=0.0, 
    format="%.1f"
)

# Header Section
st.title("🔮 Employee Salary Prediction")
st.markdown(
    """
    This application uses **Polynomial Regression** to estimate the salary for a given number of years of experience. 
    Adjust the years of experience using the sidebar and click "Enter" to get the prediction instantly.
    """
)

# Button for Prediction
if st.sidebar.button("Enter"):
    if experience_years > 0:
        # Make prediction
        prediction = model.predict(poly_reg.fit_transform([[experience_years]]))
        st.subheader("Prediction Result 💰")
        st.success(f"The estimated salary for {experience_years:.1f} years of experience is: **${prediction[0]:,.2f}**")
    else:
        st.warning("Please enter a valid number of years of experience.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("🔧 Built with Streamlit | 💡 Polynomial Regression Model")

st.markdown(
    """
    The predictions are based on a predefined dataset of employee salaries.
    """
)
