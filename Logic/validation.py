def validate_form_data(form_data):
    required_fields = {
        "Projekt Information": ["Projektname", "Kundenname"],
        "Energiebezugsdaten": ["Energieverbrauch"]
    }

    errors = []

    for section, fields in required_fields.items():
        for field in fields:
            value = form_data.get(section, {}).get(field)
            if value in [None, ""]:  # Optional: add `0` if you want to flag that as empty
                errors.append(f"❌ Feld **{field}** fehlt in Abschnitt **{section}**.")

    return errors  # Return list of error messages
