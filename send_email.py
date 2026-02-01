import smtplib
import ssl
from email.message import EmailMessage


# -------------------------------------------------------------------
# SMTP設定
# ※ 本番では環境変数または設定ファイルで管理することを推奨
# -------------------------------------------------------------------
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # STARTTLS 用ポート

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Gmail アプリパスワード
RECEIVER_EMAIL = "client@example.com"


# -------------------------------------------------------------------
# メールメッセージ作成
# -------------------------------------------------------------------
message = EmailMessage()
message.set_content(diagnostic_report)  # 診断レポート（Markdown可）

message["Subject"] = "【診断結果】LP UI/UX無料診断レポート"
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL


# -------------------------------------------------------------------
# 送信処理
# -------------------------------------------------------------------
context = ssl.create_default_context()
server = None

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls(context=context)  # TLS保護
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(message)

    print("Email sent successfully!")

    # TODO:
    # 送信成功時に Google Sheets へ送付ログを記録すると運用が安定する

except Exception as e:
    print(f"Error sending email: {e}")

finally:
    if server is not None:
        server.quit()
