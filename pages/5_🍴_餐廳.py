"""
🍴 餐廳頁面
"""

import streamlit as st
from data.restaurants import RESTAURANTS

st.set_page_config(page_title="餐廳推薦", page_icon="🍴", layout="wide")

st.title("🍴 必吃餐廳推薦")
st.markdown("---")

# 顯示餐廳卡片
for restaurant in RESTAURANTS:
    with st.expander(f"{restaurant['emoji']} {restaurant['name']} ({restaurant['name_korean']})", expanded=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"### {restaurant['emoji']} {restaurant['name']}")
            st.markdown(f"**韓文名稱：** {restaurant['name_korean']}")
            st.markdown(f"**推薦菜色：** {restaurant['recommended']}")
            st.markdown(f"**📍 位置：** {restaurant['location']}")
        
        with col2:
            # Naver Map 連結
            naver_map_url = f"https://map.naver.com/v5/search/{restaurant['name_korean']}"
            st.link_button(
                "📍 開啟 Naver Map",
                naver_map_url,
                use_container_width=True
            )
        
        st.markdown("---")

# 用餐建議
st.subheader("💡 用餐小提示")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **🍽️ 點餐技巧**
    - 使用 Papago 翻譯 App
    - 指著菜單圖片點餐
    - 學幾句簡單韓文
    - 小菜可免費續
    """)

with col2:
    st.success("""
    **⏰ 用餐時間**
    - 午餐：11:30-13:30
    - 晚餐：18:00-20:00
    - 避開尖峰時段
    - 熱門餐廳建議早點去
    """)

with col3:
    st.warning("""
    **💰 付款方式**
    - 大部分接受信用卡
    - 建議準備現金備用
    - 通常不需給小費
    - 結帳在櫃台進行
    """)

st.markdown("---")

# 特色美食清單
st.subheader("🥘 釜山必吃美食")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🍜 在地特色**
    - 豬肉湯飯（돼지국밥）
    - 生魚片（회）
    - 糖餅（씨앗호떡）
    - 炸雞（치킨）
    - 飯捲（김밥）
    """)

with col2:
    st.markdown("""
    **🥩 烤肉類**
    - 韓式烤肉（고기구이）
    - 鹽烤肉（소금구이）
    - 五花肉（삼겹살）
    - 豬頸肉（항정살）
    - 一隻雞（닭한마리）
    """)

st.markdown("---")

# 實用韓文
st.subheader("🗣️ 實用餐廳韓文")

korean_phrases = {
    "你好": "안녕하세요 (An-nyeong-ha-se-yo)",
    "謝謝": "감사합니다 (Gam-sa-ham-ni-da)",
    "請給我菜單": "메뉴 주세요 (Me-nyu ju-se-yo)",
    "這個": "이거 (I-geo)",
    "好吃": "맛있어요 (Ma-si-sseo-yo)",
    "多少錢": "얼마예요 (Eol-ma-ye-yo)",
    "結帳": "계산해 주세요 (Gye-san-hae ju-se-yo)",
    "不辣": "안 매워요 (An mae-wo-yo)",
    "水": "물 (Mul)",
    "廁所": "화장실 (Hwa-jang-sil)"
}

cols = st.columns(2)
for idx, (chinese, korean) in enumerate(korean_phrases.items()):
    with cols[idx % 2]:
        st.code(f"{chinese}\n{korean}", language=None)

st.markdown("---")
st.caption("💙 使用 Naver Map 可以獲得最準確的導航資訊")
st.caption("📱 建議下載 Papago 翻譯 App，可即時翻譯菜單")
