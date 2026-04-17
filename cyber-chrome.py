from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import subprocess
import os

STATE_FILE = os.path.expanduser("~/.cyber-chrome-state.json")

ALLOWED_KEYS = {"incognito", "gpu", "webrtc"}

def load():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save(state):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f)
    os.replace(tmp, STATE_FILE)

def build_flags(state):
    flags = [
        "--new-window",
        "--user-data-dir=/tmp/cyber-profile"
    ]

    if state.get("incognito"):
        flags.append("--incognito")

    if state.get("gpu") is False:
        flags.append("--disable-gpu")

    if state.get("webrtc") is False:
        flags.append("--disable-webrtc")

    return flags

def launch(state):
    cmd = ["chromium-browser"] + build_flags(state)
    subprocess.Popen(cmd)

def kill_browser():
    os.system("pkill -f chromium-browser")

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        state = load()

        def reply(msg):
            self.send_response(200)
            self.end_headers()
            self.wfile.write((msg + "\n").encode())

        if path == "/state":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(state).encode())
            return

        if path.startswith("/set/"):
            parts = path.split("/")
            if len(parts) < 4:
                return reply("invalid")

            key = parts[2]
            val = parts[3]

            if key not in ALLOWED_KEYS:
                return reply("invalid_key")

            state[key] = (val == "on")
            save(state)
            return reply(f"{key}={val}")

        if path == "/apply":
            kill_browser()
            launch(state)
            return reply("launched")

        if path == "/reset":
            save({})
            return reply("reset")

        return reply("ok")

HTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
