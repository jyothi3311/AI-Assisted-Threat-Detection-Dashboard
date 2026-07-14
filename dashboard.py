import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI-Assisted Threat Detection Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- Load Dataset ----------------
df = pd.read_csv("data/cleaned_portscan.csv")
df.columns = df.columns.str.strip()

# ---------------- Load Risk Data ----------------
risk_df = pd.read_csv("data/risk_data.csv")
risk_df.columns = risk_df.columns.str.strip()

# ---------------- Load Model ----------------
model = joblib.load("models/random_forest.pkl")

# ---------------- Sidebar ----------------
st.sidebar.title("🛡️ CyberShield AI")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "ML Dashboard", "Threat Reports"]
)

# ==========================================================
# OVERVIEW PAGE
# ==========================================================

if page == "Overview":

    st.title("🛡️ AI-Assisted Threat Detection Dashboard")
    st.markdown("### Cybersecurity Threat Monitoring using Machine Learning")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Records", len(df))
    col2.metric("Benign Traffic", (df["Label"] == "BENIGN").sum())
    col3.metric("PortScan Attacks", (df["Label"] == "PortScan").sum())
    col4.metric("High Risk Events", (risk_df["Risk Level"] == "High").sum())

    st.divider()

    st.subheader("🥧 Threat Distribution")

    pie = px.pie(
        df,
        names="Label",
        title="Threat Distribution"
    )

    st.plotly_chart(pie, use_container_width=True)

    st.divider()

    st.subheader("📊 Threat Count")

    threat_count = (
        df["Label"]
        .value_counts()
        .rename_axis("Threat")
        .reset_index(name="Count")
    )

    bar = px.bar(
        threat_count,
        x="Threat",
        y="Count",
        color="Threat"
    )

    st.plotly_chart(bar, use_container_width=True)

    st.divider()

    st.subheader("📋 Recent Threats")

    st.dataframe(
        risk_df[["Label", "Risk Level"]].head(10),
        use_container_width=True
    )

    st.divider()

    st.subheader("🤖 AI Prediction")

    sample = df.drop("Label", axis=1).iloc[[0]]

    prediction = model.predict(sample)

    if prediction[0] == 0:
        st.success("Prediction : BENIGN")
    else:
        st.error("Prediction : PORTSCAN")

# ==========================================================
# ML DASHBOARD
# ==========================================================

elif page == "ML Dashboard":

    st.title("🤖 Machine Learning Dashboard")

    st.metric("Model", "Random Forest")

    st.metric("Accuracy", "100%")

    st.metric("Dataset Records", len(df))

    st.metric("Features", df.shape[1] - 1)

    st.success("Model Status : Active")

    st.write("The trained Random Forest model is used to classify network traffic as BENIGN or PORTSCAN.")

# ==========================================================
# THREAT REPORTS
# ==========================================================

elif page == "Threat Reports":

    st.title("📑 Threat Reports")

    report = (
        risk_df.groupby(["Label", "Risk Level"])
        .size()
        .reset_index(name="Count")
    )

    st.dataframe(report, use_container_width=True)

    chart = px.bar(
        report,
        x="Label",
        y="Count",
        color="Risk Level",
        barmode="group",
        title="Threat Report"
    )

    st.plotly_chart(chart, use_container_width=True)

    st.success("Threat report generated successfully.")

# ---------------- Footer ----------------

st.markdown("---")
st.caption("Infosys Springboard Internship Project | Team B")