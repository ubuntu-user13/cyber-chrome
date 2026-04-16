Features
Chromium launch control via flags
Incognito mode toggle (--incognito)
GPU disable toggle (--disable-gpu)
WebRTC disable toggle (--disable-webrtc)
Persistent settings storage (/tmp/cyber-state.json)
Apply + relaunch browser with updated flags
Local web-based control panel (served at /ui)
HTTP API for settings (/set/<key>/<on|off>)
Basic VPN toggle placeholder
Basic firewall toggle placeholder
Command execution endpoint (/run if enabled)
Desktop launcher integration (optional)
Architecture
[ Browser UI (index.html) ]
            ↓ HTTP (fetch)
[ Python Backend (server.py :8080) ]
            ↓
[ State Storage (/tmp/cyber-state.json) ]
            ↓
[ Chromium Launcher (subprocess flags) ]
            ↓
[ System Layer (OS / network tools optional) ]
Data Flow
User clicks toggle
→ UI sends request (/set/incognito/on)
→ Backend stores state
→ User clicks APPLY
→ Backend builds flags
→ Chromium relaunches with flags
→ UI reload
