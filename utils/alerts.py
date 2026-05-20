def generate_budget_alert(
    total_amount,
    monthly_budget
):

    if total_amount > monthly_budget:

        return "Budget Exceeded"

    return "Budget Within Limit"


def generate_fraud_alert(
    fraud_count
):

    if fraud_count > 0:

        return "Fraud Transactions Detected"

    return "No Fraud Detected"