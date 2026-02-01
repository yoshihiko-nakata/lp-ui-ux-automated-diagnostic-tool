import openai


# -------------------------------------------------------------------
# APIキーの設定
# 本番では環境変数からの取得を推奨
# -------------------------------------------------------------------
openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXX"


def diagnose_lp(prompt_content: str) -> str | None:
    """
    LPの内容をもとにUI/UX観点で診断を行う。

    :param prompt_content: ChatGPTに渡すプロンプト本文
    :return: 診断結果テキスト（失敗時は None）
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # または "gpt-4-turbo"
            messages=[
                {
                    "role": "system",
                    "content": "あなたはUI/UXの専門家です。",
                },
                {
                    "role": "user",
                    "content": prompt_content,
                },
            ],
            temperature=0.0,   # 出力の一貫性を優先
            max_tokens=2000,   # 出力長の上限
        )

        # 応答コンテンツを取得
        result_text = response.choices[0].message.content
        return result_text

    except Exception as e:
        print(f"Error calling API: {e}")
        return None


# -------------------------------------------------------------------
# 実行
# -------------------------------------------------------------------
report = diagnose_lp(full_prompt)

if report is not None:
    print(report)
else:
    print("Diagnosis failed.")
