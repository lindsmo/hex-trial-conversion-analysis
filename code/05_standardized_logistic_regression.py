# Install and import statsmodels module
!uv pip install statsmodels==0.15.0 -q
import statsmodels.formula.api as smf

# Copy trials_df as z_df and standardize signals
z_df = trials_df.copy()

z_df[numeric_cols] = (trials_df[numeric_cols] - trials_df[numeric_cols].mean()) / trials_df[numeric_cols].std()

# Fit the model
model = smf.logit(
    "converted ~ seats_invited + datasets_connected + queries_run_wk1 + support_tickets + days_active + C(signup_channel, Treatment('organic_search'))", 
    data=z_df
).fit()

# Extract coefficients and 95% confidence intervals into a DataFrame
summary_df = pd.DataFrame({
    "coef": model.params,
    "conf_lower": model.conf_int().iloc[:, 0],
    "conf_upper": model.conf_int().iloc[:, 1],
})

# Filter to numeric columns only (excluding Intercept and categorical channels)
signals_df = summary_df.loc[numeric_cols].copy()

# Add the odds ratio, percentage change in odds, and confidence interval ratio
signals_df["odds_ratio"] = np.exp(model.params)
signals_df["odds_ratio_pct_change"] = (signals_df["odds_ratio"] - 1) * 100
signals_df["conf_lower_ratio"] = np.exp(signals_df["conf_lower"])
signals_df["conf_upper_ratio"] = np.exp(signals_df["conf_upper"])

# Add the absolute value of each coefficient for sorting purposes
signals_df["abs_coef"] = signals_df["coef"].abs()

# Sort by absolute magnitude descending
ranked_signals = signals_df.sort_values("abs_coef", ascending=False)
ranked_signals
