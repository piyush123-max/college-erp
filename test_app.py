from app import greet, login, attendance_percentage

def test_greet():
    assert greet("Piyush") == "Welcome to College ERP, Piyush!"

def test_login_valid():
    assert login("student", "pass123") is True

def test_login_empty():
    assert login("", "") is False

def test_attendance():
    assert attendance_percentage(18, 20) == 90.0

def test_attendance_zero_total():
    assert attendance_percentage(0, 0) == 0.0
