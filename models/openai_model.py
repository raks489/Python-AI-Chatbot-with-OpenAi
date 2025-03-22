"""
Model for handling complex conversations using OpenAI API.
"""
import logging
from openai import OpenAI
from config.settings import (
    OPENAI_API_KEY, OPENAI_MODEL, OPENAI_MAX_TOKENS, 
    OPENAI_TEMPERATURE, BOT_NAME, DEBUG_MODE
)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class OpenAIModel:
    """
    Handles complex conversations by leveraging the OpenAI API.
    """
    
    def __init__(self):
        """Initialize the OpenAI client."""
        if not OPENAI_API_KEY:
            logger.warning("OpenAI API key not found. Advanced responses will be limited.")
        
        self.client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
        self.conversation_history = []
        self.max_history = 10  # Keep track of last 10 exchanges
    
    def get_response(self, user_input: str) -> str:
        """
        Generate a response using OpenAI API.
        
        Args:
            user_input: The user's message
            
        Returns:
            str: The AI-generated response
        """
        if not self.client:
            return f"I'm sorry, but my advanced AI capabilities are not available right now. Please provide an OpenAI API key in the .env file to enable this feature."
        
        # Update conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Trim history if it exceeds max length
        if len(self.conversation_history) > self.max_history * 2:
            self.conversation_history = self.conversation_history[-self.max_history * 2:]
        
        try:
            # Create system message with context
            system_message = {
                "role": "system", 
                "content": f"You are {BOT_NAME}, a helpful and friendly AI assistant. Provide concise and helpful responses."
            }
            
            # Combine system message with conversation history
            messages = [system_message] + self.conversation_history
            
            # Make the API call
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
                max_tokens=OPENAI_MAX_TOKENS,
                temperature=OPENAI_TEMPERATURE
            )
            
            # Extract the response text
            ai_response = response.choices[0].message.content
            
            # Update conversation history with AI response
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            return ai_response
            
        except Exception as e:
            logger.error(f"Error with OpenAI API: {str(e)}")
            return f"I'm having trouble connecting to my AI brain right now. Error: {str(e)}"
    
    def reset_conversation(self):
        """Reset the conversation history."""
        self.conversation_history = []
        return "Conversation history has been reset."
