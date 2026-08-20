import os
import asyncio
import numpy as np
import speech_recognition as sr
from faster_whisper import WhisperModel
import edge_tts
import playsound
import pyttsx3
from core.network_check import is_online


whisper_model = WhisperModel("base.en", device="cpu", compute_type="int8", cpu_threads=4)


offline_engine = pyttsx3.init()
offline_engine.setProperty('rate', 175)

ONLINE_VOICE = "en-GB-RyanNeural"

async def _edge_speak(text: str):
    tmp_path = "voice_out.mp3"
    comm = edge_tts.Communicate(text, ONLINE_VOICE)
    await comm.save(tmp_path)
    playsound.playsound(tmp_path)
    if os.path.exists(tmp_path):
        os.remove(tmp_path)

def speak(text: str):
    if is_online():
        try:
            asyncio.run(_edge_speak(text))
            return
        except Exception:
            pass
    
    offline_engine.say(text)
    offline_engine.runAndWait()

def listen_mic() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone(sample_rate=16000) as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=9)
        except sr.WaitTimeoutError:
            return ""

    try:
        raw_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
        audio_np = np.frombuffer(raw_data, dtype=np.int16).astype(np.float32) / 32768.0
        segments, _ = whisper_model.transcribe(audio_np, beam_size=1, vad_filter=True, language="en")
        return " ".join([seg.text for seg in segments]).strip()
    except Exception as e:
        print(f"[STT Error] {e}")
        return ""