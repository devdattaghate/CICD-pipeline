from flask import Flask

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "Starting ML individual project"

if __name__== "__main__":
    app.run(debug=True)