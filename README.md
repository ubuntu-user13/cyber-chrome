Cyber Panel — Complete README (Rewritten)
Overview

Cyber Panel is a local browser control system built around a Python HTTP backend and a web UI. It manages Chromium launch behavior through persistent settings and runtime flags.

It is designed for local automation of browser startup configurations.

Core Features
Chromium launch control via command-line flags
Persistent configuration storage (~/.cyber-state.json)
Incognito mode toggle (--incognito)
GPU disable toggle (--disable-gpu)
WebRTC disable toggle (--disable-webrtc)
Apply-and-relaunch workflow
Local web interface (/ui)
Lightweight HTTP API (localhost-only)
Architecture
UI (index.html)
      ↓ HTTP requests
Backend (server.py :8080)
      ↓
State Store (~/.cyber-state.json)
      ↓
Flag Builder
      ↓
Chromium Process Launcher
      ↓
Operating System
File Structure
~/cyber-backend/server.py
~/cyber-ui/index.html
~/cyber-launch.sh
~/.cyber-state.json
Installation
1. Dependencies
sudo apt update
sudo apt install chromium-browser python3
2. Run backend
python3 ~/cyber-backend/server.py
3. Open UI
chromium-browser http://127.0.0.1:8080/ui
Usage
Toggle settings

Format:

/set/<key>/<on|off>

Examples:

curl http://127.0.0.1:8080/set/incognito/on
curl http://127.0.0.1:8080/set/gpu/off
curl http://127.0.0.1:8080/set/webrtc/off
Apply configuration
curl http://127.0.0.1:8080/apply

Behavior:

Terminates running Chromium session
Rebuilds flags from stored state
Launches new Chromium instance
Supported Settings
Setting	Effect
incognito	Enables --incognito
gpu	Disables GPU when off
webrtc	Disables WebRTC when off
API Endpoints
GET /ui
GET /state
GET /set/<key>/<on|off>
GET /apply
Data Flow
User input
→ HTTP request (/set)
→ State updated
→ Saved to disk
→ /apply triggered
→ Flags generated
→ Chromium relaunched
Launcher Script
#!/usr/bin/env bash

python3 ~/cyber-backend/server.py &
sleep 1
chromium-browser http://127.0.0.1:8080/ui
Desktop Entry (Linux)
[Desktop Entry]
Name=Cyber Panel
Exec=/bin/bash -c "$HOME/cyber-launch.sh"
Icon=chromium
Type=Application
Categories=Network;System;
Terminal=false
Troubleshooting
Backend not responding
ss -tulnp | grep 8080
Kill stuck process
sudo fuser -k 8080/tcp
Test API
curl http://127.0.0.1:8080/state
Common Issues
UI shows error → backend not running
Settings not applied → /apply not called
App not visible → broken .desktop file
Port conflict → 8080 already in use
Limitations
Requires Chromium restart for changes
Local-only (no authentication layer)
Flag system depends on Chromium CLI behavior
No hot-reload of browser state
Useful Links
Chromium flags:
https://peter.sh/experiments/chromium-command-line-switches/
Python HTTP server:
https://docs.python.org/3/library/http.server.html
WireGuard reference (optional future expansion):
https://www.wireguard.com/quickstart/
Summary

Cyber Panel is a local browser automation layer.

Pipeline:

UI → API → State → Flag Builder → Chromium Launch

It provides deterministic control over Chromium startup behavior via a simple HTTP interface.
