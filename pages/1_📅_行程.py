"""
📅 行程頁面
"""

import streamlit as st
from data.itinerary import ITINERARY

st.set_page_config(page_title="行程安排", page_icon="📅", layout="wide")

st.title("📅 釜山行程安排")
st.markdown("### 2026/01/14 (三) - 2026/01/19 (一)")
st.markdown("---")

# 使用不同顏色的容器展示每天的行程
colors = ["blue", "green", "orange", "red", "violet", "rainbow"]

for idx, (date_key, day_info) in enumerate(ITINERARY.items()):
    with st.container():
        st.subheader(f"{day_info['day']} - {day_info['date']}")
        
        # 根據日期使用不同的展示方式
        if idx % 2 == 0:
            # 使用 info 框
            items_text = "\n\n".join([f"• {item}" for item in day_info['items']])
            st.info(items_text)
        else:
            # 使用 expander
            with st.expander("📋 查看行程", expanded=True):
                for item in day_info['items']:
                    st.write(f"• {item}")
        
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
    """)

with col2:
    st.info("""
    **🍴 用餐提示**
    - 韓國餐廳通常不收服務費
    - 小菜可免費續
    - 建議避開用餐尖峰時段
    """)

with col3:
    st.warning("""
    **📱 實用 App**
    - Naver Map（地圖導航）
    - Papago（翻譯）
    - KakaoTalk（通訊）
    """)
