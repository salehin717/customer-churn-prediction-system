"""Streamlit dashboard for the Customer Churn Prediction System."""

import io

import joblib
import pandas as pd
import streamlit as st

from churn_prediction.data.preprocessing import clean_data, encode_categorical
from churn_prediction.models.evaluate import evaluate_model, feature_importance_df
from churn_prediction.visualization.shap_plots import (
    compute_shap_values,
    plot_shap_bar,
    plot_shap_summary,
)

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide",
)

st.title("📉 Customer Churn Prediction System")
st.markdown(
    "Upload a customer dataset and a trained model to explore predictions "
    "and model explanations."
)

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.header("Configuration")
target_col = st.sidebar.text_input("Target column name", value="Churn")
model_file = st.sidebar.file_uploader("Upload trained model (.joblib)", type=["joblib"])
data_file = st.sidebar.file_uploader("Upload dataset (.csv)", type=["csv"])

# ── Main content ─────────────────────────────────────────────────────────────
if data_file is not None:
    df = pd.read_csv(data_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head(20))
    st.write(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

    if target_col not in df.columns:
        st.error(f"Target column '{target_col}' not found in the dataset.")
        st.stop()

    cat_cols = df.select_dtypes(include="object").columns.tolist()
    if target_col in cat_cols:
        cat_cols.remove(target_col)

    df_clean = clean_data(df)
    df_encoded, _ = encode_categorical(df_clean, cat_cols)

    # Encode target if string
    if df_encoded[target_col].dtype == object:
        df_encoded[target_col] = (
            df_encoded[target_col].str.strip().str.lower().map({"yes": 1, "no": 0})
        )

    X = df_encoded.drop(columns=[target_col])
    y = df_encoded[target_col]

    if model_file is not None:
        model = joblib.load(io.BytesIO(model_file.read()))

        st.subheader("Model Performance")
        metrics = evaluate_model(model, X, y)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{metrics['accuracy']:.2%}")
        col2.metric("Precision", f"{metrics['precision']:.2%}")
        col3.metric("Recall", f"{metrics['recall']:.2%}")
        col4.metric("F1 Score", f"{metrics['f1']:.2%}")
        if "roc_auc" in metrics:
            st.metric("ROC-AUC", f"{metrics['roc_auc']:.4f}")

        st.subheader("Feature Importances")
        fi_df = feature_importance_df(model, list(X.columns))
        st.bar_chart(fi_df.set_index("feature")["importance"].head(20))

        st.subheader("SHAP Explanations")
        with st.spinner("Computing SHAP values…"):
            shap_values = compute_shap_values(model, X)

        tab1, tab2 = st.tabs(["Summary (Beeswarm)", "Feature Impact (Bar)"])
        with tab1:
            fig_summary = plot_shap_summary(shap_values, X)
            st.pyplot(fig_summary)
        with tab2:
            fig_bar = plot_shap_bar(shap_values)
            st.pyplot(fig_bar)

        st.subheader("Individual Prediction")
        row_idx = st.number_input(
            "Row index to explain", min_value=0, max_value=len(X) - 1, value=0
        )
        pred = model.predict(X.iloc[[row_idx]])[0]
        prob = (
            model.predict_proba(X.iloc[[row_idx]])[0][1]
            if hasattr(model, "predict_proba")
            else None
        )
        st.write(
            f"**Prediction:** {'Churn' if pred == 1 else 'No Churn'}"
            + (f"  |  **Probability:** {prob:.2%}" if prob is not None else "")
        )
else:
    st.info("👈 Upload a CSV dataset from the sidebar to get started.")
