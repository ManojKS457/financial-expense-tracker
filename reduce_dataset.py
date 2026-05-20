import pandas as pd

# Load original dataset
df = pd.read_csv(
    "data/expense_data.csv"
)

# Take first 10000 rows
small_df = df.head(10000)

# Save smaller dataset
small_df.to_csv(
    "data/sample_expense_data.csv",
    index=False
)

print("Smaller dataset created successfully!")