import plotly.express as px

def transaction_distribution_chart(df):

    chart_data = (
        df.groupby("type")["amount"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        chart_data,
        names="type",
        values="amount",
        hole=0.4,
        title="Transaction Distribution"
    )

    return fig


def transaction_trend_chart(df):

    trend_data = (
        df.groupby("step")["amount"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        trend_data,
        x="step",
        y="amount",
        title="Transaction Trend"
    )

    return fig


def fraud_analysis_chart(df):

    fraud_data = (
        df.groupby("isFraud")
        .size()
        .reset_index(name="count")
    )

    fig = px.bar(
        fraud_data,
        x="isFraud",
        y="count",
        title="Fraud Analysis"
    )

    return fig