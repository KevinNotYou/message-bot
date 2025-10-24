# WeChat Company RSS Notifier

This project automatically subscribes to new articles from any website that provides an **RSS feed**,  
and pushes updates to a **WeChat Company (企业微信)** group via webhook.

---

## 🚀 Features
- Subscribe to any RSS source (news, blogs, research papers, etc.)
- Automatically detect new articles
- Push notifications to WeChat Company group
- Easy to configure and deploy via GitHub Actions or local script

---

## ⚙️ Usage

### 1️⃣ Get a WeChat Webhook
- In your WeChat Company group, create a **bot** (添加机器人)
- Copy the **webhook URL**, e.g.:
https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY

---

### 2️⃣ Set the Webhook as a GitHub Secret
- Go to your project repository → **Settings → Secrets and variables → Actions**
- Create a new secret:

Name: WECHAT_WEBHOOK
Value: https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY

---

### 3️⃣ Configure Your RSS Target
- Open `main.py`
- Replace the RSS feed URL with your target website’s feed:


RSS_URL = "https://example.com/rss.xml"
4️⃣ Run It
You can use GitHub Actions for automatic scheduled updates.


🧠 Notes
The script keeps track of previously pushed items to avoid duplicate notifications.

It supports multiple RSS URLs (you can extend main.py to use a list).

Works with both GitHub Actions and self-hosted Ubuntu servers.

## 📄 License

MIT License © 2025

```
