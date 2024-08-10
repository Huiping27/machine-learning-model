<img width="1284" alt="Screenshot 2024-07-17 at 14 36 58" src="https://github.com/user-attachments/assets/d3e718e8-9f88-46c1-8d94-316f1cf44c8d">


This project involves analyzing Uber data to predict ride prices using machine learning models. The analysis focuses on geo data, temporal data, and user data. A Flask web application is developed to provide predictions.



## Project Overview

Data Source: Uber dataset from Kaggle.

## Tech Stack:

Data Analysis: Python, Pandas, Scikit-learn
Machine Learning: Linear Regression, Random Forest
Web Application: Flask

## Installation

Prerequisites
Python 3.8 or later

## Set Up the Environment

1. **Install Dependencies**

    ```pip install -r requirements.txt
    ```
2. Set Up Environment Variables:

Create a .env file in the root directory and add necessary environment variables, if any. For example:

```FLASK_APP=app.py
FLASK_ENV=development
```

## Data Processing

Extract: Download the dataset from Kaggle and place it in the data/ directory.

## Transform:

## Data Cleaning: Handle missing values and outliers.

Feature Engineering: Generate features from geo, temporal, and user data.

## Data Integration: Combine features into a single dataset.
Load:

Store the processed data in a database or file storage system.

## Machine Learning

Training Models: Run the train_model.py script to train linear regression and random forest models.

```
python train_model.py
```

Evaluate Models: Check the performance metrics of the trained models.

## Web Application

Run Locally:


```
flask run
```
Access the application at http://localhost:5000.

## Contributing

Feel free to open issues or submit pull requests. Please follow the contribution guidelines:

Fork the repository.
Create a feature branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
