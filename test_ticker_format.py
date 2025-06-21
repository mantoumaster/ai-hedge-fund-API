#!/usr/bin/env python3
"""
測試股票代號格式化功能
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from tools.api import _format_ticker_for_yfinance

def test_ticker_formatting():
    """測試各種股票代號的格式化"""
    
    test_cases = [
        # 台股測試
        ("2330", "2330.TW", "台積電"),
        ("0050", "0050.TW", "元大台灣50"),
        
        # 港股測試
        ("1", "0001.HK", "長和"),
        ("0001", "0001.HK", "長和"),
        ("0001.hk", "0001.HK", "長和（小寫後綴）"),
        ("700", "0700.HK", "騰訊"),
        
        # 中國股市測試
        ("600519", "600519.SS", "貴州茅台（上海）"),
        ("000001", "000001.SZ", "平安銀行（深圳）"),
        ("000002", "000002.SZ", "萬科A（深圳）"),
        ("300001", "300001.SZ", "特銳德（深圳創業板）"),
        
        # 美股測試
        ("AAPL", "AAPL", "蘋果"),
        ("TSLA", "TSLA", "特斯拉"),
        
        # 已有後綴的測試
        ("AAPL.US", "AAPL.US", "蘋果（已有後綴）"),
        ("BTC-USD", "BTC-USD", "比特幣（已有後綴）"),
    ]
    
    print("🧪 測試股票代號格式化功能")
    print("=" * 60)
    
    all_passed = True
    
    for input_ticker, expected, description in test_cases:
        result = _format_ticker_for_yfinance(input_ticker)
        status = "✅" if result == expected else "❌"
        
        print(f"{status} {input_ticker:10} -> {result:12} (預期: {expected:12}) {description}")
        
        if result != expected:
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("🎉 所有測試通過！")
    else:
        print("⚠️  部分測試失敗，請檢查實作")
    
    return all_passed

if __name__ == "__main__":
    test_ticker_formatting()