
from PIL import Image
import streamlit as st
from analytics.query import query_unique_timeframes, query_performance_overview_data


st.set_page_config(
    page_title="Office",
    page_icon=Image.open("assets/logo.ico"),
    layout='wide',
    initial_sidebar_state='auto')
st.markdown("# Head Office")
st.sidebar.header("Head Office")

timeframe = st.sidebar.radio(
    label="Select timeframe:",
    options=["Month", "Quarter", "Year"],
    index=1,
    key="timeframe",
    horizontal=True,
)
period_str_list = query_unique_timeframes(timeframe)
start_str = st.sidebar.selectbox(label="Start", options=period_str_list, index=len(period_str_list)-3, key="start_str")
end_str = st.sidebar.selectbox(label="End", options=period_str_list, index=len(period_str_list)-1, key="end_str")
if start_str > end_str:
    st.toast("Wrong period selected!", icon="🚨")
if "2020" in start_str or "2020" in end_str or "2021" in start_str or "2021" in end_str:
    st.toast("2020 and 2021 data cannot be splited by cost center!", icon="ℹ️")

report_type = st.sidebar.radio(
    label="Select report type:",
    options=["Standard", "Adjusted_coef"],
    index=0,
    key="report_type",
)

search_btn = st.sidebar.button("Search")
if search_btn:
    # Assuming you have a function to query data based on these parameters
    df = query_performance_overview_data(department_name="head office general",start_str=start_str, end_str=end_str, report_type=report_type)
    st.dataframe(df, use_container_width=True, hide_index=True)
