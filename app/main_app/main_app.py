from app.main_app import main_app

@main_app.route('/')
def home():
    return "Hello from main_app!"
