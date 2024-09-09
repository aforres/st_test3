import streamlit as st
import time
import numpy as np
import pandas as pd


st.subheader("An example plot of a widget market")
st.markdown("Yesterday's widget market was volatile and very erratic in the face of poor monthly US employment figures.")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    
    time.sleep(0.05)
    progress_bar.empty()
    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
# rerun.

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)

st.button("Re-run")
