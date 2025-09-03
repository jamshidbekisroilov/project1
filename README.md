# 🤖 BirinchiBot — Telegram Utility Bot

**BirinchiBot** is a multifunctional Telegram bot designed to simplify everyday tasks. It provides quick access to currency exchange rates, weather updates, prayer times, calculators, project links, and feedback submission — all through a user-friendly interface.

---

## 🚀 Features

- 💱 Currency exchange rates (USD/EUR to UZS)
- 🧮 Currency conversion calculator
- 🌤 Real-time weather updates
- 🕌 Daily and weekly prayer times
- 📩 Feedback submission (forwarded to a Telegram channel)
- 🌐 Project and social media links
- 🆘 Help menu with inline buttons

---

## 🛠 Technologies Used

- Python 3.10+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- Flask (for webhook-based server)
- Render (for cloud deployment)
- dotenv (for secure environment variable management)

---
## 📬 Feedback & Contact

If you have suggestions, questions, or want to collaborate:

- Telegram: [@jamshidbekisroilov](https://t.me/jamshidbekisroilov)
- GitHub Issues: [project1](https://github.com/jamshidbekisroilov/project1/issues)

---

## 📄 License

This project is open-source and available under the [MIT License]([[LICENSE](https://github.com/jamshidbekisroilov/project1/blob/main/LICENSE)].

---

## 👨‍💻 Author

**Jamshidbek Isroilov**  
Sales Economist | Aspiring Project Manager | Telegram Bot Developer  
[LinkedIn](https://linkedin.com/in/jamshidbek-isroilov) • [GitHub](https://github.com/jamshidbekisroilov) • [Website](https://jamshidbek.uz)

## ⚙️ Installation


## 🧪 Local Testing

To run the bot locally with Flask:

```bash
python bot.py

Clone the repository and install dependencies:
```bash
git clone https://github.com/jamshidbekisroilov/project1.git
cd project1
pip install -r requirements.txt
Create a `.env` file in the root directory and add your credentials:

---


```env
BOT_TOKEN=your_telegram_bot_token_here
EXCHANGE_API_KEY=your_exchange_api_key_here
TELEGRAM_URL=https://t.me/your_channel_or_username
INSTAGRAM_URL=https://instagram.com/your_instagram_profile
GITHUB_URL=https://github.com/your_github_username
WEBSITE_URL=https://yourwebsite.com
YOUTUBE_URL=https://youtube.com/@your_youtube_channel
LINKEDIN_URL=https://linkedin.com/in/your-linkedin-profile
WEBHOOK_URL=https://your-app-name.onrender.com

## 🌐 Deployment (Render)
- Connect your GitHub repo to Render

- Create a Web Service

- Set the following configuration:

- Setting	Value
- Build Command	pip install -r requirements.txt
- Start Command	python bot.py or bash start.sh
- Environment Variable	BOT_TOKEN=your_token
- WEBHOOK_URL=https://your-app-name.onrender.com

