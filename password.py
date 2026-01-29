from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    error = ""

    if request.method == "POST":
        try:
            length = int(request.form.get("length"))
            if length < 4:
                error = "Password length must be at least 4"
            else:
                characters = ""

                if request.form.get("upper"):
                    characters += string.ascii_uppercase
                if request.form.get("lower"):
                    characters += string.ascii_lowercase
                if request.form.get("digits"):
                    characters += string.digits
                if request.form.get("symbols"):
                    characters += string.punctuation

                if characters == "":
                    error = "Select at least one option"
                else:
                    password = "".join(random.choice(characters) for _ in range(length))

        except ValueError:
            error = "Enter a valid number"

    return render_template("index.html", password=password, error=error)

if __name__ == "__main__":
    app.run()
