import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

data = pd.read_csv('medical-charges.csv')

# print(data.shape)
# print(data.describe())

data['smoker'] = data['smoker'].map({'yes': 1, 'no': 0}) # Convert 'yes' to 1 and 'no' to 0
data['sex'] = data['sex'].map({'female': 0, 'male': 1}) # Convert 'male' to 1 and 'female' to 0
data = pd.get_dummies(data, columns=['region'], drop_first=True)

print("\n--- Cleaned Data ---")
print(data.head())
print("\n--- New Columns ---")
print(data.columns)


X = data.drop('charges', axis=1)
y = data['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n--- Data Split Complete ---")
print(f"Training rows: {X_train.shape[0]}")
print(f"Testing rows: {X_test.shape[0]}")

print(X_train.head())

# Model training
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("\n--- Training Complete ---")

score = r2_score(y_test, predictions)
print(f"Model Accuracy (R^2 Score): {score:.4f}")

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
print("\n--- First 5 Predictions vs Actuals ---")
print(comparison.head())

# Example prediction
new_patient = [[30, 1, 25.0, 0, 1, 0, 0, 1]]
prediction = model.predict(new_patient)
print(f"\nPredicted Medical Charges for this patient: ${prediction[0]:,.2f}")

# Feature importance
importance = pd.DataFrame({'Feature': X.columns, 'Weight': model.coef_})
print("\n--- How much each factor adds to the cost ---")
print(importance.sort_values(by='Weight', ascending=False))

import matplotlib.pyplot as plt
import seaborn as sns # Optional: for prettier colors

# --- VISUALIZATION ---

# 1. Create a scatter plot of Actual vs Predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.5, color='blue', label='Predictions')

# Draw a diagonal line showing where "Perfect Predictions" would be
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Fit')

plt.xlabel('Actual Charges')
plt.ylabel('Predicted Charges')
plt.title('Actual vs. Predicted Medical Charges')
plt.legend()
plt.show()

# 2. BMI vs Charges (Colored by Smoker)
# We use the original data for this to see the raw relationship
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='bmi', y='charges', hue='smoker', alpha=0.7)
plt.title('How BMI and Smoking Impact Charges')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()