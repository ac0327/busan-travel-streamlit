"""資料管理模組 - 處理記帳資料的存儲和操作"""

import pandas as pd
from datetime import datetime
from typing import List, Dict


def initialize_expenses_state(st_session_state):
    """
    初始化 session state 中的支出資料

    Args:
        st_session_state: Streamlit session state 物件
    """
    if 'expenses' not in st_session_state:
        st_session_state.expenses = []


def add_expense(
    st_session_state,
    date: str,
    category: str,
    amount_krw: float,
    note: str,
    rate: float
):
    """
    新增支出記錄

    Args:
        st_session_state: Streamlit session state 物件
        date: 日期
        category: 分類
        amount_krw: 韓幣金額
        note: 備註
        rate: 匯率
    """
    expense = {
        'date': date,
        'category': category,
        'amount_krw': amount_krw,
        'amount_twd': amount_krw * rate,
        'note': note
    }
    st_session_state.expenses.append(expense)


def delete_expense(st_session_state, index: int):
    """
    刪除支出記錄

    Args:
        st_session_state: Streamlit session state 物件
        index: 要刪除的記錄索引
    """
    if 0 <= index < len(st_session_state.expenses):
        st_session_state.expenses.pop(index)


def clear_all_expenses(st_session_state):
    """
    清空所有支出記錄

    Args:
        st_session_state: Streamlit session state 物件
    """
    st_session_state.expenses = []


def get_expenses_dataframe(expenses: List[Dict]) -> pd.DataFrame:
    """
    將支出列表轉換為 DataFrame

    Args:
        expenses: 支出記錄列表

    Returns:
        Pandas DataFrame
    """
    if not expenses:
        return pd.DataFrame(columns=['日期', '分類', '金額(KRW)', '金額(TWD)', '備註'])

    df = pd.DataFrame(expenses)
    df = df.rename(columns={
        'date': '日期',
        'category': '分類',
        'amount_krw': '金額(KRW)',
        'amount_twd': '金額(TWD)',
        'note': '備註'
    })

    # 格式化金額顯示
    df['金額(KRW)'] = df['金額(KRW)'].apply(lambda x: f"₩{x:,.0f}")
    df['金額(TWD)'] = df['金額(TWD)'].apply(lambda x: f"NT${x:,.0f}")

    return df


def get_expenses_csv(expenses: List[Dict]) -> str:
    """
    將支出資料轉換為 CSV 格式

    Args:
        expenses: 支出記錄列表

    Returns:
        CSV 格式字串
    """
    if not expenses:
        return "日期,分類,金額(KRW),金額(TWD),備註\n"

    df = pd.DataFrame(expenses)
    return df.to_csv(index=False, encoding='utf-8-sig')


def calculate_statistics(expenses: List[Dict]) -> Dict:
    """
    計算支出統計資料

    Args:
        expenses: 支出記錄列表

    Returns:
        包含統計資料的字典
    """
    if not expenses:
        return {
            'total_krw': 0,
            'total_twd': 0,
            'avg_daily_krw': 0,
            'avg_daily_twd': 0,
            'by_category': {},
            'by_date': {}
        }

    df = pd.DataFrame(expenses)

    stats = {
        'total_krw': df['amount_krw'].sum(),
        'total_twd': df['amount_twd'].sum(),
        'by_category': df.groupby('category')['amount_krw'].sum().to_dict(),
        'by_date': df.groupby('date')['amount_krw'].sum().to_dict()
    }

    # 計算平均每日支出
    unique_dates = df['date'].nunique()
    if unique_dates > 0:
        stats['avg_daily_krw'] = stats['total_krw'] / unique_dates
        stats['avg_daily_twd'] = stats['total_twd'] / unique_dates
    else:
        stats['avg_daily_krw'] = 0
        stats['avg_daily_twd'] = 0

    return stats
