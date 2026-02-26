def format_name(first, last):
    return f"{last}, {first}"

def validate_email(email):
    import re
    return bool(re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email))
