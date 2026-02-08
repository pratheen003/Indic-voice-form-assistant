def clean_text(raw_text):
    lines = raw_text.splitlines()
    clean_lines = []

    for line in lines:
        line = line.strip()
        if len(line) > 2:
            clean_lines.append(line)

    return clean_lines
