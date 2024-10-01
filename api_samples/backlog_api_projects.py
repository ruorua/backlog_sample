import os
from dotenv import load_dotenv
import requests

# .env ファイルから環境変数を読み込む
load_dotenv()

# Backlog API の設定
SPACE_NAME = os.getenv("BACKLOG_SPACE_NAME")
API_KEY = os.getenv("BACKLOG_API_KEY")

# APIのベースURL
BASE_URL = f"https://{SPACE_NAME}.backlog.com/api/v2/"

# プロジェクト一覧を取得する関数
def get_projects():
    url = f"{BASE_URL}projects"
    params = {
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# スクリプトを実行
if __name__ == "__main__":
    projects = get_projects()
    print(projects)