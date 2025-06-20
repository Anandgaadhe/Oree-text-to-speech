import requests

RENDER_BASE = "https://your-render-url.onrender.com"  # replace with your Render URL

def test_text_to_speech():
    print("Testing Text-to-Speech...")
    resp = requests.post(f"{RENDER_BASE}/text-to-speech", data={
        "text": "Hello Anand! This is a test of text to speech.",
        "voice_rate": "150"
    })
    print("Status Code:", resp.status_code)
    if resp.status_code == 200:
        filename = "test_audio.wav"
        with open(filename, "wb") as f:
            f.write(resp.content)
        print(f"Audio file downloaded as {filename}")
    else:
        print("Failed to get audio file.")

def test_text_to_video():
    print("Testing Text-to-Video...")
    resp = requests.post(f"{RENDER_BASE}/text-to-video", data={
        "text": "This is a sample video generated from text.",
        "background_color": "#000000",
        "text_color": "#FFFFFF",
        "duration": "5"
    })
    print("Status Code:", resp.status_code)
    if resp.status_code == 200:
        filename = "test_video.mp4"
        with open(filename, "wb") as f:
            f.write(resp.content)
        print(f"Video file downloaded as {filename}")
    else:
        print("Failed to get video file.")

if __name__ == "__main__":
    test_text_to_speech()
    test_text_to_video()
