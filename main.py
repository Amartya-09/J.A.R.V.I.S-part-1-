import threading
import eel
from core.network_check import is_online
from core.device_hub import auto_connect_mobile
from core.voice_engine import listen_mic, speak
from core.brain import think_and_act
from core.wake_detector import WakeWordDetector

eel.init('web')

def handle_query_cycle():
    net_status = is_online()
    eel.updateUI("LISTENING...", "Listening for command...", net_status)()
    
    query = listen_mic()
    if query:
        eel.updateUI("THINKING...", f"'{query}'", net_status)()
        response = think_and_act(query)
        eel.updateUI("SPEAKING...", response, net_status)()
        speak(response)
    else:
        eel.updateUI("STANDBY", "No speech detected.", net_status)()
        
    eel.updateUI("STANDBY", "Say 'Jarvis' or tap reactor core.", is_online())()

def wake_thread_runner():
    try:
        detector = WakeWordDetector(keyword="jarvis")
        while True:
            if detector.wait_for_wake_word():
                speak("Online, sir.")
                handle_query_cycle()
    except Exception as e:
        print(f"[WakeWord Disabled / Error] {e}")

@eel.expose
def manual_trigger():
    handle_query_cycle()

if __name__ == "__main__":
    auto_connect_mobile()
    
    # Start wake-word listener thread
    t = threading.Thread(target=wake_thread_runner, daemon=True)
    t.start()
    
    # Launch GUI
    eel.start('index.html', size=(850, 720))