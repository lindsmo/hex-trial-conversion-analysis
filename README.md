# hex-trial-conversion-analysis
Which self-service trial engagement signals predict conversion to paid? A full-stack, AI-assisted SQL + Python analysis.

**[View the live app](https://app.hex.tech/01a0d090-5e01-772b-89ff-513ad8433dcc/app/Trial-Conversion-Signals-034UWdJSzHR8mXQ8MOaB4w/latest)**

## Key finding
Dataset connections is the strongest predictor of trial-to-paid conversion, controlling for other engagement signals, followed by seats invited, days active, and query volume. Support ticket volume shows a near-neutral effect, likely masking opposing effects at low vs. high ticket counts.

**Recommendation:** Test whether prompting a second data source connection early in the trial improves conversion, rather than assuming the correlation is causal.

## Status
Built during a Hex free trial. The live app link above is active only while that trial runs; full documentation (exported notebook, code, screenshots, and a recording of the interactive filter) is in progress here in this repo so the analysis remains accessible after the trial ends.
