# Live-Crypto-dashboard
Real-Time Bitcoin Analytics Dashboard
A live-updating cryptocurrency dashboard built to demonstrate real-time data streaming, 
statistical analysis, and automated data pipelines.

[Live App Link] https://live-crypto-dashboard88.streamlit.app/

## 📊 Key Features
- Real-Time Data Extraction:* Fetches live BTC/USD prices every 10 seconds via CoinGecko API.
- Dynamic Analytics:* Calculates a 5-period Simple Moving Average (SMA) to identify price trends.
- Session Persistence:* Tracks price history during the active session using Streamlit Session State.
- Data Export:* Built-in functionality to download captured session data as a CSV file.

## 🛠️ Tech Stack
- Language:* Python 3.x
- Data Handling:* Pandas, Requests
- Visualization:* Plotly (Interative Charts)
- Web Framework:* Streamlit
- Deployment:* GitHub & Streamlit Community Cloud

## 📂 Project Structure
- app.py: Main application script.
- requirements.txt: List of Python dependencies for cloud deployment.
- README.md: Project documentation.

## ⚙️ How to Run Locally
1. Clone the repository: git clone https://github.com/YOUR_USERNAME/repo-name.git
2. Install dependencies: pip install -r requirements.txt
3. Launch the app: streamlit run app.py
