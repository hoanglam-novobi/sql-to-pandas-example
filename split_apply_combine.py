import pandas as pd

df = pd.DataFrame({
    'key': ['a', 'b', 'c']*3,
    'data': [0, 5, 10, 5, 10, 15, 10, 15, 20]
})

result_1 = (
    df
    # split by key
    .groupby(["key"], as_index=False)
    # apply sum() for each group
    .sum()
)
print(f"Result 1:\n{result_1}")

result_2 = (
    df
    # split by key
    .groupby(["key"], as_index=False)
    # apply sum() for data
    .agg({
        "data": ["sum", "min", "max"],
    })
)
print(f"Result 2:\n{result_2}")