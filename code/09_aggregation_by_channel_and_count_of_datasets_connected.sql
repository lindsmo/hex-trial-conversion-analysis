SELECT 
    signup_channel, 
    engagement_tier, 
    AVG(converted) AS conversion_rate, 
    COUNT(*) AS n_accounts 
FROM tiered_explicit_df
GROUP BY signup_channel, engagement_tier
ORDER BY signup_channel, engagement_tier