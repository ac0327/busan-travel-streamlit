"""天氣 API 模組 - 使用 Open-Meteo API"""

import requests
from typing import Optional, Dict


def get_weather_icon(weathercode: int) -> str:
    """
    根據天氣代碼返回對應的 emoji 圖示

    Args:
        weathercode: Open-Meteo 天氣代碼

    Returns:
        天氣圖示字串（emoji + 描述）
    """
    weather_icons = {
        0: '☀️ 晴天',
        1: '🌤️ 多雲',
        2: '⛅ 局部多雲',
        3: '☁️ 陰天',
        45: '🌫️ 霧',
        48: '🌫️ 霧',
        51: '🌦️ 小雨',
        53: '🌦️ 小雨',
        55: '🌧️ 雨',
        61: '🌧️ 雨',
        63: '🌧️ 雨',
        65: '🌧️ 大雨',
        71: '🌨️ 雪',
        73: '🌨️ 雪',
        75: '🌨️ 大雪',
        77: '🌨️ 雪',
        80: '🌧️ 陣雨',
        81: '🌧️ 陣雨',
        82: '🌧️ 大陣雨',
        85: '🌨️ 陣雪',
        86: '🌨️ 陣雪',
        95: '⛈️ 雷雨',
        96: '⛈️ 雷雨',
        99: '⛈️ 雷雨'
    }
    return weather_icons.get(weathercode, '🌤️ 多雲')


def get_clothing_suggestion(temp_max: float, temp_min: float, precipitation: float) -> str:
    """
    根據溫度和降雨機率提供穿搭建議

    Args:
        temp_max: 最高溫度
        temp_min: 最低溫度
        precipitation: 降雨機率

    Returns:
        穿搭建議字串
    """
    avg_temp = (temp_max + temp_min) / 2

    suggestions = []

    # 溫度建議
    if avg_temp < 5:
        suggestions.append("🧥 厚外套、毛衣")
    elif avg_temp < 10:
        suggestions.append("🧥 外套、長袖")
    elif avg_temp < 15:
        suggestions.append("👕 薄外套、長袖")
    elif avg_temp < 20:
        suggestions.append("👕 長袖或短袖+薄外套")
    else:
        suggestions.append("👕 短袖")

    # 降雨建議
    if precipitation > 50:
        suggestions.append("☔ 雨傘必備")
    elif precipitation > 30:
        suggestions.append("🌂 建議攜帶雨傘")

    return "、".join(suggestions)


def fetch_weather_data(
    latitude: float = 35.1796,
    longitude: float = 129.0756,
    start_date: str = "2026-01-14",
    end_date: str = "2026-01-19"
) -> Optional[Dict]:
    """
    從 Open-Meteo API 獲取天氣預報資料

    Args:
        latitude: 緯度（預設釜山）
        longitude: 經度（預設釜山）
        start_date: 開始日期 (YYYY-MM-DD)
        end_date: 結束日期 (YYYY-MM-DD)

    Returns:
        天氣資料字典，如果失敗則返回 None
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': 'temperature_2m_max,temperature_2m_min,weathercode,precipitation_probability_max',
        'timezone': 'Asia/Seoul',
        'start_date': start_date,
        'end_date': end_date
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None
