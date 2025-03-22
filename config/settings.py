"""
Configuration settings for the chatbot application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o"  # Using the latest model as of 2025
OPENAI_MAX_TOKENS = 150
OPENAI_TEMPERATURE = 0.7

# Bot settings
BOT_NAME = os.getenv("BOT_NAME", "ChatBuddy")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Basic conversation patterns
GREETING_PATTERNS = [
    "hello", "hi", "hey", "greetings", "sup", "what's up", "howdy"
]

FAREWELL_PATTERNS = [
    "bye", "goodbye", "see you", "later", "cya", "farewell", "exit", "quit"
]

GRATITUDE_PATTERNS = [
    "thanks", "thank you", "appreciate it", "grateful", "thx"
]

TIME_PATTERNS = [
    "time", "what time", "clock", "hour"
]

DATE_PATTERNS = [
    "date", "day", "today", "what day", "calendar"
]

WEATHER_PATTERNS = [
    "weather", "forecast", "temperature", "raining", "sunny"
]

HELP_PATTERNS = [
    "help", "assist", "support", "guide", "how to"
]

NAME_PATTERNS = [
    "your name", "who are you", "what are you", "what's your name"
]

# Response templates
GREETING_RESPONSES = [
    "Hello there! How can I help you today?",
    "Hi! What can I do for you?",
    "Hey! How are you doing today?",
    "Greetings! How may I assist you?"
]

FAREWELL_RESPONSES = [
    "Goodbye! Have a great day!",
    "See you later! Take care!",
    "Farewell! Come back anytime you need assistance!",
    "Bye for now! It was nice chatting with you!"
]

GRATITUDE_RESPONSES = [
    "You're welcome!",
    "Happy to help!",
    "Anytime!",
    "My pleasure!"
]

HELP_RESPONSES = [
    f"I'm {BOT_NAME}, your friendly chatbot! I can help with basic questions or use AI for more complex ones.",
    "You can ask me about the time, date, or have a general conversation. For complex questions, I'll use AI to assist you.",
    "Need help? Just ask a question, and I'll do my best to provide a helpful response!"
]

NAME_RESPONSES = [
    f"I'm {BOT_NAME}, your friendly AI chatbot assistant!",
    f"My name is {BOT_NAME}. How can I help you today?",
    f"I'm {BOT_NAME}, designed to assist you with information and conversation."
]

UNKNOWN_RESPONSES = [
    "I'm not sure I understand. Could you please rephrase that?",
    "I don't have an answer for that. Let me pass this to my AI brain...",
    "Interesting question. Let me think about that more deeply...",
    "That's beyond my basic programming. Let me consult my AI capabilities..."
]
