# Laptop Price Predictor 💻

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/SciKit--Learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Render](https://img.shields.io/badge/Render-46B3A9?style=for-the-badge&logo=render&logoColor=white)
![Project Status](https://img.shields.io/badge/status-complete-success?style=for-the-badge)
![R² Score](https://img.shields.io/badge/R²-0.874-success?style=for-the-badge)
![MAE](https://img.shields.io/badge/MAE-0.166-brightgreen?style=for-the-badge)

A machine learning web application that accurately predicts laptop prices based on hardware specifications, achieving **87.4% accuracy** with a Random Forest Regressor model.

---

## 🚀 Live Demo

**Experience the application live: [Laptop Price Predictor](https://laptop-price-predictor-aqls.onrender.com/)**

*Note: The application may take a few moments to load on first visit due to Render's free tier hosting.*

---

## 📊 Model Performance

After extensive testing of multiple machine learning algorithms, the Random Forest Regressor demonstrated superior performance:

### Model Comparison Results:
- **Linear Regression**: Baseline model
- **Ridge & Lasso Regression**: Regularized linear models
- **K-Nearest Neighbors (KNR)**: Distance-based approach
- **Support Vector Regressor (SVR)**: With hyperparameter tuning
- **Decision Tree Regressor**: Tree-based baseline
- **XGBoost Regressor**: Advanced gradient boosting

### 🏆 Best Performing Model: Random Forest Regressor
- **Test R² Score**: 0.8745 (87.4% accuracy)
- **Test MAE**: 0.1659
- **Status**: Hyperparameter tuned for optimal performance

---

## ✨ Key Features

- **Real-time Price Prediction**: Get instant price estimates based on selected specifications
- **Comprehensive Configuration**: Input brand, RAM, CPU, GPU, storage, display, and more
- **Advanced ML Pipeline**: Feature engineering and data preprocessing for accurate predictions
- **User-Friendly Interface**: Clean Streamlit interface for easy interaction
- **Model Interpretability**: Transparent pricing factors based on feature importance

---

## 📁 Dataset

The model is trained on a comprehensive dataset (`laptops.csv`) containing over 1,300 laptop records with detailed specifications. The dataset is included in the repository and features:

- **Brand specifications** (Dell, Lenovo, HP, Apple, etc.)
- **Hardware details** (RAM, CPU, GPU, Storage Type/Size)
- **Display characteristics** (Size, Resolution, Touchscreen)
- **Physical attributes** (Weight, Dimensions)

---

## 🛠️ Tech Stack & Architecture

### Backend & Machine Learning
- **Python 3.9+** - Core programming language
- **Pandas & NumPy** - Data manipulation and numerical operations
- **Scikit-learn** - Machine learning algorithms and pipeline
- **XGBoost** - Advanced gradient boosting implementation

### Frontend & Deployment
- **Streamlit** - Interactive web application framework
- **Render** - Cloud deployment platform

### Data Pipeline
1. **Data Cleaning**: Handling missing values and correcting data types
2. **Feature Engineering**:
   - Pixels Per Inch (PPI) calculation from screen specs
   - Brand extraction from CPU/GPU/OS text fields
   - Memory transformation into HDD/SSD numerical features
3. **Target Transformation**: Log transformation of prices for normal distribution
4. **Model Training**: Multi-algorithm comparison with hyperparameter tuning

---

## ⚙️ Local Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/laptop-price-predictor.git](https://github.com/YOUR_USERNAME/laptop-price-predictor.git)
cd laptop-price-predictor
```
2. Create Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the Application
```bash
streamlit run app_1.py
```
The application will open in your default browser at http://localhost:8501

📊 Model Training Details
Algorithms Tested:
Linear Models: Linear Regression, Ridge, Lasso

Instance-based: K-Nearest Neighbors

Kernel Methods: Support Vector Regressor (tuned)

Tree-based: Decision Tree, Random Forest (tuned), XGBoost

Hyperparameter Tuning:
Conducted on Random Forest and SVR models

Used GridSearchCV/RandomizedSearchCV for optimal parameters

Focus on maximizing R² score while minimizing MAE

Validation Strategy:
Train-Test split with stratification

Cross-validation for robust performance estimation

Comprehensive error metric analysis

🎯 Usage Guide
Select Brand: Choose from popular laptop manufacturers

Configure RAM: 4GB to 64GB options available

Choose CPU Type: Intel Core i3/i5/i7/i9, AMD Ryzen series

Select GPU: Integrated vs. Dedicated graphics options

Set Storage: SSD and HDD capacity combinations

Display Settings: Screen size, resolution, and touch options

Get Prediction: Click to receive instant price estimate

🔮 Future Enhancements
[ ] Integration with real-time market price data

[ ] Additional features (battery life, build materials)

[ ] Price trend analysis and forecasting

[ ] Mobile application version

[ ] Multi-currency support

[ ] User review sentiment integration

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

⭐ If you find this project helpful, please give it a star on GitHub!







