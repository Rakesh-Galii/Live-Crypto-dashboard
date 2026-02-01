import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Pro Crypto Tracker", layout="wide")

# Initialize session state for data persistence
if 'price_history' not in st.session_state:
    st.session_state.price_history = pd.DataFrame(columns=['Time', 'Price'])

# --- SIDEBAR FOR ANALYTICS ---
st.sidebar.title("📊 Session Statistics")
stats_placeholder = st.sidebar.empty()

st.title("🚀 Real-Time Bitcoin Analytics Dashboard")
placeholder = st.empty()

def get_crypto_data():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url).json()
        return response['bitcoin']['usd']
    except:
        return None

# The "Real-Time" Loop
while True:
    current_price = get_crypto_data()
    if current_price:
        current_time = datetime.now().strftime("%H:%M:%S")
        new_entry = pd.DataFrame({'Time': [current_time], 'Price': [current_price]})
        st.session_state.price_history = pd.concat([st.session_state.price_history, new_entry], ignore_index=True)
        
        # Keep the last 50 points for a better looking chart
        df = st.session_state.price_history.tail(50)

        # Update Sidebar Stats
        with stats_placeholder.container():
            st.metric("Max Price", f"${df['Price'].max():,}")
            st.metric("Avg Price", f"${round(df['Price'].mean(), 2):,}")
            st.write("---")
            # Export Button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Data as CSV", data=csv, file_name="live_btc_data.csv", mime="text/csv")

        with placeholder.container():
            st.metric("Current Price", f"${current_price:,}")

            # Plotting
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['Time'], y=df['Price'], mode='lines+markers', line=dict(color='#00ff00')))
            fig.update_layout(title="Live Price Action", template="plotly_dark", height=500)
            st.plotly_chart(fig, use_container_width=True)

    time.sleep(10)