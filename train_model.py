import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("data/resume_dataset_200k_enhanced.csv")

# Features
X = df[
    [
        "cgpa",
        "internships",
        "projects",
        "certifications",
        "experience_years",
        "research_papers",
        "hackathons",
        "skills_score"
    ]
]

# Target
y = df["hired"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/resume_model.pkl")

print("Model Saved!")