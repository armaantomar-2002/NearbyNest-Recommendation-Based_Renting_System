import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import NearestNeighbors
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


file_path = "recommendation_dataset_400.csv" 
data = pd.read_csv(file_path)

features = ["Location", "Rent (INR)", "Distance from College (km)"]


preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["Rent (INR)", "Distance from College (km)"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Location"])
    ]
)

X = preprocessor.fit_transform(data[features])

model = NearestNeighbors(n_neighbors=5, metric='euclidean')
model.fit(X)

def recommend(location, rent, distance):
    # Preprocess the new user input
    user_data = pd.DataFrame([[location, rent, distance]], columns=features)
    user_transformed = preprocessor.transform(user_data)
    
    # Find the 5 nearest neighbors
    distances, indices = model.kneighbors(user_transformed)
    
    # Return the recommended rows
    recommendations = data.iloc[indices[0]]
    return recommendations

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import NearestNeighbors
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import numpy as np

# Load the dataset
file_path = "recommendation_dataset_400.csv"  # Update this path to your file location
data = pd.read_csv(file_path)

# Features for recommendation
features = ["Location", "Rent (INR)", "Distance from College (km)"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["Rent (INR)", "Distance from College (km)"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Location"])
    ]
)

# Split data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Preprocess the training data
X_train = preprocessor.fit_transform(train_data[features])
y_train = train_data

# Build a NearestNeighbors model
model = NearestNeighbors(n_neighbors=5, metric='euclidean')
model.fit(X_train)

# Evaluation function
def evaluate_model(test_data):
    test_features = test_data[features]
    test_targets = test_data.index  # True row indices
    correct_recommendations = 0

    for idx, row in test_features.iterrows():
        user_input = pd.DataFrame([row], columns=features)
        user_transformed = preprocessor.transform(user_input)
        
        # Get recommendations
        distances, indices = model.kneighbors(user_transformed)
        recommended_indices = train_data.iloc[indices[0]].index

        # Check if the test item is in the recommendations
        if idx in recommended_indices:
            correct_recommendations += 1

    # Calculate accuracy
    accuracy = correct_recommendations / len(test_data)
    return accuracy

# Example usage
new_location = "Clement Town"
new_rent = 8000
new_distance = 3.0

# Get recommendations
recommendations = recommend(new_location, new_rent, new_distance)
print("Recommended rows:\n", recommendations)

# Evaluate model accuracy
accuracy = evaluate_model(test_data)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

new_location = "Clement Town"
new_rent = 8000
new_distance = 3.0

# Get recommendations
recommendations = recommend(new_location, new_rent, new_distance)
print("Recommended rows:\n", recommendations)
