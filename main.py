import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from openai import OpenAIApi
load_dotenv()
openai = OpenAIApi(os.getenv("OPENAI_API_KEY"))
def start(update, context):
update.message.reply_text("Привет! Я - OpenAI-бот для Telegram. Задай мне вопрос!")
def chatgpt(update, context):
query = update.message.text
response = openai.
chat(“ChatGPT”, query)
update.message.reply_html(response[‘choices’][0][‘text’])
updater = Updater(token=os.getenv(‘TELEGRAM_BOT_TOKEN’), use_context=True)
dispatcher = updater.dispatcher
