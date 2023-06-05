import re
import key_words as kw
import key_phrases as kp
import exceptions as ex

class Bot:
    def __init__(self):
        self.highest_prob_list = {}

    def message_probability(self, user_message, recognised_words, single_response=False, required_words=[]):
        #Calculate the probability of a user message matching the recognized words.
        message_certainty = sum(1 for word in user_message if word in recognised_words)
        percentage = message_certainty / len(recognised_words)

        has_required_words = all(word in user_message for word in required_words)

        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def response(self, bot_response, list_of_words, single_response=False, required_words=[]):
        #Generate a response and calculate its probability based on the user message.
        
        message = self.message  # Access the message from the class attribute
        self.highest_prob_list[bot_response] = self.message_probability(
            message, list_of_words, single_response, required_words)

    def check_all_messages(self, message):
        #Check all possible messages and generate responses.
        self.highest_prob_list = {}
        self.message = message  # Set the message to the class attribute

        # Tickers library
        self.response(kw.stock_tickers[0], ['amazon', 'ticker', 'symbol'], single_response=True)
        self.response(kw.stock_tickers[1], ['tesla', 'ticker', 'symbol'], single_response=True)
        self.response(kw.stock_tickers[2], ['netflix', 'ticker', 'symbol'], single_response=True)

        # Tickers library
        self.response(kw.crypto_tickers[0], ['bitcoin', 'ticker', 'symbol'], single_response=True)
        self.response(kw.crypto_tickers[1], ['etherium', 'ticker', 'symbol'], single_response=True)
        self.response(kw.crypto_tickers[2], ['litecoin', 'ticker', 'symbol'], single_response=True)

        # Capital Budgeting Vocabulary
        self.response(kp.irr, ['internal', 'rate', 'return'], required_words=['internal', 'rate'])
        self.response(kp.roe, ['return', 'equity'], required_words=['equity'])
        self.response(kp.roi, ['return', 'investment'], required_words=['investment'])

        best_match = max(self.highest_prob_list, key=self.highest_prob_list.get)

        return ex.unknown() if self.highest_prob_list[best_match] < 1 else best_match

    def get_response(self, user_input):
        #Process user input and generate a response.
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        response = self.check_all_messages(split_message)
        return response

# Create an instance of the bot
bot = Bot()

# Testing the response system
while True:
    user_input = input("YOU: ")
    print(' MACHINE: ' + bot.get_response(user_input))
