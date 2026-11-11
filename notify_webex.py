import json, os, sys, urllib.request

status = sys.argv[1] if len(sys.argv) > 1 else "UNKNOWN"
emoji = "✅" if status == "SUCCESS" else "❌"
msg = (f"{emoji} **{os.environ.get('JOB_NAME')}** build "
       f"#{os.environ.get('BUILD_NUMBER')}: **{status}**\n\n"
       f"{os.environ.get('BUILD_URL', '')}")

req = urllib.request.Request(
    "https://webexapis.com/v1/messages",
    data=json.dumps({"roomId": os.environ["WEBEX_ROOM_ID"], "markdown": msg}).encode(),
    headers={"Authorization": f"Bearer {os.environ['WEBEX_TOKEN']}",
             "Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as r:
    print("Webex notification sent, HTTP", r.status)