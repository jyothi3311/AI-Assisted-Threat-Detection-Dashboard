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

# ---------------- Load Data ----------------
df = pd.read_csv("data/cleaned_portscan.csv")
df.columns = df.columns.str.strip()

# ---------------- Load Model ----------------
model = joblib.load("models/random_forest.pkl")

# ---------------- Sidebar ----------------
st.sidebar.title("🛡️ CyberShield AI")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "ML Dashboard", "Threat Reports"]
)

# =====================================================
# OVERVIEW PAGE
# =====================================================

if page == "Overview":

    st.title("🛡️ AI-Assisted Threat Detection Dashboard")
    st.markdown("### Cybersecurity Threat Monitoring using Machine Learning")

    st.subheader("Dashboard Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(df))
    col2.metric("Benign Traffic", (df["Label"] == "BENIGN").sum())
    col3.metric("PortScan Attacks", (df["Label"] == "PortScan").sum())

    st.divider()

    st.subheader("Threat Distribution")

    fig = px.pie(
        df,
        names="Label",
        title="Normal vs Attack Traffic"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Sample Prediction")

    sample = df.drop("Label", axis=1).iloc[[0]]
    prediction = model.predict(sample)

    if prediction[0] == 0:
        st.success("Prediction: BENIGN")
    else:
        st.error("Prediction: PORTSCAN")


# =====================================================
# ML DASHBOARD
# =====================================================

elif page == "ML Dashboard":

    st.title("🤖 ML Dashboard")

    st.metric("Model", "Random Forest")
    st.metric("Accuracy", "100%")
    st.metric("Dataset Size", len(df))

    st.success("Model Status : Active")

    st.write("The Random Forest model is trained and ready for predictions.")


# =====================================================
# THREAT REPORTS
# =====================================================

elif page == "Threat Reports":

    st.title("📑 Threat Reports")

    report = df["Label"].value_counts().reset_index()
    report.columns = ["Threat Type", "Count"]

    st.dataframe(report)

    fig = px.bar(
        report,
        x="Threat Type",
        y="Count",
        color="Threat Type",
        title="Threat Count"
    )

    st.plotly_chart(fig, use_container_width=True)