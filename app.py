"""
🇰🇷 釜山旅遊助手 - 主頁面
"""

import streamlit as st
from datetime import datetime, timedelta

# 設定頁面配置
st.set_page_config(
    page_title="釜山旅遊助手",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 旅程資訊
TRIP_START = datetime(2026, 1, 14)
TRIP_END = datetime(2026, 1, 19)
TOTAL_DAYS = 6
TOTAL_NIGHTS = 5

# 主標題
st.title("🇰🇷 釜山旅遊助手")
st.markdown("---")

# 旅程日期
col1, col2 = st.columns(2)
with col1:
    st.subheader("📅 旅程日期")
    st.info(f"**{TRIP_START.strftime('%Y/%m/%d')} (三) - {TRIP_END.strftime('%Y/%m/%d')} (一)**")

with col2:
    st.subheader("⏳ 倒數計時")
    today = datetime.now()
    days_until = (TRIP_START - today).days

    if days_until > 0:
        st.success(f"🎉 距離出發還有 **{days_until}** 天！")
    elif days_until == 0:
        st.success("🎊 今天就要出發了！")
    elif today <= TRIP_END:
        st.success("✈️ 旅程進行中！")
    else:
        st.info("📸 旅程已結束，期待下次旅行！")

st.markdown("---")

# 快速統計
st.subheader("📊 快速統計")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="總天數",
        value=f"{TOTAL_DAYS}天{TOTAL_NIGHTS}夜"
    )

with col2:
    st.metric(
        label="去程航班",
        value="BX796",
        delta="1/14 15:00 高雄出發"
    )

with col3:
    st.metric(
        label="回程航班",
        value="BX795",
        delta="1/19 12:00 釜山出發"
    )

st.markdown("---")

# 今日行程預覽
st.subheader("📍 今日行程預覽")

today_date = datetime.now()
if TRIP_START <= today_date <= TRIP_END:
    from data.itinerary import ITINERARY

    date_key = today_date.strftime("%Y-%m-%d")
    if date_key in ITINERARY:
        day_info = ITINERARY[date_key]
        st.success(f"**{day_info['day']} - {day_info['date']}**")
        for item in day_info['items']:
            st.write(f"• {item}")
    else:
        st.info("今天沒有特別安排的行程")
else:
    st.info("目前不在旅程期間，請使用左側選單查看完整行程")

st.markdown("---")

# 導航說明
st.subheader("🧭 使用說明")

st.markdown("""
歡迎使用釜山旅遊助手！請使用左側選單瀏覽以下功能：

- **📅 行程** - 查看完整6天行程安排
- **💰 記帳** - 記錄旅遊支出，自動轉換匯率
- **🌤️ 天氣** - 查看釜山天氣預報（含穿搭建議）
- **💱 匯率** - 即時韓幣↔台幣匯率轉換
- **🍴 餐廳** - 必吃餐廳清單（含 Naver 地圖）
- **ℹ️ 資訊** - 航班、住宿、釜山Pass 景點

祝您有個愉快的釜山之旅！🎉
""")

# 頁腳
st.markdown("---")
st.caption("💙 Built with Streamlit | 100% 免費 API | 無需註冊")
