"""
📅 行程頁面
"""

import streamlit as st
from data.itinerary import ITINERARY

st.set_page_config(page_title="行程安排", page_icon="📅", layout="wide")

st.title("📅 釜山行程安排")
st.markdown("### 2026/01/14 (三) - 2026/01/19 (一)")
st.markdown("---")

# 顯示每日行程
for date, day_data in ITINERARY.items():
    with st.expander(f"📅 {date} ({day_data['day']}) - {day_data['title']}", expanded=False):
        for activity in day_data['activities']:
            col1, col2 = st.columns([1, 5])
            with col1:
                st.markdown(f"### {activity['icon']}")
            with col2:
                st.markdown(f"**{activity['time']}**")
                st.markdown(f"**{activity['title']}**")
                for detail in activity.get('details', []):
                    st.markdown(f"- {detail}")
                if 'naver_map' in activity:
                    naver_url = f"https://map.naver.com/v5/search/{activity['naver_map']}"
                    st.link_button("📍 開啟 Naver Map", naver_url)
            st.divider()

st.markdown("---")

# 行程建議
st.subheader("💡 旅遊小提示")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
    **🚇 交通建議**
    - 購買 T-money 卡
    - 使用 Naver Map 導航
    - 地鐵營運至晚上11點
    - 保留金海機場↔西面路線資訊
    """)

with col2:
    st.info("""
    **🍴 用餐提示**
    - 韓國餐廳通常不收服務費
    - 小菜可免費續
    - 建議避開用餐尖峰時段
    - 使用 Naver Map 導航最準確
    """)

with col3:
    st.warning("""
    **📱 實用 App**
    - Naver Map（地圖導航）
    - Papago（翻譯）
    - KakaoTalk（通訊）
    - Busan Pass（景點兌換）
    """)
