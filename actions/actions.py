from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from weather import get_weather
from send import crypto
from stock import stock_price
from cal_file import compute_derivative

class ActionGame(Action):

    def name(self) -> Text:
        return "action_game"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the user's message
        #user_message = tracker.latest_message.get('text', '')
        city = next(tracker.get_latest_entity_values("city"), None)

        
        # Get the user's intent
        #user_intent = tracker.latest_message.get('intent', {}).get('name', '')
        
        # Call the weather API
        #city = 'Delhi'  # For testing, replace with actual city
        temp = get_weather(city)
        
        # Pass the extracted information to the template
        dispatcher.utter_message(f"The temperature in {city} is {temp}°C.")
        
        return []

class ActionBitcoin(Action):

    def name(self) -> Text:
        return "action_bitcoin"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the user's message
        #user_message = tracker.latest_message.get('text', '')
        currency = next(tracker.get_latest_entity_values("currency"), None)

        dispatcher.utter_message(f"The bitcoin ")
        # Get the user's intent
        #user_intent = tracker.latest_message.get('intent', {}).get('name', '')
        
        # Call the weather API
        #city = 'Delhi'  # For testing, replace with actual city
        cut = crypto(currency)
        
        # Pass the extracted information to the template
        dispatcher.utter_message(f"The bitcoin {currency} is currently {cut}")
        
        return []
        
        
class ActionStock(Action):

    def name(self) -> Text:
        return "action_stock"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the user's message
        #user_message = tracker.latest_message.get('text', '')
        stock = next(tracker.get_latest_entity_values("stock"), None)


        # Get the user's intent
        #user_intent = tracker.latest_message.get('intent', {}).get('name', '')
        
        # Call the weather API
        #city = 'Delhi'  # For testing, replace with actual city
        stk = stock_price(stock)
        
        # Pass the extracted information to the template
        dispatcher.utter_message(f"The stock {stock} is currently {stk}")
        
        return []

class ActionCal(Action):

    def name(self) -> Text:
        return "action_cal"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the user's message
        #user_message = tracker.latest_message.get('text', '')
        cal = next(tracker.get_latest_entity_values("cal"), None)


        # Get the user's intent
        #user_intent = tracker.latest_message.get('intent', {}).get('name', '')
        
        # Call the weather API
        #city = 'Delhi'  # For testing, replace with actual city
        calu = compute_derivative(cal)
        
        # Pass the extracted information to the template
        dispatcher.utter_message(f"The derivative {cal} is {calu}")
        
        return []





