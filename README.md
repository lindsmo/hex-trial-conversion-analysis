# hex-trial-conversion-analysis

Which self-service trial engagement signals predict conversion to paid? A full-stack, AI-assisted SQL + Python analysis.

**[View the live app](https://app.hex.tech/01a0d090-5e01-772b-89ff-513ad8433dcc/app/Trial-Conversion-Signals-034UWdJSzHR8mXQ8MOaB4w/latest)** — *active only during the Hex trial; see Status below*

## Key Findings

Here's what the analysis found:

![Key findings published in the Hex app](/media/hero-key-findings.png)

The strongest predictor, dataset connections, shows a clear stepped increase in conversion rate for each additional dataset connected.

## Digging Into the Top Signal

An initial approach using equal-width bucketing for the dataset connections produced distributions that were too skewed, with most trials falling into the lowest buckets. After experimenting with a couple possible divisions for explicit bucketing, setting buckets for 0, 1, 2, and 3+ datasets connected yielded the most even distribution of trials across buckets.

![Comparison of the quantile and explicit binning strategies](/media/bucketing-quantile-vs-explicit.png)

## Exploring the App

An interactive signup channel filter allows exploration of differences in engagement and conversion by signup channel.

![Demo of the interactive filter](/media/app-demo.gif)

![Demo of the interactive filter: unfiltered](/media/app-filter-unfiltered.png)  ![Demo of the interactive filter: filtered to referral](/media/app-filter-referral.png)

## How This Was Built

Built with Hex's AI for data generation, chart scaffolding, statistical modeling strategy, and troubleshooting support. The agent identified that quantile-based bucketing wasn't appropriate for this dataset's skew and proposed an initial explicit-bin approach, which I verified I understood and then refined further (splitting one combined bin into two for a clearer distribution view). I drafted and adapted the SQL aggregation logic myself, with agent help debugging two issues (unnecessary CASE logic once conversion values were already 0/1, and a missing GROUP BY column). I also identified that text-only bin labels, in both the agent's suggested bins and my own original quantile bins, sorted incorrectly on the chart axis, and added numeric prefixes to fix it. I verified the agent's statistical modeling approach and outputs at each step, and made the final calls on methodology and takeaways.

## Code

- [code/01_synthetic_trial_engagement_data_generation.py](...)
- [code/02_dataset_profile.py](...)
- [code/03_overall_conversion_rate.py](...)
- [code/04_correlation_baseline.py](...)
- [code/05_standardized_logistic_regression.py](...)
- [code/06_full_model_summary_for_p-value_omit_from_published_app.py](...)
- [code/07_bucketing_top_signal_qualtiles_rejected_skewed_toward_0.py](...)
- [code/08_bucketing_top_signal_explicit_bins.py](...)
- [code/09_distill_signup_channel_distinct_values_to_populate_a_channel_filter.sql](...)
- [code/10_aggregation_by_channel_and_count_of_datasets_connected.sql](...)

## Status

Built during a free Hex trial. The live app link above is active only while that
trial runs. This repo preserves the full analysis:
- [notebook/trial_conversion_signals.ipynb](...): exported notebook (SQL/input parameters may not render identically to the live app)
- [hex-project/trial_conversion_signals.yaml](...): full project logic, lossless
- [media/archive/](...): full-page captures of both app tabs, plus the regression table and bucketing charts in isolation