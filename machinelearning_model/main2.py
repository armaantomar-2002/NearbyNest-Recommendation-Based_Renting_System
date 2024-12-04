import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import NearestNeighbors
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

file_path = "recommendation_dataset_1000.csv"
data = pd.read_csv(file_path)

features = ["Location", "Rent (INR)", "Distance from College (km)"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["Rent (INR)", "Distance from College (km)"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Location"])
    ]
)

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
X_train = preprocessor.fit_transform(train_data[features])

model = NearestNeighbors(n_neighbors=5, metric='euclidean')
model.fit(X_train)

def recommend(location, rent, distance):
    user_data = pd.DataFrame([[location, rent, distance]], columns=features)
    user_transformed = preprocessor.transform(user_data)
    distances, indices = model.kneighbors(user_transformed)
    recommendations = train_data.iloc[indices[0]]
    return recommendations

def evaluate_model_with_similarity(test_data, similarity_threshold=0.1):
    test_features = test_data[features]
    total_matches = 0

    for idx, row in test_features.iterrows():
        user_input = pd.DataFrame([row], columns=features)
        user_transformed = preprocessor.transform(user_input)
        distances, indices = model.kneighbors(user_transformed)
        recommended_rows = train_data.iloc[indices[0]]

        is_similar = False
        for _, rec_row in recommended_rows.iterrows():
            rent_diff = abs(row["Rent (INR)"] - rec_row["Rent (INR)"])
            distance_diff = abs(row["Distance from College (km)"] - rec_row["Distance from College (km)"])
            if rent_diff <= similarity_threshold * row["Rent (INR)"] and distance_diff <= similarity_threshold * row["Distance from College (km)"]:
                is_similar = True
                break
        
        if is_similar:
            total_matches += 1

    accuracy = total_matches / len(test_data)
    return accuracy

new_location = "Lane-3, Clement Town, Dehradun"
new_rent = 8000
new_distance = 3.0

recommendations = recommend(new_location, new_rent, new_distance)
print("Recommended rows:\n", recommendations)

accuracy = evaluate_model_with_similarity(test_data, similarity_threshold=0.1)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
