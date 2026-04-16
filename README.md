# Cyber Chrome

## Description
Cyber Chrome is a hardened Chromium-based browser launcher configured with system-level privacy and security defaults. It disables common background services, reduces tracking surface, and provides a minimal browsing environment using standard Chromium flags and Linux security tools.

It does not modify Chromium source code. It operates as a launch-layer configuration and system hardening profile for Chromium on Linux systems.

---

## Features

### Browser-level configuration
- Launches Chromium in a hardened mode
- Disables background networking
- Disables sync and Google integration services
- Disables extensions system by default
- Reduces telemetry-related features
- Forces new-window execution mode

### Privacy controls
- Incognito-first usage option
- Disables DNS prefetching
- Disables client-side phishing detection
- Removes search and navigation prediction features

### System-level hardening (optional install script)
- Enables UFW firewall (default deny inbound)
- Enables Fail2Ban intrusion protection
- Enables DNS encryption via dnscrypt-proxy
- Optional Tor routing via proxychains

### Tracking reduction (optional)
- Hosts-based blocking for common tracking domains

---

## Installation
## Windows Setup

1. Install Google Chrome
2. Download this repo
3. Run:
 Double-click:
cyber-chrome.bat
---
linux
```bash
git clone https://github.com/ubuntu-user13/cyber-chrome
cd cyber-chrome
bash cyber-chrome.sh
