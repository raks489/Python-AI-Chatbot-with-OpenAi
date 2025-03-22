"""
Main entry point for the chatbot application.
"""
import os
import sys
import logging
from controllers.chat_controller import ChatController
from config.settings import DEBUG_MODE

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_directories():
    """
    Create the required directories if they don't exist.
    """
    directories = [
        "config",
        "controllers",
        "models",
        "utils",
        "views"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")


def main():
    """
    Main function to start the chatbot.
    """
    try:
        # Ensure all required directories exist
        create_directories()
        
        # Create and start the chat controller
        controller = ChatController()
        controller.start()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Shutting down...")
        print("\nGoodbye! Have a great day!")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
