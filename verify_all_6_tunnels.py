import urllib.request
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tunnels = [
    ("Drone (Port 8008)", "https://spotty-limelight-stamina.ngrok-free.dev"),
    ("PTP (Port 8010)", "https://d9fc-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"),
    ("Drilling (Port 8012)", "https://e597-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"),
    ("Ahli K3 Corp (Port 8014)", "https://d651-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"),
    ("Jasa SLO (Port 8016)", "https://551b-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"),
    ("Jasa SLF (Port 8018)", "https://ee55-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"),
]

print("=== VERIFYING ALL 6 NGROK TUNNELS ===", flush=True)
for name, url in tunnels:
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "ngrok-skip-browser-warning": "69420"
            }
        )
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            code = resp.getcode()
            print(f"[OK {code}] {name} -> {url}", flush=True)
    except Exception as e:
        print(f"[ERROR] {name} -> {url} ({e})", flush=True)
