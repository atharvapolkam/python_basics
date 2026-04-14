from onvif import ONVIFCamera
import requests
from requests.auth import HTTPDigestAuth
from urllib.parse import urlparse, urlunparse
import time

DVR_IP      = "103.170.91.229"
HTTP_PORT   = 81
USER        = "admin"
PASSWORD    = "secure@123"
NUM_CAMERAS = 16
IGNORED     = {6}
ONVIF_PORTS = [80, 8000, 8080, 81]

cam = None
profiles = []

for port in ONVIF_PORTS:
    try:
        print(f"Trying ONVIF on port {port}...")
        test_cam = ONVIFCamera(DVR_IP, port, USER, PASSWORD)
        media = test_cam.create_media_service()
        profiles = media.GetProfiles()
        cam = test_cam
        print(f"Connected on port {port} — found {len(profiles)} profiles\n")
        break
    except Exception as e:
        print(f"  Port {port} failed: {e}")

FALLBACK = not profiles
if FALLBACK:
    print("\nONVIF failed — using Hikvision ISAPI fallback\n")

session = requests.Session()
session.auth = HTTPDigestAuth(USER, PASSWORD)

for ch in range(1, NUM_CAMERAS + 1):
    if ch in IGNORED:
        print(f"— Channel {ch:02d} skipped")
        continue
    try:
        if FALLBACK:
            snapshot_url = f"http://{DVR_IP}:{HTTP_PORT}/ISAPI/Streaming/channels/{ch}01/picture"
        else:
            idx = ch - 1
            if idx >= len(profiles):
                print(f"✗ Channel {ch:02d} no profile")
                continue
            uri_resp = media.GetSnapshotUri({"ProfileToken": profiles[idx].token})
            parsed = urlparse(uri_resp.Uri)
            snapshot_url = urlunparse(parsed._replace(netloc=f"{DVR_IP}:{HTTP_PORT}"))

        print(f"  Ch {ch:02d} → {snapshot_url}")
        resp = session.get(snapshot_url, timeout=15)
        resp.raise_for_status()
        filename = f"cam_{ch:02d}.jpg"
        with open(filename, "wb") as f:
            f.write(resp.content)
        print(f"✓ Channel {ch:02d} saved → {filename} ({len(resp.content)//1024} KB)")
    except Exception as e:
        print(f"✗ Channel {ch:02d} error: {e}")
    time.sleep(0.5)

print("\nDone.")
EOF