import requests

from datetime import datetime

def get_bitcoin_price():
    api_key = os.environ.get("COIN_API_KEY")
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price_usd = data["bpi"]["USD"]["rate"]
        time_updated = data["time"]["updated"]
        return f"현재 비트코인 시세: ${price_usd} (기준 시간: {time_updated})"
    else:
        return "데이터를 가져오는 데 실패했습니다."

def update_readme():
    price_info = get_bitcoin_price()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""
# 🚀 Crypto Auto Tracker

이 리포지토리는 GitHub Actions를 통해 비트코인 시세를 자동 트래킹합니다.

### 💰 Real-time Bitcoin Price
> **{price_info}**

⏳ 마지막 갱신: {now} (KST)
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
