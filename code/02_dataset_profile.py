numeric_cols = [
    "seats_invited",
    "datasets_connected",
    "queries_run_wk1",
    "support_tickets",
    "days_active"
]

# Describe the dataset for each signal to get a sense of the distribution of the data
trials_df[numeric_cols].describe()