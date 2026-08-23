from flask import Flask, render_template, request
from scam_detector import analyze_opportunity

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():

    company = request.form.get("company")
    opportunity_type = request.form.get("type")
    email = request.form.get("email")
    url = request.form.get("url")
    description = request.form.get("description")
    payment = request.form.get("payment")

    score, risk_level, warnings = analyze_opportunity(
        description,
        email,
        payment
    )

    return render_template(
        "result.html",
        company=company,
        type=opportunity_type,
        email=email,
        url=url,
        score=score,
        risk_level=risk_level,
        warnings=warnings
    )


if __name__ == "__main__":
    app.run(debug=True)