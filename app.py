"""
Simple Flask app for CSCI 4230 - Lab 8 DevOps.

Author: Sunny Patel (100867748)
Course: CSCI 4230 Advanced Web Development
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello() -> str:
    """Return a basic greeting so our tests and CI have something to hit."""
    return "Hello, DevOps World!"


if __name__ == "__main__":
    # Debug is fine for this tiny lab app; not for production.
    app.run()
