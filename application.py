"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ

try:
    from FlaskWebProject import app

    print("✅ Successfully imported app")
except Exception as e:
    print(f"❌ Failed to import app: {e}")
    # Create a minimal Flask app as fallback
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Minimal Flask app is running. Import error occurred."

    @app.route("/debug")
    def debug():
        return f"Import error: {e}"


if __name__ == "__main__":
    HOST = environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, ssl_context="adhoc")
