import pytest

from app import create_app


@pytest.fixture
def test_client():
    app = create_app()
    app.config['SECRET_KEY'] = 'sekrit!'
    return app.test_client()
