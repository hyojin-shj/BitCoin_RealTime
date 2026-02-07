
# 🚀 Crypto Real-Time Tracker

<p align="center">
  <img src="coin.jpg" width="500" />
</p>

<div align="center">
  <h3>✨ 실시간 비트코인 시세 모니터링 ✨</h3>
  <p>GitHub Actions를 활용하여 5분마다 자동으로 시세를 갱신합니다.</p>
</div>

---

### 📊 Market Overview
| Asset | Current Price (USD) | Status |
| :--- | :---: | :---: |
| **Bitcoin (BTC)** | `$68096.3128241849` | 🟢 Live |

> [!TIP]
> **최근 업데이트:** `2026-02-07 18:57:24 (KST)`  
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
