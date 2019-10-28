def test_hello_world(test_client):
    response = test_client.get('/')
    assert 200 == response.status_code
    assert b'hallo' in response.data


def test_shorter_url_should_create_data_in_redis(test_client, mock_db):
    url = 'http://google.com'
    shorter = '2e32ee40-baaa-52e8-8227-a4ced6c95d14'
    data = {'url': url}
    response = test_client.post('/url', json=data)
    expected = {'original': url, 'short': shorter}

    assert 200 == response.status_code
    assert expected == response.json
    assert 0 == int(mock_db.get(f'{shorter}:counter'))
    assert url == mock_db.get(f'{shorter}:original').decode("utf-8")


def test_shorter_url_should_duplicate_urls(test_client, mock_db):
    data = {'url': 'http://google.com'}
    test_client.post('/url', json=data)
    assert 3 == len(mock_db.keys())
    test_client.post('/url', json=data)
    assert 3 == len(mock_db.keys())


def test_redirect_should_return_301_to_the_correct_url(test_client, mock_db):
    data = {'url': 'http://google.com'}
    test_client.post('/url', json=data)
    shorter = '2e32ee40-baaa-52e8-8227-a4ced6c95d14'
    response = test_client.get(f'/{shorter}')
    assert 301 == response.status_code
    assert 1 == int(mock_db.get(f'{shorter}:counter'))
