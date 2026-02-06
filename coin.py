import os
import requests
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_bitcoin_price():
    # 깃허브 Secrets에서 키 가져오기
    api_key = os.environ.get("COIN_API_KEY")
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    # 1. 재시도 로직 설정 (DNS 에러 및 일시적 서버 오류 대비)
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    
    # 2. 헤더에 API 키 포함
    # 참고: CoinDesk API 버전에 따라 헤더 이름이 다를 수 있습니다.
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = session.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        price_usd = data["bpi"]["USD"]["rate"]
        return f"현재 비트코인 시세: ${price_usd}"
        
    except Exception as e:
        print(f"Error detail: {e}")
        return f"데이터 가져오기 실패 (네트워크/키 확인 필요)"

def update_readme():
    price_info = get_bitcoin_price()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""
# 🚀 Crypto Auto Tracker (CoinDesk)

이 리포지토리는 GitHub Actions를 통해 비트코인 시세를 자동 트래킹합니다.

### 💰 Bitcoin Price (USD)
> **{price_info}**

⏳ 마지막 갱신: {now} (UTC)

---
*발급받으신 API Key를 사용하여 안전하게 업데이트 중입니다.*
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()