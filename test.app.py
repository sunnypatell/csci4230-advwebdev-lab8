"""
Unit tests for the Lab 8 DevOps Flask app.

We keep these very small and focused so CI is fast.
"""

from app import app


def test_home() -> None:
    """Root route should return HTTP 200 and contain the word 'DevOps'."""
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"DevOps" in res.data
