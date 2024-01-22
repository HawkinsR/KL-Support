from flask import Flask

app = Flask(__name__)
count = 0

@app.route("/")
def hello_world():
    global count
    count += 1
    return f"<h1>Starter Flask App</h1>{count}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
