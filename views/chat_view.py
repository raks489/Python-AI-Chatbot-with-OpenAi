"""
View for displaying the chat interface.
"""
import os
import time
import sys
from typing import Callable
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


class ChatView:
    """
    Handles the presentation of the chat interface.
    """
    
    def __init__(self, bot_name: str):
        """
        Initialize the ChatView.
        
        Args:
            bot_name: The name of the chatbot
        """
        self.bot_name = bot_name
        self.typing_speed = 0.01  # Seconds per character
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        """Display welcome message and instructions."""
        self.clear_screen()
        print(f"{Fore.CYAN}{'=' * 60}")
        print(f"{Fore.CYAN}{'Welcome to ' + self.bot_name:^60}")
        print(f"{Fore.CYAN}{'=' * 60}")
        print(f"{Fore.YELLOW}Type 'help' for assistance or 'exit' to quit.")
        print(f"{Fore.CYAN}{'-' * 60}")
    
    def display_message(self, sender: str, message: str, is_bot: bool = False):
        """
        Display a message in the chat interface.
        
        Args:
            sender: Name of the message sender
            message: The message text
            is_bot: Whether the message is from the bot (for styling)
        """
        # Format sender name
        if is_bot:
            sender_display = f"{Fore.GREEN}{sender}{Style.RESET_ALL}"
        else:
            sender_display = f"{Fore.BLUE}{sender}{Style.RESET_ALL}"
        
        # Print the sender
        print(f"\n{sender_display}: ", end="")
        
        # Print the message with typing effect if it's from the bot
        if is_bot:
            self._type_effect(message)
        else:
            print(message)
    
    def get_user_input(self, prompt: str = "You") -> str:
        """
        Get input from the user.
        
        Args:
            prompt: The prompt to display before input
            
        Returns:
            str: The user's input
        """
        try:
            user_input = input(f"\n{Fore.BLUE}{prompt}{Style.RESET_ALL}: ")
            return user_input
        except (KeyboardInterrupt, EOFError):
            print("\nExiting gracefully...")
            sys.exit(0)
    
    def display_thinking(self):
        """Display a 'thinking' animation."""
        print(f"{Fore.YELLOW}Thinking", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print(Style.RESET_ALL)
    
    def display_exit_message(self):
        """Display exit message when the user leaves."""
        print(f"\n{Fore.CYAN}{'-' * 60}")
        print(f"{Fore.YELLOW}Thanks for chatting with {self.bot_name}! Goodbye!")
        print(f"{Fore.CYAN}{'-' * 60}")
    
    def _type_effect(self, text: str):
        """
        Create a typing effect for bot messages.
        
        Args:
            text: The text to display with typing effect
        """
        for char in text:
            print(char, end="", flush=True)
            time.sleep(self.typing_speed)
        print()
