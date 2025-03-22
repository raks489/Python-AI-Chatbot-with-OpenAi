"""
Controller for managing the chat flow and logic.
"""
import logging
from config.settings import BOT_NAME, DEBUG_MODE
from models.basic_response_model import BasicResponseModel
from models.openai_model import OpenAIModel
from views.chat_view import ChatView
from utils.text_processor import TextProcessor

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ChatController:
    """
    Controls the flow of conversation between the user and the chatbot.
    """
    
    def __init__(self):
        """Initialize the ChatController with its dependencies."""
        self.basic_model = BasicResponseModel()
        self.ai_model = OpenAIModel()
        self.view = ChatView(BOT_NAME)
        self.text_processor = TextProcessor()
        self.running = False
    
    def start(self):
        """Start the chat session."""
        self.running = True
        self.view.display_welcome()
        self.run_chat_loop()
    
    def run_chat_loop(self):
        """Run the main chat loop."""
        while self.running:
            # Get user input
            user_input = self.view.get_user_input()
            
            if not user_input:
                continue
            
            # Process special commands
            if user_input.lower() == "clear":
                self.view.clear_screen()
                self.view.display_welcome()
                continue
            elif user_input.lower() == "reset":
                reset_message = self.ai_model.reset_conversation()
                self.view.display_message(BOT_NAME, reset_message, is_bot=True)
                continue
            
            # Try to get a response using the basic model first
            response, is_farewell = self.basic_model.get_response(user_input)
            
            # If the basic model couldn't give a good response, use the AI model
            if "I don't have an answer" in response or "beyond my basic programming" in response:
                self.view.display_thinking()
                response = self.ai_model.get_response(user_input)
            
            # Display the response
            self.view.display_message(BOT_NAME, response, is_bot=True)
            
            # Check if this is a farewell message
            if is_farewell:
                self.stop()
    
    def stop(self):
        """Stop the chat session."""
        self.running = False
        self.view.display_exit_message()
