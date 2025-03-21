# AI Hedge Fund API

## 🚀 項目介紹
本專案基於 `virattt/ai-hedge-fund` 和 `KRSHH/ritadel`，並進一步擴展，
**提供 Web API 介面**，可讓其他應用直接調用 AI 分析師的投資建議。

**主要改動：**
- ✅ **使用 Python 3.12，棄用 Poetry，改用 Pip 管理依賴**
- ✅ **內建 Flask API 服務（預設運行於 `6000` 端口）**
- ✅ **支援多種 LLM（GPT-4o、Claude 3、LLaMA3、Gemini）**
- ✅ **支援金融數據 API（Alpha Vantage、StockData、Finnhub 等）**
- ✅ **支援 Docker 部署，可直接 `docker run` 啟動 API 服務**

網頁版
<img width="1516" alt="image" src="https://github.com/user-attachments/assets/e2d443f9-0a48-44ee-a9f4-a61bdfe60e96" />


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


## 📡 **Docker 部署**

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

#### **📤 回應範例**
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
- ✅ **Python 3.12 (Switched from Poetry to Pip)**
- ✅ **Built-in Flask API (default port: `6000`)**
- ✅ **Supports multiple LLMs (GPT-4o, Claude 3, LLaMA3, Gemini)**
- ✅ **Financial Data APIs (Alpha Vantage, StockData, Finnhub, etc.)**
- ✅ **Docker-ready, deploy via `docker run`**

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

#### **📤 Response Example** *(Real-time financial data required!)*
_(See JSON example in Chinese section)_


<img width="1601" alt="image" src="https://github.com/user-attachments/assets/0c2157e0-071c-4c9d-a15a-04c02912242a" />


