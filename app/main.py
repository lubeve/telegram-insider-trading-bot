"""
Main entry point for the Telegram Insider Trading Bot application.
"""

import asyncio
import logging
from .startup import initialize_application

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main application entry point"""
    try:
        # Initialize the application
        app = await initialize_application()
        
        # Run the bot
        await app.run_polling()
        
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise
    finally:
        # Cleanup resources
        await app.stop()

if __name__ == "__main__":
    # Run the application
    asyncio.run(main())