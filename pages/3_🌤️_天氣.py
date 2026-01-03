"""
🌤️ 天氣頁面
"""

import streamlit as st
from datetime import datetime
from utils.weather_api import (
    fetch_weather_data,
    get_weather_icon,
    get_clothing_suggestion
)

st.set_page_config(page_title="天氣預報", page_icon="🌤️", layout="wide")

st.title("🌤️ 釜山天氣預報")
st.markdown("### 2026/01/14 - 2026/01/19")
st.markdown("---")

# 獲取天氣資料
with st.spinner("正在獲取天氣資料..."):
    weather_data = fetch_weather_data()

if weather_data is None:
    st.error("❌ API 請求失敗：無法獲取天氣資料")
    st.info("💡 請檢查網路連線或稍後再試")
    st.info("ℹ️ 天氣資料來自 Open-Meteo API（免費無需 API Key）")
else:
    st.success("✅ 天氣資料更新成功！")
    
    # 解析資料
    daily = weather_data.get('daily', {})
    dates = daily.get('time', [])
    temp_max = daily.get('temperature_2m_max', [])
    temp_min = daily.get('temperature_2m_min', [])
    weathercodes = daily.get('weathercode', [])
    precipitation = daily.get('precipitation_probability_max', [])
    
    # 星期對應
    weekdays = ['一', '二', '三', '四', '五', '六', '日']
    
    # 顯示天氣卡片
    cols = st.columns(3)
    
    for idx, date_str in enumerate(dates):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        weekday = weekdays[date_obj.weekday()]
        
        with cols[idx % 3]:
            with st.container():
                st.markdown(f"### {date_str}")
                st.markdown(f"#### ({weekday})")
                
                # 天氣圖示
                weather_icon = get_weather_icon(weathercodes[idx])
                st.markdown(f"## {weather_icon}")
                
                # 溫度
                st.metric(
                    label="溫度",
                    value=f"{temp_max[idx]:.1f}°C",
                    delta=f"最低 {temp_min[idx]:.1f}°C"
                )
                
                # 降雨機率
                st.progress(precipitation[idx] / 100)
                st.caption(f"🌧️ 降雨機率：{precipitation[idx]}%")
                
                # 穿搭建議
                suggestion = get_clothing_suggestion(
                    temp_max[idx],
                    temp_min[idx],
                    precipitation[idx]
                )
                st.info(f"💡 {suggestion}")
                
                st.markdown("---")
    
    # 資料來源說明
    st.markdown("---")
    st.caption("📊 資料來源：Open-Meteo API | 更新時間：" + datetime.now().strftime("%Y-%m-%d %H:%M"))
    st.caption("🔄 每次重新整理頁面即可獲取最新天氣資料")

# 天氣建議
st.markdown("---")
st.subheader("🎒 冬季釜山旅遊建議")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **🧥 衣物建議**
    - 保暖外套（羽絨衣或厚外套）
    - 長袖上衣、毛衣
    - 長褲
    - 圍巾、手套（選配）
    - 舒適的運動鞋
    """)

with col2:
    st.warning("""
    **⚠️ 注意事項**
    - 釜山冬季溫度約 0-10°C
    - 海邊風較大，體感溫度更低
    - 室內暖氣充足，建議洋蔥式穿搭
    - 隨時關注天氣變化
    """)
