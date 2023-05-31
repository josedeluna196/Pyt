import os
import telebot
import random
import string

# Getting Bot Token From Secrets
BOT_TOKEN = "6021410841:AAHM9TwHMITYtzFtISMkUo66a3CRLTPRvZU"

# Creating Telebot Object
bot = telebot.TeleBot(BOT_TOKEN)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Whenever Starting Bot
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"Hola {message.chat.first_name}, soy un bot generador de contraseñas. Envíame un mensaje con la longitud de la contraseña que deseas generar. Esta contraseña debe de ser entre 8 y 64 caracteres.")
    print(f"Mensaje de bienvenida enviado a {message.chat.first_name}\n")

# Reply To All Messages
@bot.message_handler(func=lambda msg: True)
def all(message):
    try:
        length = int(message.text)
        if 8 <= length <= 64:
            password = generate_password(length)
            bot.send_message(message.chat.id, f"Aquí tienes una contraseña de {length} caracteres:")
            bot.send_message(message.chat.id, password)
        else:
            bot.reply_to(message, f"Lo siento {message.chat.first_name}, la longitud de la contraseña debe estar entre 8 y 64 caracteres.")
    except ValueError:
        bot.reply_to(message, f"Lo siento {message.chat.first_name}, no entendí tu mensaje. Por favor, envíame un número entero que represente la longitud de la contraseña que deseas generar, debe estar entre 8 y 64 caracteres.")
    
    print(f"Mensaje respondido a {message.chat.first_name}\n")

print("Bot iniciado y esperando nuevos mensajes\n")

# Waiting For New Messages
bot.infinity_polling()
