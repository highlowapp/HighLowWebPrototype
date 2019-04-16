from flask import Flask
import os

index_html = ""
with open("index.html", "r") as file:
	index_html = file.read()

app = Flask(__name__)

@app.route("/")
def root():
	return index_html

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.environ["PORT"])
