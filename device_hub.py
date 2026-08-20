import os
import subprocess
import webbrowser
import pyautogui


platform_tools_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "platform-tools"))
if platform_tools_path not in os.environ.get("PATH", ""):
    os.environ["PATH"] = platform_tools_path + os.pathsep + os.environ.get("PATH", "")

PHONE_IP = "172.25.219.136"  

def auto_connect_mobile() -> bool:
    """Silently connects to wireless ADB on initialization."""
    try:
        res = subprocess.run(
            f"adb connect {PHONE_IP}:5555",
            shell=True,
            capture_output=True,
            text=True,
            timeout=3
        )
        return "connected" in res.stdout.lower()
    except Exception:
        return False


MOBILE_COMMANDS = {
    "youtube": 'adb shell am start -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity',
    "settings": 'adb shell am start -a android.settings.SETTINGS',
    "browser": 'adb shell am start -a android.intent.action.VIEW -d "https://www.google.com"',
    "home": 'adb shell input keyevent 3',
    "power": 'adb shell input keyevent 26',
    "camera": 'adb shell am start -a android.media.action.IMAGE_CAPTURE'
}

def control_pc(action: str, target: str = "") -> str:
    """Handles laptop system actions and software controls."""
    if not action:
        return "I am online and listening."
        
    action = action.lower().strip()
    
   
    if action in ["hello", "hi", "greet", "greeting", "status"]:
        return "Hello! Systems are fully operational. How can I help you?"
    
    
    if action == "open_browser":
        target_url = target if target.startswith("http") else f"https://www.google.com/search?q={target}"
        webbrowser.open(target_url)
        return f"Opening browser for {target} on PC."
        
    elif action == "launch_app":
        os.system(f"start {target}")
        return f"Launching {target}."
        
    elif action == "take_screenshot":
        try:
            save_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            file_path = os.path.join(save_dir, "jarvis_snap.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(file_path)
            print(f"[System] Screenshot saved successfully at: {file_path}")
            return "Screenshot captured and saved to workspace."
        except Exception as e:
            print(f"[Error] Failed to capture screenshot: {e}")
            return f"Failed to take screenshot: {e}"
            
    elif action == "volume_mute":
        pyautogui.press("volumemute")
        return "Toggled volume mute."
        
    elif action == "lock_pc":
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Laptop locked."
    
    return "Command executed."

def control_mobile(action_key: str) -> str:
    """Executes verified ADB commands on the connected phone."""
    if not action_key:
        return "No mobile action specified."
        
    action_key = action_key.lower().strip()
    cmd = MOBILE_COMMANDS.get(action_key)
    
    if not cmd:
        return f"Action '{action_key}' is not recognized for mobile."
    
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        if res.returncode == 0:
            return f"Executed {action_key} on mobile."
        return "ADB command failed. Please verify phone connection."
    except Exception as e:
        return f"Mobile control error: {e}"