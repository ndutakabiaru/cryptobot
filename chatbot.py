class Cryptocoin:
        
    def __init__  (self ,name , price_trend ,market_cap ,energy_use ,sustanability_score):
        self.name = name
        self.price_trend = price_trend
        self.market_cap = market_cap
        self.energy_use = energy_use
        self. sustanability_score = sustanability_score
        
    def get_info(self):
        return(f"{self.name} : Price trend ={self.price_trend} ,Market Cap ={self.market_cap} , Energy use={self.energy_use} , Sustainability score ={self.sustanability_score}")
    
crypto_database = { 
    "Bitcoin": Cryptocoin("Bitcoin", "rising", "high", "high", 3/10),
    "Ethereum": Cryptocoin("Ethereum", "stable", "high", "medium", 6/10),
    "Cardano": Cryptocoin("Cardano", "rising", "medium", "low", 8/10)
    }

bitcoin_data = crypto_database["Bitcoin"]
print(f"Bitcoin's full info: {bitcoin_data.get_info()}")
print()
ethereum_data = crypto_database["Ethereum"]
print(f"Ethereum's full info: {ethereum_data.get_info()}")
print()
cardano_data = crypto_database["Cardano"]
print(f"Cardano's full info: {cardano_data.get_info()}")
print()


class cryptobot:
    def __init__(self ,crypto_database , greeting , name ,closing):
        
        self.crypto_data = crypto_database
        self.greeting = greeting
        self.name = name
        self.closing = closing
    def crypto_conditions (self , condition_func):
      results = []
      for coin_name , coin_obj in self.crypto_data.items():
          if condition_func(coin_obj):
              results.append(coin_obj)
      return results
    

    def advice(self,user_query):
        query = user_query.lower()

        # --- Rule 1: Profitability / Rising Trend Advice ---
        if "profit" in query or "trending up" in query or "rising" in query:
            # ... (logic for profitability) ...
            return "For potential profitability, look at coins with a 'rising' price trend and 'high' market cap."

        # --- Rule 2: Sustainability Advice ---
        elif "sustainable" in query or "eco-friendly" in query or "energy" in query:
            # ... (logic for sustainability) ...
            return " 'low' energy use and a sustainability score above 7/10. It's a great choice for long-term, eco-conscious potential!"
            

        # --- Rule 3: General Information for Specific Coins (THIS IS THE LOOP) ---
        # Note: This loop will either return a value or finish without returning.
        for coin_name_key, coin_obj in self.crypto_data.items():
            if coin_name_key.lower() in query:
                return coin_obj.get_info()

        # --- Rule 4: General Trend Query ---
        # CHANGE THIS 'elif' TO 'if'
        # Because the 'for' loop above is not an 'if/elif' block, this needs to start a new conditional check.
        if "trend" in query:
            rising_coins = self.crypto_conditions(lambda coin: coin.price_trend == "rising")
            stable_coins = self.crypto_conditions(lambda coin: coin.price_trend == "stable")

            response = "Let's look at the trends!\n"
            if rising_coins:
                response += f"Currently, **{', '.join([c.name for c in rising_coins])}** are showing a 'rising' price trend! Up, up, and away! 📈\n"
            if stable_coins:
                response += f"And **{', '.join([c.name for c in stable_coins])}** are looking 'stable'. Steady as she goes! ⚓\n"
            if not rising_coins and not stable_coins:
                response += "Based on our data, I don't have specific trend information right now. The crypto seas can be unpredictable!"
            return response

        # --- Rule 5: General Market Cap Query ---
        # This one can remain 'elif' because it follows the 'if "trend" in query' block.
        elif "market cap" in query:
            # ... (logic for market cap) ...
            return "..."

        # --- Fallback: If no specific query is understood ---
        else:
            return "..."

    # --- Part 4: The run_chatbot method for interactive conversation ---
    def run_chatbot(self):
        """Starts the interactive chat session with the user."""
        print(self.greeting) # Print the initial greeting message
        print("\nYou can ask me things like: 'Which crypto is trending up?', 'What's the most sustainable coin?', or 'Tell me about Bitcoin.'")
        print("Type 'exit' or 'quit' to end our chat.")

        while True: # Loop indefinitely until the user decides to exit
            user_input = input("\nYour query: ") # Prompt the user for input
            
            # Check for exit commands
            if user_input.lower() in ["exit", "quit", "bye", "stop"]:
                print(self.closing) # Print a farewell message
                break # Exit the loop
            
            # Get the chatbot's response
            response = self.advice(user_input)
            
            # Display the chatbot's response
            print(f"{self.name}: {response}")

# --- Part 5: Main execution block to start the chatbot ---
if __name__ == "__main__":
    # Create an instance of our CoinSageChatbot, passing it our all_crypto_data dictionary
    my_chatbot = cryptobot(crypto_database , "Hello" , "Cryptoadvisor" , "Goodbye" )

    # Start the chatbot's interactive session
    my_chatbot.run_chatbot()
