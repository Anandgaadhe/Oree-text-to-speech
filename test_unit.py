import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_text_to_speech_route(client):
    response = client.post('/text-to-speech', data={
        'text': 'Test text to speech',
        'voice_rate': '150'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Audio generated successfully!' in response.data or b'Error generating audio' in response.data

def test_text_to_video_route(client):
    response = client.post('/text-to-video', data={
        'text': 'Test text to video',
        'background_color': '#000000',
        'text_color': '#FFFFFF',
        'duration': '5'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Video generated successfully!' in response.data or b'Error generating video' in response.data
