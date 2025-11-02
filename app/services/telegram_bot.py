"""
Telegram Bot service for the Insider Trading Bot.
"""

from telegram import Bot
from telegram.ext import Application

class TelegramBotService:
    """Service for managing Telegram bot functionality"""
    
    def __init__(self, token: str):
        self.token = token
        self.bot = Bot(token=token)
        self.app = None
    
    async def send_message(self, chat_id: int, text: str, **kwargs):
        """Send a message to a chat"""
        try:
            await self.bot.send_message(chat_id=chat_id, text=text, **kwargs)
        except Exception as e:
            print(f"Error sending message: {e}")
            raise
    
    async def send_photo(self, chat_id: int, photo: str, caption: str = None, **kwargs):
        """Send a photo to a chat"""
        try:
            await self.bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, **kwargs)
        except Exception as e:
            print(f"Error sending photo: {e}")
            raise
    
    async def send_document(self, chat_id: int, document: str, caption: str = None, **kwargs):
        """Send a document to a chat"""
        try:
            await self.bot.send_document(chat_id=chat_id, document=document, caption=caption, **kwargs)
        except Exception as e:
            print(f"Error sending document: {e}")
            raise
    
    def set_application(self, app: Application):
        """Set the application instance"""
        self.app = app