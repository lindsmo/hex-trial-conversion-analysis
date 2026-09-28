#Define buckets for top signal using quantiles
tiered_qcut_df = trials_df.copy()
tiered_qcut_df['engagement_tier'] = pd.qcut(tiered_qcut_df['datasets_connected'], q=3, labels =["1-low", "2-mid", "3-high"])