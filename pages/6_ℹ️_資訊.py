"""
ℹ️ 資訊頁面 - 航班、住宿、釜山Pass
"""

import streamlit as st
from data.flights import FLIGHTS
from data.hotels import HOTELS, BUSAN_PASS

st.set_page_config(page_title="旅遊資訊", page_icon="ℹ️", layout="wide")

st.title("ℹ️ 旅遊資訊")
st.markdown("---")

# 使用 tabs 分成四個分頁
tab1, tab2, tab3, tab4 = st.tabs(["✈️ 航班資訊", "🏨 住宿資訊", "🎫 釜山 Pass 景點", "🚇 交通指南"])

# Tab 1: 航班資訊
with tab1:
    st.header("✈️ 航班資訊")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛫 去程航班")
        outbound = FLIGHTS['outbound']
        
        with st.container():
            st.info(f"""
            **日期：** {outbound['date']}
            
            **航班編號：** {outbound['flight_number']}
            
            **起飛：** {outbound['departure']['airport']} {outbound['departure']['time']}
            
            **抵達：** {outbound['arrival']['airport']} {outbound['arrival']['time']}
            
            **人數：** {outbound['passengers']} 位
            """)
    
    with col2:
        st.subheader("🛬 回程航班")
        return_flight = FLIGHTS['return']
        
        with st.container():
            st.info(f"""
            **日期：** {return_flight['date']}
            
            **航班編號：** {return_flight['flight_number']}
            
            **起飛：** {return_flight['departure']['airport']} {return_flight['departure']['time']}
            
            **抵達：** {return_flight['arrival']['airport']} {return_flight['arrival']['time']}
            
            **人數：** {return_flight['passengers']} 位
            """)
    
    st.markdown("---")
    
    st.subheader("💡 航班提醒")
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **📋 登機前準備**
        - 提前 2-3 小時到機場
        - 確認護照效期
        - 準備登機證（電子或紙本）
        - 確認托運行李規定
        """)
    
    with col2:
        st.warning("""
        **🧳 行李提醒**
        - 托運行李：23kg
        - 手提行李：7kg
        - 液體限制：100ml
        - 注意禁帶物品
        """)

# Tab 2: 住宿資訊
with tab2:
    st.header("🏨 住宿資訊")
    
    for idx, hotel in enumerate(HOTELS):
        with st.expander(f"🏨 {hotel['name']}", expanded=True):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"### {hotel['name']}")
                st.markdown(f"**韓文名稱：** {hotel['name_korean']}")
                st.markdown(f"**訂房人：** {hotel['guest_name']}")
                st.markdown(f"**入住日期：** {hotel['check_in']}")
                st.markdown(f"**退房日期：** {hotel['check_out']}")
                st.markdown(f"**訂房編號：** {hotel['booking_number']}")
            
            with col2:
                # Naver Map 連結
                naver_map_url = f"https://map.naver.com/v5/search/{hotel['name_korean']}"
                st.link_button(
                    "📍 開啟 Naver Map",
                    naver_map_url,
                    use_container_width=True
                )
        
        if idx < len(HOTELS) - 1:
            st.markdown("---")
    
    st.markdown("---")
    
    st.subheader("💡 住宿提醒")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **🏨 入住須知**
        - 攜帶護照辦理入住
        - 確認訂房編號
        - 詢問早餐時間
        - 了解設施使用規則
        """)
    
    with col2:
        st.success("""
        **🔑 退房須知**
        - 退房時間：通常 10:00-11:00
        - 歸還房卡
        - 確認無遺留物品
        - 可寄放行李
        """)

# Tab 3: 釜山 Pass 景點
with tab3:
    st.header("🎫 釜山 Pass 景點")
    
    for area, attractions in BUSAN_PASS.items():
        st.subheader(f"📍 {area}")
        
        for attraction in attractions:
            if attraction['name'] == "未定":
                st.info("🔜 景點待確認")
            else:
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"### {attraction['name']}")
                    st.markdown(f"**韓文名稱：** {attraction['name_korean']}")
                    if attraction['hours']:
                        st.markdown(f"**營業時間：** {attraction['hours']}")
                
                with col2:
                    if attraction['name_korean']:
                        # Naver Map 連結
                        naver_map_url = f"https://map.naver.com/v5/search/{attraction['name_korean']}"
                        st.link_button(
                            "📍 開啟 Naver Map",
                            naver_map_url,
                            use_container_width=True
                        )
                
                st.markdown("---")
    
    st.subheader("💡 釜山 Pass 使用須知")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **🎫 使用方式**
        - 出示電子或實體 Pass
        - 確認景點是否需預約
        - 注意使用期限
        - 每個景點限用一次
        """)
    
    with col2:
        st.success("""
        **⏰ 參觀建議**
        - 提前規劃參觀順序
        - 確認景點營業時間
        - 避開假日人潮
        - 預留交通時間
        """)

# Tab 4: 交通指南
with tab4:
    st.header("🚇 交通指南")
    
    st.subheader("📍 常用地鐵路線")
    
    # 路線1
    st.markdown("### 🔹 金海機場 ↔ 西面")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info("""
        **路線：** 金海機場 → 【輕軌】沙上站 → 【地鐵2號線】西面站
        
        **時間：** 約 40-50 分鐘
        
        **費用：** 約 2,000-2,500 KRW
        
        **備註：** 最經濟的方式，適合不趕時間的旅客
        """)
    
    st.markdown("---")
    
    # 路線2
    st.markdown("### 🔹 西面 ↔ 海雲台")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info("""
        **路線：** 西面站 → 【地鐵2號線】海雲台站
        
        **時間：** 約 30 分鐘
        
        **費用：** 約 1,500 KRW
        
        **備註：** 直達，非常方便
        """)
    
    st.markdown("---")
    
    # 路線3
    st.markdown("### 🔹 海雲台 ↔ 廣安里")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info("""
        **路線：** 海雲台站 → 【地鐵2號線】廣安站
        
        **時間：** 約 15 分鐘
        
        **費用：** 約 1,500 KRW
        
        **備註：** 廣安大橋夜景必訪
        """)
    
    st.markdown("---")
    
    # 路線4
    st.markdown("### 🔹 西面 ↔ 釜山站")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info("""
        **路線：** 西面站 → 【地鐵1號線】釜山站
        
        **時間：** 約 10 分鐘
        
        **費用：** 約 1,500 KRW
        
        **備註：** 釜山站商圈、樂天超市
        """)
    
    st.markdown("---")
    
    st.subheader("💳 T-Money 卡使用說明")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **✅ 購買與儲值**
        - 可在便利商店（CU、GS25）購買
        - 卡片費用：約 2,500-4,000 KRW
        - 可在便利商店或地鐵站儲值
        - 餘額可在便利商店退款
        """)
    
    with col2:
        st.info("""
        **🎯 使用範圍**
        - 地鐵、公車通用
        - 轉乘有優惠（30分鐘內）
        - 便利商店可使用
        - 計程車部分可用
        """)
    
    st.markdown("---")
    
    st.subheader("💰 地鐵費用參考")
    
    st.markdown("""
    | 距離 | 使用 T-Money | 單程票 |
    |------|-------------|--------|
    | 10km 以內 | 1,400 KRW | 1,500 KRW |
    | 10-40km | 1,500-1,900 KRW | 1,600-2,000 KRW |
    | 40km 以上 | 每 5km +100 KRW | 每 5km +100 KRW |
    
    💡 **小提示：** 使用 T-Money 卡比購買單程票更便宜且方便！
    """)
    
    st.markdown("---")
    
    st.subheader("🗺️ 地鐵路線圖")
    
    st.info("""
    **建議使用 Naver Map 查詢路線**
    
    - 可顯示即時轉乘資訊
    - 包含步行時間
    - 提供多種路線選擇
    - 支援中文介面
    """)

st.markdown("---")
st.caption("💙 所有地圖連結將開啟 Naver Map（韓國最準確的地圖服務）")
