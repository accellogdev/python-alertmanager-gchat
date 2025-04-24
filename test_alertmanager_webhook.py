import httpx

ALERTMANAGER_ENDPOINT = "http://localhost:5000/"

# Payload simulado com alerta de severidade crítica
payload = {
    "receiver": "google-chat-email",
    "status": "firing",
    "alerts": [
        {
            "status": "firing",
            "labels": {
                "alertname": "HighCPUUsage",
                "severity": "critical",
                "instance": "10.0.0.1:9100"
            },
            "annotations": {
                "summary": "Uso de CPU muito alto",
                "description": "CPU acima de 90% no node 10.0.0.1"
            }
        }
    ],
    "groupLabels": {"alertname": "HighCPUUsage"},
    "commonLabels": {
        "alertname": "HighCPUUsage",
        "severity": "critical"
    },
    "commonAnnotations": {
        "summary": "Uso de CPU muito alto",
        "description": "CPU acima de 90%"
    },
    "externalURL": "http://prometheus.local",
    "version": "4",
    "groupKey": "{}:{alertname=\"HighCPUUsage\"}"
}

def test_alert_delivery():
    try:
        response = httpx.post(ALERTMANAGER_ENDPOINT, json=payload, timeout=5)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Erro ao enviar alerta: {e}")

if __name__ == "__main__":
    test_alert_delivery()