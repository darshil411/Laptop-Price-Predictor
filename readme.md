# Laptop Price Predictor 💻

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/SciKit--Learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Project Status](https://img.shields.io/badge/status-complete-success?style=for-the-badge)

An intuitive web application that predicts laptop prices based on their hardware and software specifications, powered by a Random Forest Regressor model.

---

## 🚀 Live Demo & Preview

This project is built with Streamlit, creating a user-friendly and interactive interface. Below is a quick preview of the application in action.


***(Note: To create a GIF, use a free tool like [ScreenToGif](https://www.screentogif.com/) or [Kap](https://getkap.co/). Record your screen while using the app, save it as a GIF, upload it to your repository, and then replace this text with `![Demo GIF](demo.gif)`)***

---

## ✨ Key Features

-   **Dynamic Price Prediction:** Get real-time price estimates by selecting various laptop configurations.
-   **Comprehensive Specs:** Input a wide range of specifications, including Brand, RAM, CPU, GPU, Storage, and more.
-   **Accurate ML Model:** Utilizes a Random Forest Regressor, which performed best among several tested models, for robust predictions.
-   **Interactive UI:** A clean and simple interface built with Streamlit for a seamless user experience.

---

## 🛠️ Tech Stack & Data Pipeline

This project leverages a powerful stack of data science and web development tools.

-   **Backend & Modeling:** Python, Pandas, NumPy, Scikit-learn
-   **Frontend:** Streamlit
-   **Data Source:** `laptops.csv` (A dataset containing over 1300 laptop records)

The data pipeline involves several key steps to ensure model accuracy:
1.  **Data Cleaning:** Handled missing values and corrected data types for `Ram` and `Weight`.
2.  **Feature Engineering:**
    -   Calculated **Pixels Per Inch (PPI)** from screen resolution and size for a more informative display feature.
    -   Extracted **CPU, GPU, and OS brands** from complex text fields into clean, categorical features.
    -   Transformed the `Memory` column into separate numerical features for `HDD` and `SSD`.
3.  **Data Transformation:** Applied a **log transformation** to the target variable (`Price`) to normalize its distribution, improving model performance. The final prediction is exponentiated to return the actual price.

---

## ⚙️ Setup and Installation

To run this project on your local machine, please follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Required Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃‍♂️ How to Run

With all dependencies installed, launch the Streamlit application with the following command:

```bash
streamlit run app_1.py