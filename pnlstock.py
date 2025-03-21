import streamlit as st
import pandas as pd

st.set_page_config(page_title="P&L Text Insights App", layout="wide")
st.title("📊 Profit & Loss Insights (Symbol-wise)")

# --- FILE UPLOAD ---
st.sidebar.header("Upload Your P&L Excel File")
uploaded_file = st.sidebar.file_uploader("Upload Excel", type=["xlsx", "xls"])

if uploaded_file:
    # --- LOAD DATA ---
    df = pd.read_excel(uploaded_file)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df)
    st.markdown("### 🔝 Top 5 Best & Worst Stocks by Realized P&L")

    top5_best = df.sort_values(by='Realized P&L', ascending=False).head(5)
    top5_worst = df.sort_values(by='Realized P&L').head(5)

    st.markdown("**Top 5 Best Stocks:**")
    st.dataframe(top5_best[['Symbol', 'Realized P&L']])

    st.markdown("**Top 5 Worst Stocks:**")
    st.dataframe(top5_worst[['Symbol', 'Realized P&L']])


    st.subheader("🏆 Best & Worst Performing Stocks")
    
    # --- SUMMARY CALCULATIONS ---
    total_buy = df['Buy Value'].sum()
    total_sell = df['Sell Value'].sum()
    total_realized_pnl = df['Realized P&L'].sum()
    total_unrealized_pnl = df['Unrealized P&L'].sum()

    net_result = total_realized_pnl + total_unrealized_pnl

    st.subheader("📝 Insights Summary")

    st.markdown(f"- **Total Buy Value:** ₹{total_buy:,.2f}")
    st.markdown(f"- **Total Sell Value:** ₹{total_sell:,.2f}")
    st.markdown(f"- **Total Realized P&L:** ₹{total_realized_pnl:,.2f}")
    st.markdown(f"- **Total Unrealized P&L:** ₹{total_unrealized_pnl:,.2f}")
    st.markdown(f"- **Net Result (Realized + Unrealized):** ₹{net_result:,.2f}")

    # --- Best & Worst Performing Stocks ---
    best_stock = df.loc[df['Realized P&L'].idxmax()]
    worst_stock = df.loc[df['Realized P&L'].idxmin()]

    st.markdown("### 📈 Best & Worst Performing Stocks:")
    st.markdown(f"- **Best Stock:** {best_stock['Symbol']} with ₹{best_stock['Realized P&L']:,.2f} realized profit.")
    st.markdown(f"- **Worst Stock:** {worst_stock['Symbol']} with ₹{worst_stock['Realized P&L']:,.2f} realized loss.")

    # --- Average Realized P&L per Trade ---
    avg_pnl = df['Realized P&L'].mean()
    st.markdown(f"- **Average Realized P&L per Stock:** ₹{avg_pnl:,.2f}")

    # --- Total Number of Profitable vs Loss-making Stocks ---
    profitable = df[df['Realized P&L'] > 0].shape[0]
    loss_making = df[df['Realized P&L'] < 0].shape[0]

    st.markdown(f"- **Number of Profitable Stocks:** {profitable}")
    st.markdown(f"- **Number of Loss-making Stocks:** {loss_making}")

else:
    st.info("👆 Upload your Excel file to get detailed symbol-wise insights!")