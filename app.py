from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent

import os

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = "q8BdEyuWQJ6UtIgxWPKclU6AjHze2ZmT0hBr3UucxVk8PxhaEjB42isRIHpirYggtPL8dgWFtTmMly9YnGSlCSDhYOlvR57RGOfD3qyJMD5K9zTtbWPl5WUKYMlrEXMl9mJDc2fMOhC+cPo52H6sfwdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "9e77d5f4934a0d60cd1665eb6bc30a6d"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# =====================
# 加好友自動訊息
# =====================
@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="姓伊名藤和")
    )

# =====================
# webhook入口
# =====================
@app.route("/webhook", methods=['POST'])
def webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# =====================
# 啟動
# =====================
if __name__ == "__main__":
    app.run()