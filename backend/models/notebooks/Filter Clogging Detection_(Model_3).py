import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("synthetic_filtration_data_balanced_1.csv")

# 2. Define features and target
X = df.drop(columns=["Timestamp", "Clogged"])
y = df["Clogged"]

# 3. Train-test split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Create Random Forest with regularization
clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_leaf=5,
    min_samples_split=10,
    random_state=42
)

# 5. Fit the model
clf.fit(X_train, y_train)

# 6. Predict
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

# 7. Evaluate performance
print("✅ Train Accuracy:", accuracy_score(y_train, y_train_pred))
print("✅ Test Accuracy:", accuracy_score(y_test, y_test_pred))
print("\n🔍 Classification Report (Test Set):\n", classification_report(y_test, y_test_pred))
print("📉 Confusion Matrix (Test Set):\n", confusion_matrix(y_test, y_test_pred))

# 8. Cross-validation
cv_scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("🧪 Cross-Validation Accuracy (mean):", cv_scores.mean())
print("🧪 Cross-Validation Scores:", cv_scores)

# 9. Feature importance plot
importances = clf.feature_importances_
features = X.columns
sorted_idx = importances.argsort()

# plt.figure(figsize=(10, 6))
# plt.barh(features[sorted_idx], importances[sorted_idx])
# plt.xlabel("Feature Importance")
# plt.title("Random Forest Feature Importance")
# plt.tight_lay
# plt.show()

# 10. Save the trained model to a .pkl file
model_filename = "clogging_model_optimized.pkl"
joblib.dump(clf, model_filename)
print(f"\n💾 Model saved as {model_filename}")
