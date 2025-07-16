import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import xgboost as xgb
import matplotlib.pyplot as plt
import pickle  # for saving the model

# 1. Load dataset
df = pd.read_csv("synthetic_tank_data.csv")

# 2. Split features and target
X = df.drop(columns=["Overfill"])
y = df["Overfill"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 4. Define optimized XGBoost model
model = xgb.XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.7,
    colsample_bytree=0.7,
    reg_alpha=1,           # L1 regularization
    reg_lambda=2,          # L2 regularization
    early_stopping_rounds=20,
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42
)

# 5. Train model with early stopping on validation set
model.fit(
    X_train, y_train,
    eval_set=[(X_train, y_train), (X_test, y_test)],
    verbose=False
)

# 6. Predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 7. Evaluation
print("📊 Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("📊 Test Accuracy :", accuracy_score(y_test, y_test_pred))

print("\n🧾 Classification Report (Train):\n", classification_report(y_train, y_train_pred))
print("\n🧾 Classification Report (Test):\n", classification_report(y_test, y_test_pred))
print("📉 Confusion Matrix (Test):\n", confusion_matrix(y_test, y_test_pred))

# 8. Feature Importance Plot
xgb.plot_importance(model, height=0.6, importance_type='gain', max_num_features=10)
plt.title("🔍 Top 10 Feature Importances")
plt.tight_layout()
plt.show()

# 9. Save the trained model to a pickle file
with open("xgboost_tank_overfill_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("💾 Model saved as 'xgboost_tank_overfill_model.pkl'")
