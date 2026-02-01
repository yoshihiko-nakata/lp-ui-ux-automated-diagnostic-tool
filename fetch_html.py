import requests
from bs4 import BeautifulSoup


url = lp_url  # 前段で取得したLP URL

# 1. ユーザーエージェントを指定してリクエスト
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0...)",
}

try:
    # 2. HTTP GETリクエスト（タイムアウト設定）
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # エラーチェック（200 OK以外）

    # 3. HTMLからテキスト抽出
    soup = BeautifulSoup(response.text, "html.parser")

    # スクリプトやスタイルタグを除去
    for tag in soup(["script", "style"]):
        tag.extract()

    # 可読テキストのみ取得（改行区切り）
    page_text = soup.get_text(separator="\n")

    # 4. 長文対策（トークン節約のため上限カット）
    if len(page_text) > 15000:
        page_text = page_text[:15000] + "...(truncated)"

    print(f"Extracted {len(page_text)} chars")

except Exception as e:
    print(f"Error fetching URL: {e}")
