import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 2000

signup_channel = rng.choice(
    ["organic_search", "paid_search", "referral", "content", "partner"],
    size=n, p=[0.35, 0.25, 0.15, 0.15, 0.10]
)
seats_invited = rng.poisson(2, n)
datasets_connected = rng.poisson(1.2, n)
queries_run_wk1 = rng.negative_binomial(2, 0.08, n)
support_tickets = rng.poisson(0.6, n)
days_active = np.clip(
    rng.binomial(14, 0.25, n) + (queries_run_wk1 > 20) * rng.integers(0, 5, n) + datasets_connected,
    1, 14
)

channel_effect = pd.Series(signup_channel).map(
    {"organic_search": 0.0, "paid_search": -0.3, "referral": 0.6, "content": 0.1, "partner": 0.4}
).to_numpy()

logit = (
    -3.2
    + 0.35 * np.minimum(seats_invited, 6)
    + 0.55 * np.minimum(datasets_connected, 4)
    + 0.015 * np.minimum(queries_run_wk1, 80)
    + 0.12 * days_active
    + 0.15 * np.minimum(support_tickets, 2) - 0.35 * np.maximum(support_tickets - 2, 0)
    + channel_effect
    + rng.normal(0, 0.5, n)
)
converted = rng.binomial(1, 1 / (1 + np.exp(-logit)))

trials_df = pd.DataFrame({
    "account_id": [f"ACC-{i:05d}" for i in range(1, n + 1)],
    "signup_channel": signup_channel,
    "seats_invited": seats_invited,
    "datasets_connected": datasets_connected,
    "queries_run_wk1": queries_run_wk1,
    "support_tickets": support_tickets,
    "days_active": days_active,
    "converted": converted,
})
trials_df