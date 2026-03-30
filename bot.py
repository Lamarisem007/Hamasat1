import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_html(
        rf"Hi {user.mention_html()}!\nWelcome to the Hamasat SND bot. Use /help to see available commands.",
        reply_markup=ForceReply(selective=True),
    )

# Help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Available commands: /start, /help')

# Message handler for regular text messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Error handler
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

# Main function to run the bot
def main():
    # Insert your bot's token here
    updater = Updater("YOUR_BOT_TOKEN")

    # Register command and message handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Log errors
    updater.dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()