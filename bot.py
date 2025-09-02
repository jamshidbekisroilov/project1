from telebot import TeleBot, types
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🤖 Bot haqida")
    btn2 = types.KeyboardButton("🆘 Yordam")
    btn3 = types.KeyboardButton("📩 Biz bilan bog‘lanish")
    btn4 = types.KeyboardButton("🌐 Bizning loyihalar")
    btn5 = types.KeyboardButton("💱 Kurs")
    btn6 = types.KeyboardButton("🧮 Hisoblash")
    btn7 = types.KeyboardButton("🌤 Ob-havo")
    btn8 = types.KeyboardButton("🕌 Namoz vaqtlari")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! Quyidagi menyudan kerakli bo‘limni tanlang:",
        reply_markup=markup
    )
@bot.message_handler(func=lambda m: m.text == "🤖 Bot haqida")
def about_bot(message):
    text = (
        "🤖 *Bot haqida*\n\n"
        "Bu bot sizga kundalik hayotda kerak bo‘ladigan xizmatlarni tez va qulay tarzda taqdim etadi:\n"
        "• Valyuta kurslari va hisoblash\n"
        "• Ob-havo ma’lumotlari\n"
        "• Namoz vaqtlari\n"
        "• Bizning loyihalar va sahifalar\n"
        "• Fikr-mulohaza yuborish imkoniyati\n\n"
        "Bot freelance, savdo, sayohat, va shaxsiy rejalashtirish uchun ayni muddao. Har bir bo‘lim o‘z funksiyasiga ega — tanlang va foydalaning!"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")
@bot.message_handler(func=lambda m: m.text == "🆘 Yordam")
def help_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🤖 Bot haqida", callback_data="help_about"),
        types.InlineKeyboardButton("📩 Bog‘lanish", callback_data="help_contact"),
        types.InlineKeyboardButton("🌐 Loyihalar", callback_data="help_projects"),
        types.InlineKeyboardButton("💱 Kurs", callback_data="help_kurs"),
        types.InlineKeyboardButton("🧮 Hisoblash", callback_data="help_calc"),
        types.InlineKeyboardButton("🌤 Ob-havo", callback_data="help_weather"),
        types.InlineKeyboardButton("🕌 Namoz vaqtlari", callback_data="help_prayer")
    )
    bot.send_message(
        message.chat.id,
        "🆘 Yordam bo‘limi:\nQuyidagi tugmalardan birini tanlang, har bir xizmat haqida qisqacha ma’lumot olasiz.",
        reply_markup=markup
    )
@bot.callback_query_handler(func=lambda call: call.data.startswith("help_"))
def help_details(call):
    help_texts = {
        "help_about": "🤖 *Bot haqida*\nBu bot sizga valyuta, ob-havo, namoz vaqtlari, va boshqa xizmatlarni taqdim etadi.",
        "help_contact": "📩 *Biz bilan bog‘lanish*\nFikr-mulohaza yuborish uchun 'Xat yozish' tugmasini bosing.",
        "help_projects": "🌐 *Bizning loyihalar*\nIjtimoiy sahifalar va saytlarimizga havolalar bu bo‘limda.",
        "help_kurs": "💱 *Kurs*\n1 USD va 1 EUR ning UZS ga nisbatan kursini ko‘rish.",
        "help_calc": "🧮 *Hisoblash*\nValyuta miqdorini kiriting — bot sizga so‘mga aylantirib beradi.",
        "help_weather": "🌤 *Ob-havo*\nJoylashuv yoki shahar nomi orqali hozirgi va kelgusi ob-havoni ko‘rish.",
        "help_prayer": "🕌 *Namoz vaqtlari*\nBugungi, ertangi, va haftalik namoz vaqtlarini ko‘rish."
    }

    text = help_texts.get(call.data, "Ma’lumot topilmadi.")
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown")
@bot.message_handler(func=lambda m: m.text == "📩 Biz bilan bog‘lanish")
def contact_menu(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("✉️ Xat yozish", callback_data="write_message")
    markup.add(btn)
    bot.send_message(message.chat.id, "Fikr-mulohaza yoki savolingizni yuborish uchun quyidagi tugmani bosing:", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == "write_message")
def ask_feedback(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "✍️ Xabaringizni yozing. Biz uni ko‘rib chiqamiz.")
    bot.register_next_step_handler(call.message, forward_to_channel)
CHANNEL_ID = -1003066498934  # O‘zingizning kanal ID’ingizni bu yerga yozing

def forward_to_channel(message):
    user = message.from_user
    text = (
        f"📩 *Yangi xabar*\n"
        f"👤 Foydalanuvchi: @{user.username or user.first_name}\n"
        f"🆔 ID: {user.id}\n"
        f"✉️ Xabar:\n{message.text}"
    )
    bot.send_message(CHANNEL_ID, text, parse_mode="Markdown")
    bot.send_message(message.chat.id, "✅ Xabaringiz yuborildi! Rahmat.")
from config import TELEGRAM_URL, INSTAGRAM_URL, GITHUB_URL, WEBSITE_URL, YOUTUBE_URL, LINKEDIN_URL

@bot.message_handler(func=lambda m: m.text == "🌐 Bizning loyihalar")
def show_projects(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📢 Telegram kanal", url=TELEGRAM_URL),
        types.InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_URL),
        types.InlineKeyboardButton("💻 GitHub", url=GITHUB_URL),
        types.InlineKeyboardButton("🌐 Veb-sayt", url=WEBSITE_URL),
        types.InlineKeyboardButton("🎥 YouTube", url=YOUTUBE_URL),
        types.InlineKeyboardButton("🔗 LinkedIn", url=LINKEDIN_URL)
    )
    bot.send_message(
        message.chat.id,
        "🌐 *Bizning loyihalar:*\nQuyidagi sahifalar orqali bizning ishlarimizni ko‘rishingiz mumkin:",
        reply_markup=markup,
        parse_mode="Markdown"
    )
import requests
from config import EXCHANGE_API_KEY

@bot.message_handler(func=lambda m: m.text == "💱 Kurs")
def show_exchange_rates(message):
    try:
        usd_url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD"
        eur_url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/EUR"

        usd_response = requests.get(usd_url)
        eur_response = requests.get(eur_url)

        if usd_response.status_code == 200 and eur_response.status_code == 200:
            usd_rate = usd_response.json()['conversion_rates']['UZS']
            eur_rate = eur_response.json()['conversion_rates']['UZS']

            text = (
                "💱 *Valyuta kurslari:*\n\n"
                f"• 1 USD ≈ {usd_rate:,.2f} UZS\n"
                f"• 1 EUR ≈ {eur_rate:,.2f} UZS\n\n"
                "📌 Kurslar real vaqt asosida yangilanadi."
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "❌ Kursni olishda xatolik yuz berdi.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Xatolik: {e}")
@bot.message_handler(func=lambda m: m.text == "🧮 Hisoblash")
def choose_currency(message):
    markup = types.InlineKeyboardMarkup()
    usd_btn = types.InlineKeyboardButton("💵 USD → UZS", callback_data="convert_usd")
    eur_btn = types.InlineKeyboardButton("💶 EUR → UZS", callback_data="convert_eur")
    markup.add(usd_btn, eur_btn)
    bot.send_message(message.chat.id, "Qaysi valyutani so‘mga aylantirmoqchisiz?", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data in ["convert_usd", "convert_eur"])
def ask_amount(call):
    currency = "USD" if call.data == "convert_usd" else "EUR"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Necha {currency} kiritmoqchisiz?")
    bot.register_next_step_handler(call.message, lambda msg: convert_to_uzs(msg, currency))
from config import EXCHANGE_API_KEY

def convert_to_uzs(message, currency):
    try:
        amount = float(message.text)
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/{currency}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            uzs_rate = data['conversion_rates']['UZS']
            total = amount * uzs_rate
            bot.send_message(
                message.chat.id,
                f"{amount} {currency} ≈ {total:,.2f} UZS"
            )
        else:
            bot.send_message(message.chat.id, "❌ Kursni olishda xatolik yuz berdi.")
    except ValueError:
        bot.send_message(message.chat.id, "⚠️ Iltimos, faqat raqam kiriting.")
@bot.message_handler(func=lambda m: m.text == "🌤 Ob-havo")
def ask_city(message):
    bot.send_message(
        message.chat.id,
        "📍 Istalgan shahar nomini yozing (masalan: Andijon, London, Istanbul):"
    )
    bot.register_next_step_handler(message, show_weather_link)

def show_weather_link(message):
    city = message.text.strip()
    if not city:
        bot.send_message(message.chat.id, "⚠️ Shahar nomi bo‘sh bo‘lishi mumkin emas.")
        return

    # Google qidiruv havolasi
    google_url = f"https://www.google.com/search?q={city.replace(' ', '+')}+ob+havo"

    # Yandex qidiruv havolasi
    #yandex_url = f"https://yandex.uz/pogoda/search?request={city.replace(' ', '+')}"

    text = (
        f"🔎 *{city.capitalize()}* shahri uchun ob-havo ma’lumotini quyidagi havolalardan ko‘rishingiz mumkin:\n\n"
        f"🌐 [Google orqali qidirish]({google_url})\n"
        # f"🌐 [Yandex orqali qidirish]({yandex_url})"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")
import requests
import datetime
from telebot import TeleBot, types
@bot.message_handler(func=lambda message: message.text == "🕌 Namoz vaqtlari")
def choose_type(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📅 Bugungi", callback_data="type_today"),
        types.InlineKeyboardButton("🌄 Ertangi", callback_data="type_tomorrow"),
        types.InlineKeyboardButton("🗓 Haftalik", callback_data="type_week")
    )
    bot.send_message(message.chat.id, "🕋 Qaysi turdagi namoz vaqtlarini ko‘rmoqchisiz?", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data.startswith("type_"))
def choose_region(call):
    selected_type = call.data.replace("type_", "")
    markup = types.InlineKeyboardMarkup(row_width=2)
    regions = [
        ("Andijon", "Andijon"),
        ("Buxoro", "Buxoro"),
        ("Farg‘ona", "Fargona"),
        ("Jizzax", "Jizzax"),
        ("Namangan", "Namangan"),
        ("Navoiy", "Navoiy"),
        ("Qashqadaryo", "Qarshi"),
        ("Qoraqalpog‘iston", "Nukus"),
        ("Samarqand", "Samarqand"),
        ("Sirdaryo", "Guliston"),
        ("Surxondaryo", "Termiz"),
        ("Toshkent vil.", "Nurafshon"),
        ("Toshkent sh.", "Toshkent"),
        ("Xorazm", "Urganch")
    ]
    for name, city in regions:
        markup.add(types.InlineKeyboardButton(name, callback_data=f"{selected_type}_{city}"))
    bot.send_message(call.message.chat.id, "📍 Viloyatni tanlang:", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: any(call.data.startswith(prefix) for prefix in ["today_", "tomorrow_", "week_"]))
def show_times(call):
    parts = call.data.split("_")
    mode = parts[0]
    city = parts[1]

    try:
        if mode == "today":
            url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Uzbekistan&method=2"
            label = "📅 Bugungi"
            r = requests.get(url)
            times = r.json()['data']['timings']

            text = (
                f"{label} namoz vaqtlari — *{city}* shahri:\n\n"
                f"• 🌅 Bomdod: `{times['Fajr']}`\n"
                f"• ☀️ Quyosh: `{times['Sunrise']}`\n"
                f"• 🕛 Peshin: `{times['Dhuhr']}`\n"
                f"• 🕔 Asr: `{times['Asr']}`\n"
                f"• 🌇 Shom: `{times['Maghrib']}`\n"
                f"• 🌃 Xufton: `{times['Isha']}`"
            )

        elif mode == "tomorrow":
            tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
            date_str = tomorrow.strftime("%Y-%m-%d")
            url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Uzbekistan&method=2&date={date_str}"
            label = "🌄 Ertangi"
            r = requests.get(url)
            times = r.json()['data']['timings']

            text = (
                f"{label} namoz vaqtlari — *{city}* shahri:\n\n"
                f"• 🌅 Bomdod: `{times['Fajr']}`\n"
                f"• ☀️ Quyosh: `{times['Sunrise']}`\n"
                f"• 🕛 Peshin: `{times['Dhuhr']}`\n"
                f"• 🕔 Asr: `{times['Asr']}`\n"
                f"• 🌇 Shom: `{times['Maghrib']}`\n"
                f"• 🌃 Xufton: `{times['Isha']}`"
            )

        elif mode == "week":
            today = datetime.datetime.now()
            url = f"https://api.aladhan.com/v1/calendarByCity?city={city}&country=Uzbekistan&method=2&month={today.month}&year={today.year}"
            r = requests.get(url)
            week = r.json()['data'][:7]

            text = f"🗓 *{city}* shahri uchun haftalik namoz vaqtlari:\n\n"
            for day in week:
                date = day['date']['readable']
                t = day['timings']
                text += f"📆 {date}\n• Bomdod: `{t['Fajr']}` • Peshin: `{t['Dhuhr']}` • Asr: `{t['Asr']}` • Shom: `{t['Maghrib']}` • Xufton: `{t['Isha']}`\n\n"

        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ Xatolik yuz berdi:\n`{e}`", parse_mode="Markdown")
bot.polling()