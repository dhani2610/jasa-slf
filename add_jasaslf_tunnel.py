import urllib.request
import json

payload = {
    "name": "jasaslf",
    "proto": "http",
    "addr": "8018",
    "schemes": ["https"]
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request("http://127.0.0.1:4045/api/tunnels", data=data, headers={"Content-Type": "application/json"})

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("Success adding 6th tunnel (jasaslf)!")
        print("Tunnel Name:", res.get("name"))
        print("Public URL:", res.get("public_url"))
except urllib.error.HTTPError as e:
    err = e.read().decode("utf-8")
    print(f"HTTPError {e.code}: {err}")
except Exception as e:
    print("Error:", e)
