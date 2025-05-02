import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 替換為你自己的 Channel access token 和 secret
line_bot_api = LineBotApi('K6ypXkjH40KHYgR2EsCBlcaMKSGcybyXh5IbvEm65b2/fM/Uxg8kTWRvXby5EyOMjv/7AZ+x4ikXbNQAPHCI9dYaOew1UkYxxu6yxO5PPuJX3Ci7K3Y8W0TX9Qno1RrkIlhD/l4mCCEXhrP/L29DbQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d097014786bbf942bfa1913723280b25')

@app.route("/line/webhook", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK', 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你說的是：「' + event.message.text + '」'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Render 會自動提供 PORT 環境變數
    app.run(host='0.0.0.0', port=port)
