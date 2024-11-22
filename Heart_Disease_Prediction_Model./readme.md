# Heart Disease Prediction Model

## Overview

This project aims to predict the likelihood of a patient having heart disease based on various health-related features using machine learning. The model is built using a dataset sourced from Kaggle, which includes features such as age, cholesterol level, blood pressure, and other medical indicators.

The model was trained and evaluated using several machine learning algorithms, including **Logistic Regression**, **Naive Bayes**, **K-Nearest Neighbors (KNN)**, **Decision Tree**, and **Random Forest**.

### Dataset

The dataset is sourced from Kaggle and can be found [here](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset). It includes various attributes that influence the risk of heart disease.

### Features in the Dataset:
- `age`: Age of the patient
- `sex`: Gender (1 = male, 0 = female)
- `cp`: Chest pain type (4 values)
- `trestbps`: Resting blood pressure
- `chol`: Serum cholesterol
- `fbs`: Fasting blood sugar (1 = true, 0 = false)
- `restecg`: Resting electrocardiographic results
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise induced angina (1 = yes, 0 = no)
- `oldpeak`: Depression induced by exercise relative to rest
- `slope`: Slope of the peak exercise ST segment
- `ca`: Number of major vessels colored by fluoroscopy
- `thal`: Thalassemia (3 possible values)
- `target`: Heart disease (1 = disease present, 0 = disease absent)

## Project Description

This project includes the following steps:
1. **Data Preprocessing**:
    - Data cleaning and handling missing values
    - Feature scaling
    - Data splitting into training and testing sets

2. **Model Building**:
    - Machine learning models tested:
        - **Logistic Regression**
        - **Naive Bayes**
        - **K-Nearest Neighbors (KNN)**
        - **Decision Tree**
        - **Random Forest**
    - Hyperparameter tuning and model optimization.

3. **Evaluation**:
    - Models are evaluated using accuracy scores. The best-performing model is chosen based on these metrics.

4. **Deployment** (Optional for future work):
    - The final model can be deployed as a web application using frameworks such as Flask or Streamlit for real-time predictions.

## Requirements

To run this project, you will need the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

You can install the required packages by running:

```bash
pip install -r requirements.txt
```
Usage
Clone this repository:
```bash
Copy code
git clone https://github.com/yourusername/Heart-Disease-Prediction-Model.git
cd Heart-Disease-Prediction-Model
Download the dataset from Kaggle and place the heart.csv file in the data/ directory.
```
Run the model:

```bash

python heart_disease_predictor.py
```
Check the output for the evaluation metrics and the best model's performance.
Example Output
text
```bash
The accuracy score achieved using Logistic Regression is: 86.34 %
The accuracy score achieved using Naive Bayes is: 85.37 %
The accuracy score achieved using K-Nearest Neighbors is: 83.9 %
The accuracy score achieved using Decision Tree is: 72.2 %
The accuracy score achieved using Random Forest is: 100.0 %
Directory Structure
bash
Copy code
Heart-Disease-Prediction-Model/
│
├── data/
│   └── heart.csv                  # Dataset file
│
├── src/
│   ├── heart_disease_predictor.py  # Main model code
│   ├── data_preprocessing.py       # Data preprocessing code
│   └── model_training.py           # Code for training models
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── LICENSE                        # License information (optional)
Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. All contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Kaggle for providing the dataset
Scikit-learn for the machine learning models
The Python community for their amazing open-source libraries
