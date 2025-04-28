#建構  docker   ai-hedge-fund-API

docker build -t ai-hedge-fund-api .
docker run --env-file .env -p 6000:6000 ai-hedge-fund-api
docker tag ai-hedge-fund-api tbdavid2019/ai-hedge-fund-api:latest
docker push tbdavid2019/ai-hedge-fund-api:latest


python webui2.py

curl -X POST "http://localhost:6000/api/analysis" \
     -H "Content-Type: application/json" \
     -d '{
           "tickers": "tsla",
           "selectedAnalysts": ["ben_graham", "bill_ackman", "cathie_wood", "charlie_munger", "nancy_pelosi", "warren_buffett", "wsb", "technical_analyst", "fundamentals_analyst", "sentiment_analyst", "valuation_analyst"],
           "modelName": "gpt-4o"
         }'

curl -X POST "http://localhost:6000/api/analysis" \
     -H "Content-Type: application/json" \
     -d '{
           "tickers": "tsla",
           "selectedAnalysts": ["ben_graham", "bill_ackman", "cathie_wood", "charlie_munger", "michael_burry", "peter_lynch", "nancy_pelosi", "warren_buffett", "wsb", "technical_analyst", "fundamentals_analyst", "sentiment_analyst", "valuation_analyst"],
           "modelName": "gpt-4o"
         }'



curl -X POST "http://localhost:6000/api/analysis" \
     -H "Content-Type: application/json" \
     -d '{
           "tickers": "tsla",
           "selectedAnalysts": ["phil_fisher" ],
           "modelName": "gpt-4o"
         }'

