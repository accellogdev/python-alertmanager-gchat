from flask import Flask, request, jsonify
import httpx
import os

app = Flask(__name__)

GOOGLE_CHAT_WEBHOOK = os.getenv("GOOGLE_CHAT_WEBHOOK")

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

@app.route("/", methods=["POST"])
def alertmanager_webhook():
    data = request.json
    alerts = data.get("alerts", [])
    messages = []

    for alert in alerts:
        status = alert.get("status", "unknown").upper()
        name = alert.get("labels", {}).get("alertname", "N/A")
        severity = alert.get("labels", {}).get("severity", "N/A")
        summary = alert.get("annotations", {}).get("summary", "")
        description = alert.get("annotations", {}).get("description", "")

        msg = f"*[{status}]* {name} ({severity})\n{summary}\n{description}"
        messages.append(msg)

    final_message = "\n---\n".join(messages)
    payload = { "text": final_message }

    try:
        response = httpx.post(GOOGLE_CHAT_WEBHOOK, json=payload, timeout=5)
        response.raise_for_status()
    except httpx.HTTPError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Alert sent to Google Chat"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
