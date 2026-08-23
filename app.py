from flask import Flask, render_template, request
from scam_detector import analyze_opportunity

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

    score, risk_level, warnings = analyze_opportunity(
        description,
        email,
        payment
    )

    return f"""
    Company: {company}<br>
    Opportunity Type: {opportunity_type}<br>
    Risk Score: {score}/100<br>
    Risk Level: {risk_level}<br>
    Warnings: {warnings}
    """

if __name__ == "__main__":
    app.run(debug=True)