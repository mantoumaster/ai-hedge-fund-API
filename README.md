# AI Hedge Fund API

## 🚀 項目介紹
本專案基於 `virattt/ai-hedge-fund` 和 `KRSHH/ritadel`，並進一步擴展，
**提供 Web API 介面**，可讓其他應用直接調用 AI 分析師的投資建議。

**主要改動：**
- ✅ **使用 Python 3.13，棄用 Poetry，改用 Pip 管理依賴**
- ✅ **內建 Flask API 服務（預設運行於 `6000` 端口）**
- ✅ **支援多種 LLM（GPT-4o、Claude 3、LLaMA3、Gemini）**
- ✅ **支援金融數據 API（Alpha Vantage、StockData、Finnhub 等）**
- ✅ **支援 Docker 部署，可直接 `docker run` 啟動 API 服務**
- ✅ **14 個專業投資分析師 AI Agent，涵蓋價值投資、成長投資、技術分析等多種策略**

網頁版 Web Page
<img width="1516" alt="image" src="https://github.com/user-attachments/assets/e2d443f9-0a48-44ee-a9f4-a61bdfe60e96" />

telegram bot 
https://github.com/tbdavid2019/telegram-bot-stock2
![image](https://github.com/user-attachments/assets/26d173d0-cc64-4d11-b70b-7735a07c30e0)


## 📌 環境安裝

### **1️⃣ Clone 本專案**
```bash
git clone https://github.com/tbdavid2019/ai-hedge-fund-API.git
cd ai-hedge-fund-API
```

### **2️⃣ 創建虛擬環境 & 安裝依賴**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows 則使用 venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### **3️⃣ 設定環境變數**
請在專案根目錄創建 `.env` 檔案，並填入 API Keys：

```ini
# LLM API Keys（至少設定一個）
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
GROQ_API_KEY=your-groq-api-key
GEMINI_API_KEY=your-gemini-api-key

# 金融數據 API Keys（至少設定一個）
ALPHA_VANTAGE_API_KEY=your-alpha-vantage-key
STOCKDATA_API_KEY=your-stockdata-key
FINNHUB_API_KEY=your-finnhub-key
EODHD_API_KEY=your-eodhd-key
```

## 🚀 啟動 API 服務

```bash
python webui2.py --api
```
預設 API 會運行於 `http://localhost:6000`

## 🤖 **可用的 AI 投資分析師**

本專案內建 **14 個專業 AI 投資分析師**，每個分析師都基於真實投資大師的策略和哲學：

### **� 價值投資大師**

| 順序 | Key | 顯示名稱 | Agent 檔案 | 投資策略 |
|:---:|:---|:---|:---|:---|
| 0 | `ben_graham` | Ben Graham | `ben_graham.py` | 價值投資之父，重視安全邊際、低本益比、穩健財務 |
| 1 | `bill_ackman` | Bill Ackman | `bill_ackman.py` | 激進價值投資，專注優質企業、集中持股 |
| 3 | `charlie_munger` | Charlie Munger | `charlie_munger.py` | 品質投資，尋找護城河、高 ROE、優秀管理層 |
| 5 | `michael_burry` | Michael Burry | `michael_burry.py` | 深度價值投資，尋找被低估的資產淨值 |
| 6 | `peter_lynch` | Peter Lynch | `peter_lynch.py` | 成長價值投資，重視 PEG Ratio、熟悉的企業 |
| 7 | `phil_fisher` | Phil Fisher | `phil_fisher.py` | 成長潛力分析，重視研發、管理品質、產業前景 |
| 8 | `warren_buffett` | Warren Buffett | `warren_buffett.py` | 長期價值投資，尋找優質企業、合理價格 |

### **🚀 成長與創新策略**

| 順序 | Key | 顯示名稱 | Agent 檔案 | 投資策略 |
|:---:|:---|:---|:---|:---|
| 2 | `cathie_wood` | Cathie Wood | `cathie_wood.py` | 顛覆式創新投資，聚焦 AI、電動車、基因科技 |

### **📈 技術與情緒分析**

| 順序 | Key | 顯示名稱 | Agent 檔案 | 分析方式 |
|:---:|:---|:---|:---|:---|
| 4 | `nancy_pelosi` | Nancy Pelosi | `nancy_pelosi.py` | 追蹤國會議員股票交易記錄 |
| 9 | `wsb` | WallStreetBets | `wsb_agent.py` | Reddit 社群情緒、散戶動能分析 |
| 10 | `technical_analyst` | Technical Analyst | `technicals.py` | 技術分析：MA、RSI、MACD 等指標 |
| 11 | `sentiment_analyst` | Sentiment Analyst | `sentiment.py` | 新聞情緒分析、市場氛圍評估 |

### **📐 基本面與估值分析**

| 順序 | Key | 顯示名稱 | Agent 檔案 | 分析方式 |
|:---:|:---|:---|:---|:---|
| 12 | `fundamentals_analyst` | Fundamentals Analyst | `fundamentals.py` | 深度財務報表分析 |
| 13 | `valuation_analyst` | Valuation Analyst | `valuation.py` | 企業估值模型、DCF 分析 |

### **🛠 特殊角色（自動執行）**

這些 Agent 在工作流中自動執行，不需要在 API 請求中指定：

- `portfolio_manager.py` - 投資組合管理
- `risk_manager.py` - 風險管理與部位控制
- `round_table.py` - 綜合討論與決策整合

---

## � **Docker 部署**

### **1️⃣ 建立 Docker 映像**
```bash
docker build -t ai-hedge-fund-api .
```

### **2️⃣ 啟動容器**
```bash
docker run --env-file .env -p 6000:6000 ai-hedge-fund-api
```

## 🔍 **API 調用方式**

### **1️⃣ 股票分析 API**

#### **📥 請求方式**
```bash
curl -X POST "http://localhost:6000/api/analysis" \
     -H "Content-Type: application/json" \
     -d '{
           "tickers": "tsla",
           "selectedAnalysts": ["ben_graham"],
           "modelName": "gpt-4o"
         }'
```

#### **� 請求參數說明**

| 參數 | 類型 | 必填 | 說明 | 範例 |
|:---|:---|:---:|:---|:---|
| `tickers` | string | ✅ | 股票代碼（逗號分隔） | `"AAPL,TSLA,NVDA"` |
| `selectedAnalysts` | array | ⚠️ | 要使用的分析師列表（空陣列=使用全部） | `["ben_graham", "warren_buffett"]` |
| `modelName` | string | ✅ | LLM 模型名稱 | `"gpt-4o"`, `"claude-3-5-sonnet-20241022"` |
| `startDate` | string | ❌ | 分析起始日期（預設：結束日期前 3 個月） | `"2024-01-01"` |
| `endDate` | string | ❌ | 分析結束日期（預設：今天） | `"2024-12-31"` |
| `initialCash` | number | ❌ | 初始現金（預設：100000） | `100000` |

#### **可用的 `selectedAnalysts` 選項**

你可以在請求中指定以下任意組合的分析師（或留空使用全部）：

**價值投資大師：**
```json
["ben_graham", "bill_ackman", "charlie_munger", "michael_burry", "peter_lynch", "phil_fisher", "warren_buffett"]
```

**成長與創新：**
```json
["cathie_wood"]
```

**技術與情緒分析：**
```json
["nancy_pelosi", "wsb", "technical_analyst", "sentiment_analyst"]
```

**基本面與估值：**
```json
["fundamentals_analyst", "valuation_analyst"]
```

**完整範例（使用多個分析師）：**
```bash
curl -X POST "http://localhost:6000/api/analysis" \
     -H "Content-Type: application/json" \
     -d '{
           "tickers": "AAPL,NVDA",
           "selectedAnalysts": ["warren_buffett", "peter_lynch", "technical_analyst"],
           "modelName": "gpt-4o",
           "startDate": "2024-09-01",
           "endDate": "2024-11-21",
           "initialCash": 50000
         }'
```

#### **�📤 回應範例**
```json
{
  "analyst_signals": {
    "ben_graham_agent": {
      "tsla": {
        "confidence": 80.0,
        "reasoning": "Tesla's financial assessment reveals several weaknesses from a Graham perspective...",
        "signal": "bearish"
      }
    },
    "risk_management_agent": {
      "tsla": {
        "current_price": 236.25,
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
      "reasoning": "The analysis by the ben_graham_agent indicates a strong bearish signal..."
    }
  }
}
```

---

# AI Hedge Fund API (English)

## 🚀 Project Overview
This project extends `virattt/ai-hedge-fund` and `KRSHH/ritadel`,
providing a **RESTful API** for external applications to query AI-driven investment insights.

**Major Improvements:**
- ✅ **Python 3.13 (Switched from Poetry to Pip)**
- ✅ **Built-in Flask API (default port: `6000`)**
- ✅ **Supports multiple LLMs (GPT-4o, Claude 3, LLaMA3, Gemini)**
- ✅ **Financial Data APIs (Alpha Vantage, StockData, Finnhub, etc.)**
- ✅ **Docker-ready, deploy via `docker run`**
- ✅ **14 Professional AI Investment Analysts covering Value, Growth, Technical Analysis strategies**

Web
<img width="1516" alt="image" src="https://github.com/user-attachments/assets/e2d443f9-0a48-44ee-a9f4-a61bdfe60e96" />

## 📌 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/tbdavid2019/ai-hedge-fund-API.git
cd ai-hedge-fund-API
```

### **2️⃣ Set Up Virtual Environment & Install Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### **3️⃣ Configure `.env` File**
```ini
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
GROQ_API_KEY=your-groq-api-key
GEMINI_API_KEY=your-gemini-api-key
ALPHA_VANTAGE_API_KEY=your-alpha-vantage-key
STOCKDATA_API_KEY=your-stockdata-key
FINNHUB_API_KEY=your-finnhub-key
EODHD_API_KEY=your-eodhd-key
```

## 🚀 Start API Server
```bash
python webui2.py --api
```
(Default API runs on `http://localhost:6000`)

## 🤖 **Available AI Investment Analysts**

This project includes **14 professional AI investment analysts**, each based on real investment masters' strategies:

**📊 Value Investing Masters:** `ben_graham`, `bill_ackman`, `charlie_munger`, `michael_burry`, `peter_lynch`, `phil_fisher`, `warren_buffett`

**🚀 Growth & Innovation:** `cathie_wood`

**📈 Technical & Sentiment:** `nancy_pelosi`, `wsb`, `technical_analyst`, `sentiment_analyst`

**📐 Fundamentals & Valuation:** `fundamentals_analyst`, `valuation_analyst`

_(See Chinese section above for detailed strategy descriptions)_

---

## 📡 Docker Deployment

### **1️⃣ Build Docker Image**
```bash
docker build -t ai-hedge-fund-api .
```

### **2️⃣ Run Container**
```bash
docker run --env-file .env -p 6000:6000 ai-hedge-fund-api
```

## 🔍 API Usage

### **1️⃣ Stock Analysis API**
#### **📥 Request**
```bash
curl -X POST "http://localhost:6000/api/analysis" \
     -H "Content-Type: application/json" \
     -d '{
           "tickers": "tsla",
           "selectedAnalysts": ["ben_graham"],
           "modelName": "gpt-4o"
         }'
```

#### **� Request Parameters**

| Parameter | Type | Required | Description | Example |
|:---|:---|:---:|:---|:---|
| `tickers` | string | ✅ | Stock symbols (comma-separated) | `"AAPL,TSLA,NVDA"` |
| `selectedAnalysts` | array | ⚠️ | Analysts to use (empty=all) | `["ben_graham", "warren_buffett"]` |
| `modelName` | string | ✅ | LLM model name | `"gpt-4o"`, `"claude-3-5-sonnet-20241022"` |
| `startDate` | string | ❌ | Analysis start date (default: 3 months ago) | `"2024-01-01"` |
| `endDate` | string | ❌ | Analysis end date (default: today) | `"2024-12-31"` |
| `initialCash` | number | ❌ | Initial cash (default: 100000) | `100000` |

**Available `selectedAnalysts` options:** See the list in Chinese section above or leave empty to use all analysts.

#### **📤 Response Example**
_(See JSON example in Chinese section)_


<img width="1601" alt="image" src="https://github.com/user-attachments/assets/0c2157e0-071c-4c9d-a15a-04c02912242a" />


