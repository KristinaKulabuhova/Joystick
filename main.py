from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def hello_world():
    return render_template("joystick.html")

@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "user" + name + " " + str(id)

if __name__ == "__main__":
    app.run(debug=True)