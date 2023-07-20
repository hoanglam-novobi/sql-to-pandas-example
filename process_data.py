import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data
def read_data():
    # Create dataframe from recordset in Odoo
    records = [
        {
            "Customer": "Lee Bird",
            "Customer Metro": "Dallas",
        }
    ]
    df = pd.DataFrame()

    # Read data from CSV file
    df = pd.DataFrame(pd.read_csv("input/cancelled_customers.csv"))

    return df

raw_df = read_data()
print(f"Raw data:\n{raw_df}")

# transform data
raw_df["Month"] = pd.to_datetime(raw_df["Timestamp"])


result_df = (
    raw_df
    .groupby(["Month", "Customer Metro"], as_index=False)
    .agg(
        cancelled_customer_by_metro=(
            "Customer", "count"),
    )
    .sort_values(by=["Customer Metro", "Month"])
)
print(result_df)

# visualization
ax = sns.barplot(
    data=result_df,
    x="Month",
    y="cancelled_customer_by_metro",
    hue="Customer Metro"
)
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.show()