# J.A.R.V.I.S-part-1-
# 🤖 JARVIS — Hybrid AI Desktop Assistant

A futuristic, voice-controlled AI assistant with local/cloud intelligence, PC automation, and wireless Android control.

  🧠 Overview

**JARVIS** is a hybrid AI-powered desktop assistant inspired by the futuristic **Iron Man Arc Reactor interface**.

The system combines **cloud-based AI reasoning** with **local AI models**, allowing it to continue functioning even when an internet connection is unavailable.

JARVIS can understand voice commands, execute actions on a Windows PC, interact with Android devices over wireless ADB, and provide responses through natural speech.

### What makes JARVIS different?

Instead of relying entirely on cloud services, JARVIS uses a **hybrid architecture**:

```text
                    ┌─────────────────────┐
                    │     USER VOICE      │
                    │   "Hey Jarvis..."   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Wake Word Engine  │
                    │    OpenWakeWord     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Speech-to-Text    │
                    │    Faster-Whisper   │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌───────────────────────────┐
                 │      JARVIS AI BRAIN      │
                 │   Intent + Tool Router    │
                 └─────────────┬─────────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
     ┌─────────────────┐              ┌─────────────────┐
     │   OpenAI GPT     │              │     Ollama      │
     │   Cloud Reasoning│              │ Local Llama 3.2 │
     └─────────────────┘              └─────────────────┘
              │                                 │
              └────────────────┬────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Device Hub       │
                    └──────────┬──────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
          ┌──────────────┐         ┌────────────────┐
          │ Windows PC   │         │ Android Device │
          │ Automation   │         │ Wireless ADB   │
          └──────────────┘         └────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Voice Response    │
                    │ Edge-TTS / pyttsx3  │
                    └─────────────────────┘
```

---

# ✨ Features

## 🧠 Hybrid AI Engine

JARVIS can intelligently switch between cloud and local AI.

### Online Mode

Uses **OpenAI GPT-4o** for advanced reasoning and natural language understanding.

### Offline Mode

Automatically falls back to:

```text
Ollama
└── llama3.2:3b
```

This means basic AI functionality can continue even without internet access.

---

## 🎙️ Voice Interaction

JARVIS supports hands-free voice interaction using a completely integrated speech pipeline.

### Speech-to-Text

Powered by:

* `faster-whisper`
* Local processing
* Low-latency transcription

### Text-to-Speech

Primary:

```text
Microsoft Edge-TTS
```

Offline fallback:

```text
pyttsx3
```

---

## 👂 Wake-Word Detection

JARVIS continuously listens for its activation phrase:

> **"Hey Jarvis"**

Wake-word detection is handled using:

```text
openWakeWord
```

This allows the assistant to operate without requiring the user to manually activate it every time.

---

# 💻 Windows PC Automation

JARVIS can interact directly with the host computer.

Supported operations include:

* 📸 Take screenshots
* 🔊 Control system volume
* 🔇 Mute audio
* 🔒 Lock Windows
* 🚀 Launch applications
* 🖥️ Perform desktop automation
* ⌨️ Simulate keyboard/mouse interaction

The automation layer uses:

```text
PyAutoGUI
Native Windows APIs
```

---

# 📱 Wireless Android Control

JARVIS can communicate with Android devices using **Android Debug Bridge (ADB)**.

Once the phone is paired over Wi-Fi, JARVIS can issue commands such as:

* ▶️ Open YouTube
* 📷 Launch camera
* 🏠 Navigate to home
* 🔌 Manage device power actions
* 📱 Launch Android applications
* ⚡ Execute Android intents

Communication flow:

```text
JARVIS
   │
   ▼
Device Hub
   │
   ▼
ADB
   │
   ▼
Wi-Fi
   │
   ▼
Android Phone
```

---

# 🌀 Futuristic Arc Reactor GUI

JARVIS includes a futuristic web-based HUD inspired by the Iron Man Arc Reactor.

The interface uses:

* HTML5
* CSS animations
* JavaScript
* Eel
* Glowing HUD effects
* Real-time assistant status

The interface provides a visual representation of:

* Listening state
* Processing state
* AI responses
* Assistant activation
* System status

---

# 🏗️ Project Architecture

```text
JARVIS/
│
├── core/
│   ├── brain.py
│   ├── device_hub.py
│   ├── network_check.py
│   ├── voice_engine.py
│   └── wake_detector.py
│
├── platform-tools/
│   └── ADB binaries
│
├── web/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

### Core Components

| File               | Responsibility                                |
| ------------------ | --------------------------------------------- |
| `main.py`          | Application entry point and thread management |
| `brain.py`         | AI reasoning and tool-routing engine          |
| `device_hub.py`    | PC automation and Android ADB control         |
| `network_check.py` | Network connectivity detection                |
| `voice_engine.py`  | Speech-to-text and text-to-speech             |
| `wake_detector.py` | "Hey Jarvis" wake-word detection              |
| `index.html`       | GUI structure                                 |
| `style.css`        | Arc Reactor visual design                     |
| `script.js`        | GUI interaction and Eel communication         |

---

# 🛠️ Technology Stack

### Programming

* **Python**
* **HTML5**
* **CSS3**
* **JavaScript**

### Artificial Intelligence

* OpenAI GPT-4o
* Ollama
* Llama 3.2 3B

### Voice

* Faster-Whisper
* OpenWakeWord
* Microsoft Edge-TTS
* pyttsx3

### Automation

* PyAutoGUI
* Windows APIs
* Android ADB

### Interface

* Eel
* HTML5
* CSS animations
* JavaScript

---

# ⚙️ Requirements

Before installing JARVIS, make sure you have:

### Required

* Windows 10/11
* Python **3.10 or 3.11**
* Git
* Microphone
* Internet connection for cloud AI/TTS functionality

### Optional

* Ollama
* Android phone
* Android Debug Bridge
* OpenAI API key

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/JARVIS.git
cd JARVIS
```

Replace `your-username` with your GitHub username.

---

## 2. Create a Virtual Environment

Open PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\activate
```

You should now see something similar to:

```text
(venv) PS C:\...\JARVIS>
```

---

## 3. Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install the project dependencies:

```powershell
pip install -r requirements.txt
```

---

# 🧠 Configure Ollama

Install Ollama and download the local model:

```bash
ollama pull llama3.2:3b
```

Verify that the model is available:

```bash
ollama list
```

You should see:

```text
llama3.2:3b
```

JARVIS can use this model as its local AI fallback.

---

# 🔑 Configure OpenAI

Cloud AI functionality requires an OpenAI API key.

In PowerShell:

```powershell
$env:OPENAI_API_KEY="your_openai_api_key"
```

For a permanent environment variable, configure it through Windows Environment Variables.

> ⚠️ Never commit your API key to GitHub.

A `.env` file or environment variable should be used instead of hardcoding secrets.

---

# 👂 Download Wake-Word Models

Run:

```powershell
python -c "import openwakeword.utils; openwakeword.utils.download_models()"
```

This downloads the models required by OpenWakeWord.

---

# 📱 Android Wireless Setup

Android control is optional.

## Step 1 — Enable Developer Options

On your Android phone:

```text
Settings
   ↓
About Phone
   ↓
Build Number
   ↓
Tap 7 times
```

Then enable:

```text
Developer Options
└── USB Debugging
```

---

## Step 2 — Connect the Phone

Connect the phone to your PC using USB.

Verify the device:

```bash
adb devices
```

Authorize the computer on your phone if prompted.

---

## Step 3 — Enable Wireless ADB

Run:

```bash
adb tcpip 5555
```

Find your phone's local IP address.

Then connect:

```bash
adb connect <PHONE_IP>:5555
```

Example:

```bash
adb connect 192.168.1.25:5555
```

Verify:

```bash
adb devices
```

You should see something similar to:

```text
192.168.1.25:5555    device
```

---

# ▶️ Running JARVIS

Start the application:

```powershell
python main.py
```

The Arc Reactor interface should launch.

Once running:

### Voice Activation

Say:

> **"Hey Jarvis"**

Then issue a command.

### Manual Activation

Click the glowing Arc Reactor core in the interface.

---

# 🎤 Example Commands

### Computer Control

```text
"Take a screenshot"
```

```text
"Lock my laptop"
```

```text
"Open Chrome"
```

```text
"Mute system audio"
```

### Android Control

```text
"Open YouTube on my phone"
```

```text
"Open the camera on my phone"
```

```text
"Go to the home screen"
```

### General AI

```text
"What is quantum computing?"
```

```text
"Explain black holes"
```

```text
"What is machine learning?"
```

---

# 🔄 Hybrid AI Workflow

JARVIS follows a simple decision flow:

```text
              User Request
                   │
                   ▼
            Internet Check
                   │
          ┌────────┴────────┐
          │                 │
       Online             Offline
          │                 │
          ▼                 ▼
      OpenAI GPT        Ollama Llama
          │                 │
          └────────┬────────┘
                   │
                   ▼
             Tool Router
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
       PC Tools          Android Tools
          │                  │
          └────────┬─────────┘
                   │
                   ▼
             JARVIS Response
                   │
                   ▼
              Text-to-Speech
```

---

# 🔐 Security Considerations

JARVIS interacts directly with your operating system and connected Android devices.

Because of this, users should take basic security precautions.

### API Keys

Never commit:

```text
OPENAI_API_KEY
```

to GitHub.

Use environment variables instead.

### ADB

Only enable wireless ADB on trusted networks.

### System Automation

JARVIS has the ability to perform actions on the computer. Only run commands you understand and trust.

### GitHub `.gitignore`

Consider adding:

```gitignore
venv/
__pycache__/
*.pyc
.env
*.log
```

---

# 🐛 Troubleshooting

## JARVIS does not detect my voice

Check:

* Microphone permissions
* Windows microphone settings
* Faster-Whisper installation
* Wake-word model installation
* Microphone input device

---

## Ollama fallback is not working

Verify Ollama:

```bash
ollama list
```

Then test the model:

```bash
ollama run llama3.2:3b
```

If this works, verify that the JARVIS Ollama configuration points to the correct model.

---

## Android device is not detected

Run:

```bash
adb devices
```

If the device is missing:

1. Check USB debugging.
2. Authorize the computer on the phone.
3. Make sure both devices are on the same network.
4. Restart ADB.

```bash
adb kill-server
adb start-server
```

Then reconnect:

```bash
adb connect <PHONE_IP>:5555
```

---

## OpenAI requests fail

Check whether the API key is available:

```powershell
echo $env:OPENAI_API_KEY
```

If nothing is returned, set it again:

```powershell
$env:OPENAI_API_KEY="your_openai_api_key"
```

---

# 🗺️ Roadmap

Future improvements planned for JARVIS could include:

* [ ] Custom wake-word training
* [ ] More advanced PC automation
* [ ] Expanded Android controls
* [ ] Smart-home integration
* [ ] Persistent conversation memory
* [ ] User authentication
* [ ] Multi-user voice recognition
* [ ] Better offline AI capabilities
* [ ] GPU-accelerated local inference
* [ ] Custom JARVIS personality system
* [ ] Plugin/tool architecture
* [ ] More advanced Arc Reactor animations
* [ ] System monitoring dashboard
* [ ] Calendar and productivity integrations

---

# 📸 Screenshots

Add screenshots of your Arc Reactor interface here:

```markdown
![JARVIS Interface](screenshots/jarvis-interface.png)
```

Recommended screenshots:

1. Main Arc Reactor HUD
2. Listening state
3. AI processing state
4. PC automation command
5. Android control
6. Offline Ollama mode

---

# 🎥 Demo

Add your project demonstration video here:

```markdown
[![JARVIS Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
```

---

# 🤝 Contributing

Contributions are welcome!

### Steps

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# ⭐ Support

If you find JARVIS useful or interesting:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐛 Report bugs
* 💡 Suggest features
* 🤝 Contribute improvements

---

Built with Python, AI, voice technology, automation, and a little bit of Iron Man inspiration. ⚡

"Sometimes you gotta run before you can walk."

