from flask import Flask

app = Flask(__name__)
count = 0

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route("/")
def hello_world():
    global count
    count += 1
    return f"<h1>Starter Flask App</h1>{count}"

@app.route("/kill")
def kill():
    shutdown_server()
    return "shutting down"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
