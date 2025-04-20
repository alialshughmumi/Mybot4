import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import openai

# إعداد التوكنات
BOT_TOKEN = "7761916651:AAHZj3RfLrhEuupEZxqM3RZsyd5LZxu2uTo"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY
logging.basicConfig(level=logging.INFO)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"حدث خطأ: {e}"

    await update.message.reply_text(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
