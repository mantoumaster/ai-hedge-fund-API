# AI Hedge Fund API (金融 AI 對沖基金 API)

這是一個基於 AI 的對沖基金專案，提供 **API 介面** 供其他應用程式調用，讓開發者能夠透過多位知名投資大師 (如 Warren Buffett、Charlie Munger、Bill Ackman 等) 的投資策略來分析市場，並輔以 AI 進行交易決策。

本專案基於 **[virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)** 及 **[KRSHH/ritadel](https://github.com/KRSHH/ritadel)** 進行開發，重點改進了：

- ✅ **提供 API 介面**，可供外部應用請求交易決策。
- ✅ **支持 Docker 部署**，讓開發者可快速構建並運行系統。
- ✅ **整合多個 LLM (GPT-4o, Claude, Gemini, DeepSeek, LLaMA3)**，提升決策精準度。
- ✅ **數據來源擴展**，整合金融數據、技術分析、社群情緒分析等多種因子。
- ✅ **從 Poetry 轉換為 Pip 處理 Python 套件管理**。

## 🚀 功能特色

🔹 **多代理人投資分析系統**：
- 價值投資：Warren Buffett, Charlie Munger, Ben Graham
- 成長投資：Cathie Wood, Bill Ackman, Phil Fisher
- 風險管理：Risk Manager, Portfolio Manager
- 社群與市場情緒：WSB, Sentiment Analysis, Fundamentals Analysis
- 技術指標分析：Technical Analysis, Valuation Agent

🔹 **API 服務**
- 提供 `POST /api/analysis` API，讓用戶調用 AI 交易決策。
- 可選擇不同投資大師來分析特定股票。

🔹 **Docker 化部署**
- 提供 `Dockerfile`，可快速建構並啟動服務。
- 預設 **Python 3.12** 官方映像。
- API 預設 **6000 端口**。

---

## 📌 **安裝與運行方式**

### **1️⃣ 環境需求**
- **Python 3.12+** 或 **Docker**
- `pip install -r requirements.txt` 安裝相依套件

### **2️⃣ 本機運行 (Python)**
```bash
# 安裝相依套件
python -m venv venv
source venv/bin/activate  # Windows 用戶請使用 venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# 啟動 API 服務
python webui2.py --api
```

API 會運行在 `http://localhost:6000`

### **3️⃣ 使用 Docker 運行**
```bash
# 建構 Docker 映像
docker build -t ai-hedge-fund-api .

# 啟動 Docker 容器 (預設 6000 端口)
docker run -p 6000:6000 ai-hedge-fund-api
```

---

## 📡 **API 調用方式**

### **使用 `curl` 調用 API**
```bash
curl -X POST "http://localhost:6000/api/analysis" \
     -H "Content-Type: application/json" \
     -d '{
           "tickers": "tsla",
           "selectedAnalysts": ["ben_graham", "bill_ackman", "cathie_wood", "charlie_munger", "nancy_pelosi", "warren_buffett", "wsb", "technical_analyst", "fundamentals_analyst", "sentiment_analyst", "valuation_analyst"],
           "modelName": "gpt-4o"
         }'
```

### **API 回應範例 (JSON)**
```json
{
  "analyst_signals": {
    "ben_graham_agent": {
      "tsla": {
        "confidence": 80.0,
        "reasoning": "Tesla's financial assessment reveals several weaknesses from a Graham perspective. The lack of multi-year EPS data means earnings stability is uncertain, undermining the traditional insistence on proven earnings. The inability to calculate essential valuation metrics like the Graham Number and NCAV suggests it does not meet the margin of safety principle. Furthermore, the absence of dividend data limits the evaluation of Tesla's commitment to shareholder returns. Although the debt ratio is conservative, the overall financials suggest a speculative nature not in alignment with Graham's conservative investment principles.",
        "signal": "bearish"
      }
    },
    "risk_management_agent": {
      "tsla": {
        "current_price": 236.25999450683594,
        "reasoning": {
          "available_cash": 100000.0,
          "current_position": 0.0,
          "portfolio_value": 100000.0,
          "position_limit": 20000.0,
          "remaining_limit": 20000.0
        },
        "remaining_position_limit": 20000.0
      }
    }
  },
  "decisions": {
    "tsla": {
      "action": "short",
      "confidence": 80.0,
      "quantity": 84,
      "reasoning": "The analysis by the ben_graham_agent indicates a strong bearish signal with 80% confidence. Given the high confidence and the fact that there are no current positions, the decision is to short TSLA up to the maximum allowable quantity of 84 shares. This respects margin requirements as there are no constraints on the given margin at this time."
    }
  }
}
```

---

# 📖 **AI Hedge Fund API (English)**

This is an AI-driven hedge fund API that allows applications to analyze stock market data using multiple AI agents based on the investing philosophies of legendary investors like Warren Buffett, Charlie Munger, and Bill Ackman.

This project is based on **[virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)** and **[KRSHH/ritadel](https://github.com/KRSHH/ritadel)**, with key improvements:

- ✅ **Provides an API for external applications**
- ✅ **Supports Docker deployment for easy setup**
- ✅ **Integrates multiple LLMs (GPT-4o, Claude, Gemini, DeepSeek, LLaMA3)**
- ✅ **Expanded financial data sources**
- ✅ **Migrated from Poetry to Pip for dependency management**
- ✅ **Uses Python 3.12 as the default runtime**
- ✅ **API default port is 6000**

## 📌 **Installation & Usage**

### **1️⃣ Requirements**
- **Python 3.12+** or **Docker**
- Install dependencies via `pip install -r requirements.txt`

### **2️⃣ Running Locally (Python)**
```bash
# Install dependencies
python -m venv venv
source venv/bin/activate  # Windows: use venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# Start API server
python webui2.py --api
```
API runs on `http://localhost:6000`

### **3️⃣ Running with Docker**
```bash
# Build Docker Image
docker build -t ai-hedge-fund-api .

# Run Docker Container (Default port: 6000)
docker run -p 6000:6000 ai-hedge-fund-api
```

---


