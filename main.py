from flask import Flask, send_file
from io import BytesIO
import requests

app = Flask(__name__)

@app.route("/")
def index():
  return "ZONK"

@app.route("/~/<path:url>")
def mirror_image(url):
  data = requests.get(url)
  buffer = BytesIO()
  buffer.write(data.content)
  buffer.seek(0)

  return send_file(buffer, mimetype=data.headers["content-type"])