# Helper utilities - enhanced version
def greet(name, formal=False):
    """Greet someone by name."""
    if formal:
        return f"Good day, {name}."
    return f"Hey {name}!"

def farewell(name):
    """Say goodbye to someone."""
    return f"Goodbye, {name}! See you soon!"

def thank(name):
    """Thank someone."""
    return f"Thank you, {name}!"
