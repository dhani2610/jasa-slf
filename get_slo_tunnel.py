import urllib.request
import json

try:
    with urllib.request.urlopen("http://127.0.0.1:4045/api/tunnels", timeout=5) as r:
        data = json.loads(r.read())
        tunnels = data.get("tunnels", [])
        if not tunnels:
            print("No tunnels found on 4045 yet.")
        for t in tunnels:
            print(f"Tunnel: {t.get('name')} -> {t.get('public_url')} (forwarding to {t.get('config', {}).get('addr')})")
except Exception as e:
    print("Error querying 4045:", e)
