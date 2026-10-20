def greet(name):
    return f"Welcome to College ERP, {name}!"

def login(username, password):
    return bool(username and password)

def attendance_percentage(present, total):
    return round(present / total * 100, 2) if total else 0.0
