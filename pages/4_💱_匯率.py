"""
💱 匯率頁面
"""

import streamlit as st
from datetime import datetime
from utils.currency_api import (
    fetch_exchange_rate,
    get_krw_to_twd_rate,
    convert_krw_to_twd,
    convert_twd_to_krw
)

st.set_page_config(page_title="匯率轉換", page_icon="💱", layout="wide")

st.title("💱 韓幣 ↔ 台幣 匯率轉換")
st.markdown("---")

# 獲取即時匯率
with st.spinner("正在獲取最新匯率..."):
    exchange_data = fetch_exchange_rate("KRW", "TWD")

if exchange_data is None:
    st.error("❌ 無法獲取匯率資料，請檢查網路連線")
    st.info("💡 請稍後再試")
    rate = 0.025  # 預設匯率
    st.warning(f"⚠️ 使用預設匯率：1 KRW = {rate:.4f} TWD")
    last_update = "無法取得"
else:
    rate = exchange_data['rates']['TWD']
    last_update = exchange_data.get('date', datetime.now().strftime("%Y-%m-%d"))
    
    # 顯示即時匯率
    st.success("✅ 匯率資料更新成功！")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="即時匯率",
            value=f"1 KRW = {rate:.4f} TWD"
        )
    
    with col2:
        st.metric(
            label="反向匯率",
            value=f"1 TWD = {1/rate:.2f} KRW"
        )
    
    with col3:
        st.metric(
            label="最後更新",
            value=last_update
        )

st.markdown("---")

# 雙向轉換計算機
st.subheader("🔄 匯率轉換計算機")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ₩ 韓幣 → 台幣")
    
    # 快速金額按鈕
    st.markdown("**快速選擇：**")
    quick_amounts_krw = [10000, 50000, 100000, 500000]
    quick_cols = st.columns(4)
    
    selected_krw = 0
    for idx, amount in enumerate(quick_amounts_krw):
        with quick_cols[idx]:
            if st.button(f"₩{amount:,}", key=f"quick_krw_{amount}", use_container_width=True):
                selected_krw = amount
    
    krw_amount = st.number_input(
        "輸入韓幣金額 (KRW)",
        min_value=0,
        value=selected_krw if selected_krw > 0 else 10000,
        step=1000,
        key="krw_input"
    )
    
    twd_result = convert_krw_to_twd(krw_amount, rate)
    st.success(f"### = NT$ {twd_result:,.2f}")
    st.caption(f"₩{krw_amount:,} × {rate:.4f}")

with col2:
    st.markdown("### $ 台幣 → 韓幣")
    
    # 快速金額按鈕
    st.markdown("**快速選擇：**")
    quick_amounts_twd = [100, 500, 1000, 5000]
    quick_cols = st.columns(4)
    
    selected_twd = 0
    for idx, amount in enumerate(quick_amounts_twd):
        with quick_cols[idx]:
            if st.button(f"NT${amount:,}", key=f"quick_twd_{amount}", use_container_width=True):
                selected_twd = amount
    
    twd_amount = st.number_input(
        "輸入台幣金額 (TWD)",
        min_value=0,
        value=selected_twd if selected_twd > 0 else 1000,
        step=100,
        key="twd_input"
    )
    
    krw_result = convert_twd_to_krw(twd_amount, rate)
    st.success(f"### = ₩ {krw_result:,.0f}")
    st.caption(f"NT${twd_amount:,} ÷ {rate:.4f}")

st.markdown("---")

# 常用金額參考表
st.subheader("📋 常用金額參考表")

import pandas as pd

reference_krw = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
reference_twd = [convert_krw_to_twd(krw, rate) for krw in reference_krw]

df_reference = pd.DataFrame({
    '韓幣 (KRW)': [f"₩{krw:,}" for krw in reference_krw],
    '台幣 (TWD)': [f"NT${twd:,.2f}" for twd in reference_twd]
})

st.dataframe(df_reference, use_container_width=True, hide_index=True)

st.markdown("---")

# 提示資訊
col1, col2 = st.columns(2)

with col1:
    st.info("""
    **💡 換匯建議**
    - 在台灣銀行換匯通常匯率較優
    - 韓國機場匯率較差，建議少量兌換
    - 可使用信用卡，但注意手續費
    - T-money 卡可在便利商店儲值
    """)

with col2:
    st.success("""
    **💳 消費方式**
    - 大部分商店接受信用卡
    - 傳統市場建議準備現金
    - 地鐵、公車使用 T-money 卡
    - 小額消費也可刷卡
    """)

st.markdown("---")
st.caption("📊 資料來源：Frankfurter API（免費、無需 API Key）")
st.caption("🔄 每次重新整理頁面即可獲取最新匯率")
