import os
import requests

from flask import Flask, request
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

figma_api_key = os.getenv("FIGMA_API_KEY")
figma_api_url = os.getenv("FIGMA_API_URL")
headers = {"X-Figma-Token": figma_api_key}


@app.route('/get_figma_file', methods=['GET'])
def get_figma_file():
    file_id = request.args.get('file_id')
    response = requests.get(figma_api_url + file_id, headers=headers)
    data = response.json()

    return data


if __name__ == '__main__':
    app.run()
