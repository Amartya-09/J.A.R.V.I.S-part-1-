import os
import re
import json
import ollama
from openai import OpenAI
from core.network_check import is_online
from core.device_hub import control_pc, control_mobile

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your_openai_api_key"))

SYSTEM_PROMPT = """You are JARVIS.
- For PC tasks (apps, screenshots, lock, mute, browser), call 'control_pc'.
- For Mobile tasks (youtube, apps, camera, home), call 'control_mobile'.
- For general conversation, reply directly in concise text."""

openai_tools = [
    {
        "type": "function",
        "function": {
            "name": "control_pc",
            "description": "Execute PC tasks: open_browser, launch_app, take_screenshot, volume_mute, lock_pc",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["open_browser", "launch_app", "take_screenshot", "volume_mute", "lock_pc"]
                    },
                    "target": {"type": "string"}
                },
                "required": ["action"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "control_mobile",
            "description": "Execute Mobile tasks: youtube, settings, browser, home, power, camera",
            "parameters": {
                "type": "object",
                "properties": {
                    "action_key": {
                        "type": "string",
                        "enum": ["youtube", "settings", "browser", "home", "power", "camera"]
                    }
                },
                "required": ["action_key"]
            }
        }
    }
]

def fast_intent_router(q: str):
    """Bypasses LLM hallucinations to guarantee instant laptop/mobile execution."""
    q_low = q.lower().strip()

   
    if any(k in q_low for k in ["screenshot", "screen shot", "capture screen", "snap"]):
        return control_pc("take_screenshot")
    
    if any(k in q_low for k in ["lock pc", "lock laptop", "lock screen", "lock computer"]):
        return control_pc("lock_pc")
        
    if any(k in q_low for k in ["mute volume", "mute audio", "unmute", "mute system", "mute pc", "mute laptop"]):
        return control_pc("volume_mute")

    if "open" in q_low and not ("phone" in q_low or "mobile" in q_low):
        if "chrome" in q_low or "browser" in q_low or "google" in q_low:
            return control_pc("open_browser", "google.com")
        elif "notepad" in q_low:
            return control_pc("launch_app", "notepad")
        elif "calc" in q_low:
            return control_pc("launch_app", "calc")
        elif "code" in q_low or "vs code" in q_low:
            return control_pc("launch_app", "code")

  
    if any(m in q_low for m in ["phone", "mobile", "android"]):
        if "youtube" in q_low:
            return control_mobile("youtube")
        elif "settings" in q_low:
            return control_mobile("settings")
        elif "camera" in q_low:
            return control_mobile("camera")
        elif "home" in q_low:
            return control_mobile("home")

    return None

def think_and_act(query: str) -> str:
    print(f"\n[Command Received] '{query}'")

    
    direct_action = fast_intent_router(query)
    if direct_action:
        print(f"[Direct Execution] {direct_action}")
        return direct_action

   
    if is_online():
        try:
            res = openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": query}
                ],
                tools=openai_tools,
                tool_choice="auto"
            )
            msg = res.choices[0].message
            if msg.tool_calls:
                for tc in msg.tool_calls:
                    args = json.loads(tc.function.arguments)
                    print(f"[Tool Call (Online)] {tc.function.name} -> {args}")
                    if tc.function.name == "control_pc":
                        return control_pc(args.get("action"), args.get("target", ""))
                    elif tc.function.name == "control_mobile":
                        return control_mobile(args.get("action_key"))
            if msg.content:
                return msg.content
        except Exception:
            pass

   
    try:
        res = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query}
            ],
            tools=[control_pc, control_mobile]
        )
        if res.message.tool_calls:
            for call in res.message.tool_calls:
                name = call.function.name
                args = call.function.arguments
                print(f"[Tool Call (Offline)] {name} -> {args}")
                if name == "control_pc":
                    return control_pc(args.get("action"), args.get("target", ""))
                elif name == "control_mobile":
                    return control_mobile(args.get("action_key"))
        
        reply = res.message.content or "Done."
        return reply
    except Exception as e:
        return f"Offline brain error: {e}"