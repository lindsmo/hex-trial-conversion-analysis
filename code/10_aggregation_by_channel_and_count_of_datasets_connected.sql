SELECT 
    signup_channel, 
    engagement_tier, 
    AVG(converted) AS conversion_rate, 
    COUNT(*) AS n_accounts 
FROM tiered_explicit_df
WHERE 1=1
{% if channel_filter %}
    AND signup_channel IN ({{ channel_filter | array }})
{% endif %}
GROUP BY signup_channel, engagement_tier
ORDER BY signup_channel, engagement_tier