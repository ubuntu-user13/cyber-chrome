# Cyber Panel — Complete README

---

## Overview

Cyber Panel is a local control interface for managing Chromium behavior through a web-based UI and a Python backend. It allows toggling browser settings, persisting configuration, and relaunching Chromium with specific runtime flags.

---

## Core Features

* Chromium launch control via flags
* Incognito mode toggle (`--incognito`)
* GPU disable (`--disable-gpu`)
* WebRTC disable (`--disable-webrtc`)
* Persistent settings storage (`/tmp/cyber-state.json`)
* Apply + relaunch browser
* Local web UI (`/ui`)
* HTTP API for control
* Desktop launcher support (optional)

---

## Architecture

```
[ UI (index.html) ]
        ↓ HTTP (fetch)
[ Backend (server.py :8080) ]
        ↓
[ State (/tmp/cyber-state.json) ]
        ↓
[ Chromium Launcher (flags) ]
        ↓
[ OS / System Layer ]
```

---

## File Structure

```
~/cyber-backend/server.py
~/cyber-ui/index.html
~/cyber-ui-launch.sh
~/.local/share/applications/cyber-chromium.desktop
```

---

## Installation

### 1. Install dependencies

```
sudo apt update
sudo apt install chromium-browser python3
```

---

### 2. Run backend

```
sudo python3 ~/cyber-backend/server.py
```

---

### 3. Open UI

```
chromium-browser http://127.0.0.1:8080/ui
```

---

## Usage

### Toggle settings

```
/set/<key>/<on|off>
```

Example:

```
/set/incognito/on
/set/gpu/off
/set/webrtc/off
```

---

### Apply settings

```
/apply
```

Effect:

* Relaunches Chromium
* Applies flags based on stored state

---

## Supported Settings

| Setting   | Effect                      |
| --------- | --------------------------- |
| incognito | `--incognito`               |
| gpu       | `--disable-gpu` (if off)    |
| webrtc    | `--disable-webrtc` (if off) |

---

## API Endpoints

```
GET /ui                      → Load UI
GET /set/<key>/<on|off>      → Update setting
GET /apply                   → Apply + relaunch
```

---

## Example Requests

```
curl http://127.0.0.1:8080/set/incognito/on
curl http://127.0.0.1:8080/apply
```

---

## Data Flow

```
User click
→ /set request
→ state saved
→ /apply
→ flags built
→ Chromium relaunched
→ UI reload
```

---

## Launcher Script (optional)

```
#!/usr/bin/env bash
python3 ~/cyber-backend/server.py &
sleep 1
chromium-browser http://127.0.0.1:8080/ui
```

---

## Desktop App (optional)

File:

```
~/.local/share/applications/cyber-chromium.desktop
```

```
[Desktop Entry]
Name=Cyber Panel
Exec=/bin/bash -c "$HOME/cyber-ui-launch.sh"
Icon=utilities-terminal
Type=Application
Categories=Network;System;
Terminal=false
```

---

## Troubleshooting

### Check backend

```
ss -tulnp | grep 8080
```

---

### Kill port

```
sudo fuser -k 8080/tcp
```

---

### Test API

```
curl http://127.0.0.1:8080/set/incognito/on
```

---

### Common Issues

* UI shows “error” → backend not running or wrong URL
* No effect → forgot to press APPLY
* App not showing → invalid `.desktop` file
* Port in use → kill process on 8080

---

## Limitations

* Requires browser relaunch for changes
* Some toggles are placeholders
* No authentication
* Localhost only
* No runtime Chromium modification

---

## Useful URLs

* UI:

```
http://127.0.0.1:8080/ui
```

* Example API:

```
http://127.0.0.1:8080/set/incognito/on
http://127.0.0.1:8080/apply
```

---

## External Documentation

* Chromium flags reference:

```
https://peter.sh/experiments/chromium-command-line-switches/
```

* Python HTTP server:

```
https://docs.python.org/3/library/http.server.html
```

* WireGuard (if used later):

```
https://www.wireguard.com/quickstart/
```

---

## Summary

Cyber Panel provides:

* Local control UI
* Backend API
* Persistent settings
* Chromium launch control

System model:

```
UI → API → State → Flags → Browser Relaunch
```
