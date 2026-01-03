# 🇰🇷 釜山旅遊助手

> 完整的釜山旅遊行程管理 Web App - 使用 Python + Streamlit 打造

協助您輕鬆管理 **2026/1/14-1/19** 釜山旅遊行程，包含行程規劃、記帳、天氣預報、匯率轉換等實用功能！

## ✨ 功能特色

### 📅 行程管理
- 完整的 6 天 5 夜行程規劃
- 每日行程清單與景點安排
- 美觀的卡片式介面

### 💰 旅遊記帳
- 快速記錄每筆支出
- 自動轉換韓幣/台幣匯率
- 即時統計與視覺化圖表
- 支出分類管理（餐飲、交通、購物等）
- CSV 匯出功能

### 🌤️ 天氣預報
- 釜山 6 日天氣預報
- 溫度、降雨機率顯示
- 智慧穿搭建議

### 💱 匯率轉換
- 即時韓幣 ↔ 台幣匯率
- 雙向轉換計算機
- 常用金額快速按鈕
- 匯率參考表

### 🍴 餐廳推薦
- 精選必吃餐廳清單
- Naver Map 一鍵導航
- 實用韓文用餐短句

### ℹ️ 旅遊資訊
- 航班資訊（去回程）
- 住宿詳細資料
- 釜山 Pass 景點清單

## 🆓 100% 免費、無需 API Key

本專案使用完全免費的 API 服務，無需註冊或申請 API Key：

- **天氣資料**：[Open-Meteo API](https://open-meteo.com/)
- **匯率資料**：[Frankfurter API](https://www.frankfurter.app/)

## 🚀 快速開始

### 環境需求

- Python 3.8 或以上版本
- pip（Python 套件管理工具）

### 安裝步驟

1. **克隆專案**
   ```bash
   git clone https://github.com/ac0327/busan-travel-streamlit.git
   cd busan-travel-streamlit
   ```

2. **安裝相依套件**
   ```bash
   pip install -r requirements.txt
   ```

3. **啟動應用程式**
   ```bash
   streamlit run app.py
   ```

4. **開啟瀏覽器**
   
   應用程式會自動在瀏覽器中開啟，預設網址：`http://localhost:8501`

## 📦 套件需求

- `streamlit>=1.28.0` - Web 應用程式框架
- `pandas>=2.0.0` - 資料處理
- `plotly>=5.17.0` - 互動式圖表
- `requests>=2.31.0` - API 請求

詳細版本請參考 `requirements.txt`

## 📁 專案結構

```
busan-travel-streamlit/
├── app.py                      # 主頁面
├── pages/                      # 多頁面應用
│   ├── 1_📅_行程.py
│   ├── 2_💰_記帳.py
│   ├── 3_🌤️_天氣.py
│   ├── 4_💱_匯率.py
│   ├── 5_🍴_餐廳.py
│   └── 6_ℹ️_資訊.py
├── utils/                      # 工具模組
│   ├── weather_api.py         # 天氣 API
│   ├── currency_api.py        # 匯率 API
│   └── data_manager.py        # 資料管理
├── data/                       # 資料模組
│   ├── itinerary.py           # 行程資料
│   ├── restaurants.py         # 餐廳資料
│   ├── flights.py             # 航班資料
│   └── hotels.py              # 住宿資料
├── .streamlit/                 # Streamlit 配置
│   └── config.toml
├── requirements.txt            # 套件需求
├── .gitignore
└── README.md
```

## 🌐 部署到 Streamlit Cloud

### 部署步驟

1. **Fork 或 Clone 此 Repository**
   
   確保你的 GitHub 帳號有此專案的存取權限

2. **前往 Streamlit Cloud**
   
   訪問 [https://share.streamlit.io/](https://share.streamlit.io/)

3. **使用 GitHub 帳號登入**

4. **點擊 "New app" 建立新應用**

5. **設定應用資訊**
   - Repository: `ac0327/busan-travel-streamlit`
   - Branch: `main` 或 `copilot/create-busan-travel-app`
   - Main file path: `app.py`

6. **點擊 "Deploy"**

7. **等待 1-2 分鐘**
   
   應用程式即可上線，您會獲得一個公開的網址！

### 優點

- ✅ 完全免費
- ✅ 自動更新（當您 push 到 GitHub）
- ✅ HTTPS 安全連線
- ✅ 24/7 可用

## 📸 螢幕截圖

_（此處預留螢幕截圖區域）_

## 🎯 使用指南

### 首頁
- 查看旅程倒數計時
- 快速統計資訊
- 今日行程預覽

### 行程頁面
- 完整 6 天行程安排
- 每日景點與活動
- 旅遊小提示

### 記帳頁面
1. 使用表單新增支出
2. 選擇日期、分類、輸入金額
3. 自動計算台幣金額
4. 查看統計圖表
5. 匯出 CSV 報表

### 天氣頁面
- 查看未來 6 天天氣
- 溫度與降雨機率
- 獲取穿搭建議

### 匯率頁面
- 即時匯率查詢
- 韓幣/台幣互轉
- 常用金額快速計算

### 餐廳頁面
- 瀏覽推薦餐廳
- 點擊開啟 Naver Map
- 學習實用韓文短句

### 資訊頁面
- 檢視航班時間
- 查看住宿訂房資訊
- 釜山 Pass 景點清單

## 💡 開發說明

### 技術特色

- **多頁面架構**：使用 Streamlit 的 pages 機制
- **Session State**：記帳資料持久化
- **API 整合**：無縫整合免費 API 服務
- **錯誤處理**：完善的 API 錯誤處理與提示
- **視覺化**：使用 Plotly 打造互動式圖表
- **響應式設計**：自動適應不同螢幕尺寸

### 自訂資料

您可以輕鬆修改 `data/` 目錄下的檔案來自訂：
- 行程安排
- 餐廳清單
- 航班資訊
- 住宿資料

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request！

## 📝 授權

MIT License

## 👨‍💻 作者

ac0327

---

**祝您有個愉快的釜山之旅！** 🇰🇷 ✈️ 🎉
