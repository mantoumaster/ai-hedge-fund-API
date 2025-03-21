import os
import sys
# 確保 Python 可以找到 `src/` 內的模組
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
import json
import threading
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sock import Sock
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
from src.main import run_hedge_fund

# 加載 .env 環境變數
load_dotenv()

# 設置 Flask 伺服器
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # 允許跨域請求
sock = Sock(app)

# WebSocket 客戶端列表
websocket_clients = []

def broadcast_log(message, level="info"):
    log_data = {"level": level, "message": message}
    for client in websocket_clients[:]:
        try:
            client.send(json.dumps(log_data))
        except Exception:
            websocket_clients.remove(client)

@app.route('/api/analysis', methods=['POST'])
def run_analysis():
    """執行對股票的分析"""
    try:
        data = request.get_json()
        ticker_list = data.get('tickers', '').split(',')
        selected_analysts = data.get('selectedAnalysts', [])
        model_name = data.get('modelName')

        # 設定開始與結束時間
        end_date = data.get('endDate') or datetime.now().strftime('%Y-%m-%d')
        start_date = data.get('startDate') or (datetime.strptime(end_date, '%Y-%m-%d') - relativedelta(months=3)).strftime('%Y-%m-%d')

        # 初始投資組合
        portfolio = {
            "cash": data.get('initialCash', 100000),
            "positions": {},
            "cost_basis": {},
            "realized_gains": {ticker: {"long": 0.0, "short": 0.0} for ticker in ticker_list}
        }

        # 執行完整分析
        broadcast_log(f"Starting analysis for {ticker_list}", "info")
        result = run_hedge_fund(
            tickers=ticker_list,
            start_date=start_date,
            end_date=end_date,
            portfolio=portfolio,
            show_reasoning=True,
            selected_analysts=selected_analysts,
            model_name=model_name,
            model_provider="OpenAI",
            is_crypto=False
        )

        broadcast_log("Analysis completed successfully", "success")
        return jsonify(result)

    except Exception as e:
        error_message = f"API Error: {str(e)}"
        broadcast_log(error_message, "error")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@sock.route('/ws/logs')
def logs(ws):
    """WebSocket 端點來監控日誌"""
    websocket_clients.append(ws)
    try:
        while True:
            ws.receive()  # 只是保持連線，前端不會傳送訊息
    except Exception:
        websocket_clients.remove(ws)

if __name__ == "__main__":
    api_thread = threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 6000, "debug": True, "use_reloader": False})
    api_thread.daemon = True
    api_thread.start()
    print("API Server started on http://localhost:6000")
    api_thread.join()
