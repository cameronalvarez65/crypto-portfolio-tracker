<details> <summary>Показать содержимое tracker.py</summary>
import requests

# ✅ Укажите ваш портфель здесь: {токен: количество}
portfolio = {
    "bitcoin": 0.1,
    "ethereum": 1.5,
    "cardano": 500,
    "solana": 20
}

def get_prices(token_list):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(token_list),
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print(f"❌ Ошибка при получении данных: {e}")
        return {}

def calculate_portfolio_value(portfolio):
    token_list = list(portfolio.keys())
    prices = get_prices(token_list)
    
    print("💼 Crypto Portfolio Value (в USD):\n")
    total_value = 0.0

    for token, amount in portfolio.items():
        price = prices.get(token, {}).get("usd")
        if price is not None:
            value = price * amount
            total_value += value
            print(f"• {token.capitalize():10} = {amount} × ${price:.2f} = ${value:.2f}")
        else:
            print(f"⚠️ Не удалось получить цену для: {token}")

    print(f"\n🔢 Общая стоимость портфеля: ${total_value:.2f}")

if __name__ == "__main__":
    calculate_portfolio_value(portfolio)
</details>
