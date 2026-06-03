import streamlit as st
import pandas as pd
import plotly.express as px
from categorizer import clean_description, get_ai_category

st.set_page_config(page_title="AI Expense Insights", layout="wide")

@st.dialog("Welcome!")
def welcome_message():
    st.markdown("### I build AI to solve real-world problems.")
    st.write(
        "Thank you for taking the time to view my project! I built this AI-powered pipeline "
        "Because I enjoy tackling messy, unstructured data and turning it into clean, actionable insights."
    )

    st.info("**Currently open to work:** I am actively seeking opportunities where I can apply my skills in Python, Machine Learning, Data science and full-stack development.")

    if st.button("Explore the Dashboard"):
        st.session_state.message_shown = True
        st.rerun()

if "message_shown" not in st.session_state:
    welcome_message()

st.title("Personal Finance AI Expense Insights Dashboard")
st.markdown("Upload your messy bank statement CSV and let AI instantly categorize your spending patterns.")

uploaded_file = st.file_uploader("Choose your bank statement CSV file", type=["CSV"])

if uploaded_file is not None:
    with st.spinner('AI is analyzing your transactions... Please wait...'):
        df = pd.read_csv(uploaded_file)
        df['withdrawal'] = df['Withdrawal'].fillna(0)

        df['Clean_Description'] = df['Description'].apply(clean_description)
        df['AI_Category'] = df['Clean_Description'].apply(get_ai_category)

        display_df = df[['Date', 'Description', 'Withdrawal', 'AI_Category']].copy()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Categorized Transactions')
            st.dataframe(display_df, use_container_width=True)

        with col2:
            st.subheader('Spending Breakdown')
            expense_df = display_df[display_df['Withdrawal']>0]

            if not expense_df.empty:
                chart_data = expense_df.groupby('AI_Category')['Withdrawal'].sum().reset_index()
                fig = px.pie(chart_data, values='Withdrawal', names='AI_Category', hole = 0.4, color_discrete_sequence = px.colors.sequential.RdBu)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No withdrawal transactions detected to display the spending breakdown chart.")