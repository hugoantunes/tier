import pytest

from mockredis import mock_strict_redis_client

from app import create_app


@pytest.fixture
def test_client():
    app = create_app()
    app.config['SECRET_KEY'] = 'sekrit!'
    return app.test_client()


@pytest.fixture
def mock_db(monkeypatch):
    db = mock_strict_redis_client()
    monkeypatch.setattr('app.views.db', db)
    return db
