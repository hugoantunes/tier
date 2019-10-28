def test_hello_world(test_client):
    response = test_client.get('/')
    assert 200 == response.status_code
    assert b'hallo' in response.data
