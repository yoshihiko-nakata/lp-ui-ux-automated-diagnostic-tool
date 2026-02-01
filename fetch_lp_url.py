import gspread
from google.oauth2.service_account import Credentials


# -------------------------------------------------------------------
# 1. サービスアカウント認証の設定
# -------------------------------------------------------------------
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES,
)

gc = gspread.authorize(creds)


# -------------------------------------------------------------------
# 2. スプレッドシートを開く（URLで指定）
# -------------------------------------------------------------------
SHEET_URL = "https://docs.google.com/spreadsheets/d/XXXXXXXX/edit"

spreadsheet = gc.open_by_url(SHEET_URL)
worksheet = spreadsheet.sheet1  # 最初のワークシートを使用


# -------------------------------------------------------------------
# 3. 最新の回答行を取得
# -------------------------------------------------------------------
# ヘッダー行を含め、全データをリストとして取得
all_rows = worksheet.get_all_values()

# 最終行が最新の回答
latest_row = all_rows[-1]


# -------------------------------------------------------------------
# 4. LPのURLを抽出（最後の列と仮定）
# -------------------------------------------------------------------
lp_url = latest_row[-1]

print(f"Latest LP URL: {lp_url}")
