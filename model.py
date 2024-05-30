import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# Load or train the model
def load_or_train_model():
    if os.path.exists('model.pkl'):
        model = joblib.load('model.pkl')
        return model
    else:
        # Load your data
        df = pd.read_csv('uber_peru_2010_cleaned.csv')

        # Select relevant columns for training
        relevant_columns = ['price_distance', 'start_lat', 'start_lon', 'end_lat', 'end_lon', 'price_duration', 'distance', 'duration', 'cost', 'cost_distance', 'cost_duration', 'driver_score', 'rider_score']
        X = df[relevant_columns]
        y = df['price']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train the Random Forest model
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)

        # Save the trained model
        joblib.dump(model, 'model.pkl')
        return model

# Predict using the model
def predict(features):
    model = load_or_train_model()
    prediction = model.predict([features])
    return prediction
