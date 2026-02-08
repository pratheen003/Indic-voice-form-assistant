def extract_sections(lines):
    sections = {
        "title": [],
        "company_details": [],
        "software_details": []
    }

    for line in lines:
        if "Application Form" in line or "விண்ணப்பம்" in line:
            sections["title"].append(line)

        elif "Company" in line or "நிறுவன" in line:
            sections["company_details"].append(line)

        elif "Software" in line or "மென்பொருள்" in line:
            sections["software_details"].append(line)

    return sections
