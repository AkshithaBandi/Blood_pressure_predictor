import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load your dataset
df = pd.read_csv(r"C:\Users\akshi\Downloads\data.csv")  # Make sure data.csv is in the same folder

# Replace missing or invalid values
df = df.replace('?', np.nan)
df = df.fillna(df.mean())

# Define features and target
X = df[['Level_of_Hemoglobin', 'Genetic_Pedigree_Coefficient', 'Age', 'BMI',
        'Sex', 'Pregnancy', 'Smoking', 'Physical_activity',
        'salt_content_in_the_diet', 'alcohol_consumption_per_day',
        'Level_of_Stress', 'Chronic_kidney_disease', 'Adrenal_and_thyroid_disorders']]

y = df['Blood_Pressure_Abnormality']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a .pkl file
with open("bp_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved successfully as 'bp_model.pkl'")
