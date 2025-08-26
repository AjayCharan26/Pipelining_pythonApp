from flask import Flask, render_template, request
import csv
from model import predict

app = Flask(__name__)

def read_sample_rows(path="data.csv", limit=5):
    rows = []
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i >= limit:
                    break
                rows.append(row)
    except FileNotFoundError:
        pass
    return rows

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_text = request.form.get("text", "")
        result = predict(user_text)
    rows = read_sample_rows()
    return render_template("index.html", result=result, rows=rows)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

