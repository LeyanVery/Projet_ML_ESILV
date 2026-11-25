
from ucimlrepo import fetch_ucirepo

dataset = fetch_ucirepo(id=350)

X = dataset.data.features
y = dataset.data.targets.iloc[:, 0]

print("Number of customers:", len(X))
print("Number of features:", X.shape[1])

print("\nFirst 5 rows:")
print(X.head())

print("\nTarget distribution:")
print(y.value_counts().sort_index())

print("\nDefault rate:")
print(round(y.mean() * 100, 2), "%")

print("\nTotal missing values:")
print(X.isna().sum().sum() + y.isna().sum())

print("\nDuplicate rows:", X.duplicated().sum())

for col in ["X2", "X3", "X4"]:
    print(f"\nValues of {col}:")
    print(X[col].value_counts().sort_index())