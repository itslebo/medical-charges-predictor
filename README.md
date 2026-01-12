# Medical Charges Prediction

Simple regression project that predicts individual medical charges using the "medical-charges.csv" dataset.

- Script: [main.py](main.py) — loads [`data`](main.py), encodes categorical features, trains a [`model`](main.py) (LinearRegression), evaluates using [`r2_score`](main.py), prints comparisons and shows visualizations.
- Dataset: [medical-charges.csv](medical-charges.csv)
- License: [LICENSE](LICENSE)

## Quickstart

1. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows
   ```
2. Install dependencies:
   ```sh
   pip install pandas scikit-learn matplotlib seaborn
   ```
3. Run the script:
   ```sh
   python main.py
   ```

## What you'll see
- Cleaned data preview and new columns.
- Train/test split sizes and first rows of training data.
- Model training completion and R^2 score.
- First 5 Actual vs Predicted comparisons.
- Example single prediction using the [`new_patient`](main.py) row in the script.
- Two visualizations: Actual vs Predicted and BMI vs Charges (colored by smoker).

## Notes
- Categorical encodings and dummy variables are performed in [main.py](main.py).
- The dataset has no missing values and shape (1338, 7).
- To change the example prediction, modify the [`new_patient`](main.py) line in [main.py](main.py).