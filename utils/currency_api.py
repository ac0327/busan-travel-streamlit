"""匯率 API 模組 - 使用 Frankfurter API"""

import requests
from typing import Optional, Dict


def fetch_exchange_rate(from_currency: str = "KRW", to_currency: str = "TWD") -> Optional[Dict]:
    """
    從 Frankfurter API 獲取匯率資料
    
    Args:
        from_currency: 來源貨幣代碼
        to_currency: 目標貨幣代碼
        
    Returns:
        包含匯率資料的字典，如果失敗則返回 None
    """
    url = "https://api.frankfurter.app/latest"
    params = {
        'from': from_currency,
        'to': to_currency
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None


def get_krw_to_twd_rate() -> Optional[float]:
    """
    獲取韓幣對台幣的匯率
    
    Returns:
        匯率（float），如果失敗則返回 None
    """
    data = fetch_exchange_rate("KRW", "TWD")
    if data and 'rates' in data and 'TWD' in data['rates']:
        return data['rates']['TWD']
    return None


def convert_krw_to_twd(krw_amount: float, rate: float) -> float:
    """
    將韓幣轉換為台幣
    
    Args:
        krw_amount: 韓幣金額
        rate: 匯率
        
    Returns:
        台幣金額
    """
    return krw_amount * rate


def convert_twd_to_krw(twd_amount: float, rate: float) -> float:
    """
    將台幣轉換為韓幣
    
    Args:
        twd_amount: 台幣金額
        rate: 匯率
        
    Returns:
        韓幣金額
    """
    return twd_amount / rate
