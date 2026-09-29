correlation_baseline_trials_df = (
    trials_df[numeric_cols]
    .corrwith(trials_df["converted"])
    .sort_values(ascending=False)
    .round(3)
    .rename("correlation_with_conversion")
    .to_frame()
)
correlation_baseline_trials_df