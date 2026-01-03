"""
💰 記帳頁面
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
from utils.data_manager import (
    initialize_expenses_state,
    add_expense,
    delete_expense,
    clear_all_expenses,
    get_expenses_dataframe,
    get_expenses_csv,
    calculate_statistics
)
from utils.currency_api import get_krw_to_twd_rate

st.set_page_config(page_title="旅遊記帳", page_icon="💰", layout="wide")

# 初始化 session state
initialize_expenses_state(st.session_state)

st.title("💰 旅遊記帳")
st.markdown("---")

# 獲取匯率
with st.spinner("正在獲取最新匯率..."):
    exchange_rate = get_krw_to_twd_rate()

if exchange_rate is None:
    st.error("❌ 無法獲取匯率資料，請檢查網路連線")
    exchange_rate = 0.025  # 使用預設匯率
    st.warning(f"⚠️ 使用預設匯率：1 KRW = {exchange_rate} TWD")
else:
    st.success(f"💱 目前匯率：1 KRW = {exchange_rate:.4f} TWD")

st.markdown("---")

# 新增支出表單
st.subheader("➕ 新增支出")

with st.form("expense_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        expense_date = st.date_input(
            "日期",
            value=datetime(2026, 1, 14),
            min_value=datetime(2026, 1, 14),
            max_value=datetime(2026, 1, 19)
        )
        
        category = st.selectbox(
            "分類",
            ["🍴 餐飲", "🚇 交通", "🛍️ 購物", "🏨 住宿", "🎫 景點", "📦 其他"]
        )
    
    with col2:
        amount = st.number_input(
            "金額 (KRW)",
            min_value=0,
            value=10000,
            step=1000
        )
        
        note = st.text_input("備註")
    
    submitted = st.form_submit_button("💾 儲存", use_container_width=True)
    
    if submitted:
        if amount > 0:
            add_expense(
                st.session_state,
                str(expense_date),
                category,
                amount,
                note,
                exchange_rate
            )
            st.success("✅ 支出已記錄！")
            st.rerun()
        else:
            st.error("❌ 請輸入有效的金額")

st.markdown("---")

# 統計資料
if st.session_state.expenses:
    stats = calculate_statistics(st.session_state.expenses)
    
    st.subheader("📊 支出統計")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="總支出 (KRW)",
            value=f"₩{stats['total_krw']:,.0f}"
        )
    
    with col2:
        st.metric(
            label="總支出 (TWD)",
            value=f"NT${stats['total_twd']:,.0f}"
        )
    
    with col3:
        st.metric(
            label="平均每日 (KRW)",
            value=f"₩{stats['avg_daily_krw']:,.0f}"
        )
    
    with col4:
        st.metric(
            label="平均每日 (TWD)",
            value=f"NT${stats['avg_daily_twd']:,.0f}"
        )
    
    st.markdown("---")
    
    # 圖表
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🥧 分類支出圓餅圖")
        if stats['by_category']:
            fig_pie = px.pie(
                values=list(stats['by_category'].values()),
                names=list(stats['by_category'].keys()),
                title="各分類支出比例"
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("尚無資料")
    
    with col2:
        st.subheader("📈 每日支出長條圖")
        if stats['by_date']:
            df_daily = pd.DataFrame({
                '日期': list(stats['by_date'].keys()),
                '金額': list(stats['by_date'].values())
            })
            fig_bar = px.bar(
                df_daily,
                x='日期',
                y='金額',
                title="每日支出趨勢"
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("尚無資料")
    
    st.markdown("---")

# 支出列表
st.subheader("📝 支出明細")

if st.session_state.expenses:
    # 篩選選項
    col1, col2 = st.columns(2)
    
    with col1:
        all_dates = sorted(list(set([e['date'] for e in st.session_state.expenses])))
        selected_date = st.selectbox("篩選日期", ["全部"] + all_dates)
    
    with col2:
        all_categories = sorted(list(set([e['category'] for e in st.session_state.expenses])))
        selected_category = st.selectbox("篩選分類", ["全部"] + all_categories)
    
    # 應用篩選
    filtered_expenses = st.session_state.expenses
    if selected_date != "全部":
        filtered_expenses = [e for e in filtered_expenses if e['date'] == selected_date]
    if selected_category != "全部":
        filtered_expenses = [e for e in filtered_expenses if e['category'] == selected_category]
    
    # 顯示表格
    if filtered_expenses:
        df = get_expenses_dataframe(filtered_expenses)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # 刪除功能
        st.markdown("#### 🗑️ 刪除記錄")
        for idx, expense in enumerate(st.session_state.expenses):
            col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
            with col1:
                st.text(expense['date'])
            with col2:
                st.text(expense['category'])
            with col3:
                st.text(f"₩{expense['amount_krw']:,.0f}")
            with col4:
                if st.button("🗑️", key=f"del_{idx}"):
                    delete_expense(st.session_state, idx)
                    st.rerun()
    else:
        st.info("沒有符合條件的記錄")
    
    st.markdown("---")
    
    # 資料管理
    st.subheader("💾 資料管理")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 匯出 CSV
        csv_data = get_expenses_csv(st.session_state.expenses)
        st.download_button(
            label="📥 匯出 CSV",
            data=csv_data,
            file_name=f"busan_expenses_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col2:
        # 清空記錄
        if st.button("🗑️ 清空所有記錄", use_container_width=True, type="secondary"):
            if st.button("⚠️ 確認清空？此操作無法復原", use_container_width=True, type="primary"):
                clear_all_expenses(st.session_state)
                st.success("✅ 已清空所有記錄")
                st.rerun()

else:
    st.info("📝 尚無支出記錄，請使用上方表單新增")
