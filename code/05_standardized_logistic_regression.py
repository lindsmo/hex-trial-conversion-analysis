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
).fit(disp=0)

# Extract coefficients and 95% confidence intervals into a DataFrame
summary_df = pd.DataFrame({
    "coef": model.params,
    "conf_lower": model.conf_int().iloc[:, 0],
    "conf_upper": model.conf_int().iloc[:, 1],
})

# Filter to numeric columns only (excluding Intercept and categorical channels)
signals_df = summary_df.loc[numeric_cols].copy()

# Add the odds ratio, confidence interval ratio, and percentage change in odds
signals_df["odds_ratio"] = np.exp(model.params)
signals_df["conf_lower_ratio"] = np.exp(signals_df["conf_lower"])
signals_df["conf_upper_ratio"] = np.exp(signals_df["conf_upper"])
signals_df["odds_ratio_pct_change"] = (signals_df["odds_ratio"] - 1) * 100

# Add the absolute value of each coefficient for sorting purposes
signals_df["abs_coef"] = signals_df["coef"].abs()

# Rename columns for clarity
signals_df = signals_df.rename(
    columns={
        "coef": "log_odds_coefficient",
        "conf_lower": "log_odds_ci_95_lower",
        "conf_upper": "log_odds_ci_95_upper",
        "odds_ratio": "odds_ratio",
        "conf_lower_ratio": "odds_ratio_ci_95_lower",
        "conf_upper_ratio": "odds_ratio_ci_95_upper",
        "odds_ratio_pct_change": "odds_pct_change",
        "abs_coef": "abs_log_odds_coefficient",
    }
)

# Sort by absolute magnitude descending, then drop absolute magnitude
ranked_signals = signals_df.sort_values("abs_log_odds_coefficient", ascending=False).drop(columns=["abs_log_odds_coefficient"])
ranked_signals
