from flask import Flask, render_template, request
from scam_detector import analyze_opportunity
from database import create_database, save_analysis

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():

    company = request.form.get("company", "").strip()
    opportunity_type = request.form.get("type", "").strip()
    email = request.form.get("email", "").strip()
    url = request.form.get("url", "").strip()
    description = request.form.get("description", "").strip()
    payment = request.form.get("payment", "No").strip()

    score, risk_level, warnings = analyze_opportunity(
        description,
        email,
        payment
    )

    save_analysis(
        company,
        opportunity_type,
        email,
        url,
        description,
        payment,
        score,
        risk_level,
        warnings
    )

    return render_template(
        "result.html",
        company=company,
        opportunity_type=opportunity_type,
        email=email,
        url=url,
        description=description,
        payment=payment,
        score=score,
        risk_level=risk_level,
        warnings=warnings
    )

if __name__ == "__main__":
    app.run(debug=True)
