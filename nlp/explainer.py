def explain_form(sections):
    explanation = []

    explanation.append(
        "இந்த படிவம் தமிழ் மென்பொருள் சான்றிதழ் பெறுவதற்கான விண்ணப்பப் படிவம்."
    )

    if sections["company_details"]:
        explanation.append(
            "இந்த பகுதியில் நிறுவனத்தின் பெயர், முகவரி, தொலைபேசி மற்றும் மின் அஞ்சல் விவரங்களை நிரப்ப வேண்டும்."
        )

    if sections["software_details"]:
        explanation.append(
            "இந்த பகுதியில் மென்பொருளின் பெயர், பதிப்பு மற்றும் அதன் வகையை குறிப்பிட வேண்டும்."
        )

    return explanation
