# app/app.py
from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<html>
  <head><title>Demo App</title></head>
  <body>
    <h1 id="welcome">Hello from Flask!</h1>
    <a id="next" href="/next">Next</a>
  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE)

@app.route("/next")
def next_page():
    return "<h2 id='nextpage'>Next page reached</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
