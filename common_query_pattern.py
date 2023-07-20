import pandas as pd


result_df = (
    df
    .groupby(["condition"], as_index=False)
    .agg(
        group_size=("user_id", "nunique")
    )
)