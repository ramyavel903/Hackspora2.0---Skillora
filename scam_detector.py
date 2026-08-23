def analyze_opportunity(description, email, payment):

    score = 0
    warnings = []

    description = description or ""
    email = email or ""
    payment = payment or "No"

    text = description.lower()

    # -----------------------------
    # PAYMENT / FEE DETECTION
    # -----------------------------

    payment_words = [
        "registration fee",
        "processing fee",
        "security deposit",
        "pay now",
        "payment required",
        "pay immediately",
        "fee"
    ]

    if payment.lower() == "yes" or any(
        word in text for word in payment_words
    ):
        score += 25
        warnings.append(
            "Payment or registration fee requested."
        )

    # -----------------------------
    # URGENCY DETECTION
    # -----------------------------

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
        warnings.append(
            "Urgent or pressure-based language detected."
        )

    # -----------------------------
    # SENSITIVE INFORMATION
    # -----------------------------

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
        warnings.append(
            "Sensitive personal or financial information requested."
        )

    # -----------------------------
    # EMAIL CHECK
    # -----------------------------

    email_lower = email.lower()

    if (
        email_lower.endswith("@gmail.com")
        or email_lower.endswith("@yahoo.com")
    ):
        score += 10
        warnings.append(
            "Free email provider used instead of a company domain."
        )

    # -----------------------------
    # UNREALISTIC OFFER DETECTION
    # -----------------------------

    unrealistic_words = [
        "₹1 lakh",
        "1 lakh per month",
        "no experience",
        "earn huge",
        "guaranteed income"
    ]

    if any(word in text for word in unrealistic_words):
        score += 15
        warnings.append(
            "Potentially unrealistic salary or income claim."
        )

    # Maximum score = 100
    score = min(score, 100)

    # -----------------------------
    # RISK LEVEL
    # -----------------------------

    if score <= 30:
        risk_level = "LOW"

    elif score <= 60:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"

    return score, risk_level, warnings