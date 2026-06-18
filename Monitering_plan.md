# Monitoring Plan

## Objective

Monitor the churn prediction service after deployment to ensure reliability, fairness, and business value.

## Metrics to Track

### 1. Data Drift

Monitor whether incoming customer data differs significantly from training data.

Examples:

* Distribution of total_spend
* Sessions_30d changes
* Ticket_count trends

Trigger investigation if drift exceeds predefined thresholds.

---

### 2. Prediction Distribution

Track:

* Percentage of customers predicted as churners
* Average churn probability
* Changes in risk-level distribution

Sudden changes may indicate model degradation.

---

### 3. Business Outcomes

Measure:

* Customer retention rate
* Campaign conversion rate
* Revenue saved through interventions
* Reduction in churn rate

---

### 4. API Errors

Track:

* Response latency
* Failed requests
* HTTP 4xx errors
* HTTP 5xx errors

Set alerts for increased error rates.

---

### 5. Retraining Triggers

Retrain the model when:

* Significant data drift is detected
* Prediction quality decreases
* Business KPIs decline
* Every 3–6 months as part of routine maintenance

## Responsible Use Note

The API should support retention strategies and customer engagement.

The API should NOT be used to:

* Deny services to customers
* Make fully automated business decisions
* Discriminate against customer groups

Human review should be included in high-impact decisions.
