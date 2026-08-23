def analyze_opportunity(description, email, payment):

    score = 0
    warnings = []

    text = description.lower()

    # Payment-related warning
    payment_words = [
        "registration fee",
        "processing fee",
        "security deposit",
        "pay now",
        "payment required",
        "pay immediately",
        "fee"
    ]

    if payment.lower() == "yes" or any(word in text for word in payment_words):
        score += 25
        warnings.append("Payment or registration fee requested.")

    # Urgency warning
    urgent_words = [
        "immediately",
        "urgent",
        "limited seats",
        "act now",
        "today only",
        "last chance"
    ]

    if any(word in text for word in urgent_words):
        score += 10
        warnings.append("Urgent or pressure-based language detected.")

    # Sensitive information warning
    sensitive_words = [
        "aadhaar",
        "aadhar",
        "pan card",
        "bank details",
        "otp",
        "password",
        "credit card"
    ]

    if any(word in text for word in sensitive_words):
        score += 30
        warnings.append("Sensitive personal or financial information requested.")

    # Free email warning
    if email.lower().endswith("@gmail.com") or email.lower().endswith("@yahoo.com"):
        score += 10
        warnings.append("Free email provider used instead of a company domain.")

    # Unrealistic opportunity warning
    unrealistic_words = [
        "₹1 lakh",
        "1 lakh per month",
        "no experience",
        "earn huge",
        "guaranteed income"
    ]

    if any(word in text for word in unrealistic_words):
        score += 15
        warnings.append("Potentially unrealistic salary or income claim.")

    # Maximum score = 100
    score = min(score, 100)

    # Risk level
    if score <= 30:
        risk_level = "LOW"
    elif score <= 60:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return score, risk_level, warnings