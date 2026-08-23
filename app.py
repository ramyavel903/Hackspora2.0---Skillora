from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():

    company = request.form["company"]
    opportunity_type = request.form["type"]
    email = request.form["email"]
    url = request.form["url"]
    description = request.form["description"]
    payment = request.form["payment"]

    print("Company:", company)
    print("Type:", opportunity_type)
    print("Email:", email)
    print("URL:", url)
    print("Payment:", payment)
    print("Description:", description)

    return "Opportunity received successfully!"


if __name__ == "__main__":
    app.run(debug=True)