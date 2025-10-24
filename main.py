import feedparser
import requests
import json
import os

WEBHOOK_URL = os.getenv("WECHAT_WEBHOOK")
FEED_URL = "https://openaccess.thecvf.com/rss"  # 示例RSS地址

def send_wechat_message(text):
    data = {
        "msgtype": "markdown",
        "markdown": {"content": text}
    }
    headers = {"Content-Type": "application/json"}
    requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)

def main():
    feed = feedparser.parse(FEED_URL)
    if not feed.entries:
        print("未获取到RSS内容")
        return

    msg = "**📢 CVPR 最新论文更新：**\n"
    for entry in feed.entries[:5]:  # 推送前5篇
        msg += f"> [{entry.title}]({entry.link})\n"
    send_wechat_message(msg)
    print("推送完成！")

if __name__ == "__main__":
    main()
