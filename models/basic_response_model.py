"""
Model for handling basic conversation patterns using if-else logic.
"""
import random
import datetime
from config.settings import (
    GREETING_PATTERNS, FAREWELL_PATTERNS, GRATITUDE_PATTERNS,
    TIME_PATTERNS, DATE_PATTERNS, HELP_PATTERNS, NAME_PATTERNS,
    GREETING_RESPONSES, FAREWELL_RESPONSES, GRATITUDE_RESPONSES,
    HELP_RESPONSES, NAME_RESPONSES, UNKNOWN_RESPONSES, BOT_NAME
)


class BasicResponseModel:
    """
    Handles basic conversation patterns using pattern matching and predefined responses.
    """

    def __init__(self):
        """Initialize the BasicResponseModel."""
        self.patterns = {
            "greeting": GREETING_PATTERNS,
            "farewell": FAREWELL_PATTERNS,
            "gratitude": GRATITUDE_PATTERNS,
            "time": TIME_PATTERNS,
            "date": DATE_PATTERNS,
            "help": HELP_PATTERNS,
            "name": NAME_PATTERNS,
        }
        
        self.responses = {
            "greeting": GREETING_RESPONSES,
            "farewell": FAREWELL_RESPONSES,
            "gratitude": GRATITUDE_RESPONSES,
            "help": HELP_RESPONSES,
            "name": NAME_RESPONSES,
            "unknown": UNKNOWN_RESPONSES,
        }
    
    def get_response(self, user_input: str) -> tuple[str, bool]:
        """
        Generate a response based on the user input using pattern matching.
        
        Args:
            user_input: The user's message as a string
            
        Returns:
            tuple[str, bool]: A tuple containing (response_text, is_farewell)
        """
        clean_input = user_input.lower().strip()
        
        # Check for pattern matches
        for pattern_type, patterns in self.patterns.items():
            if any(pattern in clean_input for pattern in patterns):
                if pattern_type == "time":
                    return self._get_time_response(), False
                elif pattern_type == "date":
                    return self._get_date_response(), False
                elif pattern_type == "farewell":
                    return random.choice(self.responses[pattern_type]), True
                else:
                    return random.choice(self.responses[pattern_type]), False
        
        # If no pattern matches, return an unknown response
        return random.choice(self.responses["unknown"]), False
    
    def _get_time_response(self) -> str:
        """Generate a response with the current time."""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        responses = [
            f"It's currently {current_time}.",
            f"The time is {current_time}.",
            f"Right now, it's {current_time}.",
        ]
        return random.choice(responses)
    
    def _get_date_response(self) -> str:
        """Generate a response with the current date."""
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        responses = [
            f"Today is {current_date}.",
            f"The date today is {current_date}.",
            f"It's {current_date} today.",
        ]
        return random.choice(responses)
