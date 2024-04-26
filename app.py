from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
	return "<h2>Hello World - Docker Flask Deployment Lab</h2><br/>"


app.run(host="0.0.0.0", port=3000)
