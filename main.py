import feedparser
import requests
import json
import os

WEBHOOK_URL = os.getenv("WECHAT_WEBHOOK")
FEED_URL = "https://openai.com/blog/rss.xml"  # 示例openai文章
HISTORY_FILE = "pushed_links.txt"  # 存储已推送文章的链接

def load_history():
    """加载已推送的文章链接"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f)
    return set()

def save_history(links):
    """保存已推送的文章链接（按列表顺序保存，保持顺序）"""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        if isinstance(links, set):
            # 如果是 set，转换为 list（但顺序不可控）
            links = list(links)
        for link in links:
            f.write(link + '\n')

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

    # 加载历史记录
    pushed_links = load_history()
    print(f"调试信息：历史记录数量 = {len(pushed_links)}")
    print(f"调试信息：pushed_links 是否为空 = {not pushed_links}")
    
    # 如果是首次运行（历史记录为空），标记所有当前文章为已读，不推送
    if not pushed_links:
        print("首次运行，初始化历史记录")
        for entry in feed.entries:
            pushed_links.add(entry.link)
        save_history(pushed_links)
        print(f"已标记全部 {len(feed.entries)} 篇文章，下次只推送新增文章")
        return
    
    # 筛选出未推送的文章（只看最新的5篇）
    new_entries = [entry for entry in feed.entries[:5] if entry.link not in pushed_links]
    
    if not new_entries:
        print("没有新文章")
        return
    
    # 推送新文章
    msg = "**📢 Openai 最新文章更新：**\n"
    for entry in new_entries:
        msg += f"> [{entry.title}]({entry.link})\n"
        pushed_links.add(entry.link)
    
    send_wechat_message(msg)
    save_history(pushed_links)
    print(f"推送完成！共推送 {len(new_entries)} 篇新文章")

if __name__ == "__main__":
    main()
