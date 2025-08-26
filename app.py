from flask import Flask, render_template, request
import csv

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
        # get numbers from the form
        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")

        # validate input
        try:
            result = int(num1) + int(num2)
        except ValueError:
            result = "Please enter valid numbers."

    rows = read_sample_rows()
    return render_template("index.html", result=result, rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
