class CryptoAdvisor:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3 / 10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6 / 10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8 / 10
            },
            "Solana": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7 / 10
            },
            "Polygon": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7 / 10
            }
        }

    def greet(self):
        return f"Hey there! I'm {self.name}, your AI-powered crypto sidekick! 🌟\nLet's find you a green and growing cryptocurrency to invest in!\n\nYou can ask me things like:\n- Which crypto is trending up?\n- What's the most sustainable coin?\n- What should I buy for long-term growth?\n- Show me all crypto info\n\nType 'exit' to quit."

    def recommend_by_profitability(self):
        profitable_coins = [
            (name, data) for name, data in self.crypto_db.items()
            if data["price_trend"] == "rising" and data["market_cap"] == "high"
        ]

        if not profitable_coins:
            return "I couldn't find any highly profitable coins right now."

        # Sort by sustainability score as secondary factor
        profitable_coins.sort(key=lambda x: x[1]["sustainability_score"], reverse=True)
        best_coin, data = profitable_coins[0]

        return f"For maximum profitability, consider {best_coin}! 💰\n" \
               f"It's currently trending up with a high market cap.\n" \
               f"Sustainability score: {data['sustainability_score'] * 10}/10"

    def recommend_by_sustainability(self):
        sustainable_coins = [
            (name, data) for name, data in self.crypto_db.items()
            if data["energy_use"] == "low" and data["sustainability_score"] >= 0.7
        ]

        if not sustainable_coins:
            return "I couldn't find any highly sustainable coins right now."

        # Sort by price trend as secondary factor
        sustainable_coins.sort(key=lambda x: (x[1]["price_trend"] == "rising", x[1]["market_cap"] == "high"),
                               reverse=True)
        best_coin, data = sustainable_coins[0]

        return f"For maximum sustainability, consider {best_coin}! 🌱\n" \
               f"It has low energy use and a sustainability score of {data['sustainability_score'] * 10}/10.\n" \
               f"Price trend: {data['price_trend']}, Market cap: {data['market_cap']}"

    def recommend_long_term(self):
        # Balance between sustainability and profitability
        scored_coins = []
        for name, data in self.crypto_db.items():
            score = 0
            # Profitability factors
            if data["price_trend"] == "rising":
                score += 3
            if data["market_cap"] == "high":
                score += 2
            elif data["market_cap"] == "medium":
                score += 1
            # Sustainability factors
            score += data["sustainability_score"] * 5
            if data["energy_use"] == "low":
                score += 2
            elif data["energy_use"] == "medium":
                score += 1

            scored_coins.append((name, score, data))

        if not scored_coins:
            return "I couldn't evaluate any coins for long-term growth right now."

        scored_coins.sort(key=lambda x: x[1], reverse=True)
        best_coin, _, data = scored_coins[0]

        return f"For long-term growth, I recommend {best_coin}! 🚀\n" \
               f"Combined score: {_}/12\n" \
               f"Price trend: {data['price_trend']}, Market cap: {data['market_cap']}\n" \
               f"Sustainability: {data['sustainability_score'] * 10}/10, Energy use: {data['energy_use']}"

    def show_all_info(self):
        result = "Here's information on all cryptocurrencies I track:\n\n"
        for name, data in self.crypto_db.items():
            result += f"🔹 {name}:\n"
            result += f"  Price trend: {data['price_trend']}\n"
            result += f"  Market cap: {data['market_cap']}\n"
            result += f"  Energy use: {data['energy_use']}\n"
            result += f"  Sustainability score: {data['sustainability_score'] * 10}/10\n\n"
        return result

    def process_query(self, query):
        query = query.lower()

        if any(word in query for word in ["trend", "profit", "grow", "rising"]):
            return self.recommend_by_profitability()
        elif any(word in query for word in ["sustain", "green", "eco", "energy"]):
            return self.recommend_by_sustainability()
        elif any(word in query for word in ["long term", "long-term", "future", "hold"]):
            return self.recommend_long_term()
        elif any(word in query for word in ["all", "list", "show", "info"]):
            return self.show_all_info()
        else:
            return "I'm not sure I understand. Try asking about:\n- Trending cryptocurrencies\n- Sustainable coins\n- Long-term investments\n- Or ask to see all info"


def main():
    bot = CryptoAdvisor()
    print(bot.greet())

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print(f"{bot.name}: Happy investing! Come back anytime you need crypto advice. 💎🙌")
            break

        response = bot.process_query(user_input)
        print(f"{bot.name}: {response}")


if __name__ == "__main__":
    main()