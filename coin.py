import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime, timedelta 

def get_btc_usd():
    api_key = os.environ.get("COIN_API_KEY")
    if not api_key:
        return "실패: COIN_API_KEY가 비어있음"


    url = "https://data-api.coindesk.com/index/cc/v1/latest/tick"

    params = {
        "market": "cadli",        # 대표 시장 예시(문서/상품에 따라 ccix 등도 있음)
        "instruments": "BTC-USD", # 또는 instrument(s) 파라미터 형태는 문서에 맞춰 조정
        "api_key": api_key,       # ✅ 쿼리로 키 붙이기(가장 확실)
    }

    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (GitHubActions; +https://github.com/)"
    }

    r = requests.get(url, params=params, headers=headers, timeout=20)
    if r.status_code != 200:
        return f"실패: HTTP {r.status_code} - {r.text[:160]}"

    data = r.json()

    # 응답 구조는 market/상품마다 달라질 수 있어서 안전하게 접근
    # (예: Data -> BTC-USD -> VALUE 같은 형태로 오는 케이스가 있음)
    try:
        value = data["Data"]["BTC-USD"]["VALUE"]
        return f"현재 비트코인 시세: ${value}"
    except Exception:
        return f"성공은 했는데 파싱 실패: {str(data)[:200]}"

def update_readme():
    price_info = get_btc_usd()
    now_utc = datetime.utcnow()
    now_kst = now_utc + timedelta(hours=9)
    formatted_time = now_kst.strftime("%Y-%m-%d %H:%M:%S")

    content = f"""
# 🚀 Crypto Real-Time Tracker

<p align="center">
  <img src="coin.jpg" width="100" />
</p>

<div align="center">
  <h3>✨ 실시간 비트코인 시세 모니터링 ✨</h3>
  <p>GitHub Actions를 활용하여 5분마다 자동으로 시세를 갱신합니다.</p>
</div>

---

### 📊 Market Overview
| Asset | Current Price (USD) | Status |
| :--- | :---: | :---: |
| **Bitcoin (BTC)** | `{price_info.split(': ')[1] if ':' in price_info else price_info}` | 🟢 Live |

> [!TIP]
> **최근 업데이트:** `{formatted_time} (KST)`  
> 이 리포지토리는 오픈 데이터를 활용하여 투명한 시세 정보를 제공합니다.

---

### 🛠 Tech Stack
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=GitHub%20Actions&logoColor=white"/>
  <img src="https://img.shields.io/badge/CoinDesk%20API-FF6F61?style=flat-square&logo=c&logoColor=white"/>
</p>

<details>
  <summary><b>어떻게 작동하나요? (How it works)</b></summary>
  <br />
  1. <b>Cron Job:</b> 5분마다 워크플로우를 트리거합니다.<br />
  2. <b>Python Script:</b> CoinDesk API를 통해 최신 시세를 수집합니다.<br />
  3. <b>Git Bot:</b> 갱신된 내용을 자동으로 README에 커밋하고 푸시합니다.
</details>

---
<p align="center">Managed by <b>github-actions[bot]</b></p>
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
