import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("../dataset/dataset.csv")

# Select features & label
X = data[['payload_length', 'special_char_count', 'sql_flag', 'failed_login_flag']]
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("../ML_Model/threat_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully!")